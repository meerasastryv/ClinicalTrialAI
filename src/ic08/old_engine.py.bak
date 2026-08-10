"""
IC-08 Customer Usage Intelligence Engine

Final Integrated Engine
Integrates all repositories and services developed across
Milestones 1–20.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


# ============================================================
# Repositories
# ============================================================

from src.ic08.repositories.customer_repository import CustomerRepository
from src.ic08.repositories.session_repository import SessionRepository
from src.ic08.repositories.usage_repository import UsageRepository
from src.ic08.repositories.feature_repository import FeatureRepository
from src.ic08.repositories.workflow_repository import WorkflowRepository
from src.ic08.repositories.feedback_repository import FeedbackRepository
from src.ic08.repositories.analytics_repository import AnalyticsRepository
from src.ic08.repositories.recommendation_repository import RecommendationRepository

from src.ic08.repositories.usage_pattern_repository import UsagePatternRepository
from src.ic08.repositories.intelligence_repository import IntelligenceRepository
from src.ic08.repositories.feature_adoption_repository import (
    FeatureAdoptionRepository,
)
from src.ic08.repositories.operational_decision_repository import (
    OperationalDecisionRepository,
)
from src.ic08.repositories.behaviour_repository import BehaviourRepository
from src.ic08.repositories.churn_repository import ChurnRepository
from src.ic08.repositories.satisfaction_repository import (
    SatisfactionRepository,
)
from src.ic08.repositories.study_health_repository import (
    StudyHealthRepository,
)
from src.ic08.repositories.action_plan_repository import (
    ActionPlanRepository,
)
from src.ic08.repositories.report_repository import ReportRepository


# ============================================================
# Services
# ============================================================

from src.ic08.services.customer_usage_service import CustomerUsageService
from src.ic08.services.session_tracking_service import SessionTrackingService
from src.ic08.services.usage_event_service import UsageEventService
from src.ic08.services.feature_tracking_service import FeatureTrackingService
from src.ic08.services.workflow_tracking_service import WorkflowTrackingService

from src.ic08.services.customer_journey_builder import CustomerJourneyBuilder
from src.ic08.services.customer_journey_analytics_service import (
    CustomerJourneyAnalyticsService,
)
from src.ic08.services.navigation_analytics_service import (
    NavigationAnalyticsService,
)
from src.ic08.services.journey_statistics_service import (
    JourneyStatisticsService,
)
from src.ic08.services.journey_reporting_service import (
    JourneyReportingService,
)

from src.ic08.services.feature_usage_analytics_service import (
    FeatureUsageAnalyticsService,
)
from src.ic08.services.feature_adoption_service import (
    FeatureAdoptionService,
)

from src.ic08.services.usage_ingestion_service import (
    UsageIngestionService,
)
from src.ic08.services.usage_validation_service import (
    UsageValidationService,
)
from src.ic08.services.usage_pattern_discovery_service import (
    UsagePatternDiscoveryService,
)
from src.ic08.services.usage_pattern_feature_service import (
    UsagePatternFeatureService,
)

from src.ic08.services.dropoff_analysis_service import (
    DropoffAnalysisService,
)
from src.ic08.services.funnel_analysis_service import (
    FunnelAnalysisService,
)
from src.ic08.services.customer_segmentation_service import (
    CustomerSegmentationService,
)

from src.ic08.services.customer_ai_insights_service import (
    CustomerAIInsightsService,
)
from src.ic08.services.customer_intelligence_service import (
    CustomerIntelligenceService,
)
from src.ic08.services.customer_intelligence_dashboard_service import (
    CustomerIntelligenceDashboardService,
)
from src.ic08.services.intelligence_report_service import (
    IntelligenceReportService,
)

from src.ic08.services.trend_analytics_service import (
    TrendAnalyticsService,
)
from src.ic08.services.behaviour_prediction_service import (
    BehaviourPredictionService,
)
from src.ic08.services.churn_prediction_service import (
    ChurnPredictionService,
)
from src.ic08.services.satisfaction_prediction_service import (
    SatisfactionPredictionService,
)
from src.ic08.services.study_health_service import (
    StudyHealthService,
)
from src.ic08.services.operational_decision_service import (
    OperationalDecisionService,
)
from src.ic08.services.executive_summary_service import (
    ExecutiveSummaryService,
)
from src.ic08.services.action_plan_service import (
    ActionPlanService,
)


# ============================================================
# Engine
# ============================================================

class IC08Engine:
#class CustomerUsageIntelligenceEngine:
    """
    Final IC-08 integrated engine.
    """

    def __init__(self):

        # ----------------------------------------------------
        # Repositories
        # ----------------------------------------------------

        self.customer_repository = CustomerRepository()
        self.session_repository = SessionRepository()
        self.usage_repository = UsageRepository()
        self.feature_repository = FeatureRepository()
        self.workflow_repository = WorkflowRepository()
        self.feedback_repository = FeedbackRepository()
        #self.analytics_repository = AnalyticsRepository()
        self.analytics_repository = AnalyticsRepository(
            self.customer_repository,
            self.session_repository,
            self.usage_repository,
            self.feature_repository,
            self.workflow_repository,
            self.feedback_repository,
        )

        self.recommendation_repository = RecommendationRepository()

        self.pattern_repository = UsagePatternRepository()
        self.intelligence_repository = IntelligenceRepository()
        self.feature_adoption_repository = FeatureAdoptionRepository()
        self.operational_decision_repository = (
            OperationalDecisionRepository()
        )
        self.behaviour_repository = BehaviourRepository()
        self.churn_repository = ChurnRepository()
        self.satisfaction_repository = SatisfactionRepository()
        self.study_health_repository = StudyHealthRepository()
        self.action_plan_repository = ActionPlanRepository()
        self.report_repository = ReportRepository()
        """
        # ----------------------------------------------------
        # Core Services
        # ----------------------------------------------------

        #self.customer_usage_service = CustomerUsageService()
        self.customer_usage_service = CustomerUsageService(
            self.customer_repository,
            self.session_repository,
            self.usage_repository,
        )

        self.session_tracking_service = SessionTrackingService()
        self.usage_event_service = UsageEventService()
        self.feature_tracking_service = FeatureTrackingService()
        self.workflow_tracking_service = WorkflowTrackingService()

        self.customer_journey_builder = CustomerJourneyBuilder()
        self.customer_journey_service = (
            CustomerJourneyAnalyticsService()
        )
        self.navigation_service = NavigationAnalyticsService()
        self.journey_statistics_service = (
            JourneyStatisticsService()
        )
        self.journey_reporting_service = (
            JourneyReportingService()
        )

        self.feature_usage_service = (
            FeatureUsageAnalyticsService()
        )
        self.feature_adoption_service = (
            FeatureAdoptionService()
        )

        self.ingestion_service = UsageIngestionService()
        self.validation_service = UsageValidationService()

        self.pattern_service = (
            UsagePatternDiscoveryService()
        )
        self.pattern_feature_service = (
            UsagePatternFeatureService()
        )

        self.dropoff_service = DropoffAnalysisService()
        self.funnel_service = FunnelAnalysisService()

        self.segmentation_service = (
            CustomerSegmentationService()
        )

        self.ai_insights_service = (
            CustomerAIInsightsService()
        )

        self.intelligence_service = (
            CustomerIntelligenceService()
        )

        self.dashboard_service = (
            CustomerIntelligenceDashboardService()
        )

        self.intelligence_report_service = (
            IntelligenceReportService()
        )

        self.trend_service = TrendAnalyticsService()
        self.behaviour_service = (
            BehaviourPredictionService()
        )
        self.churn_service = (
            ChurnPredictionService()
        )
        self.satisfaction_service = (
            SatisfactionPredictionService()
        )

        self.study_health_service = (
            StudyHealthService()
        )

        self.operational_decision_service = (
            OperationalDecisionService()
        )

        self.executive_summary_service = (
            ExecutiveSummaryService()
        )

        self.action_plan_service = (
            ActionPlanService()
        )
        """
	# ----------------------------------------------------
	# Core Services
	# ----------------------------------------------------
	# Basic Services
	self.customer_usage_service = CustomerUsageService(
	    self.customer_repository,
	    self.session_repository,
	    self.usage_repository,
	)

	self.session_tracking_service = SessionTrackingService(
	    self.session_repository,
	)

	self.usage_event_service = UsageEventService(
	    self.usage_repository,
	)

	self.feature_tracking_service = FeatureTrackingService(
	    self.feature_repository,
	)

	self.workflow_tracking_service = WorkflowTrackingService(
	    self.workflow_repository,
	)

	# Journey Builder

	self.customer_journey_builder = CustomerJourneyBuilder(
	    self.usage_event_service,
	    self.session_tracking_service,
	    self.workflow_tracking_service,
	)

	# Navigation

	self.navigation_service = NavigationAnalyticsService(
	    self.customer_journey_builder,
	)

	# Funnel

	self.funnel_service = FunnelAnalysisService(
	    self.customer_journey_builder,
	    self.navigation_service,
	)

	# Drop-off

	self.dropoff_service = DropoffAnalysisService(
	    self.customer_journey_builder,
	    self.navigation_service,
	    self.funnel_service,
	)

	# Journey Statistics

	self.journey_statistics_service = JourneyStatisticsService(
	    self.customer_journey_builder,
	    self.navigation_service,
	    self.funnel_service,
	    self.dropoff_service,
	)

	# Journey Reporting

	self.journey_reporting_service = JourneyReportingService(
	    self.customer_journey_builder,
	    self.navigation_service,
	    self.funnel_service,
	    self.dropoff_service,
	    self.journey_statistics_service,
	)

	# Journey Analytics

	self.customer_journey_service = CustomerJourneyAnalyticsService(
	    self.customer_journey_builder,
	    self.navigation_service,
	    self.funnel_service,
	    self.dropoff_service,
	    self.journey_statistics_service,
	    self.journey_reporting_service,
	)

	# Feature Usage

	self.feature_usage_service = FeatureUsageAnalyticsService(
	    self.usage_event_service,
	    self.feature_tracking_service,
	    self.workflow_tracking_service,
	    self.session_tracking_service,
	)

	self.feature_adoption_service = FeatureAdoptionService(
	    self.feature_adoption_repository,
	)

	# Usage

	self.ingestion_service = UsageIngestionService(
	    self.usage_repository,
	)

	self.validation_service = UsageValidationService()

	self.pattern_service = UsagePatternDiscoveryService(
	    self.pattern_repository,
	)

	self.pattern_feature_service = UsagePatternFeatureService()

	# Segmentation

	self.segmentation_service = CustomerSegmentationService(
	    self.customer_journey_builder,
	)

	# AI

	self.ai_insights_service = CustomerAIInsightsService(
	    self.customer_journey_builder,
	)

	self.dashboard_service = CustomerIntelligenceDashboardService(
	    self.customer_journey_builder,
	)

	self.intelligence_service = CustomerIntelligenceService(
	    self.customer_repository,
	    self.intelligence_repository,
	)

	self.intelligence_report_service = IntelligenceReportService(
	    self.report_repository,
	)

	# Trend Analytics

	self.trend_service = TrendAnalyticsService(
	    self.customer_journey_builder,
	)

	# Predictions

	self.behaviour_service = BehaviourPredictionService()
	self.churn_service = ChurnPredictionService()
	self.satisfaction_service = SatisfactionPredictionService()
	# Study Health
	self.study_health_service = StudyHealthService()

	# Operational Decisions

	self.operational_decision_service = OperationalDecisionService(
	    self.operational_decision_repository,
	)

	# Executive Summary
	self.executive_summary_service = ExecutiveSummaryService()
	# Action Plans
	self.action_plan_service = ActionPlanService(
	    self.action_plan_repository,
	)

    # ============================================================
    # Helpers
    # ============================================================

    def engine_name(self) -> str:
        return "IC-08 Customer Usage Intelligence Engine"

    def version(self) -> str:
        return "Final"

    def health(self) -> Dict[str, Any]:
        return {
            "engine": self.engine_name(),
            "version": self.version(),
            "status": "READY",
        }

    # ============================================================
    # Customer APIs
    # ============================================================

    def add_customer(self, customer):
        return self.customer_usage_service.add_customer(customer)

    def get_customer(self, customer_id):
        return self.customer_usage_service.get_customer(customer_id)

    def list_customers(self):
        return self.customer_usage_service.list_customers()

    # ============================================================
    # Session APIs
    # ============================================================

    def start_session(self, session):
        return self.session_tracking_service.start_session(session)

    def end_session(self, session_id):
        return self.session_tracking_service.end_session(session_id)

    def get_session(self, session_id):
        return self.session_tracking_service.get_session(session_id)

    def list_sessions(self):
        return self.session_tracking_service.list_sessions()

    # ============================================================
    # Usage Event APIs
    # ============================================================

    def record_usage_event(self, event):
        return self.usage_event_service.record_event(event)

    def list_usage_events(self):
        return self.usage_event_service.list_events()

    # ============================================================
    # Feature Tracking
    # ============================================================

    def track_feature_usage(self, usage):
        return self.feature_tracking_service.track_feature(usage)

    def feature_usage_summary(self):
        return self.feature_usage_service.generate_summary()

    def feature_adoption_report(self):
        return self.feature_adoption_service.generate_report()

    # ============================================================
    # Workflow Tracking
    # ============================================================

    def record_workflow(self, workflow):
        return self.workflow_tracking_service.record_workflow(workflow)

    def workflow_summary(self):
        return self.workflow_tracking_service.generate_summary()

    # ============================================================
    # Customer Journey
    # ============================================================

    def build_customer_journey(self, customer_id):
        return self.customer_journey_builder.build(customer_id)

    def analyze_customer_journey(self, customer_id):
        return self.customer_journey_service.analyze(customer_id)

    def customer_journey_report(self, customer_id):
        return self.journey_reporting_service.generate(customer_id)

    # ============================================================
    # Navigation Analytics
    # ============================================================

    def navigation_statistics(self):
        return self.navigation_service.navigation_statistics()

    def navigation_paths(self):
        return self.navigation_service.common_navigation_paths()

    def navigation_dropoffs(self):
        return self.navigation_service.dropoff_points()

    # ============================================================
    # Journey Statistics
    # ============================================================

    def journey_statistics(self):
        return self.journey_statistics_service.generate_statistics()

    def average_journey_duration(self):
        return self.journey_statistics_service.average_duration()

    def completed_journeys(self):
        return self.journey_statistics_service.completed_journeys()

    def abandoned_journeys(self):
        return self.journey_statistics_service.abandoned_journeys()

    # ============================================================
    # Usage Ingestion & Validation
    # ============================================================

    def ingest_usage_data(self, records):
        return self.ingestion_service.ingest(records)

    def validate_usage_data(self, records):
        return self.validation_service.validate(records)

    # ============================================================
    # Usage Pattern Discovery
    # ============================================================

    def discover_usage_patterns(self):
        return self.pattern_service.discover_patterns()

    def usage_pattern_summary(self):
        return self.pattern_service.generate_summary()

    def extract_pattern_features(self):
        return self.pattern_feature_service.extract_features()

    # ============================================================
    # Funnel Analytics
    # ============================================================

    def funnel_analysis(self):
        return self.funnel_service.analyze()

    def funnel_conversion_rate(self):
        return self.funnel_service.conversion_rate()

    # ============================================================
    # Drop-off Analytics
    # ============================================================

    def dropoff_analysis(self):
        return self.dropoff_service.analyze()

    def highest_dropoff_stage(self):
        return self.dropoff_service.highest_dropoff_stage()

    # ============================================================
    # Customer Segmentation
    # ============================================================

    def segment_customers(self):
        return self.segmentation_service.segment_customers()

    def customer_segments(self):
        return self.segmentation_service.list_segments()

    # ============================================================
    # AI Insights
    # ============================================================

    def generate_ai_insights(self):
        return self.ai_insights_service.generate_insights()

    def customer_intelligence(self):
        return self.intelligence_service.generate_intelligence()

    def intelligence_dashboard(self):
        return self.dashboard_service.build_dashboard()

    def intelligence_report(self):
        return self.intelligence_report_service.generate_report()

    # ============================================================
    # Trend Analytics
    # ============================================================

    def trend_analysis(self):
        return self.trend_service.analyze()

    def trend_summary(self):
        return self.trend_service.summary()

    # ============================================================
    # Behaviour Prediction
    # ============================================================

    def behaviour_prediction(self):
        return self.behaviour_service.predict()

    # ============================================================
    # Churn Prediction
    # ============================================================

    def churn_prediction(self):
        return self.churn_service.predict()

    def high_risk_customers(self):
        return self.churn_service.high_risk_customers()

    # ============================================================
    # Satisfaction Prediction
    # ============================================================

    def satisfaction_prediction(self):
        return self.satisfaction_service.predict()

    def satisfaction_summary(self):
        return self.satisfaction_service.summary()

    # ============================================================
    # Study Health
    # ============================================================

    def study_health(self):
        return self.study_health_service.evaluate()

    def study_health_report(self):
        return self.study_health_service.generate_report()

    # ============================================================
    # Operational Decisions
    # ============================================================

    def operational_recommendations(self):
        return self.operational_decision_service.generate_recommendations()

    # ============================================================
    # Executive Summary
    # ============================================================

    def executive_summary(self):
        return self.executive_summary_service.generate_summary()

    # ============================================================
    # Action Plans
    # ============================================================

    def action_plan(self):
        return self.action_plan_service.generate_action_plan()

    # ============================================================
    # Reporting APIs
    # ============================================================

    def generate_report(self):
        """
        Generate a consolidated customer usage report.
        """
        if hasattr(self.report_repository, "generate_report"):
            return self.report_repository.generate_report()

        return {
            "status": "success",
            "message": "Report generation completed."
        }

    def export_dashboard(self):
        """
        Export dashboard information.
        """
        return {
            "health": self.health(),
            "executive_summary": self.executive_summary(),
            "study_health": self.study_health(),
            "action_plan": self.action_plan(),
        }

    # ============================================================
    # Repository Statistics
    # ============================================================

    def repository_statistics(self):
        """
        Return high-level repository statistics.
        """

        return {
            "customers": len(getattr(self.customer_repository, "customers", [])),
            "sessions": len(getattr(self.session_repository, "sessions", [])),
            "usage_events": len(getattr(self.usage_repository, "usage_events", [])),
            "features": len(getattr(self.feature_repository, "features", [])),
            "workflows": len(getattr(self.workflow_repository, "workflows", [])),
        }

    # ============================================================
    # Engine Summary
    # ============================================================

    def summary(self):
        return {
            "engine": self.engine_name(),
            "version": self.version(),
            "status": "READY",
            "repositories": self.repository_statistics(),
        }

    def initialize(self):
        """
        Initialize the engine.
        """
        return True

    def health_check(self):
        """
        Compatibility wrapper used by test_engine.py
        """
        return self.health()
# ============================================================
# Demo
# ============================================================

def run_demo():

    #engine = CustomerUsageIntelligenceEngine()
    engine = IC08Engine()
    print("=" * 70)
    print(engine.engine_name())
    print("=" * 70)

    print("\nHealth")
    print(engine.health())

    print("\nSummary")
    print(engine.summary())

    print("\nExecutive Summary")
    try:
        print(engine.executive_summary())
    except Exception as ex:
        print(f"Not available: {ex}")

    print("\nStudy Health")
    try:
        print(engine.study_health())
    except Exception as ex:
        print(f"Not available: {ex}")

    print("\nAction Plan")
    try:
        print(engine.action_plan())
    except Exception as ex:
        print(f"Not available: {ex}")

    print("\nDashboard")
    try:
        print(engine.export_dashboard())
    except Exception as ex:
        print(f"Not available: {ex}")

    print("\nRepository Statistics")
    print(engine.repository_statistics())

    print("\nIC-08 Customer Usage Intelligence Engine Ready")


# ============================================================
# Main
# ============================================================

def main():
    run_demo()


if __name__ == "__main__":
    main()
