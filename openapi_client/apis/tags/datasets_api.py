# coding: utf-8

"""
    TinyMLaaS

    TinyMLaaS Ecosystem for Machine Learning in IoT  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.datasets_.post import AddDatasetDatasetsPost
#from openapi_client.paths.datasets_dataset_id_.post import AddImageToDatasetDatasetsDatasetIdPost
from openapi_client.paths.datasets_.get import GetDatasetsDatasetsGet


class DatasetsApi(
    AddDatasetDatasetsPost,
    #AddImageToDatasetDatasetsDatasetIdPost,
    GetDatasetsDatasetsGet,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass