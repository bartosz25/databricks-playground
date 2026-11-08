from databricks.bundles.jobs import Job

python_defined = Job.from_dict(
    {
        "name": "python_defined",
        "max_concurrent_runs": 1,
        "queue": {"enabled": True},
        "tasks": [
            {
                "task_key": "hello",
                "environment_key": "default",
                "python_wheel_task": {
                    "package_name": "pydabs_demo",
                    "entry_point": "hello",
                },
            },
        ],
        "environments": [
            {
                "environment_key": "default",
                "spec": {
                    "environment_version": "6",
                    # paths in Python resources are relative to the bundle root
                    "dependencies": ["dist/*.whl"],
                },
            },
        ],
    }
)
