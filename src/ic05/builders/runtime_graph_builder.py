from src.ic05.services.graph_service import GraphService


class RuntimeGraphBuilder:
    """
    Builds a Knowledge Graph from IC-04 Runtime artifacts.
    """

    def __init__(self):

        self.graph_service = GraphService()

    # ---------------------------------------------------------

    def build(
        self,
        runtime_repository,
        api_call_repository,
        database_query_repository,
    ):

        #
        # Pass 1
        #

        for event in runtime_repository.get_all_events():

            self.add_runtime_event(event)

        #
        # Pass 2
        #

        for api_call in api_call_repository.get_all_api_calls():

            self.add_api_call(api_call)

        #
        # Pass 3
        #

        for query in database_query_repository.get_all_queries():

            self.add_database_query(query)

        return self.graph_service

    # ---------------------------------------------------------

    def add_runtime_event(
        self,
        event,
    ):

        node_id = (
            f"EVENT::{event.trace_id}"
        )

        node = self.graph_service.add_node(
            node_id=node_id,
            node_type="RuntimeEvent",
            name=event.method_name,
        )

        node.source = "IC-04"

        node.add_label("Runtime")

        node.add_tag("Execution")

        node.add_property(
            "Module",
            event.module_name,
        )

        node.add_property(
            "Class",
            event.class_name,
        )

        node.add_property(
            "Method",
            event.method_name,
        )

        node.add_property(
            "Caller",
            event.caller,
        )

        node.add_property(
            "Duration",
            event.duration_ms,
        )

        node.add_property(
            "Status",
            event.status,
        )

    # ---------------------------------------------------------

    def add_api_call(
        self,
        api_call,
    ):

        api_node_id = (
            f"API::{api_call.endpoint}"
        )

        if not self.graph_service.has_node(api_node_id):

            node = self.graph_service.add_node(
                node_id=api_node_id,
                node_type="API",
                name=api_call.endpoint,
            )

            node.source = "IC-04"

            node.add_label("API")

            node.add_tag("Runtime")

            node.add_property(
                "HTTP Method",
                api_call.http_method,
            )

            node.add_property(
                "Duration",
                api_call.duration_ms,
            )

            node.add_property(
                "Status Code",
                api_call.status_code,
            )

        runtime_node = (
            f"EVENT::{api_call.caller_method}"
        )

        if self.graph_service.has_node(runtime_node):

            self.graph_service.add_edge(
                source=runtime_node,
                target=api_node_id,
                relationship="CALLS_API",
            )

    # ---------------------------------------------------------

    def add_database_query(
        self,
        query,
    ):

        query_node_id = (
            f"DB::{query.operation}:{query.table_name}"
        )

        if not self.graph_service.has_node(query_node_id):

            node = self.graph_service.add_node(
                node_id=query_node_id,
                node_type="DatabaseQuery",
                name=query.table_name,
            )

            node.source = "IC-04"

            node.add_label("Database")

            node.add_tag("Runtime")

            node.add_property(
                "Operation",
                query.operation,
            )

            node.add_property(
                "Rows Affected",
                query.rows_affected,
            )

            node.add_property(
                "Duration",
                query.duration_ms,
            )

        runtime_node = (
            f"EVENT::{query.caller_method}"
        )

        if self.graph_service.has_node(runtime_node):

            self.graph_service.add_edge(
                source=runtime_node,
                target=query_node_id,
                relationship="EXECUTES_QUERY",
            )
