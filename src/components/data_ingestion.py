import pandas as pd
import numpy as np
from logger import logging
from src.exceptions.exception import CustomException


import os
import sys
from dataclasses import dataclass
from pathlib import Path

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
  raw_data_path:str = os.path.join("artificats", "raw")
  train_data_path:str = os.path.join("artificats", "train.csv")
  test_data_path:str = os.path.join("artificats", "test.csv")


class DataIngestion():
  def __init__(self):
    self.ingestion_config = DataIngestionConfig()

  def initiate_data_ingestion(self):
    logging.info("Data Ingestion has started")
    try:
      data = pd.read_csv(r"C:\Users\Gaurav\OneDrive\Desktop\GemStone\data\playground-series-s3e8\train.csv")
      
      logging.info("Data has been read")

      os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path))),
      data.to_csv(self.ingestion_config.raw_data_path, index=False)
      logging.info("Data has been saved in artifact folder")

      logging.info("Performing train test split")
      train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
      logging.info("Train test split completed")

      train_data.to_csv(self.ingestion_config.train_data_path, index=False)
      test_data.to_csv(self.ingestion_config.test_data_path, index=False)

      logging.info("Data Ingestion has completed")

      return (
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path
      )
    



    except Exception as e:
      logging.info("Exception occured in data ingestion")
      raise CustomException(e, sys)


if __name__ == "__main__":
  obj = DataIngestion()
  obj.initiate_data_ingestion()
