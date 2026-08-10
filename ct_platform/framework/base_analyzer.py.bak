"""
base_analyzer.py

Base class for all Platform Foundation analyzers.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from time import perf_counter

from .analysis_result import AnalysisResult
from .analyzer_context import AnalyzerContext


class BaseAnalyzer(ABC):
    """
    Common execution pipeline for every analyzer.
    """

    def __init__(self, context: AnalyzerContext):

        self.context = context

    def execute(self):

        start = perf_counter()

        result = AnalysisResult(
            analyzer_name=self.__class__.__name__
        )

        try:

            data = self.collect()

            self.analyze(data, result)

            self.finalize(result)

        except Exception as ex:

            result.add_error(str(ex))

        result.execution_time = perf_counter() - start

        result.generated_at = datetime.now().isoformat()

        return result

    @abstractmethod
    def collect(self):
        """
        Collect raw data.
        """

    @abstractmethod
    def analyze(self, data, result: AnalysisResult):
        """
        Populate AnalysisResult.
        """

    def finalize(self, result: AnalysisResult):
        """
        Optional hook for subclasses.
        """
        pass
