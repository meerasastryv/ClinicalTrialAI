#!/bin/bash

echo "=========================================="
echo " ClinicalTrialAI Platform Foundation Setup"
echo "=========================================="

echo ""
echo "Creating folders..."

mkdir -p platform/core
mkdir -p platform/graph
mkdir -p platform/models
mkdir -p platform/reports
mkdir -p platform/output

echo "Creating __init__.py files..."

touch platform/core/__init__.py
touch platform/graph/__init__.py
touch platform/models/__init__.py
touch platform/reports/__init__.py

echo "Creating core files..."

touch platform/core/platform_context.py
touch platform/core/project_scanner.py
touch platform/core/dependency_inspector.py
touch platform/core/dependency_resolver.py
touch platform/core/registry_builder.py
touch platform/core/engine_generator.py

echo "Creating graph files..."

touch platform/graph/dependency_graph.py
touch platform/graph/dependency_node.py
touch platform/graph/dependency_edge.py
touch platform/graph/dependency_builder.py
touch platform/graph/cycle_detector.py
touch platform/graph/graph_exporter.py
touch platform/graph/graph_statistics.py

echo "Creating model files..."

touch platform/models/module_info.py

echo "Creating report files..."

touch platform/reports/dependency_report.py

echo "Creating entry point..."

touch platform/main.py

echo ""
echo "Backing up existing files..."

FILES=(
platform/project_scanner.py
platform/dependency_inspector.py
platform/dependency_builder.py
platform/dependency_graph.py
platform/module_info.py
)

for FILE in "${FILES[@]}"
do
    if [ -f "$FILE" ]; then
        cp "$FILE" "$FILE.bak"
        echo "Backup created: $FILE.bak"
    fi
done

echo ""
echo "Directory Structure"

find platform -type f | sort

echo ""
echo "Setup Complete."
