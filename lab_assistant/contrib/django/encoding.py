import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.core import serializers


class LaboratoryJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Model):
            # the json.loads here is not ideal but we need to prevent
            # the value from being double-encoded
            return json.loads(serializers.serialize('json', [obj]))
        return super(LaboratoryJSONEncoder, self).default(obj)
