r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class DeploymentInstance(InstanceResource):

    """
    :ivar sid: The unique string that we created to identify the Deployment resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Deployment resource.
    :ivar service_sid: The SID of the Service that the Deployment resource is associated with.
    :ivar environment_sid: The SID of the Environment for the Deployment.
    :ivar build_sid: The SID of the Build for the deployment.
    :ivar date_created: The date and time in GMT when the Deployment resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the Deployment resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Deployment resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        environment_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.environment_sid: Optional[str] = payload.get("environment_sid")
        self.build_sid: Optional[str] = payload.get("build_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "environment_sid": environment_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[DeploymentContext] = None

    @property
    def _proxy(self) -> "DeploymentContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DeploymentContext for this DeploymentInstance
        """
        if self._context is None:
            self._context = DeploymentContext(
                self._version,
                service_sid=self._solution["service_sid"],
                environment_sid=self._solution["environment_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "DeploymentInstance":
        """
        Fetch the DeploymentInstance


        :returns: The fetched DeploymentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "DeploymentInstance":
        """
        Asynchronous coroutine to fetch the DeploymentInstance


        :returns: The fetched DeploymentInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.DeploymentInstance {}>".format(context)


class DeploymentContext(InstanceContext):
    def __init__(
        self, version: Version, service_sid: str, environment_sid: str, sid: str
    ):
        """
        Initialize the DeploymentContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Deployment resource from.
        :param environment_sid: The SID of the Environment used by the Deployment to fetch.
        :param sid: The SID that identifies the Deployment resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "environment_sid": environment_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Environments/{environment_sid}/Deployments/{sid}".format(
            **self._solution
        )

    def fetch(self) -> DeploymentInstance:
        """
        Fetch the DeploymentInstance


        :returns: The fetched DeploymentInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return DeploymentInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> DeploymentInstance:
        """
        Asynchronous coroutine to fetch the DeploymentInstance


        :returns: The fetched DeploymentInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return DeploymentInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.DeploymentContext {}>".format(context)


class DeploymentPage(Page):
    def get_instance(self, payload) -> DeploymentInstance:
        """
        Build an instance of DeploymentInstance

        :param dict payload: Payload response from the API
        """
        return DeploymentInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.DeploymentPage>"


class DeploymentList(ListResource):
    def __init__(self, version: Version, service_sid: str, environment_sid: str):
        """
        Initialize the DeploymentList

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Deployment resources from.
        :param environment_sid: The SID of the Environment used by the Deployment resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "environment_sid": environment_sid,
        }
        self._uri = (
            "/Services/{service_sid}/Environments/{environment_sid}/Deployments".format(
                **self._solution
            )
        )

    def create(self, build_sid=values.unset) -> DeploymentInstance:
        """
        Create the DeploymentInstance

        :param str build_sid: The SID of the Build for the Deployment.

        :returns: The created DeploymentInstance
        """
        data = values.of(
            {
                "BuildSid": build_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeploymentInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
        )

    async def create_async(self, build_sid=values.unset) -> DeploymentInstance:
        """
        Asynchronously create the DeploymentInstance

        :param str build_sid: The SID of the Build for the Deployment.

        :returns: The created DeploymentInstance
        """
        data = values.of(
            {
                "BuildSid": build_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeploymentInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
        )

    def stream(self, limit=None, page_size=None) -> List[DeploymentInstance]:
        """
        Streams DeploymentInstance records from the API as a generator stream.
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
    ) -> List[DeploymentInstance]:
        """
        Asynchronously streams DeploymentInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[DeploymentInstance]:
        """
        Lists DeploymentInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[DeploymentInstance]:
        """
        Asynchronously lists DeploymentInstance records from the API as a list.
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
    ) -> DeploymentPage:
        """
        Retrieve a single page of DeploymentInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DeploymentInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return DeploymentPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> DeploymentPage:
        """
        Asynchronously retrieve a single page of DeploymentInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DeploymentInstance
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
        return DeploymentPage(self._version, response, self._solution)

    def get_page(self, target_url) -> DeploymentPage:
        """
        Retrieve a specific page of DeploymentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeploymentInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return DeploymentPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> DeploymentPage:
        """
        Asynchronously retrieve a specific page of DeploymentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeploymentInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return DeploymentPage(self._version, response, self._solution)

    def get(self, sid) -> DeploymentContext:
        """
        Constructs a DeploymentContext

        :param sid: The SID that identifies the Deployment resource to fetch.
        """
        return DeploymentContext(
            self._version,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> DeploymentContext:
        """
        Constructs a DeploymentContext

        :param sid: The SID that identifies the Deployment resource to fetch.
        """
        return DeploymentContext(
            self._version,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.DeploymentList>"
