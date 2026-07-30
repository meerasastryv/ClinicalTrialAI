#!/bin/bash

echo "=========================================="
echo " ClinicalTrialAI - Graph Intelligence"
echo "=========================================="

echo ""
echo "Checking project..."

if [ ! -d "platform" ]; then
    echo "ERROR: platform folder not found."
    exit 1
fi

mkdir -p platform/output

echo ""
echo "Backing up graph files..."

FILES=(
platform/graph/dependency_graph.py
platform/graph/dependency_builder.py
platform/graph/cycle_detector.py
platform/graph/graph_statistics.py
platform/graph/graph_exporter.py
platform/reports/dependency_report.py
)

for FILE in "${FILES[@]}"
do
    if [ -f "$FILE" ]; then
        cp "$FILE" "$FILE.bak"
        echo "Backup : $FILE"
    fi
done

echo ""
echo "Graph module ready."
echo ""
echo "Done."
