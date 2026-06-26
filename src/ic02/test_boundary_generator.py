"""
test_boundary_generator.py

Unit tests for Boundary Value Generator.

Author: Meera Sastry
Project: ClinicalTrialAI - IC-02 Test Design Engine
"""

from boundary_value_generator import BoundaryValueGenerator


def test_age_boundary():

    generator = BoundaryValueGenerator()

    requirement = "Age should be between 18 and 60."

    result = generator.generate(requirement)

    assert result is not None

    assert result.constraint.parameter == "age"
    assert result.constraint.minimum == 18
    assert result.constraint.maximum == 60

    assert len(result.boundary_values) == 7
    assert len(result.test_cases) == 7

    assert result.boundary_values[0].label == "Min-1"
    assert result.boundary_values[0].value == 17

    assert result.boundary_values[-1].label == "Max+1"
    assert result.boundary_values[-1].value == 61

    assert result.test_cases[0].test_id == "TC_BVA_001"
    assert result.test_cases[-1].test_id == "TC_BVA_007"

    print("✓ Age Boundary Test Passed")


def test_password_boundary():

    generator = BoundaryValueGenerator()

    requirement = "Password length should be 8-20 characters."

    result = generator.generate(requirement)

    assert result is not None

    assert result.constraint.parameter == "password"
    assert result.constraint.minimum == 8
    assert result.constraint.maximum == 20

    assert len(result.boundary_values) == 7

    print("✓ Password Boundary Test Passed")


def test_quantity_boundary():

    generator = BoundaryValueGenerator()

    requirement = "Quantity should be at least 1."

    result = generator.generate(requirement)

    assert result is not None

    assert result.constraint.parameter == "quantity"
    assert result.constraint.minimum == 1

    assert len(result.boundary_values) == 3

    print("✓ Quantity Boundary Test Passed")


if __name__ == "__main__":

    print("\nRunning Boundary Generator Tests")
    print("--------------------------------")

    test_age_boundary()
    test_password_boundary()
    test_quantity_boundary()

    print("\n🎉 All Boundary Generator Tests Passed Successfully.")
