# pre-commit hook demo

To see the hook in action, you need to temporarly initialize a new Git repository inside this project:
```commandline
git init
```

Install the hook:
```commandline
uv sync
uv run pre-commit install
```

Next, try to commit a file while the [sample_job.job.yml](resources/sample_job.job.yml) file is invalid:
```commandline
git add uv.lock
git commit uv.lock  -m "lock file"
```

Misc:
1. Authenticate to your Databricks workspace, if you have not done so already:
    ```
    $ databricks configure
    ```

2. To deploy a development copy of this project, type:
    ```
    $ databricks bundle deploy --target dev --profile personal_free_edition
    ```
