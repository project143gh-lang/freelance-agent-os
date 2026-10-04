import re

class DynamicPortfolioGenSkill:
    """Skill to generate tailored portfolio snippets based on client needs."""
    def __init__(self):
        self.name = "dynamic_portfolio_gen"

    def execute(self, args):
        # args should be the client's needs or company description
        client_needs = args if args else "General Professional Services"
        
        return (
            f"STRATEGY_SUCCESS: Dynamic Portfolio Generator activated for: {client_needs}. "
            f"Recommended Workflow: "
            f"1. research_service.analyze_company(url='{client_needs}') "
            f"2. portfolio_service.get_matching_cases(keywords=extracted_needs) "
            f"3. portfolio_service.generate_custom_snippet(case_id=id, context=client_needs) "
            f"Please synthesize these into a tailored 'Proof of Work' section."
        )
