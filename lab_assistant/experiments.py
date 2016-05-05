import laboratory
from lab_assistant import tasks


class Experiment(laboratory.Experiment):

    publish_tasks = [
        tasks.store_result,
    ]

    def publish(self, result):
        for task in self.publish_tasks:
            try:
                task(result)
            except Exception, e:
                logger.exception(e)
        return super(Experiment, self).publish(result)
