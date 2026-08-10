from ct_platform.repositories.engine_registry import EngineRegistry
from ct_platform.services.engine_discovery_service import EngineDiscoveryService
from ct_platform.services.manifest_reader import ManifestReader
from ct_platform.services.engine_validator import EngineValidator


class EngineLoader:
    """
    Coordinates discovery, validation and registration.
    """

    def __init__(self):

        self.registry = EngineRegistry()

        self.discovery = EngineDiscoveryService(
            self.registry
        )

        self.reader = ManifestReader()

        self.validator = EngineValidator()

    def load(self):

        discovered = self.discovery.discover_folders()

        for folder in discovered:

            metadata = self.reader.read(folder)

            self.validator.validate(metadata)

            self.registry.register(metadata)

        return self.registry
