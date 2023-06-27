# TinyML-CLI

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
