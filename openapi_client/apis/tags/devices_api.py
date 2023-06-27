# coding: utf-8

"""
    TinyMLaaS

    TinyMLaaS Ecosystem for Machine Learning in IoT  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.devices_.post import AddDeviceDevicesPost
from openapi_client.paths.devices_.get import ListRegisteredDevicesDevicesGet
from openapi_client.paths.devices_device_id.delete import RemoveRegisteredDeviceDevicesDeviceIdDelete


class DevicesApi(
    AddDeviceDevicesPost,
    ListRegisteredDevicesDevicesGet,
    RemoveRegisteredDeviceDevicesDeviceIdDelete,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass