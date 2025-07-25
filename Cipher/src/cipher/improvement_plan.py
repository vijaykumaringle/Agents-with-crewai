from typing import List

class ImprovementPlanner:
    """
    Generates a business improvement plan based on pros and cons.
    """
    @staticmethod
    def generate_plan(pros: List[str], cons: List[str]) -> str:
        plan = ["Business Improvement Plan:\n"]
        if pros:
            plan.append("What customers like (Strengths):")
            for p in pros:
                plan.append(f"- {p}")
            plan.append("")
        if cons:
            plan.append("Areas to Improve (Weaknesses):")
            for c in cons:
                plan.append(f"- {c}")
            plan.append("")
            plan.append("Recommended Actions:")
            for c in cons:
                plan.append(f"- Address: {c}")
        else:
            plan.append("No significant weaknesses detected from the reviews.")
        return "\n".join(plan)
