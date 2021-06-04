"""
Test that the asdf library integration is working properly.
"""
import sys

if sys.version_info < (3, 9):
    import importlib_resources
else:
    import importlib.resources as importlib_resources

import asdf
import pytest
import yaml

from {{ cookiecutter.module_name }} import resources


@pytest.mark.parametrize("manifest_path", (importlib_resources.files(resources) / "manifests").glob("**/*.yaml"))
def test_manifest_integration(manifest_path):
    content = manifest_path.read_bytes()
    manifest = yaml.safe_load(content)
    asdf_content = asdf.get_config().resource_manager[manifest["id"]]
    assert asdf_content == content


@pytest.mark.parametrize("schema_path", (importlib_resources.files(resources) / "schemas").glob("**/*.yaml"))
def test_schema_integration(schema_path):
    content = schema_path.read_bytes()
    schema = yaml.safe_load(content)
    asdf_content = asdf.get_config().resource_manager[schema["id"]]
    assert asdf_content == content