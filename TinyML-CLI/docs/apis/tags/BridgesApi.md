<a id="__pageTop"></a>
# openapi_client.apis.tags.bridges_api.BridgesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bridge_bridges_post**](#add_bridge_bridges_post) | **post** /bridges/ | Add Bridge
[**check_bridge_status_bridges_bridge_id_health_get**](#check_bridge_status_bridges_bridge_id_health_get) | **get** /bridges/{bridge_id}/health | Check Bridge Status
[**get_bridge_devices_bridges_bridge_id_devices_get**](#get_bridge_devices_bridges_bridge_id_devices_get) | **get** /bridges/{bridge_id}/devices | Get Bridge Devices
[**get_registered_bridges_bridges_get**](#get_registered_bridges_bridges_get) | **get** /bridges/ | Get Registered Bridges
[**remove_registered_bridge_bridges_bridge_id_delete**](#remove_registered_bridge_bridges_bridge_id_delete) | **delete** /bridges/{bridge_id} | Remove Registered Bridge

# **add_bridge_bridges_post**
<a id="add_bridge_bridges_post"></a>
> Bridge add_bridge_bridges_post(bridge_create)

Add Bridge

Adds a bridge.

### Example

```python
import openapi_client
from openapi_client.apis.tags import bridges_api
from openapi_client.model.bridge_create import BridgeCreate
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.bridge import Bridge
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bridges_api.BridgesApi(api_client)

    # example passing only required values which don't have defaults set
    body = BridgeCreate(
        ip_address="ip_address_example",
        name="name_example",
    )
    try:
        # Add Bridge
        api_response = api_instance.add_bridge_bridges_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BridgesApi->add_bridge_bridges_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BridgeCreate**](../../models/BridgeCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#add_bridge_bridges_post.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#add_bridge_bridges_post.ApiResponseFor422) | Validation Error

#### add_bridge_bridges_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Bridge**](../../models/Bridge.md) |  | 


#### add_bridge_bridges_post.ApiResponseFor422
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

# **check_bridge_status_bridges_bridge_id_health_get**
<a id="check_bridge_status_bridges_bridge_id_health_get"></a>
> BridgeStatus check_bridge_status_bridges_bridge_id_health_get(bridge_id)

Check Bridge Status

Ping the bridge to find out weather or not it is online

### Example

```python
import openapi_client
from openapi_client.apis.tags import bridges_api
from openapi_client.model.bridge_status import BridgeStatus
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bridges_api.BridgesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bridge_id': None,
    }
    try:
        # Check Bridge Status
        api_response = api_instance.check_bridge_status_bridges_bridge_id_health_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BridgesApi->check_bridge_status_bridges_bridge_id_health_get: %s\n" % e)
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

# BridgeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#check_bridge_status_bridges_bridge_id_health_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#check_bridge_status_bridges_bridge_id_health_get.ApiResponseFor422) | Validation Error

#### check_bridge_status_bridges_bridge_id_health_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BridgeStatus**](../../models/BridgeStatus.md) |  | 


#### check_bridge_status_bridges_bridge_id_health_get.ApiResponseFor422
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

# **get_bridge_devices_bridges_bridge_id_devices_get**
<a id="get_bridge_devices_bridges_bridge_id_devices_get"></a>
> BridgeDevices get_bridge_devices_bridges_bridge_id_devices_get(bridge_id)

Get Bridge Devices

Get the devices connected to the bridge

### Example

```python
import openapi_client
from openapi_client.apis.tags import bridges_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.bridge_devices import BridgeDevices
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bridges_api.BridgesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bridge_id': None,
    }
    try:
        # Get Bridge Devices
        api_response = api_instance.get_bridge_devices_bridges_bridge_id_devices_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BridgesApi->get_bridge_devices_bridges_bridge_id_devices_get: %s\n" % e)
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

# BridgeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_bridge_devices_bridges_bridge_id_devices_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_bridge_devices_bridges_bridge_id_devices_get.ApiResponseFor422) | Validation Error

#### get_bridge_devices_bridges_bridge_id_devices_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BridgeDevices**](../../models/BridgeDevices.md) |  | 


#### get_bridge_devices_bridges_bridge_id_devices_get.ApiResponseFor422
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

# **get_registered_bridges_bridges_get**
<a id="get_registered_bridges_bridges_get"></a>
> [Bridge] get_registered_bridges_bridges_get()

Get Registered Bridges

Displays registered Bridges

### Example

```python
import openapi_client
from openapi_client.apis.tags import bridges_api
from openapi_client.model.bridge import Bridge
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bridges_api.BridgesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Registered Bridges
        api_response = api_instance.get_registered_bridges_bridges_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BridgesApi->get_registered_bridges_bridges_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_registered_bridges_bridges_get.ApiResponseFor200) | Successful Response

#### get_registered_bridges_bridges_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Bridge**]({{complexTypePrefix}}Bridge.md) | [**Bridge**]({{complexTypePrefix}}Bridge.md) | [**Bridge**]({{complexTypePrefix}}Bridge.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_registered_bridge_bridges_bridge_id_delete**
<a id="remove_registered_bridge_bridges_bridge_id_delete"></a>
> remove_registered_bridge_bridges_bridge_id_delete(bridge_id)

Remove Registered Bridge

Removes a Bridge

### Example

```python
import openapi_client
from openapi_client.apis.tags import bridges_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bridges_api.BridgesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bridge_id': None,
    }
    try:
        # Remove Registered Bridge
        api_response = api_instance.remove_registered_bridge_bridges_bridge_id_delete(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling BridgesApi->remove_registered_bridge_bridges_bridge_id_delete: %s\n" % e)
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

# BridgeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#remove_registered_bridge_bridges_bridge_id_delete.ApiResponseFor204) | Successful Response
422 | [ApiResponseFor422](#remove_registered_bridge_bridges_bridge_id_delete.ApiResponseFor422) | Validation Error

#### remove_registered_bridge_bridges_bridge_id_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_registered_bridge_bridges_bridge_id_delete.ApiResponseFor422
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

