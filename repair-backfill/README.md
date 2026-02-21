# Repair-backfill demo

1. Authenticate to your Databricks workspace, if you have not done so already:
    ```
    $ databricks configure
    ```

2. To deploy a development copy of this project, type:
    ```
    $ BROWSER="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" databricks auth login --profile personal_free_wfc 
    $ databricks bundle deploy --target dev --profile personal_free_wfc
    ```

# Using the demo
The demo has two entrypoints: 
```yaml
package_name: repair_backfill
entry_point: main
#entry_point: failing_main
```

If you want to test a failure, uncomment the `failing_main` part.