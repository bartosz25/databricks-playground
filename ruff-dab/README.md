# Ruff with Declarative Automation Bundles demo

1. Configure your Databricks workspace, if you haven't done it yet:
```shell
databricks configure
```

2. To deploy a development copy of this project, type:
```shell
BROWSER="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" databricks auth login --profile personal_free_wfc 
databricks bundle deploy --target dev --profile personal_free_wfc
```