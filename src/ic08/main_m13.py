import logging

from src.ic08.services.churn_prediction_service import (
    ChurnPredictionService,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

logger = logging.getLogger(__name__)


def main():

    logger.info("=" * 60)
    logger.info("IC-08 - Milestone 13")
    logger.info("Churn Prediction using Random Forest")
    logger.info("=" * 60)

    service = ChurnPredictionService()

    logger.info("\nTraining model...")
    service.train_model()

    logger.info("\nModel Summary")
    service.print_model_summary()

    logger.info("\nGenerating Predictions")
    logger.info("-" * 60)

    customers = [

        # customer_id,
        # session_count,
        # total_events,
        # avg_duration,
        # adoption_rate,
        # inactive_days,
        # workflow_completion

        ("C001", 5, 120, 35, 80, 2, 90),

        ("C002", 2, 40, 15, 30, 35, 40),

        ("C003", 8, 260, 60, 96, 1, 98),

        ("C004", 3, 70, 20, 45, 28, 50),

        ("C005", 9, 300, 70, 97, 0, 99)

    ]

    for customer in customers:

        prediction = service.predict(*customer)

        logger.info(
            f"{prediction.customer_id:5}"
            f" -> "
            f"{prediction.risk_level:6}"
            f" "
            f"(Churn Probability: "
            f"{prediction.churn_probability:.2%}, "
            f"Confidence: {prediction.confidence:.2f}%)"
        )

    logger.info("\nStored Predictions")
    logger.info("-" * 60)

    for prediction in service.get_predictions():

        logger.info(prediction)


if __name__ == "__main__":
    main()
