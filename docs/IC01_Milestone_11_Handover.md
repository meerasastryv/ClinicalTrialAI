# IC-01 Milestone 11 – Explainable RAG Requirement Assistant

## Handover Document

### Project

AI-Enabled Quality Engineering Platform

### Intelligence Component

IC-01 – Requirement Intelligence Engine

### Milestone

Milestone 11 – Explainable RAG Requirement Assistant with Requirement Traceability

### Completion Date

24-Jun-2026

---

# Objective

Enhance the Requirement Intelligence Engine with Retrieval-Augmented Generation (RAG) capabilities to enable intelligent question answering over the requirement repository while ensuring traceability and reducing hallucinations.

---

# Scope Completed

## Requirement Repository Integration

Integrated the Requirement Intelligence Engine with ChromaDB vector storage.

Capabilities:

* Requirement embedding generation
* Persistent vector storage
* Semantic similarity search
* Context retrieval for user questions

---

## RAG-Based Requirement Assistant

Implemented an interactive requirement assistant using:

### Embedding Model

```text
all-MiniLM-L6-v2
```

### Vector Database

```text
ChromaDB
```

### Large Language Model

```text
Llama 3 8B
```

### Local Inference Engine

```text
Ollama
```

---

# Implemented Workflow

```text
User Question
      |
      v
Generate Embedding
      |
      v
Semantic Search in ChromaDB
      |
      v
Retrieve Relevant Requirements
      |
      v
Build Context
      |
      v
Prompt Llama 3
      |
      v
Generate Answer
      |
      v
Display Sources
```

---

# Hallucination Control

Prompt engineering was implemented to reduce unsupported answers.

The assistant is instructed to:

* Use only retrieved requirements
* Avoid external knowledge
* Avoid guessing
* Avoid inference beyond requirements
* Return a standard response when information is unavailable

Standard response:

```text
Information not available in the current requirement repository.
```

---

# Explainable AI Enhancement

Requirement traceability was added.

For every generated answer, the assistant displays:

* Retrieved requirement IDs
* Source requirements used during context generation

Example:

```text
Question:
What authentication method is used?

Answer:
Single Sign-On using SAML and OAuth2.

Sources:
SPA-FRD001
SPA-BRD001
SPA-TST001
```

---

# Files Updated

## New / Enhanced Components

```text
src/ic01/rag_assistant.py
```

Capabilities:

* Context retrieval
* Context construction
* LLM interaction
* Requirement traceability
* Interactive question answering

---

# Validation Performed

## Query 1

```text
What authentication method is used?
```

Result:

```text
Single Sign-On using SAML and OAuth2
```

Status:

```text
PASS
```

---

## Query 2

```text
What user roles are available?
```

Result:

```text
Information not available in the current requirement repository.
```

Status:

```text
PASS
```

---

## Query 3

```text
What security controls exist?
```

Result:

Retrieved authentication and authorization controls from requirements.

Status:

```text
PASS
```

---

## Query 4

```text
What is the maximum file upload size?
```

Result:

```text
Information not available in the current requirement repository.
```

Status:

```text
PASS
```

---

# Git Commit

```text
Milestone 11: Added requirement traceability to RAG assistant
```

Commit ID:

```text
b7d6184
```

---

# Current IC-01 Status

Completed Milestones:

```text
M1  Requirement Search Engine
M2  Requirement Quality Analyzer
M3  Requirement Classification Engine
M4  Metadata Extraction Engine
M5  Relationship Discovery Engine
M6  Acceptance Criteria Generator
M7  Requirement Summary Engine
M8  Documentation & Structure
M9  Vector Database Integration
M10 RAG Requirement Assistant
M11 Explainable RAG with Traceability
```

Status:

```text
IC-01 Phase 1 MVP COMPLETE
```

---

# Key Achievements

* Requirement intelligence repository established
* Semantic search implemented
* Vector database integrated
* Local LLM integration completed
* RAG question answering operational
* Hallucination reduction implemented
* Requirement traceability implemented
* Explainable AI capability introduced

---

# Recommended Next Steps

## Option A – Advanced RAG Enhancements

* Similarity score display
* Confidence scoring
* Source ranking
* Top-k retrieval optimization
* Hybrid search

## Option B – IC-02 Test Design Engine

Start implementation of:

* Requirement-to-Test-Case Generation
* Positive Test Scenarios
* Negative Test Scenarios
* Boundary Value Tests
* Risk-Based Test Suggestions
* Test Coverage Metrics

Recommended Path:

```text
Begin IC-02 Test Design Engine
```

---

# Milestone Conclusion

Milestone 11 successfully transformed the Requirement Intelligence Engine into an Explainable Retrieval-Augmented Generation (RAG) platform capable of answering requirement-related questions using locally hosted LLMs while providing traceable evidence for generated responses.

IC-01 Phase 1 MVP is complete and ready for extension into downstream Quality Engineering Intelligence Components.

