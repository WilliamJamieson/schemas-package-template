from pathlib import Path
import sys

if sys.version_info < (3, 9):
    import importlib_resources
else:
    import importlib.resources as importlib_resources

from asdf.resource import DirectoryResourceMapping

import {{ cookiecutter.module_name }}


def get_resource_mappings():
    resources_root = importlib_resources.files({{ cookiecutter.module_name }}) / "resources"
    if not resources_root.is_dir():
        # In an editable install, the resources directory will exist off the
        # repository root:
        resources_root = Path(__file__).absolute().parent.parent.parent / "resources"
        if not resources_root.is_dir():
            raise RuntimeError("Missing resources directory")

    return [
        DirectoryResourceMapping(
            resources_root / "schemas",
            "asdf://{{ cookiecutter.uri_authority }}/{{ cookiecutter.uri_project }}/schemas/",
        ),
        DirectoryResourceMapping(
            resources_root / "manifests",
            "asdf://{{ cookiecutter.uri_authority }}/{{ cookiecutter.uri_project }}/manifests/",
        ),
    ]
