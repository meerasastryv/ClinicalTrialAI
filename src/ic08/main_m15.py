"""
IC-08 - Customer Usage Intelligence
Milestone 15 - Customer Churn Prediction
"""

import logging

from src.ic08.services.churn_prediction_service import (
    ChurnPredictionService,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

logger = logging.getLogger(__name__)


def print_prediction(prediction):
    """
    Display a churn prediction.
    """

    logger.info("")
    logger.info("=" * 60)
    logger.info("CUSTOMER CHURN PREDICTION")
    logger.info("=" * 60)

    logger.info(f"Customer ID         : {prediction.customer_id}")

    logger.info(
        f"Churn Probability   : "
        f"{prediction.churn_probability:.2%}"
    )

    logger.info(
        f"Risk Level          : "
        f"{prediction.risk_level}"
    )

    logger.info(
        f"Confidence          : "
        f"{prediction.confidence:.2f}%"
    )

    logger.info(
        f"Model               : "
        f"{prediction.model_name}"
    )

    logger.info(
        f"Explanation         : "
        f"{prediction.explanation}"
    )

    logger.info("=" * 60)


def main():

    logger.info("")
    logger.info("IC-08 - Milestone 15")
    logger.info("Customer Churn Prediction")
    logger.info("-" * 60)

    service = ChurnPredictionService()

    #
    # Train ML Model
    #
    logger.info("")
    logger.info("Training Random Forest model...")

    service.train_model()

    logger.info("Training completed successfully.")

    #
    # Model Summary
    #
    logger.info("")
    service.print_model_summary()

    #
    # Predict for Sample Customer
    #
    prediction = service.predict(
        customer_id="CUST001",
        session_count=3,
        total_events=70,
        avg_duration=18,
        adoption_rate=42,
        inactive_days=26,
        workflow_completion=48
    )

    print_prediction(prediction)

    #
    # Repository Statistics
    #
    logger.info("")
    logger.info("Repository Statistics")
    logger.info("-" * 60)

    logger.info(
        f"Stored Predictions : "
        f"{service.prediction_count()}"
    )

    logger.info("")

    logger.info("Prediction History")

    for result in service.get_predictions():

        logger.info(
            f"{result.customer_id:<10}"
            f"{result.churn_probability:.2%}"
            f"   {result.risk_level}"
        )

    logger.info("")
    logger.info("Milestone 15 completed successfully.")


if __name__ == "__main__":
    main()
