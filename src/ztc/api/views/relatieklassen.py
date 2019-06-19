from rest_framework import viewsets, mixins
from vng_api_common.viewsets import NestedViewSetMixin

from ...datamodel.models import (
    ZaakInformatieobjectType, ZaakInformatieobjectTypeArchiefregime
)
from ..filters import ZaakInformatieobjectTypeFilter
from ..scopes import SCOPE_ZAAKTYPES_READ, SCOPE_ZAAKTYPES_WRITE
from ..serializers import (
    ZaakInformatieobjectTypeArchiefregimeSerializer,
    ZaakTypeInformatieObjectTypeSerializer
)
from ..utils.rest_flex_fields import FlexFieldsMixin
from ..utils.viewsets import FilterSearchOrderingViewSetMixin


class ZaakTypeInformatieObjectTypeViewSet(mixins.CreateModelMixin,
                                          mixins.DestroyModelMixin,
                                          viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Relatie met informatieobjecttype dat relevant is voor zaaktype.

    list:
    Een verzameling van ZAAKINFORMATIEOBJECTTYPEn.

    Filteren van de gegevens kan middels de querystringparameters:
    - zaaktype: URL van het zaaktype
    - informatie_object_type: URL van het zaaktype
    - richting: waarde van de richting (string)

    Meerdere querystring-parameters tegelijk worden als een AND beschouwd.
    """
    queryset = ZaakInformatieobjectType.objects.all()
    serializer_class = ZaakTypeInformatieObjectTypeSerializer
    filterset_class = ZaakInformatieobjectTypeFilter
    lookup_field = 'uuid'
    pagination_class = None
    required_scopes = {
        'list': SCOPE_ZAAKTYPES_READ,
        'retrieve': SCOPE_ZAAKTYPES_READ,
        'create': SCOPE_ZAAKTYPES_WRITE,
        'destroy': SCOPE_ZAAKTYPES_WRITE,
    }


class ZaakInformatieobjectTypeArchiefregimeViewSet(NestedViewSetMixin, FilterSearchOrderingViewSetMixin,
                                                   FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Afwijkende archiveringskenmerken van informatieobjecten van een INFORMATIEOBJECTTYPE bij zaken van een ZAAKTYPE op
    grond van resultaten van een RESULTAATTYPE bij dat ZAAKTYPE.

    list:
    Een verzameling van ZAAKINFORMATIEOBJECTTYPEARCHIEFREGIMEs.
    """
    queryset = ZaakInformatieobjectTypeArchiefregime.objects.all()
    serializer_class = ZaakInformatieobjectTypeArchiefregimeSerializer
    required_scopes = {
        'list': SCOPE_ZAAKTYPES_READ,
        'retrieve': SCOPE_ZAAKTYPES_READ,
    }
