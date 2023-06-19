<a id="__pageTop"></a>
# openapi_client.apis.tags.compiled_models_api.CompiledModelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compile_model_compiled_models_models_model_id_post**](#compile_model_compiled_models_models_model_id_post) | **post** /compiled_models/models/{model_id} | Compile Model
[**get_compiled_model_compiled_models_compiled_model_id_get**](#get_compiled_model_compiled_models_compiled_model_id_get) | **get** /compiled_models/{compiled_model_id} | Get Compiled Model
[**get_compiled_models_compiled_models_get**](#get_compiled_models_compiled_models_get) | **get** /compiled_models/ | Get Compiled Models
[**install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post**](#install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post) | **post** /compiled_models/{compiled_model_id}/bridges/{bridge_id}/devices/{device_id} | Install Model To Device On Brdige

# **compile_model_compiled_models_models_model_id_post**
<a id="compile_model_compiled_models_models_model_id_post"></a>
> CompiledModel compile_model_compiled_models_models_model_id_post(model_id)

Compile Model

Compile an existing model

### Example

```python
import openapi_client
from openapi_client.apis.tags import compiled_models_api
from openapi_client.model.compiled_model import CompiledModel
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
    api_instance = compiled_models_api.CompiledModelsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'model_id': None,
    }
    try:
        # Compile Model
        api_response = api_instance.compile_model_compiled_models_models_model_id_post(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompiledModelsApi->compile_model_compiled_models_models_model_id_post: %s\n" % e)
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
model_id | ModelIdSchema | | 

# ModelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#compile_model_compiled_models_models_model_id_post.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#compile_model_compiled_models_models_model_id_post.ApiResponseFor422) | Validation Error

#### compile_model_compiled_models_models_model_id_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CompiledModel**](../../models/CompiledModel.md) |  | 


#### compile_model_compiled_models_models_model_id_post.ApiResponseFor422
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

# **get_compiled_model_compiled_models_compiled_model_id_get**
<a id="get_compiled_model_compiled_models_compiled_model_id_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_compiled_model_compiled_models_compiled_model_id_get(compiled_model_id)

Get Compiled Model

Get the compiled model.  This returns the compiled cc array file.

### Example

```python
import openapi_client
from openapi_client.apis.tags import compiled_models_api
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
    api_instance = compiled_models_api.CompiledModelsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'compiled_model_id': None,
    }
    try:
        # Get Compiled Model
        api_response = api_instance.get_compiled_model_compiled_models_compiled_model_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompiledModelsApi->get_compiled_model_compiled_models_compiled_model_id_get: %s\n" % e)
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
compiled_model_id | CompiledModelIdSchema | | 

# CompiledModelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_compiled_model_compiled_models_compiled_model_id_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_compiled_model_compiled_models_compiled_model_id_get.ApiResponseFor422) | Validation Error

#### get_compiled_model_compiled_models_compiled_model_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### get_compiled_model_compiled_models_compiled_model_id_get.ApiResponseFor422
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

# **get_compiled_models_compiled_models_get**
<a id="get_compiled_models_compiled_models_get"></a>
> [CompiledModel] get_compiled_models_compiled_models_get()

Get Compiled Models

Display compiled models

### Example

```python
import openapi_client
from openapi_client.apis.tags import compiled_models_api
from openapi_client.model.compiled_model import CompiledModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compiled_models_api.CompiledModelsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Compiled Models
        api_response = api_instance.get_compiled_models_compiled_models_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompiledModelsApi->get_compiled_models_compiled_models_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_compiled_models_compiled_models_get.ApiResponseFor200) | Successful Response

#### get_compiled_models_compiled_models_get.ApiResponseFor200
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
[**CompiledModel**]({{complexTypePrefix}}CompiledModel.md) | [**CompiledModel**]({{complexTypePrefix}}CompiledModel.md) | [**CompiledModel**]({{complexTypePrefix}}CompiledModel.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post**
<a id="install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post(compiled_model_idbridge_iddevice_id)

Install Model To Device On Brdige

Installs selected compiled model on a specified device connected to a specified bridge

### Example

```python
import openapi_client
from openapi_client.apis.tags import compiled_models_api
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
    api_instance = compiled_models_api.CompiledModelsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'compiled_model_id': None,
        'bridge_id': None,
        'device_id': None,
    }
    try:
        # Install Model To Device On Brdige
        api_response = api_instance.install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompiledModelsApi->install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post: %s\n" % e)
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
compiled_model_id | CompiledModelIdSchema | | 
bridge_id | BridgeIdSchema | | 
device_id | DeviceIdSchema | | 

# CompiledModelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# BridgeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# DeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post.ApiResponseFor422) | Validation Error

#### install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### install_model_to_device_on_brdige_compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id_post.ApiResponseFor422
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

