from src.ic04.models.runtime_event import RuntimeEvent
from src.ic04.repositories.runtime_repository import RuntimeRepository


class RuntimeAnalysisService:
    """
    High-level service for runtime event management.
    """

    def __init__(self):
        self.repository = RuntimeRepository()

    def record_event(self, event: RuntimeEvent):
        """
        Record a runtime event.
        """
        self.repository.add_event(event)

    def get_runtime_events(self):
        """
        Return all captured runtime events.
        """
        return self.repository.get_all_events()

    def get_repository(self):
        """
        Return the underlying RuntimeRepository.
        This is used by analyzers that operate directly
        on the repository.
        """
        return self.repository

    def get_event_count(self):
        """
        Return the total number of captured events.
        """
        return self.repository.size()

    def clear_events(self):
        """
        Remove all captured runtime events.
        """
        self.repository.clear()
