from kedro.pipeline import node, Pipeline
from kedro_tutorial.pipelines.data_engineering.nodes import (
    create_features,
    create_labels,
)

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=create_features,
                inputs="wdbc",
                outputs="features",
                name="creating_features",
            ),
            node(
                func=create_labels,
                inputs="wdbc",
                outputs="labels",
                name="creating_labels",
            ),
        ]
    )