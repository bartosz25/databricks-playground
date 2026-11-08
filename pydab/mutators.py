from dataclasses import replace

from databricks.bundles.core import Bundle, job_mutator
from databricks.bundles.jobs import Job


@job_mutator
def add_demo_tags(bundle: Bundle, job: Job) -> Job:
    return replace(job, tags={**job.tags, "blog": "pydabs", "target": bundle.target})
