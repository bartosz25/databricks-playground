import os
from dataclasses import replace
from functools import cache

from databricks.bundles.core import Bundle, job_mutator
from databricks.bundles.jobs import Job
from databricks.sdk import WorkspaceClient

from create_condition_queries import CONDITION_QUERIES, create_condition_queries


@cache
def get_saved_query_ids(warehouse_id: str, bundle_target: str) -> dict[str, str]:
    return create_condition_queries(workspace_client=WorkspaceClient(), warehouse_id=warehouse_id,
                                    bundle_target=bundle_target)


@job_mutator
def get_condition_query_ids(bundle: Bundle, job: Job) -> Job:
    if os.environ.get('DO_NOT_RUN_MUTATOR') == 'true':
        return job
    query_name = next(query_name for query_name in CONDITION_QUERIES if job.name.endswith(query_name))
    sql_condition = job.trigger.sql_condition
    warehouse_id = bundle.resolve_variable(sql_condition.warehouse_id)
    bundle_target = bundle.target
    query_id = get_saved_query_ids(warehouse_id=warehouse_id, bundle_target=bundle_target)[query_name]
    return replace(job, trigger=replace(job.trigger, sql_condition=replace(sql_condition, sql_query_id=query_id)))
