"""
trend.py

Trend model for the Customer Usage Intelligence Engine.

Represents historical trends for customer usage metrics. Trend analysis
helps identify growth, decline, seasonality, and long-term usage patterns
that support forecasting and strategic decision-making.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Trend:
    """
    Represents a historical trend for a usage metric.
    """

    metric_name: str

    time_period: str

    values: list[float] = field(default_factory=list)

    trend_direction: str = "Stable"

    growth_percentage: float = 0.0

    moving_average: float = 0.0

    generated_at: datetime = field(default_factory=datetime.utcnow)

    def add_value(self, value: float) -> None:
        """
        Adds a metric value and recalculates the moving average.
        """
        self.values.append(value)
        self._calculate_moving_average()

    def _calculate_moving_average(self) -> None:
        """
        Calculates the moving average of the collected values.
        """
        if not self.values:
            self.moving_average = 0.0
            return

        self.moving_average = sum(self.values) / len(self.values)

    def update_growth_percentage(
        self,
        previous_value: float,
        current_value: float,
    ) -> None:
        """
        Updates the percentage growth between two values.
        """
        if previous_value == 0:
            self.growth_percentage = 0.0
        else:
            self.growth_percentage = (
                (current_value - previous_value) / previous_value
            ) * 100

        if self.growth_percentage > 0:
            self.trend_direction = "Increasing"
        elif self.growth_percentage < 0:
            self.trend_direction = "Decreasing"
        else:
            self.trend_direction = "Stable"
