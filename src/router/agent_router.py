class AgentRouter:
    def __init__(self, portfolio_health_agent, stub_agent):
        self.portfolio_health_agent = portfolio_health_agent
        self.stub_agent = stub_agent

    def dispatch(self, classification_result, user_profile):
        if classification_result.target_agent == "portfolio_health":
            return self.portfolio_health_agent.run(user_profile)
        return self.stub_agent.run(classification_result)