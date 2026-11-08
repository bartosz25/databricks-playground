from databricks.bundles.core import (
    Bundle,
    Resources,
    load_resources_from_current_package_module,
)


def load_resources(bundle: Bundle) -> Resources:
    # loads all resources declared as module-level variables in the 'resources' package
    return load_resources_from_current_package_module()
