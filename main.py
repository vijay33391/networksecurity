# test data ingestion pipeline
from NETWORKSECURITY.constants import training_pipeline
from NETWORKSECURITY.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig  
from NETWORKSECURITY.entity.artifict_entity import DataIngestionArtifact
from NETWORKSECURITY.exception.exception import NetworkSecurityException
from NETWORKSECURITY.components.data_ingestion import DataIngestion
from NETWORKSECURITY.components.data_validation import DataValidation

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

        
    except Exception as e:
        raise NetworkSecurityException(e, sys) 