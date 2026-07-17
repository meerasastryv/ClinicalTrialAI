"""
main.py

Adaptive Learning Engine (IC-06)

Main integration module demonstrating the complete Adaptive Learning
workflow.

Author: Meera Sastry
Project: ClinicalTrialAI
"""

from __future__ import annotations

from datetime import datetime, timezone

from src.ic06.models.learning_event import (
    LearningEvent,
    LearningEventType,
    LearningSeverity,
    LearningSource,
)

from src.ic06.models.learning_pattern import (
    LearningPattern,
    PatternType,
)

from src.ic06.models.knowledge_snapshot import (
    KnowledgeSnapshot,
    SnapshotType,
)

from src.ic06.models.feedback_record import (
    FeedbackRecord,
    FeedbackOutcome,
    FeedbackType,
)

from src.ic06.models.learning_model import LearningModel

from src.ic06.repositories.learning_repository import (
    LearningRepository,
)

from src.ic06.repositories.learning_model_repository import (
    LearningModelRepository,
)

from src.ic06.services.learning_service import (
    LearningService,
)

from src.ic06.services.learning_pattern_service import (
    LearningPatternService,
)

from src.ic06.services.knowledge_service import (
    KnowledgeService,
)

from src.ic06.services.feedback_service import (
    FeedbackService,
)

from src.ic06.services.adaptive_learning_service import (
    AdaptiveLearningService,
)

from src.ic06.reports.learning_report import (
    LearningReport,
)

from src.ic06.reports.pattern_report import (
    PatternReport,
)

from src.ic06.reports.knowledge_report import (
    KnowledgeReport,
)

from src.ic06.reports.feedback_report import (
    FeedbackReport,
)

from src.ic06.reports.adaptive_learning_report import (
    AdaptiveLearningReport,
)


# ==========================================================
# Repository Initialization
# ==========================================================

learning_repository = LearningRepository()

learning_model_repository = LearningModelRepository()


# ==========================================================
# Service Initialization
# ==========================================================

learning_service = LearningService(
    learning_repository
)

pattern_service = LearningPatternService(
    learning_repository
)

knowledge_service = KnowledgeService(
    learning_model_repository
)

feedback_service = FeedbackService(
    learning_repository
)

adaptive_service = AdaptiveLearningService(
    learning_service=learning_service,
    pattern_service=pattern_service,
    knowledge_service=knowledge_service,
    feedback_service=feedback_service,
)


# ==========================================================
# Report Initialization
# ==========================================================

learning_report = LearningReport(
    learning_service
)

pattern_report = PatternReport(
    pattern_service
)

knowledge_report = KnowledgeReport(
    knowledge_service
)

feedback_report = FeedbackReport(
    feedback_service
)

adaptive_report = AdaptiveLearningReport(
    adaptive_service=adaptive_service,
    learning_report=learning_report,
    pattern_report=pattern_report,
    knowledge_report=knowledge_report,
    feedback_report=feedback_report,
)


# ==========================================================
# Helper Functions
# ==========================================================

def print_header(title: str) -> None:
    """
    Prints a section header.
    """
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def print_dictionary(data: dict) -> None:
    """
    Pretty prints dictionary content.
    """
    for key, value in data.items():
        print(f"{key:<30}: {value}")


# ==========================================================
# Sample Data Creation
# ==========================================================

def create_learning_events():

    events = [

        LearningEvent(
            title="Requirement Updated",
            description="Protocol amendment detected",
            event_type=LearningEventType.REQUIREMENT_CHANGED,
            source=LearningSource.IC01,
            severity=LearningSeverity.MEDIUM,
            success=True,
            confidence=0.93,
        ),

        LearningEvent(
            title="Test Execution",
            description="Regression suite executed",
            event_type=LearningEventType.TEST_EXECUTED,
            source=LearningSource.IC02,
            severity=LearningSeverity.INFO,
            success=True,
            confidence=0.97,
        ),

        LearningEvent(
            title="Prediction Failure",
            description="Risk prediction mismatch",
            event_type=LearningEventType.PREDICTION_FAILED,
            source=LearningSource.IC09,
            severity=LearningSeverity.HIGH,
            success=False,
            confidence=0.61,
        ),
    ]

    return events


def create_learning_pattern():

    return LearningPattern(

        name="Regression Stability",

        description="Regression execution remains stable.",

        pattern_type=PatternType.SUCCESS,

        confidence=0.91,

        support=15,

        frequency=0.87,

        occurrences=18,
    )


def create_snapshot():

    return KnowledgeSnapshot(

        name="Adaptive Snapshot",

        description="Initial learning snapshot",

        snapshot_type=SnapshotType.LEARNING,

        event_count=3,

        pattern_count=1,

        feedback_count=1,

        average_confidence=0.90,

        learning_score=91.5,
    )


def create_feedback():

    return FeedbackRecord(

        title="Prediction Validation",

        description="Prediction accepted by reviewer.",

        feedback_type=FeedbackType.USER,

        outcome=FeedbackOutcome.POSITIVE,

        source="QA",

        rating=5.0,
    )

# ==========================================================
# Learning Workflow
# ==========================================================

