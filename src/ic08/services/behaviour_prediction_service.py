from typing import List

import numpy as np
from sklearn.ensemble import RandomForestClassifier

from src.ic08.models.behaviour_prediction import BehaviourPrediction
from src.ic08.repositories.behaviour_repository import BehaviourRepository
from sklearn.metrics import accuracy_score
import logging

logger = logging.getLogger(__name__)
POWER_USER = "Power User"
REGULAR_USER = "Regular User"

class BehaviourPredictionService:
    """
    Predicts customer behaviour using a Random Forest classifier.
    """

    def __init__(self):

        self.repository = BehaviourRepository()

        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )


    def prepare_training_data(self):
        """
        Creates a sample training dataset.
        """

        X = np.array([
            [5, 120, 35, 80],
            [2, 40, 15, 30],
            [8, 240, 60, 95],
            [3, 75, 20, 45],
            [10, 350, 75, 98],
            [4, 90, 25, 55],
            [6, 180, 42, 88],
            [1, 20, 8, 15]
        ])

        y = np.array([
            1,
            0,
            1,
            0,
            1,
            0,
            1,
            0
        ])

        return X, y


    def train_model(self):
        """
        Trains the Random Forest model.
        """

        X, y = self.build_training_dataset()
        self.is_model_trained = True
        self.model.fit(X, y)


    def predict(
            self,
            customer_id: str,
            session_count: int,
            total_events: int,
            avg_duration: float,
            adoption_rate: float
    ) -> BehaviourPrediction:
        if not self.is_model_trained:
            raise RuntimeError("Model has not been trained. Call train_model() first.")
        features = np.array([[
            session_count,
            total_events,
            avg_duration,
            adoption_rate
        ]])

        probability = self.model.predict_proba(features)[0][1]

        prediction = POWER_USER 

        if probability < 0.5:
            prediction = REGULAR_USER

        result = BehaviourPrediction(
            customer_id=customer_id,
            predicted_behaviour=prediction,
            probability=float(probability),
            confidence=float(probability * 100),
            explanation="Prediction generated using Random Forest."
        )

        self.repository.add_prediction(result)

        return result
    def build_training_dataset(self):
        """
        Builds the training dataset.(Currently uses synthetic analytics.Later this can be replaced with repository data.)
        """
        X = []
        y = []
        customers = [
            ("C001", 5, 120, 35, 80),
            ("C002", 2, 40, 15, 30),
            ("C003", 8, 240, 60, 95),
            ("C004", 3, 75, 20, 45),
            ("C005", 10, 350, 75, 98),
            ("C006", 4, 90, 25, 55),
            ("C007", 6, 180, 42, 88),
            ("C008", 1, 20, 8, 15)
        ]
        for _, sessions, events, duration, adoption in customers:
            X.append([sessions,events,duration,adoption])
            power_user = ( sessions >= 5 and adoption >= 80)
            y.append(1 if power_user else 0)
        return np.array(X), np.array(y)
    def evaluate_model(self):
        """
        Evaluates the trained model.
        """
        X, y = self.build_training_dataset()
        predictions = self.model.predict(X)
        accuracy = accuracy_score(y, predictions)
        return accuracy

    def get_feature_importance(self):
        feature_names = ["Session Count","Total Events","Average Duration","Feature Adoption"]
        importance = list( zip( feature_names, self.model.feature_importances_ ))
        importance.sort( key=lambda x: x[1], reverse=True)
        return importance
    def get_feature_importance(self):
        feature_names = ["Session Count","Total Events","Average Duration","Feature Adoption"]
        importance = self.model.feature_importances_
        return list(zip(feature_names, importance)) 
    def print_model_summary(self):
        accuracy = self.evaluate_model()
        logger.info("")
        logger.info("Behaviour Prediction Model")
        logger.info("-" * 40)
        logger.info(f"Algorithm : Random Forest")
        logger.info(f"Accuracy  : {accuracy:.2%}")
        logger.info("")
        logger.info("Feature Importance")
        for feature, score in self.get_feature_importance():
            logger.info(f"{feature:<25} {score:.3f}")


    def get_predictions(self):
        return self.repository.get_all_predictions()
