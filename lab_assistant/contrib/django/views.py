from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import HttpResponse
from simpleflake import parse_simpleflake

from lab_assistant.storage import get_storage


@staff_member_required
def mismatch_list(request):
    name = request.GET.get('name')
    if not name:
        return render(request, 'lab_assistant/pick_experiment.html')

    storage = get_storage(name=name)
    results = storage.list()
    for result in results:
        result.timestamp = datetime.fromtimestamp(parse_simpleflake(result.key).timestamp).isoformat()

    return render(request, 'lab_assistant/result_list.html', {
        'results': results,
    })


@staff_member_required
def specific_mismatch(request, result_id):
    storage = get_storage(name='Hotspot_cache_results')
    result = storage.get(result_id)
    return HttpResponse(str(result))
