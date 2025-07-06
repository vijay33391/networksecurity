from NETWORKSECURITY.exception.exception import NetworkSecurityException
from NETWORKSECURITY.logging.logger import logging
import pandas as pd
import sys
## Data Validation 
from NETWORKSECURITY.entity.config_entity import DataValidationConfig
from NETWORKSECURITY.entity.artifict_entity import DataValidationArtifact
from NETWORKSECURITY.constants.training_pipeline import sechame_FILE_PATH
from NETWORKSECURITY.utils.main_utils.utils import write_yaml_file ,read_yaml_file 
from NETWORKSECURITY.constants.training_pipeline import sechame_FILE_PATH
import os
from scipy.stats import ks_2samp    # check for data drift

class DataValidation:
    def __init__(self, data_validation_config: DataValidationConfig,data_ingestion_artifact: DataValidationArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            
            # read the schema file
            self.schema = read_yaml_file(file_path=sechame_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e)
    @staticmethod
    def read_data(file_path: str):
        """
        Read data from the given file path.
        """
        try:
           return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def validate_column_length(self,dataframe:pd.DataFrame) -> bool:
        """
        Validate the number of columns in the dataframe against the schema.
        """
        try:
            logging.info(f"Validating number of columns in the dataframe.")
            # Get the required number of columns from the schema
            required_columns = len(self.schema["columns"])
            logging.info(f"Required number of columns: {required_columns}")
            logging.info(f"Data frame has columns: {len(dataframe.columns)}")
            if len(dataframe.columns) == required_columns:
                logging.info("Number of columns validation passed.")
                return True
            else:
                logging.error("Number of columns validation failed.")
                return False
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def validate_number_of_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            logging.info("Validating numerical columns in the dataframe.")
            # Get the numerical columns from the schema
            numerical_columns = self.schema["numerical_columns"]
            # Check if all numerical columns are present in the dataframe
            for column in numerical_columns:
                if column not in dataframe.columns:
                    logging.error(f"Numerical column '{column}' is missing in the dataframe.")
                    return False
            logging.info("Numerical columns validation passed.")
            return True
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def validate_data_drift(self, base_df: pd.DataFrame, current_df: pd.DataFrame, threshold: float = 0.05) -> bool:
        """
        Detect dataset drift using the Kolmogorov-Smirnov test.
        """
        try:
            logging.info("Detecting dataset drift.")
            status = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_same_dist = ks_2samp(d1, d2)
                if threshold <= is_same_dist.pvalue:
                    is_found = False
                else:
                    is_found = True
                    status = False
                report.update({column: {
                    "p_value": float(is_same_dist.pvalue),
                    "drift_status": is_found
                }})
            # Save the drift report to a YAML file
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            os.makedirs(os.path.dirname(drift_report_file_path), exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path, content=report)
            logging.info(f"Drift report saved at {drift_report_file_path}")
            return status
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    
    def initiate_data_validation(self):
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            # read the train and test data
            train_dataframe = self.read_data(file_path=train_file_path)
            test_dataframe = self.read_data(file_path=test_file_path)
            
            ## validate number of columns

            status=self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message=f"Train dataframe does not contain all columns.\n"
            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message=f"Test dataframe does not contain all columns.\n"   
                
            ## validate numerical columns
            status=self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message=f"Train dataframe does not contain all numerical columns.\n"

            ## lets check datadrift
            status=self.validate_data_drift(base_df=train_dataframe,current_df=test_dataframe)
            dir_path=os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            # id status is False, we will not save the valid files
            train_dataframe.to_csv(
                self.data_validation_config.valid_train_file_path, index=False, header=True

            )

            test_dataframe.to_csv(
                self.data_validation_config.valid_test_file_path, index=False, header=True
            )
            
            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_ingestion_artifact.trained_file_path,
                valid_test_file_path=self.data_ingestion_artifact.test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )
            return data_validation_artifact
           
        
            
            # validate the train and test data columns
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
        



