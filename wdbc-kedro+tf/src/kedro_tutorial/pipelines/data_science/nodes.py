# Copyright 2018-2019 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
#     or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from typing import Dict, List

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from kedro.extras.datasets.tensorflow import TensorFlowModelDataset

def split_data(features: pd.DataFrame, labels: pd.DataFrame, parameters: Dict) -> List:
    """Splits data into training and test sets.

        Args:
            data: Source data.
            parameters: Parameters defined in parameters.yml.
        Returns:
            A list containing split data.

    """
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )

    return [np.array(X_train), np.array(X_test), np.array(y_train), np.array(y_test)]


def train_model(X_train: np.ndarray, y_train: np.ndarray) -> tf.keras.Model:
    """Train a Tensorflow data into wdbc dataset.

        Args:
            X_train: Training data of independent features.
            y_train: Training data for price.

        Returns:
            Trained model.

    """
    model = tf.keras.Sequential([
            tf.keras.layers.Dense(256, activation='relu'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1)
            ])

    model.compile(loss = tf.losses.BinaryCrossentropy(from_logits=True), metrics= tf.metrics.BinaryAccuracy(),
                      optimizer = tf.optimizers.Adam())

    print(".........Training Started.........")
    model.fit(X_train, y_train, epochs=10)
    return model


def evaluate_model(model: TensorFlowModelDataset, X_test: np.ndarray, y_test: np.ndarray):
    """Evaluate the model into test dataset

        Args:
            model: Trained model.
            X_test: Testing data of independent features.
            y_test: labels of the testing set

    """
    print(".........Evaluation Started.........")
    history = model.evaluate(X_test, y_test)