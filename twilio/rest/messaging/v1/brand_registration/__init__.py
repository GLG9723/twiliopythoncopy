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

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.messaging.v1.brand_registration.brand_registration_otp import (
    BrandRegistrationOtpList,
)
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

    """
    :ivar sid: The unique string to identify Brand Registration.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Brand Registration resource.
    :ivar customer_profile_bundle_sid: A2P Messaging Profile Bundle BundleSid.
    :ivar a2p_profile_bundle_sid: A2P Messaging Profile Bundle BundleSid.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar brand_type: Type of brand. One of: \"STANDARD\", \"SOLE_PROPRIETOR\". SOLE_PROPRIETOR is for the low volume, SOLE_PROPRIETOR campaign use case. There can only be one SOLE_PROPRIETOR campaign created per SOLE_PROPRIETOR brand. STANDARD is for all other campaign use cases. Multiple campaign use cases can be created per STANDARD brand.
    :ivar status: 
    :ivar tcr_id: Campaign Registry (TCR) Brand ID. Assigned only after successful brand registration.
    :ivar failure_reason: DEPRECATED. A reason why brand registration has failed. Only applicable when status is FAILED.
    :ivar errors: A list of errors that occurred during the brand registration process.
    :ivar url: The absolute URL of the Brand Registration resource.
    :ivar brand_score: The secondary vetting score if it was done. Otherwise, it will be the brand score if it's returned from TCR. It may be null if no score is available.
    :ivar brand_feedback: DEPRECATED. Feedback on how to improve brand score
    :ivar identity_status: 
    :ivar russell_3000: Publicly traded company identified in the Russell 3000 Index
    :ivar government_entity: Identified as a government entity
    :ivar tax_exempt_status: Nonprofit organization tax-exempt status per section 501 of the U.S. tax code.
    :ivar skip_automatic_sec_vet: A flag to disable automatic secondary vetting for brands which it would otherwise be done.
    :ivar mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
    :ivar links: 
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.customer_profile_bundle_sid: Optional[str] = payload.get(
            "customer_profile_bundle_sid"
        )
        self.a2p_profile_bundle_sid: Optional[str] = payload.get(
            "a2p_profile_bundle_sid"
        )
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.brand_type: Optional[str] = payload.get("brand_type")
        self.status: Optional["BrandRegistrationInstance.Status"] = payload.get(
            "status"
        )
        self.tcr_id: Optional[str] = payload.get("tcr_id")
        self.failure_reason: Optional[str] = payload.get("failure_reason")
        self.errors: Optional[List[Dict[str, object]]] = payload.get("errors")
        self.url: Optional[str] = payload.get("url")
        self.brand_score: Optional[int] = deserialize.integer(
            payload.get("brand_score")
        )
        self.brand_feedback: Optional[
            List["BrandRegistrationInstance.BrandFeedback"]
        ] = payload.get("brand_feedback")
        self.identity_status: Optional["BrandRegistrationInstance.IdentityStatus"] = (
            payload.get("identity_status")
        )
        self.russell_3000: Optional[bool] = payload.get("russell_3000")
        self.government_entity: Optional[bool] = payload.get("government_entity")
        self.tax_exempt_status: Optional[str] = payload.get("tax_exempt_status")
        self.skip_automatic_sec_vet: Optional[bool] = payload.get(
            "skip_automatic_sec_vet"
        )
        self.mock: Optional[bool] = payload.get("mock")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[BrandRegistrationContext] = None

    @property
    def _proxy(self) -> "BrandRegistrationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BrandRegistrationContext for this BrandRegistrationInstance
        """
        if self._context is None:
            self._context = BrandRegistrationContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "BrandRegistrationInstance":
        """
        Fetch the BrandRegistrationInstance


        :returns: The fetched BrandRegistrationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "BrandRegistrationInstance":
        """
        Asynchronous coroutine to fetch the BrandRegistrationInstance


        :returns: The fetched BrandRegistrationInstance
        """
        return await self._proxy.fetch_async()

    def update(self) -> "BrandRegistrationInstance":
        """
        Update the BrandRegistrationInstance


        :returns: The updated BrandRegistrationInstance
        """
        return self._proxy.update()

    async def update_async(self) -> "BrandRegistrationInstance":
        """
        Asynchronous coroutine to update the BrandRegistrationInstance


        :returns: The updated BrandRegistrationInstance
        """
        return await self._proxy.update_async()

    @property
    def brand_registration_otps(self) -> BrandRegistrationOtpList:
        """
        Access the brand_registration_otps
        """
        return self._proxy.brand_registration_otps

    @property
    def brand_vettings(self) -> BrandVettingList:
        """
        Access the brand_vettings
        """
        return self._proxy.brand_vettings

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.BrandRegistrationInstance {}>".format(context)


class BrandRegistrationContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the BrandRegistrationContext

        :param version: Version that contains the resource
        :param sid: The SID of the Brand Registration resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/a2p/BrandRegistrations/{sid}".format(**self._solution)

        self._brand_registration_otps: Optional[BrandRegistrationOtpList] = None
        self._brand_vettings: Optional[BrandVettingList] = None

    def fetch(self) -> BrandRegistrationInstance:
        """
        Fetch the BrandRegistrationInstance


        :returns: The fetched BrandRegistrationInstance
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

    async def fetch_async(self) -> BrandRegistrationInstance:
        """
        Asynchronous coroutine to fetch the BrandRegistrationInstance


        :returns: The fetched BrandRegistrationInstance
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

    def update(self) -> BrandRegistrationInstance:
        """
        Update the BrandRegistrationInstance


        :returns: The updated BrandRegistrationInstance
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

    async def update_async(self) -> BrandRegistrationInstance:
        """
        Asynchronous coroutine to update the BrandRegistrationInstance


        :returns: The updated BrandRegistrationInstance
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
    def brand_registration_otps(self) -> BrandRegistrationOtpList:
        """
        Access the brand_registration_otps
        """
        if self._brand_registration_otps is None:
            self._brand_registration_otps = BrandRegistrationOtpList(
                self._version,
                self._solution["sid"],
            )
        return self._brand_registration_otps

    @property
    def brand_vettings(self) -> BrandVettingList:
        """
        Access the brand_vettings
        """
        if self._brand_vettings is None:
            self._brand_vettings = BrandVettingList(
                self._version,
                self._solution["sid"],
            )
        return self._brand_vettings

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.BrandRegistrationContext {}>".format(context)


class BrandRegistrationPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> BrandRegistrationInstance:
        """
        Build an instance of BrandRegistrationInstance

        :param payload: Payload response from the API
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

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/a2p/BrandRegistrations"

    def create(
        self,
        customer_profile_bundle_sid: str,
        a2p_profile_bundle_sid: str,
        brand_type: Union[str, object] = values.unset,
        mock: Union[bool, object] = values.unset,
        skip_automatic_sec_vet: Union[bool, object] = values.unset,
    ) -> BrandRegistrationInstance:
        """
        Create the BrandRegistrationInstance

        :param customer_profile_bundle_sid: Customer Profile Bundle Sid.
        :param a2p_profile_bundle_sid: A2P Messaging Profile Bundle Sid.
        :param brand_type: Type of brand being created. One of: \\\"STANDARD\\\", \\\"SOLE_PROPRIETOR\\\". SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.
        :param mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
        :param skip_automatic_sec_vet: A flag to disable automatic secondary vetting for brands which it would otherwise be done.

        :returns: The created BrandRegistrationInstance
        """

        data = values.of(
            {
                "CustomerProfileBundleSid": customer_profile_bundle_sid,
                "A2PProfileBundleSid": a2p_profile_bundle_sid,
                "BrandType": brand_type,
                "Mock": serialize.boolean_to_string(mock),
                "SkipAutomaticSecVet": serialize.boolean_to_string(
                    skip_automatic_sec_vet
                ),
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
        customer_profile_bundle_sid: str,
        a2p_profile_bundle_sid: str,
        brand_type: Union[str, object] = values.unset,
        mock: Union[bool, object] = values.unset,
        skip_automatic_sec_vet: Union[bool, object] = values.unset,
    ) -> BrandRegistrationInstance:
        """
        Asynchronously create the BrandRegistrationInstance

        :param customer_profile_bundle_sid: Customer Profile Bundle Sid.
        :param a2p_profile_bundle_sid: A2P Messaging Profile Bundle Sid.
        :param brand_type: Type of brand being created. One of: \\\"STANDARD\\\", \\\"SOLE_PROPRIETOR\\\". SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.
        :param mock: A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
        :param skip_automatic_sec_vet: A flag to disable automatic secondary vetting for brands which it would otherwise be done.

        :returns: The created BrandRegistrationInstance
        """

        data = values.of(
            {
                "CustomerProfileBundleSid": customer_profile_bundle_sid,
                "A2PProfileBundleSid": a2p_profile_bundle_sid,
                "BrandType": brand_type,
                "Mock": serialize.boolean_to_string(mock),
                "SkipAutomaticSecVet": serialize.boolean_to_string(
                    skip_automatic_sec_vet
                ),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BrandRegistrationInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[BrandRegistrationInstance]:
        """
        Streams BrandRegistrationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[BrandRegistrationInstance]:
        """
        Asynchronously streams BrandRegistrationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BrandRegistrationInstance]:
        """
        Lists BrandRegistrationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BrandRegistrationInstance]:
        """
        Asynchronously lists BrandRegistrationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BrandRegistrationPage:
        """
        Retrieve a single page of BrandRegistrationInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BrandRegistrationInstance
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
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BrandRegistrationPage:
        """
        Asynchronously retrieve a single page of BrandRegistrationInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BrandRegistrationInstance
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

    def get_page(self, target_url: str) -> BrandRegistrationPage:
        """
        Retrieve a specific page of BrandRegistrationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BrandRegistrationInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return BrandRegistrationPage(self._version, response)

    async def get_page_async(self, target_url: str) -> BrandRegistrationPage:
        """
        Asynchronously retrieve a specific page of BrandRegistrationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BrandRegistrationInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return BrandRegistrationPage(self._version, response)

    def get(self, sid: str) -> BrandRegistrationContext:
        """
        Constructs a BrandRegistrationContext

        :param sid: The SID of the Brand Registration resource to update.
        """
        return BrandRegistrationContext(self._version, sid=sid)

    def __call__(self, sid: str) -> BrandRegistrationContext:
        """
        Constructs a BrandRegistrationContext

        :param sid: The SID of the Brand Registration resource to update.
        """
        return BrandRegistrationContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.BrandRegistrationList>"
