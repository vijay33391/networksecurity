import os
import sys

from NETWORKSECURITY.constants import training_pipeline
from NETWORKSECURITY.entity.config_entity import (
    TrainingPipelineConfig, DataIngestionConfig,
    DataValidationConfig, DataTransformationConfig,
    ModelTrainerConfig
)
from NETWORKSECURITY.entity.artifict_entity import (
    DataIngestionArtifact, DataValidationArtifact,
    DataTransformationArtifact, ModelTrainerArtifact
)
from NETWORKSECURITY.components.data_ingestion import DataIngestion
from NETWORKSECURITY.components.data_validation import DataValidation
from NETWORKSECURITY.components.data_transformation import DataTransformation
from NETWORKSECURITY.components.model_trainer import ModelTrainer
from NETWORKSECURITY.exception.exception import NetworkSecurityException
from NETWORKSECURITY.logging.logger import logging


class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def run_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config)
            logging.info("Initiating data ingestion...")
            artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed: {artifact}")
            return artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def run_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(self.training_pipeline_config)
            data_validation = DataValidation(data_validation_config, data_ingestion_artifact)
            logging.info("Initiating data validation...")
            artifact = data_validation.initiate_data_validation()
            logging.info(f"Data validation completed: {artifact}")
            return artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def run_data_transformation(self, data_validation_artifact: DataValidationArtifact) -> DataTransformationArtifact:
        try:
            data_transformation_config = DataTransformationConfig(self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
            logging.info("Initiating data transformation...")
            artifact = data_transformation.initiate_data_transformation()
            logging.info(f"Data transformation completed: {artifact}")
            return artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def run_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        try:
            model_trainer_config = ModelTrainerConfig(self.training_pipeline_config)
            model_trainer = ModelTrainer(model_trainer_config, data_transformation_artifact)
            logging.info("Initiating model training...")
            artifact = model_trainer.initiate_model_trainer()
            logging.info(f"Model training completed: {artifact}")
            return artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.run_data_ingestion()
            data_validation_artifact = self.run_data_validation(data_ingestion_artifact)
            data_transformation_artifact = self.run_data_transformation(data_validation_artifact)
            model_trainer_artifact = self.run_model_trainer(data_transformation_artifact)

            logging.info("Full pipeline executed successfully.")
            return model_trainer_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)


# Entry point
if __name__ == "__main__":
    try:
        pipeline_runner = SimplePipelineRunner()
        pipeline_runner.run_pipeline()
    except Exception as e:
        logging.error(f"Pipeline execution failed: {e}")
        raise NetworkSecurityException(e, sys)
