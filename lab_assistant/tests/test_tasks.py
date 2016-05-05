import mock

from laboratory.observation import Observation
from laboratory.result import Result


from lab_assistant import tasks, experiments
from lab_assistant.tests import cases


def result_factory(first, second):
    control = Observation('Control')
    control.set_start_time()
    control.record(first)
    control.set_end_time()

    candidate = Observation('Candidate')
    candidate.set_start_time()
    candidate.record(second)
    candidate.set_end_time()

    return Result(experiments.Experiment(), control, [candidate])


class TestStorageTask(cases.TestCase):
    @mock.patch('lab_assistant.tasks.storage.store')
    def test_task_stores_in_backend_on_mismatch(self, store):
        result = result_factory(True, False)
        assert not result.match
        tasks.store_result(result)
        store.assert_called_once_with(result)

    @mock.patch('lab_assistant.tasks.storage.store')
    def test_task_does_not_store_on_match(self, store):
        result = result_factory(True, True)
        assert result.match
        tasks.store_result(result)
        assert not store.called
