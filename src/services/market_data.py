# class MarketDataService:
#     def benchmark_for_user(self, user_profile) -> str:
#         preferred = ((user_profile.metadata.get("preferences") or {}).get("preferred_benchmark"))
#         if preferred:
#             return preferred

#         mapping = {
#             "US": "S&P 500",
#             "USA": "S&P 500",
#             "UK": "FTSE 100",
#             "GB": "FTSE 100",
#             "JP": "NIKKEI 225",
#             "JAPAN": "NIKKEI 225",
#         }
#         return mapping.get((user_profile.country or "").upper(), "MSCI World")

#     def synthetic_portfolio_return(self, weights: list[float]) -> float:
#         if not weights:
#             return 0.0
#         concentration_penalty = max(weights) / 100
#         return round(max(2.0, 11.5 - concentration_penalty * 5), 2)

#     def synthetic_benchmark_return(self, benchmark: str) -> float:
#         mapping = {
#             "S&P 500": 9.4,
#             "FTSE 100": 6.8,
#             "NIKKEI 225": 8.1,
#             "MSCI World": 8.6,
#         }
#         return mapping.get(benchmark, 8.6)

#     def annualized_return(self, total_return_pct: float, years: float = 1.0) -> float:
#         if years <= 0:
#             return total_return_pct
#         total_factor = 1 + total_return_pct / 100
#         return round((total_factor ** (1 / years) - 1) * 100, 2)







import yfinance as yf


class MarketDataService:
    def benchmark_for_user(self, user_profile) -> str:
        preferred = ((user_profile.metadata.get("preferences") or {}).get("preferred_benchmark"))
        if preferred:
            return preferred

        mapping = {
            "US": "S&P 500",
            "USA": "S&P 500",
            "UK": "FTSE 100",
            "GB": "FTSE 100",
            "JAPAN": "NIKKEI 225",
            "JP": "NIKKEI 225",
        }
        return mapping.get((user_profile.country or "").upper(), "MSCI World")

    def benchmark_symbol(self, label: str) -> str:
        mapping = {
            "S&P 500": "^GSPC",
            "FTSE 100": "^FTSE",
            "NIKKEI 225": "^N225",
            "MSCI World": "URTH",
        }
        return mapping.get(label, label)

    def latest_price(self, ticker: str) -> float | None:
        try:
            history = yf.Ticker(ticker).history(period="5d", auto_adjust=True)
            if history.empty:
                return None
            return float(history["Close"].dropna().iloc[-1])
        except Exception:
            return None

    def holding_weights(self, holdings: list) -> dict[str, float]:
        values = {}
        for h in holdings:
            price = self.latest_price(h.ticker)
            if price is not None:
                values[h.ticker] = h.quantity * price

        total = sum(values.values())
        if total > 0:
            return {k: round((v / total) * 100, 2) for k, v in values.items()}

        qty_total = sum(h.quantity for h in holdings) or 1.0
        return {h.ticker: round((h.quantity / qty_total) * 100, 2) for h in holdings}

    def one_year_return(self, ticker: str) -> float | None:
        try:
            history = yf.Ticker(ticker).history(period="1y", auto_adjust=True)
            closes = history["Close"].dropna()
            if len(closes) < 2:
                return None
            return round((float(closes.iloc[-1]) / float(closes.iloc[0]) - 1) * 100, 2)
        except Exception:
            return None

    def portfolio_return_pct(self, holdings: list) -> float | None:
        weights = self.holding_weights(holdings)
        total = 0.0
        used = 0

        for h in holdings:
            ret = self.one_year_return(h.ticker)
            if ret is None:
                continue
            total += ret * (weights.get(h.ticker, 0) / 100)
            used += 1

        return round(total, 2) if used else None

    def benchmark_return_pct(self, benchmark_label: str) -> float | None:
        return self.one_year_return(self.benchmark_symbol(benchmark_label))

    def annualized_return(self, total_return_pct: float | None, years: float = 1.0) -> float | None:
        if total_return_pct is None:
            return None
        if years <= 0:
            return total_return_pct
        total_factor = 1 + total_return_pct / 100
        return round((total_factor ** (1 / years) - 1) * 100, 2)
    
    def benchmark_label(self, benchmark: str) -> str:
       labels = {
        "^GSPC": "S&P 500",
        "^FTSE": "FTSE 100",
        "^N225": "NIKKEI 225",
        "URTH": "MSCI World",
        "S&P 500": "S&P 500",
        "FTSE 100": "FTSE 100",
        "NIKKEI 225": "NIKKEI 225",
        "MSCI World": "MSCI World",
    }
       return labels.get(benchmark, benchmark)   