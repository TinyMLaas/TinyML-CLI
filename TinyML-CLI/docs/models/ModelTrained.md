# openapi_client.model.model_trained.ModelTrained

A trained model includes prediction image, the prediction that  the model has made of the image and some statistics in a plot.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A trained model includes prediction image, the prediction that  the model has made of the image and some statistics in a plot. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**statistic_image** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 
**prediction** | str,  | str,  |  | 
**prediction_image** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**model_path** | str,  | str,  |  | 
**[parameters](#parameters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**dataset_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parameters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

