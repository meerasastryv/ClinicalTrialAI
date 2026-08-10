from ct_platform.repositories.engine_registry import EngineRegistry
from ct_platform.services.engine_discovery_service import EngineDiscoveryService


registry = EngineRegistry()

discovery = EngineDiscoveryService(registry)

discovery.discover()

print("\nDiscovered Engines\n")

for engine in registry.list_all():
    print(engine)
