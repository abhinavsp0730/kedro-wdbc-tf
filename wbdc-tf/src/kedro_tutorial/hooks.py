from typing import Dict

from kedro.framework.hooks import hook_impl
from kedro.pipeline import Pipeline

from kedro_tutorial.pipelines.data_engineering import pipeline as de


class ProjectHooks:
    @hook_impl
    def register_pipelines(self) -> Dict[str, Pipeline]:
        """Register the project's pipeline.

        Returns:
            A mapping from a pipeline name to a ``Pipeline`` object.

        """
        de_pipeline = de.create_pipeline()

        return {
            "de": de_pipeline,
            "__default__": de_pipeline,
        }


project_hooks = ProjectHooks()