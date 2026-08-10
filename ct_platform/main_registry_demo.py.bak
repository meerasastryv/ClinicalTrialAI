from ct_platform.models.engine_metadata import EngineMetadata
from ct_platform.repositories.engine_registry import EngineRegistry


registry = EngineRegistry()

registry.register(
    EngineMetadata(
        engine_id="IC01",
        name="Requirement Intelligence",
        version="1.0",
        description="Requirement Analysis Engine",
        services=["Search", "Classification", "Summary"],
    )
)

registry.register(
    EngineMetadata(
        engine_id="IC08",
        name="Customer Usage Intelligence",
        version="1.0",
        description="Customer Analytics",
        services=["Usage", "Journey", "Recommendation"],
    )
)

for engine in registry.list_all():
    print(engine)
