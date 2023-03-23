r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class TemplateInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the TemplateInstance

        :returns: twilio.rest.verify.v2.template.TemplateInstance
        :rtype: twilio.rest.verify.v2.template.TemplateInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "friendly_name": payload.get("friendly_name"),
            "channels": payload.get("channels"),
            "translations": payload.get("translations"),
        }

        self._solution = {}

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies a Verification Template.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def friendly_name(self):
        """
        :returns: A descriptive string that you create to describe a Template.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def channels(self):
        """
        :returns: A list of channels that support the Template. Can include: sms, voice
        :rtype: List[str]
        """
        return self._properties["channels"]

    @property
    def translations(self):
        """
        :returns: An object that contains the different translations of the template. Every translation is identified by the language short name and contains its respective information as the approval status, text and created/modified date.
        :rtype: dict
        """
        return self._properties["translations"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.TemplateInstance {}>".format(context)


class TemplatePage(Page):
    def get_instance(self, payload):
        """
        Build an instance of TemplateInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.template.TemplateInstance
        :rtype: twilio.rest.verify.v2.template.TemplateInstance
        """
        return TemplateInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.TemplatePage>"


class TemplateList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the TemplateList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.verify.v2.template.TemplateList
        :rtype: twilio.rest.verify.v2.template.TemplateList
        """
        super().__init__(version)

        self._uri = "/Templates"

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams TemplateInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str friendly_name: String filter used to query templates with a given friendly name
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.template.TemplateInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(friendly_name=friendly_name, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, friendly_name=values.unset, limit=None, page_size=None
    ):
        """
        Asynchronously streams TemplateInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str friendly_name: String filter used to query templates with a given friendly name
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.template.TemplateInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            friendly_name=friendly_name, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists TemplateInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str friendly_name: String filter used to query templates with a given friendly name
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.template.TemplateInstance]
        """
        return list(
            self.stream(
                friendly_name=friendly_name,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Asynchronously lists TemplateInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str friendly_name: String filter used to query templates with a given friendly name
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.template.TemplateInstance]
        """
        return list(
            await self.stream_async(
                friendly_name=friendly_name,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        friendly_name=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of TemplateInstance records from the API.
        Request is executed immediately

        :param str friendly_name: String filter used to query templates with a given friendly name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TemplateInstance
        :rtype: twilio.rest.verify.v2.template.TemplatePage
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return TemplatePage(self._version, response)

    async def page_async(
        self,
        friendly_name=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of TemplateInstance records from the API.
        Request is executed immediately

        :param str friendly_name: String filter used to query templates with a given friendly name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TemplateInstance
        :rtype: twilio.rest.verify.v2.template.TemplatePage
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return TemplatePage(self._version, response)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TemplateInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TemplateInstance
        :rtype: twilio.rest.verify.v2.template.TemplatePage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return TemplatePage(self._version, response)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of TemplateInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TemplateInstance
        :rtype: twilio.rest.verify.v2.template.TemplatePage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return TemplatePage(self._version, response)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Verify.V2.TemplateList>"
