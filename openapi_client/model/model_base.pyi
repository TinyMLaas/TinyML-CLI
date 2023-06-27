# coding: utf-8

"""
    TinyMLaaS

    TinyMLaaS Ecosystem for Machine Learning in IoT  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class ModelBase(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Base for Model trained on Tensorflow. Lacks id as it is assigned by database
    
    """


    class MetaOapg:
        required = {
            "description",
            "parameters",
        }
        
        class properties:
            parameters = schemas.DictSchema
            description = schemas.StrSchema
            dataset_id = schemas.IntSchema
            __annotations__ = {
                "parameters": parameters,
                "description": description,
                "dataset_id": dataset_id,
            }
    
    description: MetaOapg.properties.description
    parameters: MetaOapg.properties.parameters
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parameters"]) -> MetaOapg.properties.parameters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataset_id"]) -> MetaOapg.properties.dataset_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["parameters", "description", "dataset_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parameters"]) -> MetaOapg.properties.parameters: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataset_id"]) -> typing.Union[MetaOapg.properties.dataset_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parameters", "description", "dataset_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        parameters: typing.Union[MetaOapg.properties.parameters, dict, frozendict.frozendict, ],
        dataset_id: typing.Union[MetaOapg.properties.dataset_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelBase':
        return super().__new__(
            cls,
            *_args,
            description=description,
            parameters=parameters,
            dataset_id=dataset_id,
            _configuration=_configuration,
            **kwargs,
        )