from src.ic02.models.requirement import Requirement
from src.ic02.engine.test_design_engine import TestDesignEngine

from src.ic02.generators.boundary_value_generator import BoundaryValueGenerator
from src.ic02.generators.decision_table_generator import DecisionTableGenerator
from src.ic02.formatters.report_formatter import ReportFormatter

def main():

    requirement = Requirement(
        requirement_id="REQ-001",
        title="Login",
        # Temporary description for Boundary Value testing
        # description="Age must be between 18 and 60.",
        description="The system shall allow a valid user to login using username and password.",
        priority="High",
        business_rules=[
            "Password length >= 8"
        ],
        acceptance_criteria=[
            "User lands on dashboard"
        ]
    )

    # Generate scenarios, conditions, test cases and test data
    engine = TestDesignEngine()
    results = engine.generate(requirement)

    # Boundary Value Analysis
    boundary_generator = BoundaryValueGenerator()
    boundary_cases = boundary_generator.generate(requirement)

    # Decision Table
    decision_generator = DecisionTableGenerator()
    decision_rules = decision_generator.generate(requirement)
    formatter = ReportFormatter()
    formatter.print_scenarios(results)
    formatter.print_boundary_cases(boundary_cases)
    formatter.print_decision_tables(decision_rules)

if __name__ == "__main__":
    main()
