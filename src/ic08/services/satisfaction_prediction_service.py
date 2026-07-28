"""
IC-08 - Customer Usage Intelligence
Milestone 14 - Satisfaction Prediction Service
"""

from src.ic08.models.satisfaction_prediction import SatisfactionPrediction
from src.ic08.repositories.satisfaction_repository import (
    SatisfactionRepository,
)


class SatisfactionPredictionService:
    """
    AI service for predicting customer satisfaction.
    """

    def __init__(self):
        self.repository = SatisfactionRepository()

    def predict(
        self,
        customer_id: str,
        feature_adoption_score: float,
        journey_completion_score: float,
        session_activity_score: float,
        feedback_score: float,
        recommendation_score: float,
        history_count: int,
    ) -> SatisfactionPrediction:
        """
        Predict customer satisfaction using weighted analytics.
        """

        score = (
            feature_adoption_score * 0.30
            + journey_completion_score * 0.25
            + session_activity_score * 0.20
            + feedback_score * 0.15
            + recommendation_score * 0.10
        )

        score = round(score, 2)

        category = self._determine_category(score)
        confidence = self._determine_confidence(history_count)

        prediction = SatisfactionPrediction(
            customer_id=customer_id,
            score=score,
            confidence=confidence,
            category=category,
        )

        self._add_contributing_factors(
            prediction,
            feature_adoption_score,
            journey_completion_score,
            session_activity_score,
            feedback_score,
            recommendation_score,
        )

        self.repository.save(prediction)

        return prediction

    def get_prediction(self, customer_id: str):
        """
        Retrieve an existing prediction.
        """
        return self.repository.find_by_customer(customer_id)

    def get_all_predictions(self):
        """
        Return all stored predictions.
        """
        return self.repository.find_all()

    def average_satisfaction(self) -> float:
        """
        Return average satisfaction score.
        """
        return self.repository.average_score()

    def top_customers(self, limit: int = 5):
        """
        Return top satisfied customers.
        """
        return self.repository.top_customers(limit)

    def _determine_category(self, score: float) -> str:
        """
        Determine satisfaction category.
        """

        if score >= 90:
            return "Excellent"

        if score >= 80:
            return "Highly Satisfied"

        if score >= 70:
            return "Satisfied"

        if score >= 60:
            return "Neutral"

        return "At Risk"

    def _determine_confidence(self, history_count: int) -> float:
        """
        Estimate prediction confidence.
        """

        if history_count >= 20:
            return 0.95

        if history_count >= 10:
            return 0.80

        return 0.60

    def _add_contributing_factors(
        self,
        prediction: SatisfactionPrediction,
        feature_adoption_score: float,
        journey_completion_score: float,
        session_activity_score: float,
        feedback_score: float,
        recommendation_score: float,
    ):
        """
        Identify positive contributing factors.
        """

        if feature_adoption_score >= 80:
            prediction.add_factor("High Feature Adoption")

        if journey_completion_score >= 80:
            prediction.add_factor("Strong Journey Completion")

        if session_activity_score >= 80:
            prediction.add_factor("Frequent Product Usage")

        if feedback_score >= 80:
            prediction.add_factor("Positive Customer Feedback")

        if recommendation_score >= 80:
            prediction.add_factor("Recommendation Acceptance")

        if not prediction.contributing_factors:
            prediction.add_factor("Limited Positive Indicators")
