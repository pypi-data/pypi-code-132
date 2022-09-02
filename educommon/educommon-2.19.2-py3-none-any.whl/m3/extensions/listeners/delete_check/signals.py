# coding: utf-8
from django.db.models.signals import ModelSignal


# Сигналы перед и после каскадного удаления объекта (CascadeDeleteMixin)
#   - instance - удаляемый объект
#   - initiator - объект, который стал инициатором удаления instance
pre_cascade = ModelSignal(providing_args=["instance", "initiator"])
post_cascade = ModelSignal(providing_args=["instance", "initiator"])
