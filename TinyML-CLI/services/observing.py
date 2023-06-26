import openapi_client
from openapi_client.apis.tags import observing_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.observation import Observation
from pprint import pprint
from rich import print


def observe_device_on_bridge(configuration):
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = observing_api.ObservingApi(api_client)

        # example passing only required values which don't have defaults set
        path_params = {
            'bridge_id': 3,
            'device_id': 5,
        }
        try:
            # Observe Device On Bridge
            api_response = api_instance.observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get(
                path_params=path_params,
            )
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling ObservingApi->observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get: %s\n" % e)