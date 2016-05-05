from lab_assistant import storage


def store_result(result):
    if not result.match:
        storage.store(result)
