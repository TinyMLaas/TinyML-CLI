import json
import openapi_client
from pandas import json_normalize
from openapi_client.apis.tags import datasets_api
from rich import print

def datasets_get(configuration):
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = datasets_api.DatasetsApi(api_client)

        try:
            # List registered devices
            api_response = api_instance.get_datasets_datasets_get()
            #print(api_response)
            data = api_response.response.data
            data_json = json.loads(data)
            data_dataframe = json_normalize(data_json)
            
            #print(api_response.response.data)
            #print(":floppy_disk:")
            print("[green]Existing datasets:[/green]")
            print(data_dataframe)
            
        except openapi_client.ApiException as e:
            print("Exception when calling DatasetsApi->get_datasets_datasets_get: %s\n" % e)