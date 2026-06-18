# SQLFluff with Declarative Automation Bundles demo

1. Configure your Databricks workspace, if you haven't done it yet:
```shell
databricks configure
```

2. To deploy a development copy of this project, type:
```shell
BROWSER="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" databricks auth login --profile personal_free_wfc 
databricks bundle deploy --target dev --profile personal_free_wfc
```

3. Validate the queries correctness with:
```shell
poe validate_code
```
You should see some linting errors:
```
== [queries/get_active_users.sql] FAIL                                                                                                                                                                    
L:   1 | P:   1 | LT01 | Expected only single space before 'select' keyword.                                                                                                                              
                       | Found '    '. [layout.spacing]
L:   1 | P:   1 | LT02 | First line should not be indented.
                       | [layout.indent]
L:   1 | P:   1 | LT13 | Files must not begin with newlines or whitespace.
                       | [layout.start_of_file]
L:   1 | P:   5 | LT09 | Select targets should be on a new line unless there is
                       | only one select target. [layout.select_targets]
L:   2 | P:  25 | LT01 | Expected only single space before naked identifier.
                       | Found '   '. [layout.spacing]
L:   2 | P:  28 | AL01 | Implicit/explicit aliasing of table.
                       | [aliasing.table]
L:   2 | P:  28 | AL05 | Alias 'users' is never used in SELECT statement.
                       | [aliasing.unused]
L:   2 | P:  28 | RF04 | Keywords should not be used as identifiers.
                       | [references.keywords]
L:   3 | P:  27 | LT12 | Files must end with a single trailing newline.
                       | [layout.end_of_file]
== [queries/get_revenue.sql] FAIL                                                                                                                                                                         
L:   1 | P:   1 | LT01 | Expected only single space before 'SELECT' keyword.                                                                                                                              
                       | Found '    '. [layout.spacing]
L:   1 | P:   1 | LT02 | First line should not be indented.
                       | [layout.indent]
L:   1 | P:   1 | LT13 | Files must not begin with newlines or whitespace.
                       | [layout.start_of_file]
L:   2 | P:   1 | LT02 | Expected indent of 4 spaces. [layout.indent]
L:   3 | P:   1 | LT02 | Expected indent of 4 spaces. [layout.indent]
L:   3 | P:   9 | LT04 | Found leading comma ','. Expected only trailing near
                       | line breaks. [layout.commas]
L:   3 | P:  10 | LT01 | Expected single whitespace between comma ',' and
                       | function name identifier. [layout.spacing]
L:   3 | P:  26 | AL02 | Implicit/explicit aliasing of columns.
                       | [aliasing.column]
L:   4 | P:   1 | LT02 | Expected indent of 4 spaces. [layout.indent]
L:   4 | P:   9 | LT04 | Found leading comma ','. Expected only trailing near
                       | line breaks. [layout.commas]
L:   4 | P:  10 | CP03 | Function names must be consistently lower case.
                       | [capitalisation.functions]
L:   4 | P:  10 | LT01 | Expected single whitespace between comma ',' and
                       | function name identifier. [layout.spacing]
L:   6 | P:  15 | LT12 | Files must end with a single trailing newline.
                       | [layout.end_of_file]
All Finished 📜 🎉!                       
```