import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.devices_api import DevicesApi
from openapi_client.apis.tags.datasets_api import DatasetsApi
from openapi_client.apis.tags.bridges_api import BridgesApi
from openapi_client.apis.tags.models_api import ModelsApi
from openapi_client.apis.tags.compiled_models_api import CompiledModelsApi
from openapi_client.apis.tags.installers_api import InstallersApi
from openapi_client.apis.tags.observing_api import ObservingApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DEVICES: DevicesApi,
        TagValues.DATASETS: DatasetsApi,
        TagValues.BRIDGES: BridgesApi,
        TagValues.MODELS: ModelsApi,
        TagValues.COMPILED_MODELS: CompiledModelsApi,
        TagValues.INSTALLERS: InstallersApi,
        TagValues.OBSERVING: ObservingApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DEVICES: DevicesApi,
        TagValues.DATASETS: DatasetsApi,
        TagValues.BRIDGES: BridgesApi,
        TagValues.MODELS: ModelsApi,
        TagValues.COMPILED_MODELS: CompiledModelsApi,
        TagValues.INSTALLERS: InstallersApi,
        TagValues.OBSERVING: ObservingApi,
    }
)
