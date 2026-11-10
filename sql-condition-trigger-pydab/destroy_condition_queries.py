from databricks.sdk import WorkspaceClient

from create_condition_queries import CONDITION_QUERIES


def destroy_condition_queries(workspace_client: WorkspaceClient):
    # the queries are matched by their display name, the same way as in create_condition_queries
    existing_queries = {query.display_name: query.id for query in workspace_client.queries.list()}
    for query_name in CONDITION_QUERIES:
        if query_name in existing_queries:
            query_id = existing_queries[query_name]
            # the deleted query goes to the trash and is permanently deleted after 30 days
            workspace_client.queries.delete(id=query_id)
            print(f'Deleted query {query_name} ({query_id})')
        else:
            print(f'Query {query_name} not found, nothing to delete')


if __name__ == '__main__':
    # the bundle script exports the authentication environment variables, WorkspaceClient picks them up
    destroy_condition_queries(WorkspaceClient())