from src.ic04.models.runtime_event import RuntimeEvent
from src.ic04.repositories.runtime_repository import RuntimeRepository


class RuntimeAnalysisService:
    """
    High-level service for runtime event management.
    """

    def __init__(self):
        self.repository = RuntimeRepository()

    def record_event(self, event: RuntimeEvent):
        self.repository.add_event(event)

    def get_runtime_events(self):
        return self.repository.get_all_events()

    def get_event_count(self):
        return self.repository.size()

    def clear_events(self):
        self.repository.clear()
