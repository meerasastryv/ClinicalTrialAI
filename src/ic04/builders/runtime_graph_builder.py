from src.ic04.repositories.runtime_graph_repository import (
    RuntimeGraphRepository,
)


class RuntimeGraphBuilder:
    """
    Builds a runtime call graph from runtime events.
    """

    def __init__(self):

        self.repository = RuntimeGraphRepository()

    def build(self, runtime_events):

        for event in runtime_events:

            if (
                event.event_type == "METHOD_END"
                and event.caller is not None
            ):

                self.repository.add_relationship(
                    caller=event.caller,
                    callee=event.method_name,
                    duration_ms=event.duration_ms or 0.0,
                )

        return self.repository
