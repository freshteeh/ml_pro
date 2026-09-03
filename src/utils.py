import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)  ## ۱. اسم فایل را پاک می‌کند تا فقط آدرس پوشه بماند

        os.makedirs(dir_path, exist_ok=True)  # ۲. می‌رود روی هارد و مطمئن می‌شود آن پوشه واقعاً وجود دارد (اگر نبود می‌سازدش)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