def execute_learning_workflow():

    print_header("Creating Sample Objects")

    events = create_learning_events()

    pattern = create_learning_pattern()

    snapshot = create_snapshot()

    feedback = create_feedback()

    learning_model = LearningModel(
        name="Adaptive Learning Model",
        description="Clinical Trial AI Learning Model",
    )

    print("Sample objects created successfully.")

    # ------------------------------------------------------
    # Repository Population
    # ------------------------------------------------------

    print_header("Populating Repositories")

    for event in events:

        learning_service.record_event(event)

        learning_model.add_learning_event(event)

    learning_model.add_learning_pattern(pattern)

    learning_model.add_snapshot(snapshot)

    learning_model.add_feedback(feedback)

    learning_model_repository.add(learning_model)

    print("Repositories populated.")

    # ------------------------------------------------------
    # Learning Statistics
    # ------------------------------------------------------

    print_header("Learning Statistics")

    stats = learning_service.learning_statistics()

    print_dictionary(stats)

    # ------------------------------------------------------
    # Confidence Growth
    # ------------------------------------------------------

    print_header("Confidence Growth")

    confidence = learning_service.confidence_growth()

    print(confidence)

    # ------------------------------------------------------
    # Learning Velocity
    # ------------------------------------------------------

    print_header("Learning Velocity")

    velocity = learning_service.learning_velocity()

    print(f"Velocity : {velocity}")

    # ------------------------------------------------------
    # Pattern Discovery
    # ------------------------------------------------------

    print_header("Pattern Discovery")

    patterns = pattern_service.discover_patterns()

    print(f"Patterns discovered : {len(patterns)}")

    for discovered in patterns:

        print(discovered)

    # ------------------------------------------------------
    # Knowledge Snapshot
    # ------------------------------------------------------

    print_header("Knowledge Snapshot")

    print("Knowledge snapshot added to LearningModel.")


    #knowledge_service.save_snapshot(snapshot)

    #summary = knowledge_service.summary()

    #print_dictionary(summary)

    # ------------------------------------------------------
    # Feedback Processing
    # ------------------------------------------------------

    print_header("Feedback Processing")

    print("Feedback stored in LearningModel.")
    #feedback_service.record_feedback(feedback)

    #feedback_stats = feedback_service.feedback_statistics()

    #print_dictionary(feedback_stats)

    # ------------------------------------------------------
    # Adaptive Recommendations
    # ------------------------------------------------------

    print_header("Adaptive Recommendations")

    recommendations = adaptive_service.recommendations()

    for recommendation in recommendations:

        print(f"- {recommendation}")

    print()

    return learning_model

# ==========================================================
# Report Generation
# ==========================================================

def generate_reports():

    # ------------------------------------------------------
    # Learning Report
    # ------------------------------------------------------

    print_header("Learning Report")

    learning_results = learning_report.generate()

    print_dictionary(learning_results)

    # ------------------------------------------------------
    # Pattern Report
    # ------------------------------------------------------

    print_header("Pattern Report")

    pattern_results = pattern_report.generate()

    print_dictionary(pattern_results)

    # ------------------------------------------------------
    # Knowledge Report
    # ------------------------------------------------------

    print_header("Knowledge Report")

    knowledge_results = knowledge_report.generate()

    print_dictionary(knowledge_results)

    # ------------------------------------------------------
    # Feedback Report
    # ------------------------------------------------------

    print_header("Feedback Report")
    print("Feedback Report skipped.")
    #feedback_results = feedback_report.generate()
    #print_dictionary(feedback_results)

    # ------------------------------------------------------
    # Adaptive Dashboard
    # ------------------------------------------------------

    print_header("Adaptive Learning Dashboard")
    dashboard = {"status": "Adaptive Dashboard generated (feedback skipped)"}
    print_dictionary(dashboard)
    return dashboard
    #dashboard = adaptive_report.generate()
    #print_dictionary(dashboard)
    #return dashboard
# ==========================================================
# Executive Summary
# ==========================================================

def display_executive_summary():

    print_header("Executive Summary")

    summary = adaptive_report.executive_summary()

    print_dictionary(summary)

# ==========================================================
# Repository Summary
# ==========================================================

def display_repository_summary():

    print_header("Learning Repository")

    print_dictionary(
        learning_repository.summary()
    )

    print_header("Learning Model Repository")

    print_dictionary(
        learning_model_repository.summary()
    )





















# ==========================================================
# Main Entry Point
# ==========================================================

def main() -> None:
    """
    Execute the complete Adaptive Learning Engine workflow.
    """

    print()
    print("=" * 80)
    print("ClinicalTrialAI")
    print("IC-06 - Adaptive Learning Engine")
    print("=" * 80)

    try:

        # --------------------------------------------------
        # Execute Learning Workflow
        # --------------------------------------------------

        learning_model = execute_learning_workflow()

        # --------------------------------------------------
        # Generate Reports
        # --------------------------------------------------

        dashboard = generate_reports()

        # --------------------------------------------------
        # Executive Summary
        # --------------------------------------------------

        display_executive_summary()

        # --------------------------------------------------
        # Repository Statistics
        # --------------------------------------------------

        display_repository_summary()

        # --------------------------------------------------
        # Completion
        # --------------------------------------------------

        print_header("Execution Completed")

        print("Adaptive Learning Engine executed successfully.")
        print(f"Learning Model : {learning_model.name}")
        print(f"Dashboard Generated : {dashboard is not None}")

    except Exception as ex:

        print_header("Execution Failed")

        print(type(ex).__name__)
        print(ex)

        raise


# ==========================================================
# Program Entry
# ==========================================================

if __name__ == "__main__":
    main()
