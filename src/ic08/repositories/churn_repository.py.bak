from typing import List

from src.ic08.models.churn_prediction import ChurnPrediction


class ChurnRepository:
    """
    Stores churn prediction results.
    """

    def __init__(self):

        self._predictions: List[ChurnPrediction] = []

    def add_prediction(self, prediction: ChurnPrediction):

        self._predictions.append(prediction)

    def get_all_predictions(self):

        return self._predictions

    def clear(self):

        self._predictions.clear()

    def count(self):

        return len(self._predictions)
