import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.devices_ import Devices
from openapi_client.apis.paths.devices_device_id import DevicesDeviceId
from openapi_client.apis.paths.bridges_ import Bridges
from openapi_client.apis.paths.bridges_bridge_id import BridgesBridgeId
from openapi_client.apis.paths.bridges_bridge_id_devices import BridgesBridgeIdDevices
from openapi_client.apis.paths.bridges_bridge_id_health import BridgesBridgeIdHealth
from openapi_client.apis.paths.compiled_models_models_model_id import CompiledModelsModelsModelId
from openapi_client.apis.paths.compiled_models_ import CompiledModels
from openapi_client.apis.paths.compiled_models_compiled_model_id import CompiledModelsCompiledModelId
from openapi_client.apis.paths.compiled_models_compiled_model_id_bridges_bridge_id_devices_device_id import CompiledModelsCompiledModelIdBridgesBridgeIdDevicesDeviceId
from openapi_client.apis.paths.datasets_ import Datasets
from openapi_client.apis.paths.datasets_dataset_id_ import DatasetsDatasetId
from openapi_client.apis.paths.models_datasets_dataset_id import ModelsDatasetsDatasetId
from openapi_client.apis.paths.models_datasets_ import ModelsDatasets
from openapi_client.apis.paths.models_ import Models
from openapi_client.apis.paths.installers_ import Installers
from openapi_client.apis.paths.observations_bridges_bridge_id_devices_device_id import ObservationsBridgesBridgeIdDevicesDeviceId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DEVICES_: Devices,
        PathValues.DEVICES_DEVICE_ID: DevicesDeviceId,
        PathValues.BRIDGES_: Bridges,
        PathValues.BRIDGES_BRIDGE_ID: BridgesBridgeId,
        PathValues.BRIDGES_BRIDGE_ID_DEVICES: BridgesBridgeIdDevices,
        PathValues.BRIDGES_BRIDGE_ID_HEALTH: BridgesBridgeIdHealth,
        PathValues.COMPILED_MODELS_MODELS_MODEL_ID: CompiledModelsModelsModelId,
        PathValues.COMPILED_MODELS_: CompiledModels,
        PathValues.COMPILED_MODELS_COMPILED_MODEL_ID: CompiledModelsCompiledModelId,
        PathValues.COMPILED_MODELS_COMPILED_MODEL_ID_BRIDGES_BRIDGE_ID_DEVICES_DEVICE_ID: CompiledModelsCompiledModelIdBridgesBridgeIdDevicesDeviceId,
        PathValues.DATASETS_: Datasets,
        PathValues.DATASETS_DATASET_ID_: DatasetsDatasetId,
        PathValues.MODELS_DATASETS_DATASET_ID: ModelsDatasetsDatasetId,
        PathValues.MODELS_DATASETS_: ModelsDatasets,
        PathValues.MODELS_: Models,
        PathValues.INSTALLERS_: Installers,
        PathValues.OBSERVATIONS_BRIDGES_BRIDGE_ID_DEVICES_DEVICE_ID: ObservationsBridgesBridgeIdDevicesDeviceId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DEVICES_: Devices,
        PathValues.DEVICES_DEVICE_ID: DevicesDeviceId,
        PathValues.BRIDGES_: Bridges,
        PathValues.BRIDGES_BRIDGE_ID: BridgesBridgeId,
        PathValues.BRIDGES_BRIDGE_ID_DEVICES: BridgesBridgeIdDevices,
        PathValues.BRIDGES_BRIDGE_ID_HEALTH: BridgesBridgeIdHealth,
        PathValues.COMPILED_MODELS_MODELS_MODEL_ID: CompiledModelsModelsModelId,
        PathValues.COMPILED_MODELS_: CompiledModels,
        PathValues.COMPILED_MODELS_COMPILED_MODEL_ID: CompiledModelsCompiledModelId,
        PathValues.COMPILED_MODELS_COMPILED_MODEL_ID_BRIDGES_BRIDGE_ID_DEVICES_DEVICE_ID: CompiledModelsCompiledModelIdBridgesBridgeIdDevicesDeviceId,
        PathValues.DATASETS_: Datasets,
        PathValues.DATASETS_DATASET_ID_: DatasetsDatasetId,
        PathValues.MODELS_DATASETS_DATASET_ID: ModelsDatasetsDatasetId,
        PathValues.MODELS_DATASETS_: ModelsDatasets,
        PathValues.MODELS_: Models,
        PathValues.INSTALLERS_: Installers,
        PathValues.OBSERVATIONS_BRIDGES_BRIDGE_ID_DEVICES_DEVICE_ID: ObservationsBridgesBridgeIdDevicesDeviceId,
    }
)
