import laboratory

from lab_assistant import storage


class Experiment(laboratory.Experiment):
    def publish(self, result):
        if not result.match:
            storage.store(result)
