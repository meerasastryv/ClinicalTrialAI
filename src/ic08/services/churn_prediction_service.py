from typing import List

import logging
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from src.ic08.models.churn_prediction import ChurnPrediction
from src.ic08.repositories.churn_repository import ChurnRepository


logger = logging.getLogger(__name__)


class ChurnPredictionService:
    """
    Predicts customer churn using a Random Forest classifier.
    """

    def __init__(self):

        self.repository = ChurnRepository()

        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        self.is_model_trained = False

    # ----------------------------------------------------------
    # Training Dataset
    # ----------------------------------------------------------

    def build_training_dataset(self):
        """
        Creates a synthetic training dataset.
        """

        customers = [

            # sessions, events, duration,
            # adoption, inactive_days,
            # workflow_completion, churn

            (5, 120, 35, 80, 2, 90, 0),

            (2, 40, 15, 30, 35, 40, 1),

            (8, 240, 60, 95, 1, 98, 0),

            (3, 75, 20, 45, 28, 55, 1),

            (10, 350, 75, 98, 0, 99, 0),

            (4, 90, 25, 55, 18, 60, 1),

            (6, 180, 42, 88, 3, 92, 0),

            (1, 20, 8, 15, 45, 20, 1)

        ]

        X = []
        y = []

        for (
            sessions,
            events,
            duration,
            adoption,
            inactive_days,
            workflow_completion,
            churn
        ) in customers:

            X.append([
                sessions,
                events,
                duration,
                adoption,
                inactive_days,
                workflow_completion
            ])

            y.append(churn)

        return np.array(X), np.array(y)

    # ----------------------------------------------------------
    # Train Model
    # ----------------------------------------------------------

    def train_model(self):

        X, y = self.build_training_dataset()

        self.model.fit(X, y)

        self.is_model_trained = True

    # ----------------------------------------------------------
    # Evaluate
    # ----------------------------------------------------------

    def evaluate_model(self):

        X, y = self.build_training_dataset()

        predictions = self.model.predict(X)

        return accuracy_score(y, predictions)

    # ----------------------------------------------------------
    # Feature Importance
    # ----------------------------------------------------------

    def get_feature_importance(self):

        feature_names = [

            "Session Count",

            "Total Events",

            "Average Duration",

            "Feature Adoption",

            "Inactive Days",

            "Workflow Completion"

        ]

        importance = list(
            zip(
                feature_names,
                self.model.feature_importances_
            )
        )

        importance.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return importance

    # ----------------------------------------------------------
    # Model Summary
    # ----------------------------------------------------------

    def print_model_summary(self):

        accuracy = self.evaluate_model()

        logger.info("")
        logger.info("Churn Prediction Model")
        logger.info("-" * 40)

        logger.info("Algorithm : Random Forest")

        logger.info(f"Accuracy  : {accuracy:.2%}")

        logger.info("")
        logger.info("Feature Importance")

        for feature, score in self.get_feature_importance():

            logger.info(f"{feature:<25} {score:.3f}")


    # ----------------------------------------------------------
    # Predict Churn
    # ----------------------------------------------------------

    def predict(
            self,
            customer_id: str,
            session_count: int,
            total_events: int,
            avg_duration: float,
            adoption_rate: float,
            inactive_days: int,
            workflow_completion: float
    ) -> ChurnPrediction:

        if not self.is_model_trained:
            raise RuntimeError(
                "Model has not been trained. Call train_model() first."
            )

        features = np.array([[
            session_count,
            total_events,
            avg_duration,
            adoption_rate,
            inactive_days,
            workflow_completion
        ]])

        probability = float(
            self.model.predict_proba(features)[0][1]
        )

        if probability >= 0.80:
            risk = "HIGH"
        elif probability >= 0.50:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        result = ChurnPrediction(
            customer_id=customer_id,
            churn_probability=probability,
            risk_level=risk,
            confidence=probability * 100,
            explanation="Prediction generated using Random Forest."
        )

        self.repository.add_prediction(result)

        return result

    # ----------------------------------------------------------
    # Repository
    # ----------------------------------------------------------

    def get_predictions(self):

        return self.repository.get_all_predictions()

    def clear_predictions(self):

        self.repository.clear()

    def prediction_count(self):

        return self.repository.count()
