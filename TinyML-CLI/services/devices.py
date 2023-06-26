import json
import pprint
import openapi_client
from pandas import json_normalize
from openapi_client.apis.tags import devices_api
from openapi_client.model.device_create import DeviceCreate
from rich import print

def devices_get(configuration):
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = devices_api.DevicesApi(api_client)

        try:
            # List registered devices
            api_response = api_instance.list_registered_devices_devices_get()
            data = api_response.response.data
            data_json = json.loads(data)
            data_dataframe = json_normalize(data_json)
            print("[green]Registered devices:[/green]")
            print(data_dataframe)
            
        except openapi_client.ApiException as e:
            print("Exception when calling DevicesApi->list_registered_devices_devices_get: %s\n" % e)

def add_new_device(configuration):
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = devices_api.DevicesApi(api_client)

        # example passing only required values which don't have defaults set
        body = DeviceCreate(
            name="Arduino",
            connection="1",
            installer_id=1,
            model="Nano 33 BLE",
            description="CLI-laite",
            serial="F404BF521AE99972",
            #detail=(1, 2)
        )
        try:
            # Add Device
            api_response = api_instance.add_device_devices_post(
                body=body,
            )
            pprint(api_response)
            pprint(api_response.body)
        except openapi_client.ApiException as e:
            print("Exception when calling DevicesApi->add_device_devices_post: %s\n" % e)