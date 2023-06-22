import json
import pprint
import openapi_client
from pandas import json_normalize
from openapi_client.apis.tags import devices_api
from rich import print

def devices_get(configuration):
    # with openapi_client.ApiClient(configuration) as api_client:
    #     # Create an instance of the API class
    #     api_instance = devices_api.DevicesApi(api_client)

    #     try:
    #         # List registered devices
    #         api_response = api_instance.list_registered_devices_devices_get()
    #         jeoj= api_response.body
    #         print(jeoj)
    #         data = api_response.response.data
    #         data_json = json.loads(data)
    #         data_dataframe = json_normalize(data_json)
    #         #print(api_response.response.data)
    #         #print(":radio:")
    #         print("[green]Registered devices:[/green]")
    #         print(data_dataframe)
            
    #     except openapi_client.ApiException as e:
    #         print("Exception when calling DevicesApi->list_registered_devices_devices_get: %s\n" % e)
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = devices_api.DevicesApi(api_client)

        # example, this endpoint has no required or optional parameters
        try:
            # List Registered Devices
            api_response = api_instance.list_registered_devices_devices_get()
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling DevicesApi->list_registered_devices_devices_get: %s\n" % e)