# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
import logging
import os
import pickle
import numpy as np
import pandas as pd
import joblib

import azureml.automl.core
from azureml.automl.core.shared import logging_utilities, log_server
from azureml.telemetry import INSTRUMENTATION_KEY

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType


input_sample = pd.DataFrame({"Column1": pd.Series([0], dtype="int64"), "Age": pd.Series([0.0], dtype="float64"), "Number of sexual partners": pd.Series([0.0], dtype="float64"), "First sexual intercourse": pd.Series([0.0], dtype="float64"), "Num of pregnancies": pd.Series([0.0], dtype="float64"), "Smokes": pd.Series([0.0], dtype="float64"), "Smokes (years)": pd.Series([0.0], dtype="float64"), "Smokes (packs/year)": pd.Series([0.0], dtype="float64"), "Hormonal Contraceptives": pd.Series([0.0], dtype="float64"), "Hormonal Contraceptives (years)": pd.Series([0.0], dtype="float64"), "IUD": pd.Series([0.0], dtype="float64"), "IUD (years)": pd.Series([0.0], dtype="float64"), "STDs": pd.Series([0.0], dtype="float64"), "STDs (number)": pd.Series([0.0], dtype="float64"), "STDs:condylomatosis": pd.Series([0.0], dtype="float64"), "STDs:vaginal condylomatosis": pd.Series([0.0], dtype="float64"), "STDs:vulvo-perineal condylomatosis": pd.Series([0.0], dtype="float64"), "STDs:syphilis": pd.Series([0.0], dtype="float64"), "STDs:pelvic inflammatory disease": pd.Series([0.0], dtype="float64"), "STDs:genital herpes": pd.Series([0.0], dtype="float64"), "STDs:molluscum contagiosum": pd.Series([0.0], dtype="float64"), "STDs:HIV": pd.Series([0.0], dtype="float64"), "STDs:Hepatitis B": pd.Series([0.0], dtype="float64"), "STDs:HPV": pd.Series([0.0], dtype="float64"), "STDs: Number of diagnosis": pd.Series([0.0], dtype="float64"), "Dx:Cancer": pd.Series([0.0], dtype="float64"), "Dx:CIN": pd.Series([0.0], dtype="float64"), "Dx:HPV": pd.Series([0.0], dtype="float64"), "Dx": pd.Series([0.0], dtype="float64")})
output_sample = np.array([0])
try:
    log_server.enable_telemetry(INSTRUMENTATION_KEY)
    log_server.set_verbosity('INFO')
    logger = logging.getLogger('azureml.automl.core.scoring_script')
except:
    pass


def init():
    global model
    # This name is model.id of model that we want to deploy deserialize the model file back
    # into a sklearn model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    path = os.path.normpath(model_path)
    path_split = path.split(os.sep)
    log_server.update_custom_dimensions({'model_name': path_split[1], 'model_version': path_split[2]})
    try:
        logger.info("Loading model from path.")
        model = joblib.load(model_path)
        logger.info("Loading successful.")
    except Exception as e:
        logging_utilities.log_traceback(e, logger)
        raise


@input_schema('data', PandasParameterType(input_sample))
@output_schema(NumpyParameterType(output_sample))
def run(data):
    try:
        result = model.predict(data)
        return json.dumps({"result": result.tolist()})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
