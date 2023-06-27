# TinyML-CLI

This is a command-line interface for the [TinyMLaaS](https://github.com/TinyMLaas) project.

## Instructions for running the CLI

Start by [cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository. Then setup and run CLI with the following steps.

## Virtual environment

Setup [venv](https://docs.python.org/3/library/venv.html) with:

```
python -m venv venv
```

Activate the virtual environment with:

```
source venv/bin/activate
```

## Dependencies

Install project dependencies by running the following command inside the virtual environment:

```
pip install -r requirements.txt
```

## Usage

Run [backend](https://github.com/TinyMLaas/TinyML-backend) and [bridge](https://github.com/TinyMLaas/TinyML-MCU).

Create a .env file with BACKEND_URL in the project root. 

For available commands run the command:

```
python3 tinyml_cli.py --help
```

Hint: For instructions and a list of required parameters, run --help after any command. For example:

```
python3 tinyml_cli.py list-datasets --help
```

## CLI tool installation:

Install OpenAPI Generator CLI. This is a package that is used to generate the CLI tool.

```
npm install @openapitools/openapi-generator-cli -g
```

Once installed, any of the [available generators](https://openapi-generator.tech/docs/generators) can be used. We're using Python.

## Generating a Python CLI tool

To generate a Python CLI tool we need to define a generator and provide it with an OpenAPI specification in YAML and an output path.

```
npx @openapitools/openapi-generator-cli generate -i *your_yaml-file*.yaml -g python -o *your_output_path*
```

### Setup

Run a virtual environment and install dependencies:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
pip install setuptools / pip install -r requirements.txt
```

Finish the installation with:

```
python3 setup.py install
```
