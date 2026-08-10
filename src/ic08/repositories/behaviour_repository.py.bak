from typing import List

from src.ic08.models.behaviour_prediction import BehaviourPrediction


class BehaviourRepository:
    """
    Stores behaviour prediction results.
    """

    def __init__(self):
        self._predictions: List[BehaviourPrediction] = []

    def add_prediction(self, prediction: BehaviourPrediction):
        self._predictions.append(prediction)

    def get_all_predictions(self) -> List[BehaviourPrediction]:
        return self._predictions

    def clear(self):
        self._predictions.clear()

    def count(self) -> int:
        return len(self._predictions)
