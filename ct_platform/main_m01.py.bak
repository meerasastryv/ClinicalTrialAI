from ct_platform.dependency_inspector import DependencyInspector


def main():

    inspector = DependencyInspector()

    modules = inspector.scan()

    print("=" * 70)
    print("ClinicalTrialAI Platform Foundation")
    print("=" * 70)

    print(f"\nModules discovered: {len(modules)}\n")
    for module in modules:
        print("=" * 80)
        print(module)
        print(f"\nImports ({len(module.imports)})")
        for imp in module.imports:
            print(f"   • {imp}")
        print(f"\nClasses ({len(module.classes)})")
        for cls in module.classes:
            print(f"   • {cls}")
        print(f"\nFunctions ({len(module.functions)})")
        for func in module.functions:
            print(f"   • {func}")
        print(f"\nMethods ({len(module.methods)})")
        for method in module.methods:
            print(f"   • {method}")
        print()

if __name__ == "__main__":
    main()
