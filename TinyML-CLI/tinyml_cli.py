import time
from typing import Annotated, Optional

import typer
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import bridges_api
from openapi_client.model.bridge import Bridge
from openapi_client.model.bridge_create import BridgeCreate
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.loss_functions import LossFunctions
from services.compiling import compile_model, list_compiled_models
from services.devices import devices_get
from services.datasets import datasets_get
from services.models import train_model, list_trained_models
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8000" #backend URL
)

app = typer.Typer(help="CLI for TinyMLaaS.")

@app.command()
def list_devices():
    """
    List all registered devices.
    """
    devices_get(configuration)
    
@app.command()
def list_datasets():
    """
    List existing datasets.
    """
    datasets_get(configuration)
    
@app.command()
def list_models():
    """
    List trained models.
    """
    list_trained_models(configuration)
    
@app.command()
#def train_compile(name: Annotated[str, typer.Argument()]):
def train(dataset_id: int):
    """
    Train a model.
    """

    id = 1
    
    # Alla olevat kovakoodattu train_model -funktioon, myöhemmin vaihtaa ottamaan train-funktion argumentteina
    # query_params = {'lossfunc': LossFunctions("Categorical crossentropy"),}
    # dataset_id=dataset_id,
    # parameters = {
    #     "epochs": 1,
    #     "img_width": 96,
    #     "img_height": 96,
    #     "batch_size": 10
    # }
    # description="description_example"
    
    train_model(configuration, id)
    
@app.command()
def compile(model_id: int):
    """
    Compile a model.
    """
    compile_model(configuration, model_id)
    
@app.command()
def compiled_models():
    """
    List compiled models.
    """
    list_compiled_models(configuration)
    
    
if __name__ == "__main__":
    app()
