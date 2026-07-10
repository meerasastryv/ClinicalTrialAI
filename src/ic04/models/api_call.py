from dataclasses import dataclass


@dataclass
class ApiCall:
    """
    Represents an outbound API call.
    """

    endpoint: str

    http_method: str

    response_code: int

    duration_ms: float
