import logging

from src.ic08.services.behaviour_prediction_service import (
    BehaviourPredictionService,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

logger = logging.getLogger(__name__)


def main():

    logger.info("=" * 60)
    logger.info("IC-08 - Milestone 12")
    logger.info("Behaviour Prediction using Random Forest")
    logger.info("=" * 60)

    service = BehaviourPredictionService()

    logger.info("\nTraining model...")
    service.train_model()

    logger.info("\nModel Summary")
    service.print_model_summary()

    logger.info("\nGenerating Predictions")
    logger.info("-" * 60)

    customers = [

        ("C001", 5, 120, 35, 80),

        ("C002", 2, 40, 15, 30),

        ("C003", 9, 260, 70, 96),

        ("C004", 4, 85, 22, 58),

        ("C005", 8, 300, 65, 94)

    ]

    for customer in customers:

        prediction = service.predict(*customer)

        logger.info(
            f"{prediction.customer_id:5}"
            f" -> "
            f"{prediction.predicted_behaviour:12}"
            f" "
            f"(Confidence: {prediction.confidence:.2f}%)"
        )

    logger.info("\nStored Predictions")
    logger.info("-" * 60)

    for prediction in service.get_predictions():

        logger.info(prediction)


if __name__ == "__main__":
    main()
