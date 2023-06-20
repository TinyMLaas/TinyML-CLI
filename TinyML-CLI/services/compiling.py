import json

from pandas import json_normalize
import openapi_client
from openapi_client.apis.tags import compiled_models_api
from openapi_client.model.compiled_model import CompiledModel
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint

def compile_model(configuration, model_id):
    with openapi_client.ApiClient(configuration) as api_client:

        api_instance = compiled_models_api.CompiledModelsApi(api_client)

        path_params = {
            'model_id': model_id,
            #"quant": 0,
            #"c_array": 1
        }
    try:
        # Compile Model
        api_response = api_instance.compile_model_compiled_models_models_model_id_post(
        path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompiledModelsApi->compile_model_compiled_models_models_model_id_post:")

def list_compiled_models(configuration):
    with openapi_client.ApiClient(configuration) as api_client:

        api_instance = compiled_models_api.CompiledModelsApi(api_client)

        path_params = {'compiled_model_id': None,}
    try:
    # Get Compiled Model
        api_response = api_instance.get_compiled_model_compiled_models_compiled_model_id_get(path_params=path_params)
        data = api_response.response.data
        data_json = json.loads(data)
        data_dataframe = json_normalize(data_json)
        #print(api_response.response.data)
        #print(":floppy_disk:")
        print("[green]Compiled models:[/green]:")
        print(data_dataframe)
    except openapi_client.ApiException as e:
        print("Exception when calling CompiledModelsApi->get_compiled_model_compiled_models_compiled_model_id_get:")