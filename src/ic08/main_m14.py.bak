"""
IC-08 - Customer Usage Intelligence
Milestone 14 - Satisfaction Prediction Demo
"""

from src.ic08.services.satisfaction_prediction_service import (
    SatisfactionPredictionService,
)


def print_prediction(prediction):
    """Display a satisfaction prediction."""

    print("\n" + "=" * 60)
    print("CUSTOMER SATISFACTION PREDICTION")
    print("=" * 60)

    print(f"Customer ID : {prediction.customer_id}")
    print(f"Score       : {prediction.score:.2f}")
    print(f"Category    : {prediction.category}")

    confidence_percent = prediction.confidence * 100
    print(f"Confidence  : {confidence_percent:.0f}%")

    print("\nContributing Factors")
    print("-" * 60)

    if prediction.contributing_factors:
        for factor in prediction.contributing_factors:
            print(f"✓ {factor}")
    else:
        print("No contributing factors identified.")

    print("=" * 60)


def main():
    print("\nIC-08 - Milestone 14")
    print("Customer Satisfaction Prediction")
    print("-" * 60)

    service = SatisfactionPredictionService()

    prediction = service.predict(
        customer_id="CUST001",
        feature_adoption_score=92,
        journey_completion_score=80,
        session_activity_score=95,
        feedback_score=75,
        recommendation_score=90,
        history_count=25,
    )

    print_prediction(prediction)

    print("\nRepository Statistics")
    print("-" * 60)

    print(f"Total Predictions : {len(service.get_all_predictions())}")
    print(f"Average Score     : {service.average_satisfaction():.2f}")

    print("\nTop Customers")
    print("-" * 60)

    for index, customer in enumerate(service.top_customers(), start=1):
        print(
            f"{index}. "
            f"{customer.customer_id} "
            f"({customer.score:.2f}) - "
            f"{customer.category}"
        )

    print("\nMilestone 14 completed successfully.")


if __name__ == "__main__":
    main()
