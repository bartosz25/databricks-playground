import json
import os

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sql

# The query name is the display name in the Queries tab, used by the `lookup: query:` variables
CONDITION_QUERIES = {
    'customers_changed': '''SELECT COUNT(*) FROM workspace.sql_condition_trigger.customers''',
    'dummy_query': 'SELECT "a" AS letter' # dummy query to see how many times the create gets called
}


def create_condition_queries(workspace_client: WorkspaceClient, warehouse_id: str,
                             bundle_target: str) -> dict[str, str]:
    existing_queries = {query.display_name: query.id for query in workspace_client.queries.list()}
    query_ids = {}
    for query_name, query_text in CONDITION_QUERIES.items():
        if query_name in existing_queries:
            query_id = existing_queries[query_name]
            workspace_client.queries.update(id=query_id, update_mask='query_text,warehouse_id',
                                            query=sql.UpdateQueryRequestQuery(query_text=query_text,
                                                                              warehouse_id=warehouse_id))
            print(f'Updated query {query_name} ({query_id})')
        else:
            query_id = workspace_client.queries.create(query=sql.CreateQueryRequestQuery(
                display_name=query_name, query_text=query_text, warehouse_id=warehouse_id)).id
            print(f'Created query {query_name} ({query_id})')
        query_ids[query_name] = query_id
    overrides_file = f'.databricks/bundle/{bundle_target}/variable-overrides.json'
    os.makedirs(os.path.dirname(overrides_file), exist_ok=True)
    with open(overrides_file, 'w') as f:
        json.dump({f'{query_name}_query_id': query_id for query_name, query_id in query_ids.items()}, f, indent=2)
    print(f'Written query ids to {overrides_file}')
    return query_ids


