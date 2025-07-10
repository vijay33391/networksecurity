# test data ingestion pipeline
from NETWORKSECURITY.constants import training_pipeline
from NETWORKSECURITY.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig ,DataTransformationConfig
from NETWORKSECURITY.entity.artifict_entity import DataIngestionArtifact
from NETWORKSECURITY.exception.exception import NetworkSecurityException
from NETWORKSECURITY.components.data_ingestion import DataIngestion
from NETWORKSECURITY.components.data_validation import DataValidation
from NETWORKSECURITY.components.data_transformation import DataTransformation

from NETWORKSECURITY.exception.exception import NetworkSecurityException
from NETWORKSECURITY.logging.logger import logging
import os
import sys
from NETWORKSECURITY.logging.logger import logging

if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        print("--------------------------------------------------")
        data_validation_config=DataValidationConfig(trainingpipelineconfig) # pick up constants from training_pipeline.py
        data_validation=DataValidation(data_validation_config,dataingestionartifact)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)
        print("--------------------------------------------------")
        # test data transformation
        data_tranasformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_tranasformation_config)
        logging.info("Initiate the data Transformation")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("data Transformation Completed")
        print(data_transformation_artifact)
        print("--------------------------------------------------")
        # mdoel trainer
        
        from NETWORKSECURITY.components.model_trainer import ModelTrainer
        from NETWORKSECURITY.entity.artifict_entity import DataValidationArtifact
        from NETWORKSECURITY.entity.config_entity import ModelTrainerConfig 
        from NETWORKSECURITY.entity.artifict_entity import ModelTrainerArtifact        
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config, data_transformation_artifact)
        logging.info("Initiate the model trainer")
        model_trainer_artifact: ModelTrainerArtifact = model_trainer.initiate_model_trainer()
        logging.info("Model trainer completed")
        print(model_trainer_artifact)
        print("--------------------------------------------------")

        
    except Exception as e:
        raise NetworkSecurityException(e, sys) 