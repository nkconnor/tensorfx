# Copyright 2016 TensorLab. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

# _graphs.py
# Implements the GraphBuilder base class.

class GraphDefinition(object):
  """Base class for different types of graph definitions
  """
  def __init__(self, graph):
    """Initializes a GraphDefinition object.

    Arguments:
      graph: The TensorFlow graph.
    """
    self.graph = graph


class TrainingGraph(GraphDefinition):
  """A GraphDefinition object for containing a TensorFlow graph used for training.
  """
  def __init__(self, graph):
    """Initializes a TrainingGraph object.

    Arguments:
      graph: The TensorFlow graph.
    """
    super(TrainingGraph, self).__init__(graph)


class EvaluationGraph(GraphDefinition):
  """A GraphDefinition object for containing a TensorFlow graph used for evaluation.
  """
  def __init__(self, graph):
    """Initializes an EvaluationGraph object.

    Arguments:
      graph: The TensorFlow graph.
    """
    super(EvaluationGraph, self).__init__(graph)


class PredictionGraph(GraphDefinition):
  """A GraphDefinition object for containing a TensorFlow graph used for prediction.
  """
  def __init__(self, graph):
    """Initializes a PredictionGraph object.

    Arguments:
      graph: The TensorFlow graph.
    """
    super(PredictionGraph, self).__init__(graphg)


class GraphBuilder(object):
  """Builds TensorFlow graphs for different phases: training, evaluation and prediction.
  """
  def build_training_graph(self, args):
    """Builds the graph to use for training a model.

    Arguments:
      args: An args object containing all training job arguments including hyperparameters.
    Returns:
      A TrainingGraph instance.
    """
    raise NotImplementedError()

  def build_evaluation_graph(self, args):
    """Builds the graph to use for evaluating a model during training.

    Arguments:
      args: An args object containing all training job arguments including hyperparameters.
    Returns:
      An EvaluationGraph instance.
    """
    raise NotImplementedError()

  def build_prediction_graph(self, args):
    """Builds the graph to use for predictions with the trained model.

    Arguments:
      args: An args object containing all training job arguments including hyperparameters.
    Returns:
      A PredictionGraph instance.
    """
    raise NotImplementedError()