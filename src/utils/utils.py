import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.logger.logging import logging
from src.exceptions.exception import CustomException 
from sklearn.metrics import r2, mean_absolute_error, mean_squared_error



def save_object(file_path, obj):
  try:
    dir_path = os.path.dirname(file_path)

    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "wb") as file_obj:
      pickle.dump(obj, file_obj)

  except Exception as e:
    raise CustomException(e, sys)
  


def evaluate_model(X_train, y_train, X_test, y_test, models):
  try:
    report = {}

    for i in range(len(list(models))):
      model = list(models.values())[i]

      # Train model
      model.fit(X_train, y_train)

      # Predict testing data
      y_test_pred = model.predict(X_test)

      # Get R2 score
      r2_score = r2_score(y_test, y_test_pred)
      report[list(models.keys())[i]] = r2_score

    return report

  except Exception as e:
    logging.info("Error occured during model evaluation")
    raise CustomException(e, sys)
  

def load_object(file_path):
  try:
    with open(file_path, "rb") as file_obj:
      return pickle.load(file_obj)

  except Exception as e:
    logging.info("Error occured while loading object")
    raise CustomException(e, sys)