"""
boundary_rules.py

Boundary Value Analysis rule engine.

Generates boundary values from a detected boundary constraint.

Author: Meera Sastry
Project: ClinicalTrialAI - IC-02 Test Design Engine
"""

from typing import List

from boundary_models import BoundaryConstraint, BoundaryValue


class BoundaryRuleEngine:
    """
    Generates Boundary Value Analysis (BVA) values.
    """

    def generate(self, constraint: BoundaryConstraint) -> List[BoundaryValue]:

        values: List[BoundaryValue] = []

        minimum = constraint.minimum
        maximum = constraint.maximum

        # Range available
        if minimum is not None and maximum is not None:

            nominal = (minimum + maximum) / 2

            values.extend([
                BoundaryValue("Min-1", minimum - 1, "Rejected"),
                BoundaryValue("Min", minimum, "Accepted"),
                BoundaryValue("Min+1", minimum + 1, "Accepted"),
                BoundaryValue("Nominal", nominal, "Accepted"),
                BoundaryValue("Max-1", maximum - 1, "Accepted"),
                BoundaryValue("Max", maximum, "Accepted"),
                BoundaryValue("Max+1", maximum + 1, "Rejected"),
            ])

        # Minimum only
        elif minimum is not None:

            values.extend([
                BoundaryValue("Min-1", minimum - 1, "Rejected"),
                BoundaryValue("Min", minimum, "Accepted"),
                BoundaryValue("Min+1", minimum + 1, "Accepted"),
            ])

        # Maximum only
        elif maximum is not None:

            values.extend([
                BoundaryValue("Max-1", maximum - 1, "Accepted"),
                BoundaryValue("Max", maximum, "Accepted"),
                BoundaryValue("Max+1", maximum + 1, "Rejected"),
            ])

        return values


if __name__ == "__main__":

    constraint = BoundaryConstraint(
        parameter="Age",
        minimum=18,
        maximum=60
    )

    engine = BoundaryRuleEngine()

    boundary_values = engine.generate(constraint)

    for value in boundary_values:
        print(value)
