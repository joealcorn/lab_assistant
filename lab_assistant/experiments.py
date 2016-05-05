from logging import getLogger

import laboratory
from lab_assistant import tasks

logger = getLogger(__name__)


class Experiment(laboratory.Experiment):

    publish_tasks = [
        tasks.store_result,
    ]

    def publish(self, result):
        for task in self.publish_tasks:
            try:
                task(result)
            except Exception as e:
                logger.exception(e)
        return super(Experiment, self).publish(result)
