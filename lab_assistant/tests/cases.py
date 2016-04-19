from exam.cases import Exam
import exam
import lab_assistant


class TestCase(exam.cases.Exam):
    @exam.before
    def reset_config(self):
        lab_assistant.conf.update({
            'storage': {
                'path': 'lab_assistant.storage.backends.null.NullBackend',
                'options': {},
            }
        })
