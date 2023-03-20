r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
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
from twilio.rest.messaging.v1.brand_registration.brand_vetting import BrandVettingList


class BrandRegistrationInstance(InstanceResource):
    class BrandFeedback(object):
        TAX_ID = "TAX_ID"
        STOCK_SYMBOL = "STOCK_SYMBOL"
        NONPROFIT = "NONPROFIT"
        GOVERNMENT_ENTITY = "GOVERNMENT_ENTITY"
        OTHERS = "OTHERS"

    class IdentityStatus(object):
        SELF_DECLARED = "SELF_DECLARED"
        UNVERIFIED = "UNVERIFIED"
        VERIFIED = "VERIFIED"
        VETTED_VERIFIED = "VETTED_VERIFIED"

    class Status(object):
        PENDING = "PENDING"
        APPROVED = "APPROVED"
        FAILED = "FAILED"
        IN_REVIEW = "IN_REVIEW"
        DELETED = "DELETED"

    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the BrandRegistrationInstance

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "customer_profile_bundle_sid": payload.get("customer_profile_bundle_sid"),
            "a2p_profile_bundle_sid": payload.get("a2p_profile_bundle_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "brand_type": payload.get("brand_type"),
            "status": payload.get("status"),
            "tcr_id": payload.get("tcr_id"),
            "failure_reason": payload.get("failure_reason"),
            "url": payload.get("url"),
            "brand_score": deserialize.integer(payload.get("brand_score")),
            "brand_feedback": payload.get("brand_feedback"),
            "identity_status": payload.get("identity_status"),
            "russell_3000": payload.get("russell_3000"),
            "government_entity": payload.get("government_entity"),
            "tax_exempt_status": payload.get("tax_exempt_status"),
            "skip_automatic_sec_vet": payload.get("skip_automatic_sec_vet"),
            "mock": payload.get("mock"),
            "links": payload.get("links"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[BrandRegistrationContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BrandRegistrationContext for this BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        """
        if self._context is None:
            self._context = BrandRegistrationContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string to identify Brand Registration.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Brand Registration resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def customer_profile_bundle_sid(self):
        """
        :returns: A2P Messaging Profile Bundle BundleSid.
        :rtype: str
        """
        return self._properties["customer_profile_bundle_sid"]

    @property
    def a2p_profile_bundle_sid(self):
        """
        :returns: A2P Messaging Profile Bundle BundleSid.
        :rtype: str
        """
        return self._properties["a2p_profile_bundle_sid"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def brand_type(self):
        """
        :returns: Type of brand. One of: \"STANDARD\", \"STARTER\". STARTER is for the low volume, STARTER campaign use case. There can only be one STARTER campaign created per STARTER brand. STANDARD is for all other campaign use cases. Multiple campaign use cases can be created per STANDARD brand.
        :rtype: str
        """
        return self._properties["brand_type"]

    @property
    def status(self):
        """
        :returns:
        :rtype: BrandRegistrationInstance.Status
        """
        return self._properties["status"]

    @property
    def tcr_id(self):
        """
        :returns: Campaign Registry (TCR) Brand ID. Assigned only after successful brand registration.
        :rtype: str
        """
        return self._properties["tcr_id"]

    @property
    def failure_reason(self):
        """
        :returns: A reason why brand registration has failed. Only applicable when status is FAILED.
        :rtype: str
        """
        return self._properties["failure_reason"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Brand Registration resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def brand_score(self):
        """
        :returns: The secondary vetting score if it was done. Otherwise, it will be the brand score if it's returned from TCR. It may be null if no score is available.
        :rtype: int
        """
        return self._properties["brand_score"]

    @property
    def brand_feedback(self):
        """
        :returns: Feedback on how to improve brand score
        :rtype: list[BrandRegistrationInstance.BrandFeedback]
        """
        return self._properties["brand_feedback"]

    @property
    def identity_status(self):
        """
        :returns:
        :rtype: BrandRegistrationInstance.IdentityStatus
        """
        return self._properties["identity_status"]

    @property
    def russell_3000(self):
        """
        :returns: Publicly traded company identified in the Russell 3000 Index
        :rtype: bool
        """
        return self._properties["russell_3000"]

    @property
    def government_entity(self):
        """
        :returns: Identified as a government entity
        :rtype: bool
        """
        return self._properties["government_entity"]

    @property
    def tax_exempt_status(self):
        """
        :returns: Nonprofit organization tax-exempt status per section 501 of the U.S. tax code.
        :rtype: str
        """
        return self._properties["tax_exempt_status"]

    @property
    def skip_automatic_sec_vet(self):
        """
        :returns: A flag to disable automatic secondary vetting for brands which it would otherwise be done.
        :rtype: bool
        """
        return self._properties["skip_automatic_sec_vet"]

    @property
    def mock(self):
        """
        :returns: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
        :rtype: bool
        """
        return self._properties["mock"]

    @property
    def links(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["links"]

    def fetch(self):
        """
        Fetch the BrandRegistrationInstance


        :returns: The fetched BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the BrandRegistrationInstance


        :returns: The fetched BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        return await self._proxy.fetch_async()

    def update(self):
        """
        Update the BrandRegistrationInstance


        :returns: The updated BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        return self._proxy.update()

    async def update_async(self):
        """
        Asynchronous coroutine to update the BrandRegistrationInstance


        :returns: The updated BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        return await self._proxy.update_async()

    @property
    def brand_vettings(self):
        """
        Access the brand_vettings

        :returns: twilio.rest.messaging.v1.brand_registration.BrandVettingList
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandVettingList
        """
        return self._proxy.brand_vettings

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.BrandRegistrationInstance {}>".format(context)


class BrandRegistrationContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the BrandRegistrationContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Brand Registration resource to update.

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/a2p/BrandRegistrations/{sid}".format(**self._solution)

        self._brand_vettings: Optional[BrandVettingList] = None

    def fetch(self):
        """
        Fetch the BrandRegistrationInstance


        :returns: The fetched BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return BrandRegistrationInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the BrandRegistrationInstance


        :returns: The fetched BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return BrandRegistrationInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(self):
        """
        Update the BrandRegistrationInstance


        :returns: The updated BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        data = values.of({})

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BrandRegistrationInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    async def update_async(self):
        """
        Asynchronous coroutine to update the BrandRegistrationInstance


        :returns: The updated BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        data = values.of({})

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BrandRegistrationInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    @property
    def brand_vettings(self):
        """
        Access the brand_vettings

        :returns: twilio.rest.messaging.v1.brand_registration.BrandVettingList
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandVettingList
        """
        if self._brand_vettings is None:
            self._brand_vettings = BrandVettingList(
                self._version,
                self._solution["sid"],
            )
        return self._brand_vettings

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.BrandRegistrationContext {}>".format(context)


class BrandRegistrationPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of BrandRegistrationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        return BrandRegistrationInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.BrandRegistrationPage>"


class BrandRegistrationList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the BrandRegistrationList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationList
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationList
        """
        super().__init__(version)

        self._uri = "/a2p/BrandRegistrations"

    def create(
        self,
        customer_profile_bundle_sid,
        a2p_profile_bundle_sid,
        brand_type=values.unset,
        mock=values.unset,
        skip_automatic_sec_vet=values.unset,
    ):
        """
        Create the BrandRegistrationInstance

        :param str customer_profile_bundle_sid: Customer Profile Bundle Sid.
        :param str a2p_profile_bundle_sid: A2P Messaging Profile Bundle Sid.
        :param str brand_type: Type of brand being created. One of: \\\"STANDARD\\\", \\\"STARTER\\\". STARTER is for low volume, starter use cases. STANDARD is for all other use cases.
        :param bool mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
        :param bool skip_automatic_sec_vet: A flag to disable automatic secondary vetting for brands which it would otherwise be done.

        :returns: The created BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        data = values.of(
            {
                "CustomerProfileBundleSid": customer_profile_bundle_sid,
                "A2PProfileBundleSid": a2p_profile_bundle_sid,
                "BrandType": brand_type,
                "Mock": mock,
                "SkipAutomaticSecVet": skip_automatic_sec_vet,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BrandRegistrationInstance(self._version, payload)

    async def create_async(
        self,
        customer_profile_bundle_sid,
        a2p_profile_bundle_sid,
        brand_type=values.unset,
        mock=values.unset,
        skip_automatic_sec_vet=values.unset,
    ):
        """
        Asynchronously create the BrandRegistrationInstance

        :param str customer_profile_bundle_sid: Customer Profile Bundle Sid.
        :param str a2p_profile_bundle_sid: A2P Messaging Profile Bundle Sid.
        :param str brand_type: Type of brand being created. One of: \\\"STANDARD\\\", \\\"STARTER\\\". STARTER is for low volume, starter use cases. STANDARD is for all other use cases.
        :param bool mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
        :param bool skip_automatic_sec_vet: A flag to disable automatic secondary vetting for brands which it would otherwise be done.

        :returns: The created BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance
        """
        data = values.of(
            {
                "CustomerProfileBundleSid": customer_profile_bundle_sid,
                "A2PProfileBundleSid": a2p_profile_bundle_sid,
                "BrandType": brand_type,
                "Mock": mock,
                "SkipAutomaticSecVet": skip_automatic_sec_vet,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BrandRegistrationInstance(self._version, payload)

    def stream(self, limit=None, page_size=None):
        """
        Streams BrandRegistrationInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams BrandRegistrationInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists BrandRegistrationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists BrandRegistrationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.brand_registration.BrandRegistrationInstance]
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
        Retrieve a single page of BrandRegistrationInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return BrandRegistrationPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of BrandRegistrationInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationPage
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
        return BrandRegistrationPage(self._version, response)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BrandRegistrationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return BrandRegistrationPage(self._version, response)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of BrandRegistrationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BrandRegistrationInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return BrandRegistrationPage(self._version, response)

    def get(self, sid):
        """
        Constructs a BrandRegistrationContext

        :param sid: The SID of the Brand Registration resource to update.

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        """
        return BrandRegistrationContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a BrandRegistrationContext

        :param sid: The SID of the Brand Registration resource to update.

        :returns: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationContext
        """
        return BrandRegistrationContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Messaging.V1.BrandRegistrationList>"
