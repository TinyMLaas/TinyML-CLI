import json

from pandas import json_normalize
import openapi_client
from openapi_client.apis.tags import bridges_api
from openapi_client.model.bridge import Bridge
from pprint import pprint

from openapi_client.model.bridge_create import BridgeCreate
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.

def bridges_get(configuration):
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = bridges_api.BridgesApi(api_client)
        # example, this endpoint has no required or optional parameters
        try:
            # Get Registered Bridges
            api_response = api_instance.get_registered_bridges_bridges_get()
            data = api_response.response.data
            data_json = json.loads(data)
            data_dataframe = json_normalize(data_json)
            print("[green]Registered bridges:[/green]")
            print(data_dataframe)
    
        except openapi_client.ApiException as e:
            print("Exception when calling BridgesApi->get_registered_bridges_bridges_get: %s\n" % e)

def add_new_bridge(configuration):
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = bridges_api.BridgesApi(api_client)

        # example passing only required values which don't have defaults set
        body = BridgeCreate(
            address="127.0.0.1",
            name="name_example",
            https=False,
        )
        try:
            # Add Bridge
            api_response = api_instance.add_bridge_bridges_post(
                body=body,
            )
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling BridgesApi->add_bridge_bridges_post: %s\n" % e)