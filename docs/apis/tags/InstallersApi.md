<a id="__pageTop"></a>
# openapi_client.apis.tags.installers_api.InstallersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_registered_installers_installers_get**](#list_registered_installers_installers_get) | **get** /installers/ | List Registered Installers

# **list_registered_installers_installers_get**
<a id="list_registered_installers_installers_get"></a>
> [Installer] list_registered_installers_installers_get()

List Registered Installers

Displays registered devices

### Example

```python
import openapi_client
from openapi_client.apis.tags import installers_api
from openapi_client.model.installer import Installer
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

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
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_registered_installers_installers_get.ApiResponseFor200) | Successful Response

#### list_registered_installers_installers_get.ApiResponseFor200
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
[**Installer**]({{complexTypePrefix}}Installer.md) | [**Installer**]({{complexTypePrefix}}Installer.md) | [**Installer**]({{complexTypePrefix}}Installer.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

