# coding: utf-8

"""
    TinyMLaaS

    TinyMLaaS Ecosystem for Machine Learning in IoT  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.bridges_.post import AddBridgeBridgesPost
from openapi_client.paths.bridges_bridge_id_health.get import CheckBridgeStatusBridgesBridgeIdHealthGet
from openapi_client.paths.bridges_bridge_id_devices.get import GetBridgeDevicesBridgesBridgeIdDevicesGet
from openapi_client.paths.bridges_.get import GetRegisteredBridgesBridgesGet
from openapi_client.paths.bridges_bridge_id.delete import RemoveRegisteredBridgeBridgesBridgeIdDelete


class BridgesApi(
    AddBridgeBridgesPost,
    CheckBridgeStatusBridgesBridgeIdHealthGet,
    GetBridgeDevicesBridgesBridgeIdDevicesGet,
    GetRegisteredBridgesBridgesGet,
    RemoveRegisteredBridgeBridgesBridgeIdDelete,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass