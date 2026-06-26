# IC-02 Milestone 4 – Boundary Value Generator (BVA)

## ClinicalTrialAI – AI-Enabled Quality Engineering Platform

### Overview

The Boundary Value Generator (BVA) is the fourth milestone of the IC-02 Test Design Engine within the ClinicalTrialAI platform.

This component automatically detects boundary constraints from natural language requirements and generates Boundary Value Analysis (BVA) test cases.

Instead of manually identifying minimum and maximum values, the engine extracts constraints, applies Boundary Value Analysis rules, and produces executable test cases together with machine-readable JSON output.

---

# Objectives

The Boundary Value Generator is designed to:

* Detect boundary constraints from natural language requirements.
* Generate standard Boundary Value Analysis (BVA) values.
* Automatically create executable boundary test cases.
* Export results to JSON.
* Serve as a reusable component within the ClinicalTrialAI platform.

---

# Features

* Natural language boundary detection
* Boundary Value Analysis rule engine
* Automatic test case generation
* JSON export
* Automated unit testing
* Modular architecture
* Extensible design

---

# Supported Requirement Patterns

Examples of supported requirements:

```
Age should be between 18 and 60.

Password length should be 8-20 characters.

Quantity should be at least 1.

Discount should be at most 50.
```

---

# Project Structure

```
src/ic02/

├── boundary_models.py
├── boundary_detector.py
├── boundary_rules.py
├── boundary_value_generator.py
├── boundary_exporter.py
├── test_boundary_generator.py
├── sample_requirements/
├── output/
│   └── boundary_analysis.json
└── README.md
```

---

# Architecture

```
Natural Language Requirement
               │
               ▼
      BoundaryDetector
               │
               ▼
     BoundaryConstraint
               │
               ▼
     BoundaryRuleEngine
               │
               ▼
     Boundary Values
               │
               ▼
 Boundary Test Case Builder
               │
               ▼
 BoundaryAnalysisResult
               │
               ▼
     BoundaryExporter
               │
               ▼
boundary_analysis.json
```

---

# Components

## boundary_detector.py

Extracts minimum and maximum boundary constraints from natural language requirements.

---

## boundary_rules.py

Generates Boundary Value Analysis values.

Example:

```
Minimum = 18

Maximum = 60
```

Produces:

```
17
18
19
39
59
60
61
```

---

## boundary_value_generator.py

Acts as the Facade for the complete Boundary Value Analysis workflow.

Responsibilities:

* Detect boundaries
* Generate boundary values
* Create test cases
* Return BoundaryAnalysisResult

---

## boundary_exporter.py

Exports BoundaryAnalysisResult into formatted JSON.

---

## test_boundary_generator.py

Contains automated tests verifying:

* Boundary detection
* Rule engine
* Test case generation
* Complete workflow

---

# Example Output

Requirement

```
Age should be between 18 and 60.
```

Generated Boundary Values

| Label   | Value | Expected |
| ------- | ----: | -------- |
| Min-1   |    17 | Rejected |
| Min     |    18 | Accepted |
| Min+1   |    19 | Accepted |
| Nominal |    39 | Accepted |
| Max-1   |    59 | Accepted |
| Max     |    60 | Accepted |
| Max+1   |    61 | Rejected |

---

# JSON Output

The generator exports:

```
src/ic02/output/boundary_analysis.json
```

The JSON contains:

* Boundary constraint
* Boundary values
* Generated test cases

---

# Running the Component

Run the Boundary Generator:

```bash
python src/ic02/boundary_value_generator.py
```

Run Unit Tests:

```bash
python src/ic02/test_boundary_generator.py
```

---

# Design Principles

The implementation follows:

* Single Responsibility Principle (SRP)
* Facade Pattern
* Modular architecture
* Dataclass-based domain models
* Separation of concerns
* Reusable components
* Extensible design

---

# Future Enhancements

Planned improvements include:

* Decimal boundary detection
* Date boundary analysis
* Time boundary analysis
* Currency boundary analysis
* File size boundaries
* Clinical visit number boundaries
* Protocol version boundaries
* AI-assisted boundary extraction using LLMs
* Integration with IC-01 Requirement Intelligence Engine
* Integration with Decision Table Generator
* Integration with State Transition Generator

---

# Milestone Status

Milestone 4 has successfully implemented:

* Boundary Detection
* Boundary Rule Engine
* Boundary Value Generation
* Automatic Test Case Generation
* JSON Export
* Automated Unit Testing

---

# Author

Meera Sastry

ClinicalTrialAI

AI-Enabled Quality Engineering Platform

IC-02 Test Design Engine

Milestone 4 – Boundary Value Generator

