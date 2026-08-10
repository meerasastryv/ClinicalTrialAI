from ct_platform.models.engine_metadata import EngineMetadata


class EngineValidator:
    """
    Validates an engine before registration.
    """

    def validate(self, metadata: EngineMetadata):

        if not metadata.engine_id:
            raise ValueError("Engine ID cannot be empty.")

        if not metadata.version:
            raise ValueError(
                f"{metadata.engine_id}: version missing."
            )

        return True
