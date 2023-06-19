# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    DEVICES_ = "/devices/"
    DEVICES_DEVICE_ID = "/devices/{device_id}"
    BRIDGES_ = "/bridges/"
    BRIDGES_BRIDGE_ID = "/bridges/{bridge_id}"
    BRIDGES_BRIDGE_ID_DEVICES = "/bridges/{bridge_id}/devices"
    BRIDGES_BRIDGE_ID_HEALTH = "/bridges/{bridge_id}/health"
    COMPILED_MODELS_MODELS_MODEL_ID = "/compiled_models/models/{model_id}"
    COMPILED_MODELS_ = "/compiled_models/"
    COMPILED_MODELS_COMPILED_MODEL_ID = "/compiled_models/{compiled_model_id}"
    COMPILED_MODELS_COMPILED_MODEL_ID_BRIDGES_BRIDGE_ID_DEVICES_DEVICE_ID = "/compiled_models/{compiled_model_id}/bridges/{bridge_id}/devices/{device_id}"
    DATASETS_ = "/datasets/"
    DATASETS_DATASET_ID_ = "/datasets/{dataset_id}/"
    MODELS_DATASETS_DATASET_ID = "/models/datasets/{dataset_id}"
    MODELS_DATASETS_ = "/models/datasets/"
    MODELS_ = "/models/"
    INSTALLERS_ = "/installers/"
    OBSERVATIONS_BRIDGES_BRIDGE_ID_DEVICES_DEVICE_ID = "/observations/bridges/{bridge_id}/devices/{device_id}"
