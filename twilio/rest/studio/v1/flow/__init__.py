r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.studio.v1.flow.engagement import EngagementList
from twilio.rest.studio.v1.flow.execution import ExecutionList


class FlowList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the FlowList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.studio.v1.flow.FlowList
        :rtype: twilio.rest.studio.v1.flow.FlowList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Flows".format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams FlowInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.studio.v1.flow.FlowInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams FlowInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.studio.v1.flow.FlowInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists FlowInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v1.flow.FlowInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists FlowInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v1.flow.FlowInstance]
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
        Retrieve a single page of FlowInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return FlowPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of FlowInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowPage
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
        return FlowPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FlowInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FlowPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of FlowInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FlowPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a FlowContext

        :param sid: The SID of the Flow resource to fetch.

        :returns: twilio.rest.studio.v1.flow.FlowContext
        :rtype: twilio.rest.studio.v1.flow.FlowContext
        """
        return FlowContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a FlowContext

        :param sid: The SID of the Flow resource to fetch.

        :returns: twilio.rest.studio.v1.flow.FlowContext
        :rtype: twilio.rest.studio.v1.flow.FlowContext
        """
        return FlowContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Studio.V1.FlowList>"


class FlowPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the FlowPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.studio.v1.flow.FlowPage
        :rtype: twilio.rest.studio.v1.flow.FlowPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FlowInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v1.flow.FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowInstance
        """
        return FlowInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Studio.V1.FlowPage>"


class FlowInstance(InstanceResource):
    class Status(object):
        DRAFT = "draft"
        PUBLISHED = "published"

    def __init__(self, version, payload, sid: str | None = None):
        """
        Initialize the FlowInstance

        :returns: twilio.rest.studio.v1.flow.FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "friendly_name": payload.get("friendly_name"),
            "status": payload.get("status"),
            "version": deserialize.integer(payload.get("version")),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._context = None
        self._solution = {
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FlowContext for this FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowContext
        """
        if self._context is None:
            self._context = FlowContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Flow resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flow resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the Flow.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def status(self):
        """
        :returns:
        :rtype: FlowInstance.Status
        """
        return self._properties["status"]

    @property
    def version(self):
        """
        :returns: The latest version number of the Flow's definition.
        :rtype: int
        """
        return self._properties["version"]

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
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns: The URLs of the Flow's nested resources.
        :rtype: dict
        """
        return self._properties["links"]

    def delete(self):
        """
        Deletes the FlowInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the FlowInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the FlowInstance


        :returns: The fetched FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FlowInstance


        :returns: The fetched FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowInstance
        """
        return await self._proxy.fetch_async()

    @property
    def engagements(self):
        """
        Access the engagements

        :returns: twilio.rest.studio.v1.flow.EngagementList
        :rtype: twilio.rest.studio.v1.flow.EngagementList
        """
        return self._proxy.engagements

    @property
    def executions(self):
        """
        Access the executions

        :returns: twilio.rest.studio.v1.flow.ExecutionList
        :rtype: twilio.rest.studio.v1.flow.ExecutionList
        """
        return self._proxy.executions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V1.FlowInstance {}>".format(context)


class FlowContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the FlowContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Flow resource to fetch.

        :returns: twilio.rest.studio.v1.flow.FlowContext
        :rtype: twilio.rest.studio.v1.flow.FlowContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Flows/{sid}".format(**self._solution)

        self._engagements = None
        self._executions = None

    def delete(self):
        """
        Deletes the FlowInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the FlowInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the FlowInstance


        :returns: The fetched FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FlowInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FlowInstance


        :returns: The fetched FlowInstance
        :rtype: twilio.rest.studio.v1.flow.FlowInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FlowInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    @property
    def engagements(self):
        """
        Access the engagements

        :returns: twilio.rest.studio.v1.flow.EngagementList
        :rtype: twilio.rest.studio.v1.flow.EngagementList
        """
        if self._engagements is None:
            self._engagements = EngagementList(
                self._version,
                self._solution["sid"],
            )
        return self._engagements

    @property
    def executions(self):
        """
        Access the executions

        :returns: twilio.rest.studio.v1.flow.ExecutionList
        :rtype: twilio.rest.studio.v1.flow.ExecutionList
        """
        if self._executions is None:
            self._executions = ExecutionList(
                self._version,
                self._solution["sid"],
            )
        return self._executions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V1.FlowContext {}>".format(context)
