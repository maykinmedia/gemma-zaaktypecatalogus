from django.conf import settings
from django.utils.module_loading import import_string
from django.utils.translation import ugettext_lazy as _

from rest_framework.serializers import ValidationError
from vng_api_common.models import APICredential


def fetch_object(resource: str, url: str) -> dict:
    Client = import_string(settings.ZDS_CLIENT_CLASS)
    client = Client.from_url(url)
    client.auth = APICredential.get_auth(url)
    obj = client.retrieve(resource, url=url)
    return obj


class RelationCatalogValidator:
    code = 'relations-incorrect-catalogus'
    message = _("The {} has catalogus different from created object")

    def __init__(self, relation_field: str, catalogus_field='catalogus'):
        self.relation_field = relation_field
        self.catalogus_field = catalogus_field

    def __call__(self, attrs: dict):
        relations = attrs.get(self.relation_field)
        catalogus = attrs.get(self.catalogus_field)

        if not relations:
            return

        if not isinstance(relations, list):
            relations = [relations]

        for relation in relations:
            if relation.catalogus != catalogus:
                raise ValidationError(self.message.format(self.relation_field), code=self.code)


class ProcesTypeValidator:
    code = 'procestype-mismatch'
    message = _("{} should belong to the same procestype as {}")

    def __init__(self, relation_field: str, zaaktype_field='zaaktype'):
        self.relation_field = relation_field
        self.zaaktype_field = zaaktype_field

    def __call__(self, attrs: dict):
        selectielijstklasse_url = attrs.get(self.relation_field)
        zaaktype = attrs.get(self.zaaktype_field)

        if not selectielijstklasse_url:
            return

        selectielijstklasse = fetch_object('resultaat', selectielijstklasse_url)

        if selectielijstklasse['procesType'] != zaaktype.selectielijst_procestype:
            raise ValidationError(self.message.format(self.relation_field, self.zaaktype_field), code=self.code)
