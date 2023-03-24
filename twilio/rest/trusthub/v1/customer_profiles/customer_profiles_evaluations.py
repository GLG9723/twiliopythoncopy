r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CustomerProfilesEvaluationsInstance(InstanceResource):
    class Status(object):
        COMPLIANT = "compliant"
        NONCOMPLIANT = "noncompliant"

    def __init__(
        self, version, payload, customer_profile_sid: str, sid: Optional[str] = None
    ):
        """
        Initialize the CustomerProfilesEvaluationsInstance
        """
        super().__init__(version)

        self._sid: Optional[str] = payload.get("sid")
        self._account_sid: Optional[str] = payload.get("account_sid")
        self._policy_sid: Optional[str] = payload.get("policy_sid")
        self._customer_profile_sid: Optional[str] = payload.get("customer_profile_sid")
        self._status: Optional[
            "CustomerProfilesEvaluationsInstance.Status"
        ] = payload.get("status")
        self._results: Optional[List[object]] = payload.get("results")
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._url: Optional[str] = payload.get("url")

        self._solution = {
            "customer_profile_sid": customer_profile_sid,
            "sid": sid or self._sid,
        }
        self._context: Optional[CustomerProfilesEvaluationsContext] = None

    @property
    def _proxy(self) -> "CustomerProfilesEvaluationsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CustomerProfilesEvaluationsContext for this CustomerProfilesEvaluationsInstance
        """
        if self._context is None:
            self._context = CustomerProfilesEvaluationsContext(
                self._version,
                customer_profile_sid=self._solution["customer_profile_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that identifies the Evaluation resource.
        """
        return self._sid

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the customer_profile resource.
        """
        return self._account_sid

    @property
    def policy_sid(self) -> Optional[str]:
        """
        :returns: The unique string of a policy that is associated to the customer_profile resource.
        """
        return self._policy_sid

    @property
    def customer_profile_sid(self) -> Optional[str]:
        """
        :returns: The unique string that we created to identify the customer_profile resource.
        """
        return self._customer_profile_sid

    @property
    def status(self) -> Optional["CustomerProfilesEvaluationsInstance.Status"]:
        return self._status

    @property
    def results(self) -> Optional[List[object]]:
        """
        :returns: The results of the Evaluation which includes the valid and invalid attributes.
        """
        return self._results

    @property
    def date_created(self) -> Optional[datetime]:
        return self._date_created

    @property
    def url(self) -> Optional[str]:
        return self._url

    def fetch(self) -> "CustomerProfilesEvaluationsInstance":
        """
        Fetch the CustomerProfilesEvaluationsInstance


        :returns: The fetched CustomerProfilesEvaluationsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CustomerProfilesEvaluationsInstance":
        """
        Asynchronous coroutine to fetch the CustomerProfilesEvaluationsInstance


        :returns: The fetched CustomerProfilesEvaluationsInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trusthub.V1.CustomerProfilesEvaluationsInstance {}>".format(
            context
        )


class CustomerProfilesEvaluationsContext(InstanceContext):
    def __init__(self, version: Version, customer_profile_sid: str, sid: str):
        """
        Initialize the CustomerProfilesEvaluationsContext

        :param version: Version that contains the resource
        :param customer_profile_sid: The unique string that we created to identify the customer_profile resource.
        :param sid: The unique string that identifies the Evaluation resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "customer_profile_sid": customer_profile_sid,
            "sid": sid,
        }
        self._uri = "/CustomerProfiles/{customer_profile_sid}/Evaluations/{sid}".format(
            **self._solution
        )

    def fetch(self) -> CustomerProfilesEvaluationsInstance:
        """
        Fetch the CustomerProfilesEvaluationsInstance


        :returns: The fetched CustomerProfilesEvaluationsInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CustomerProfilesEvaluationsInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution["customer_profile_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CustomerProfilesEvaluationsInstance:
        """
        Asynchronous coroutine to fetch the CustomerProfilesEvaluationsInstance


        :returns: The fetched CustomerProfilesEvaluationsInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CustomerProfilesEvaluationsInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution["customer_profile_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trusthub.V1.CustomerProfilesEvaluationsContext {}>".format(
            context
        )


class CustomerProfilesEvaluationsPage(Page):
    def get_instance(self, payload) -> CustomerProfilesEvaluationsInstance:
        """
        Build an instance of CustomerProfilesEvaluationsInstance

        :param dict payload: Payload response from the API
        """
        return CustomerProfilesEvaluationsInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution["customer_profile_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.CustomerProfilesEvaluationsPage>"


class CustomerProfilesEvaluationsList(ListResource):
    def __init__(self, version: Version, customer_profile_sid: str):
        """
        Initialize the CustomerProfilesEvaluationsList

        :param version: Version that contains the resource
        :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "customer_profile_sid": customer_profile_sid,
        }
        self._uri = "/CustomerProfiles/{customer_profile_sid}/Evaluations".format(
            **self._solution
        )

    def create(self, policy_sid) -> CustomerProfilesEvaluationsInstance:
        """
        Create the CustomerProfilesEvaluationsInstance

        :param str policy_sid: The unique string of a policy that is associated to the customer_profile resource.

        :returns: The created CustomerProfilesEvaluationsInstance
        """
        data = values.of(
            {
                "PolicySid": policy_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CustomerProfilesEvaluationsInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution["customer_profile_sid"],
        )

    async def create_async(self, policy_sid) -> CustomerProfilesEvaluationsInstance:
        """
        Asynchronously create the CustomerProfilesEvaluationsInstance

        :param str policy_sid: The unique string of a policy that is associated to the customer_profile resource.

        :returns: The created CustomerProfilesEvaluationsInstance
        """
        data = values.of(
            {
                "PolicySid": policy_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CustomerProfilesEvaluationsInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution["customer_profile_sid"],
        )

    def stream(
        self, limit=None, page_size=None
    ) -> List[CustomerProfilesEvaluationsInstance]:
        """
        Streams CustomerProfilesEvaluationsInstance records from the API as a generator stream.
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
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, limit=None, page_size=None
    ) -> List[CustomerProfilesEvaluationsInstance]:
        """
        Asynchronously streams CustomerProfilesEvaluationsInstance records from the API as a generator stream.
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
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self, limit=None, page_size=None
    ) -> List[CustomerProfilesEvaluationsInstance]:
        """
        Lists CustomerProfilesEvaluationsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self, limit=None, page_size=None
    ) -> List[CustomerProfilesEvaluationsInstance]:
        """
        Asynchronously lists CustomerProfilesEvaluationsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> CustomerProfilesEvaluationsPage:
        """
        Retrieve a single page of CustomerProfilesEvaluationsInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CustomerProfilesEvaluationsInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CustomerProfilesEvaluationsPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> CustomerProfilesEvaluationsPage:
        """
        Asynchronously retrieve a single page of CustomerProfilesEvaluationsInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CustomerProfilesEvaluationsInstance
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
        return CustomerProfilesEvaluationsPage(self._version, response, self._solution)

    def get_page(self, target_url) -> CustomerProfilesEvaluationsPage:
        """
        Retrieve a specific page of CustomerProfilesEvaluationsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CustomerProfilesEvaluationsInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CustomerProfilesEvaluationsPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> CustomerProfilesEvaluationsPage:
        """
        Asynchronously retrieve a specific page of CustomerProfilesEvaluationsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CustomerProfilesEvaluationsInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CustomerProfilesEvaluationsPage(self._version, response, self._solution)

    def get(self, sid) -> CustomerProfilesEvaluationsContext:
        """
        Constructs a CustomerProfilesEvaluationsContext

        :param sid: The unique string that identifies the Evaluation resource.
        """
        return CustomerProfilesEvaluationsContext(
            self._version,
            customer_profile_sid=self._solution["customer_profile_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> CustomerProfilesEvaluationsContext:
        """
        Constructs a CustomerProfilesEvaluationsContext

        :param sid: The unique string that identifies the Evaluation resource.
        """
        return CustomerProfilesEvaluationsContext(
            self._version,
            customer_profile_sid=self._solution["customer_profile_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.CustomerProfilesEvaluationsList>"
