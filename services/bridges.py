import json
from pandas import json_normalize
import openapi_client
from openapi_client.apis.tags import installers_api
from openapi_client.model.installer import Installer
from openapi_client.apis.tags import bridges_api
from openapi_client.model.bridge import Bridge
from pprint import pprint
from rich import print

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
            name="CLI bridge",
            https=False,
        )
        try:
            # Add Bridge
            api_response = api_instance.add_bridge_bridges_post(
                body=body,
            )
            pprint("[green]Bridge added succesfully.[/green]")
        except openapi_client.ApiException as e:
            print("Exception when calling BridgesApi->add_bridge_bridges_post: %s\n" % e)
            
def get_installers(configuration):
    
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = installers_api.InstallersApi(api_client)

        # example, this endpoint has no required or optional parameters
        try:
            # List Registered Installers
            api_response = api_instance.list_registered_installers_installers_get()
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling InstallersApi->list_registered_installers_installers_get: %s\n" % e)