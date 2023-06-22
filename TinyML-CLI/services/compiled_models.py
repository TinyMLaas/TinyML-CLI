import openapi_client
from openapi_client.apis.tags import compiled_models_api
from openapi_client.model.http_validation_error import HTTPValidationError
from rich import print

def install_model_to_device(configuration):
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = compiled_models_api.CompiledModelsApi(api_client)

        # example passing only required values which don't have defaults set
        path_params = {
            'compiled_model_id': 1,
            'bridge_id': 3,
            'device_id': 5,
        }
        try:
            # Install Model To Device On Brdige
            api_response = api_instance.install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post(
                path_params=path_params,
            )
            print("[green]Model installed succesfully.[/green]")
        except openapi_client.ApiException as e:
            print("Exception when calling CompiledModelsApi->install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post: %s\n" % e)