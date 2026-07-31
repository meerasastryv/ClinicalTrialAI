from platform.services.engine_loader import EngineLoader

loader = EngineLoader()
registry = loader.load()

print("\n========== Registered Engines ==========\n")

for engine in registry.list_all():

    print(f"Engine        : {engine.engine_id}")
    print(f"Name          : {engine.name}")
    print(f"Python Files  : {engine.file_count}")
    print(f"Services      : {len(engine.services)}")
    print(f"Repositories  : {len(engine.repositories)}")
    print(f"Models        : {len(engine.models)}")
    print(f"Generators    : {len(engine.generators)}")
    print(f"Analyzers     : {len(engine.analyzers)}")
    print(f"Main Files    : {engine.main_files}")
    print(f"README Exists : {engine.readme}")
    print("-" * 50)
