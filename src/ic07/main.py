"""
IC-07 – Test Data Intelligence Engine

Author : Meera Sastry
Project : ClinicalTrialAI
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd
from src.ic07.services.data_cleansing_service import (
    DataCleansingService,
)

from src.ic07.reports.data_cleansing_report import (
    DataCleansingReport,
)
from src.ic07.services.quality_recommendation_engine import (
    QualityRecommendationEngine,
)

from src.ic07.reports.quality_recommendation_report import (
    QualityRecommendationReport,
)
from src.ic07.models.synthetic_data_request import SyntheticDataRequest

from src.ic07.repositories.data_quality_repository import DataQualityRepository
from src.ic07.repositories.data_set_repository import DataSetRepository

from src.ic07.services.data_quality_service import DataQualityService
from src.ic07.services.metadata_analyzer import MetadataAnalyzer
from src.ic07.services.data_profiling_service import DataProfilingService
from src.ic07.services.synthetic_data_service import SyntheticDataService

from src.ic07.reports.data_quality_report import DataQualityReport
from src.ic07.reports.synthetic_data_report import SyntheticDataReport

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
)

logger = logging.getLogger(__name__)


def print_banner() -> None:

    print("\n" + "=" * 80)
    print("ClinicalTrialAI")
    print("IC-07 : Test Data Intelligence Engine")
    print("=" * 80)


def main():

    print_banner()

    # -------------------------------------------------------------
    # Initialize Repositories
    # -------------------------------------------------------------

    dataset_repository = DataSetRepository()

    quality_repository = DataQualityRepository()

    # -------------------------------------------------------------
    # Initialize Services
    # -------------------------------------------------------------

    metadata_analyzer = MetadataAnalyzer()

    profiling_service = DataProfilingService()

    synthetic_service = SyntheticDataService()

    quality_service = DataQualityService(
        repository=quality_repository
    )

    # -------------------------------------------------------------
    # Initialize Reports
    # -------------------------------------------------------------

    synthetic_report = SyntheticDataReport()

    quality_report = DataQualityReport(quality_repository)

    # -------------------------------------------------------------
    # Input / Output Locations
    # -------------------------------------------------------------

    project_root = Path(__file__).parent

    input_folder = project_root / "data" / "input"

    output_folder = project_root / "data" / "output"

    output_folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    input_file = input_folder / "customers.csv"

    output_file = output_folder / "synthetic_customers.csv"

    logger.info("Loading dataset from %s", input_file)

    source_df = pd.read_csv(input_file)
    print("PRINTING SOURCE_DF PRINTING SOURCE_DF PRINTING SOURCE_DF")
    print(source_df.columns.tolist())
    logger.info(
        "Loaded %d rows and %d columns.",
        len(source_df),
        len(source_df.columns),
    )

    logger.info(
        "Dataset Repository Count : %d",
        dataset_repository.count(),
    )

    # -------------------------------------------------------------
    # Metadata Analysis
    # -------------------------------------------------------------

    logger.info("Running Metadata Analysis...")

    #metadata = metadata_analyzer.analyze(source_df)
    metadata = metadata_analyzer.analyze(dataframe=source_df,dataset_name="Customer Dataset",) 
    logger.info("Metadata Analysis Completed.")

    # -------------------------------------------------------------
    # Data Profiling
    # -------------------------------------------------------------

    logger.info("Running Data Profiling...")
    profile = profiling_service.profile_dataset(dataframe=source_df,dataset_name="Customer Dataset",)
    #profile = profiling_service.profile_dataset(source_df)
    #profile = profiling_service.profile(source_df)

    logger.info("Data Profiling Completed.")

    # -------------------------------------------------------------
    # Synthetic Data Generation
    # -------------------------------------------------------------
    """
    request = SyntheticDataRequest(
        number_of_rows=100,
        include_nulls=True,
        include_duplicates=True,
        include_invalid_values=True,
        include_boundary_values=True,
        random_seed=42,
    )
    """
    request = SyntheticDataRequest(rows=100,
        include_nulls=True,
        include_duplicates=True,
        include_invalid_values=True,
        include_boundary_values=True,
        preserve_distribution=True,
        random_seed=42,
        output_format="csv",)

    synthetic_result = synthetic_service.generate(
        source_df=source_df,
        request=request,
    )

    logger.info("Synthetic data generation completed.")

    # -------------------------------------------------------------
    # Synthetic Data Report
    # -------------------------------------------------------------

    synthetic_report.print_report(
        synthetic_result
    )

    # -------------------------------------------------------------
    # Save Synthetic Dataset
    # -------------------------------------------------------------
    synthetic_service.save_output(df=synthetic_result.generated_dataframe,filename=str(output_file),output_format="csv",)
    logger.info(
        "Synthetic dataset saved to %s",
        output_file,
    )

    # -------------------------------------------------------------
    # Data Quality Evaluation
    # -------------------------------------------------------------

    logger.info("Running Data Quality Evaluation...")

    quality_metric = quality_service.evaluate(
        dataset_name="Synthetic Customer Dataset",
        dataframe=synthetic_result.generated_dataframe,
    )

    logger.info(
        "Overall Data Quality Score : %.2f",
        quality_metric.overall_score,
    )

    # -------------------------------------------------------------
    # Data Quality Report
    # -------------------------------------------------------------

    quality_report.generate(
        "Synthetic Customer Dataset"
    )

    logger.info("IC-07 Pipeline completed successfully.")

    print("PRINTING SOURCE DF PRINTING SOURCE DF \n")
    print(source_df["AccountType"].unique())
    print(synthetic_result.generated_dataframe["AccountType"].unique())
    from src.ic07.models.validation_rule import ValidationRule
    from src.ic07.services.validation_engine import ValidationEngine
    from src.ic07.reports.validation_report import ValidationReport

    rules = [
    ValidationRule(name="Age Required", description="Age cannot be null", rule_type="required", column="Age", required=True),
    ValidationRule(name="Age Range", description="Age must be between 0 and 120", rule_type="range", column="Age", minimum=0, maximum=120),
    #ValidationRule(name="Customer ID Duplicate", description="CustomerID must be unique", rule_type="duplicate", column="CustomerID"),
    ValidationRule(name="Gender", description="Allowed genders", rule_type="allowed", column="Gender", allowed_values=["Male", "Female", "Other"]),
    ValidationRule(name="Email Format", description="Email validation", rule_type="pattern", column="Email", pattern=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"),
    ValidationRule(name="Credit Score", description="Credit score must be between 300 and 850", rule_type="range", column="CreditScore", minimum=300, maximum=850),
    ValidationRule(name="Annual Income", description="Annual income cannot be negative", rule_type="range", column="AnnualIncome", minimum=0),

    ValidationRule(name="Account Type", description="Allowed account types", rule_type="allowed", column="AccountType", allowed_values=["Standard", "Premium", "Gold"]),
    ValidationRule(name="Is Active", description="Boolean validation", rule_type="allowed", column="IsActive", allowed_values=[True, False]),
    ]
    engine = ValidationEngine()
    #result = engine.validate_dataset(dataframe=df,rules=rules,)
    result = engine.validate_dataset(dataframe=synthetic_result.generated_dataframe,rules=rules,)
    ValidationReport.print_report(result)
    # ---------------------------------------------------------
    # AI-Assisted Data Quality Recommendation Engine
    recommendation_engine = (QualityRecommendationEngine())
    recommendations = (recommendation_engine.generate(result))
    recommendation_report = (QualityRecommendationReport())
    recommendation_report.generate(recommendations)
    # ---------------------------------------------------------
    # Intelligent Data Cleansing Engine
    cleansing_service = (DataCleansingService())
    cleansing_result = (cleansing_service.clean(dataframe=synthetic_result.generated_dataframe,validation_result=result,))
    cleansing_report = (DataCleansingReport())
    cleansing_report.generate(cleansing_result["actions"])

if __name__ == "__main__":
    main()
