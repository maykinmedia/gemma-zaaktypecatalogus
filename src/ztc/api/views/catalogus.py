from rest_framework import viewsets

from ztc.datamodel.models import Catalogus

from ..serializers import CatalogusSerializer


class CatalogusViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    De verzameling van ZAAKTYPEn - incl. daarvoor relevante objecttypen - voor een Domein die als één geheel beheerd
    wordt.

    list:
    Een verzameling van CATALOGUSsen.
    """
    queryset = Catalogus.objects.all()
    serializer_class = CatalogusSerializer
    pagination_class = None

    # This makes the URLs consistent with `NestedSimpleRouter`, which uses `<prefix>_id` instead of `<prefix>_pk`.
    # lookup_url_kwarg = 'id'
