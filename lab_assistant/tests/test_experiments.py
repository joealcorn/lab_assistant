import mock

from lab_assistant.tests import cases
import lab_assistant


class TestExperimentPublish(cases.TestCase):
    def test_publish_calls_tasks(self):
        task = mock.MagicMock()
        experiment = type('Experiment', (lab_assistant.experiments.Experiment,), {
            'publish_tasks': [task]
        })()
        result = object()
        experiment.publish(result)
        task.assert_called_once_with(result)
