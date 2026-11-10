import json
import os

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sql

# The query name is the display name in the Queries tab, used by the `lookup: query:` variables
CONDITION_QUERIES = {
    'count_without_having': 'SELECT COUNT(*) AS orders_count FROM workspace.sql_condition_trigger.orders',
    'wait_for_orders': 'SELECT COUNT(*) AS orders_count FROM workspace.sql_condition_trigger.orders HAVING COUNT(*) >= 3',
}


def create_condition_queries(workspace_client: WorkspaceClient, warehouse_id: str) -> dict[str, str]:
    # creating a query with an already existing name doesn't fail but makes the `lookup: query:` ambiguous
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
    return query_ids


if __name__ == '__main__':
    query_ids = create_condition_queries(WorkspaceClient(), os.environ['WAREHOUSE_ID'])
    overrides_file = f'.databricks/bundle/{os.environ["BUNDLE_TARGET"]}/variable-overrides.json'
    os.makedirs(os.path.dirname(overrides_file), exist_ok=True)
    with open(overrides_file, 'w') as f:
        json.dump({f'{query_name}_query_id': query_id for query_name, query_id in query_ids.items()}, f, indent=2)
    print(f'Written query ids to {overrides_file}')
