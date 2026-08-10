from dataclasses import dataclass


@dataclass
class ChurnPrediction:
    """
    Stores churn prediction results for a customer.
    """

    customer_id: str

    churn_probability: float

    risk_level: str

    confidence: float

    model_name: str = "Random Forest"

    explanation: str = ""
