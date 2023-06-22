import json

from pandas import json_normalize
import openapi_client
from openapi_client.apis.tags import bridges_api
from openapi_client.model.bridge import Bridge
from pprint import pprint
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