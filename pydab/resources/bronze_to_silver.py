from databricks.bundles.core import Bundle, Resources
from databricks.bundles.jobs import Job

TABLES = ["orders", "customers"]


def load_resources(bundle: Bundle) -> Resources:
    resources = Resources()

    for table in TABLES:
        job = Job.from_dict(
            {
                "name": f"bronze_to_silver_{table}",
                "max_concurrent_runs": 1,
                "queue": {"enabled": True},
                "tasks": [
                    {
                        "task_key": "bronze_to_silver",
                        "environment_key": "default",
                        "python_wheel_task": {
                            "package_name": "pydabs_demo",
                            "entry_point": "bronze_to_silver",
                            "named_parameters": {
                                "bronze_table": f"${{var.catalog}}.${{var.schema}}.bronze_{table}",
                                "silver_table": f"${{var.catalog}}.${{var.schema}}.silver_{table}",
                            },
                        },
                    },
                ],
                "environments": [
                    {
                        "environment_key": "default",
                        "spec": {
                            "environment_version": "6",
                            "dependencies": ["dist/*.whl"],
                        },
                    },
                ],
            }
        )
        resources.add_resource(f"bronze_to_silver_{table}", job)

    return resources
