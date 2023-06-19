<a id="__pageTop"></a>
# openapi_client.apis.tags.models_api.ModelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_models_models_get**](#get_all_models_models_get) | **get** /models/ | Get All Models
[**train_model_dataset_id_in_training_data_models_datasets_post**](#train_model_dataset_id_in_training_data_models_datasets_post) | **post** /models/datasets/ | Train Model Dataset Id In Training Data
[**train_model_models_datasets_dataset_id_post**](#train_model_models_datasets_dataset_id_post) | **post** /models/datasets/{dataset_id} | Train Model

# **get_all_models_models_get**
<a id="get_all_models_models_get"></a>
> [Model] get_all_models_models_get()

Get All Models

Return all models

### Example

```python
import openapi_client
from openapi_client.apis.tags import models_api
from openapi_client.model.model import Model
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = models_api.ModelsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get All Models
        api_response = api_instance.get_all_models_models_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModelsApi->get_all_models_models_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_models_models_get.ApiResponseFor200) | Successful Response

#### get_all_models_models_get.ApiResponseFor200
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
[**Model**]({{complexTypePrefix}}Model.md) | [**Model**]({{complexTypePrefix}}Model.md) | [**Model**]({{complexTypePrefix}}Model.md) |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **train_model_dataset_id_in_training_data_models_datasets_post**
<a id="train_model_dataset_id_in_training_data_models_datasets_post"></a>
> ModelTrained train_model_dataset_id_in_training_data_models_datasets_post(lossfuncmodel_base)

Train Model Dataset Id In Training Data

Train a model

### Example

```python
import openapi_client
from openapi_client.apis.tags import models_api
from openapi_client.model.loss_functions import LossFunctions
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.model_base import ModelBase
from openapi_client.model.model_trained import ModelTrained
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = models_api.ModelsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'lossfunc': LossFunctions("Categorical crossentropy"),
    }
    body = ModelBase(
        dataset_id=1,
        parameters=dict(),
        description="description_example",
    )
    try:
        # Train Model Dataset Id In Training Data
        api_response = api_instance.train_model_dataset_id_in_training_data_models_datasets_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModelsApi->train_model_dataset_id_in_training_data_models_datasets_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelBase**](../../models/ModelBase.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
lossfunc | LossfuncSchema | | 


# LossfuncSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**LossFunctions**](../../models/LossFunctions.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#train_model_dataset_id_in_training_data_models_datasets_post.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#train_model_dataset_id_in_training_data_models_datasets_post.ApiResponseFor422) | Validation Error

#### train_model_dataset_id_in_training_data_models_datasets_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelTrained**](../../models/ModelTrained.md) |  | 


#### train_model_dataset_id_in_training_data_models_datasets_post.ApiResponseFor422
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

# **train_model_models_datasets_dataset_id_post**
<a id="train_model_models_datasets_dataset_id_post"></a>
> ModelTrained train_model_models_datasets_dataset_id_post(dataset_idlossfuncmodel_base)

Train Model

Train a model based on dataset_id

### Example

```python
import openapi_client
from openapi_client.apis.tags import models_api
from openapi_client.model.loss_functions import LossFunctions
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.model_base import ModelBase
from openapi_client.model.model_trained import ModelTrained
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = models_api.ModelsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'dataset_id': 1,
    }
    query_params = {
        'lossfunc': LossFunctions("Categorical crossentropy"),
    }
    body = ModelBase(
        dataset_id=1,
        parameters=dict(),
        description="description_example",
    )
    try:
        # Train Model
        api_response = api_instance.train_model_models_datasets_dataset_id_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ModelsApi->train_model_models_datasets_dataset_id_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelBase**](../../models/ModelBase.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
lossfunc | LossfuncSchema | | 


# LossfuncSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**LossFunctions**](../../models/LossFunctions.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dataset_id | DatasetIdSchema | | 

# DatasetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#train_model_models_datasets_dataset_id_post.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#train_model_models_datasets_dataset_id_post.ApiResponseFor422) | Validation Error

#### train_model_models_datasets_dataset_id_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelTrained**](../../models/ModelTrained.md) |  | 


#### train_model_models_datasets_dataset_id_post.ApiResponseFor422
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

