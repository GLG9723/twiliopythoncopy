r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class PhoneNumberInstance(InstanceResource):
    class AddressRequirement(object):
        NONE = "none"
        ANY = "any"
        LOCAL = "local"
        FOREIGN = "foreign"

    def __init__(self, version, payload, trunk_sid: str, sid: Optional[str] = None):
        """
        Initialize the PhoneNumberInstance

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "address_requirements": payload.get("address_requirements"),
            "api_version": payload.get("api_version"),
            "beta": payload.get("beta"),
            "capabilities": payload.get("capabilities"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "friendly_name": payload.get("friendly_name"),
            "links": payload.get("links"),
            "phone_number": payload.get("phone_number"),
            "sid": payload.get("sid"),
            "sms_application_sid": payload.get("sms_application_sid"),
            "sms_fallback_method": payload.get("sms_fallback_method"),
            "sms_fallback_url": payload.get("sms_fallback_url"),
            "sms_method": payload.get("sms_method"),
            "sms_url": payload.get("sms_url"),
            "status_callback": payload.get("status_callback"),
            "status_callback_method": payload.get("status_callback_method"),
            "trunk_sid": payload.get("trunk_sid"),
            "url": payload.get("url"),
            "voice_application_sid": payload.get("voice_application_sid"),
            "voice_caller_id_lookup": payload.get("voice_caller_id_lookup"),
            "voice_fallback_method": payload.get("voice_fallback_method"),
            "voice_fallback_url": payload.get("voice_fallback_url"),
            "voice_method": payload.get("voice_method"),
            "voice_url": payload.get("voice_url"),
        }

        self._solution = {
            "trunk_sid": trunk_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[PhoneNumberContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                trunk_sid=self._solution["trunk_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the PhoneNumber resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def address_requirements(self):
        """
        :returns:
        :rtype: PhoneNumberInstance.AddressRequirement
        """
        return self._properties["address_requirements"]

    @property
    def api_version(self):
        """
        :returns: The API version used to start a new TwiML session.
        :rtype: str
        """
        return self._properties["api_version"]

    @property
    def beta(self):
        """
        :returns: Whether the phone number is new to the Twilio platform. Can be: `true` or `false`.
        :rtype: bool
        """
        return self._properties["beta"]

    @property
    def capabilities(self):
        """
        :returns: The set of Boolean properties that indicate whether a phone number can receive calls or messages.  Capabilities are  `Voice`, `SMS`, and `MMS` and each capability can be: `true` or `false`.
        :rtype: dict
        """
        return self._properties["capabilities"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties["links"]

    @property
    def phone_number(self):
        """
        :returns: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        :rtype: str
        """
        return self._properties["phone_number"]

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the PhoneNumber resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def sms_application_sid(self):
        """
        :returns: The SID of the application that handles SMS messages sent to the phone number. If an `sms_application_sid` is present, we ignore all `sms_*_url` values and use those of the application.
        :rtype: str
        """
        return self._properties["sms_application_sid"]

    @property
    def sms_fallback_method(self):
        """
        :returns: The HTTP method we use to call `sms_fallback_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties["sms_fallback_method"]

    @property
    def sms_fallback_url(self):
        """
        :returns: The URL that we call using the `sms_fallback_method` when an error occurs while retrieving or executing the TwiML from `sms_url`.
        :rtype: str
        """
        return self._properties["sms_fallback_url"]

    @property
    def sms_method(self):
        """
        :returns: The HTTP method we use to call `sms_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties["sms_method"]

    @property
    def sms_url(self):
        """
        :returns: The URL we call using the `sms_method` when the phone number receives an incoming SMS message.
        :rtype: str
        """
        return self._properties["sms_url"]

    @property
    def status_callback(self):
        """
        :returns: The URL we call using the `status_callback_method` to send status information to your application.
        :rtype: str
        """
        return self._properties["status_callback"]

    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method we use to call `status_callback`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties["status_callback_method"]

    @property
    def trunk_sid(self):
        """
        :returns: The SID of the Trunk that handles calls to the phone number. If a `trunk_sid` is present, we ignore all of the voice URLs and voice applications and use those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
        :rtype: str
        """
        return self._properties["trunk_sid"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def voice_application_sid(self):
        """
        :returns: The SID of the application that handles calls to the phone number. If a `voice_application_sid` is present, we ignore all of the voice URLs and use those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
        :rtype: str
        """
        return self._properties["voice_application_sid"]

    @property
    def voice_caller_id_lookup(self):
        """
        :returns: Whether we look up the caller's caller-ID name from the CNAM database ($0.01 per look up). Can be: `true` or `false`.
        :rtype: bool
        """
        return self._properties["voice_caller_id_lookup"]

    @property
    def voice_fallback_method(self):
        """
        :returns: The HTTP method that we use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties["voice_fallback_method"]

    @property
    def voice_fallback_url(self):
        """
        :returns: The URL that we call using the `voice_fallback_method` when an error occurs retrieving or executing the TwiML requested by `url`.
        :rtype: str
        """
        return self._properties["voice_fallback_url"]

    @property
    def voice_method(self):
        """
        :returns: The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties["voice_method"]

    @property
    def voice_url(self):
        """
        :returns: The URL we call using the `voice_method` when the phone number receives a call. The `voice_url` is not be used if a `voice_application_sid` or a `trunk_sid` is set.
        :rtype: str
        """
        return self._properties["voice_url"]

    def delete(self):
        """
        Deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.PhoneNumberInstance {}>".format(context)


class PhoneNumberContext(InstanceContext):
    def __init__(self, version: Version, trunk_sid: str, sid: str):
        """
        Initialize the PhoneNumberContext

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to fetch the PhoneNumber resource.
        :param sid: The unique string that we created to identify the PhoneNumber resource to fetch.

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
            "sid": sid,
        }
        self._uri = "/Trunks/{trunk_sid}/PhoneNumbers/{sid}".format(**self._solution)

    def delete(self):
        """
        Deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.PhoneNumberContext {}>".format(context)


class PhoneNumberPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of PhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        return PhoneNumberInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.PhoneNumberPage>"


class PhoneNumberList(ListResource):
    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to read the PhoneNumber resources.

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberList
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
        }
        self._uri = "/Trunks/{trunk_sid}/PhoneNumbers".format(**self._solution)

    def create(self, phone_number_sid):
        """
        Create the PhoneNumberInstance

        :param str phone_number_sid: The SID of the [Incoming Phone Number](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) that you want to associate with the trunk.

        :returns: The created PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        data = values.of(
            {
                "PhoneNumberSid": phone_number_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PhoneNumberInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    async def create_async(self, phone_number_sid):
        """
        Asynchronously create the PhoneNumberInstance

        :param str phone_number_sid: The SID of the [Incoming Phone Number](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) that you want to associate with the trunk.

        :returns: The created PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        data = values.of(
            {
                "PhoneNumberSid": phone_number_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PhoneNumberInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams PhoneNumberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams PhoneNumberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists PhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists PhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return PhoneNumberPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return PhoneNumberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return PhoneNumberPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return PhoneNumberPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a PhoneNumberContext

        :param sid: The unique string that we created to identify the PhoneNumber resource to fetch.

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(
            self._version, trunk_sid=self._solution["trunk_sid"], sid=sid
        )

    def __call__(self, sid):
        """
        Constructs a PhoneNumberContext

        :param sid: The unique string that we created to identify the PhoneNumber resource to fetch.

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(
            self._version, trunk_sid=self._solution["trunk_sid"], sid=sid
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Trunking.V1.PhoneNumberList>"
