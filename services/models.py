import json
import openapi_client
from openapi_client.apis.tags import models_api
from openapi_client.model.loss_functions import LossFunctions
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.model_base import ModelBase
from openapi_client.model.model_trained import ModelTrained
from pprint import pprint
from pandas import json_normalize
from rich import print

def train_model(configuration, dataset_id, description):
    with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
        api_instance = models_api.ModelsApi(api_client)
    # example passing only required values which don't have defaults set
        query_params = {'lossfunc': LossFunctions("Categorical crossentropy"),}
        body = ModelBase(
            dataset_id=dataset_id,
            parameters = {
                "epochs": 1,
                "img_width": 96,
                "img_height": 96,
                "batch_size": 10
            },
            description=description,
        )
        try:
            api_response = api_instance.train_model_dataset_id_in_training_data_models_datasets_post(
                query_params=query_params, body=body,
                )
            print("[green]Model trained succesfully.[/green]")
        except openapi_client.ApiException as e:
            print("Exception when calling ModelsApi->train_model_dataset_id_in_training_data_models_datasets_post:")

def list_trained_models(configuration):
    with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
        api_instance = models_api.ModelsApi(api_client)
    # example, this endpoint has no required or optional parameters
    try:
    # Get All Models
        api_response = api_instance.get_all_models_models_get()
        data = api_response.response.data
        data_json = json.loads(data)
        data_dataframe = json_normalize(data_json)
        #print(api_response.response.data)
        #print(":floppy_disk:")
        print("[green]Trained models:[/green]")
        print(data_dataframe)
    except openapi_client.ApiException as e:
        print("Exception when calling ModelsApi->get_all_models_models_get: %s\n" % e)