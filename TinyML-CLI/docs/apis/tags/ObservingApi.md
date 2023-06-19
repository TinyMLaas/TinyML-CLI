<a id="__pageTop"></a>
# openapi_client.apis.tags.observing_api.ObservingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get**](#observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get) | **get** /observations/bridges/{bridge_id}/devices/{device_id} | Observe Device On Bridge

# **observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get**
<a id="observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get"></a>
> Observation observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get(bridge_iddevice_id)

Observe Device On Bridge

Requests a single observation from a specified device on a specified bridge.

### Example

```python
import openapi_client
from openapi_client.apis.tags import observing_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.observation import Observation
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = observing_api.ObservingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bridge_id': 1,
        'device_id': 1,
    }
    try:
        # Observe Device On Bridge
        api_response = api_instance.observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ObservingApi->observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
bridge_id | BridgeIdSchema | | 
device_id | DeviceIdSchema | | 

# BridgeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get.ApiResponseFor422) | Validation Error

#### observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Observation**](../../models/Observation.md) |  | 


#### observe_device_on_bridge_observations_bridges_bridge_id_devices_device_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

