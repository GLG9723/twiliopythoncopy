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
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.serverless.v1.service.function.function_version.function_version_content import (
    FunctionVersionContentList,
)


class FunctionVersionInstance(InstanceResource):
    class Visibility(object):
        PUBLIC = "public"
        PRIVATE = "private"
        PROTECTED = "protected"

    """
    :ivar sid: The unique string that we created to identify the Function Version resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Function Version resource.
    :ivar service_sid: The SID of the Service that the Function Version resource is associated with.
    :ivar function_sid: The SID of the Function resource that is the parent of the Function Version resource.
    :ivar path: The URL-friendly string by which the Function Version resource can be referenced. It can be a maximum of 255 characters. All paths begin with a forward slash ('/'). If a Function Version creation request is submitted with a path not containing a leading slash, the path will automatically be prepended with one.
    :ivar visibility: 
    :ivar date_created: The date and time in GMT when the Function Version resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Function Version resource.
    :ivar links: 
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        function_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.function_sid: Optional[str] = payload.get("function_sid")
        self.path: Optional[str] = payload.get("path")
        self.visibility: Optional["FunctionVersionInstance.Visibility"] = payload.get(
            "visibility"
        )
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "service_sid": service_sid,
            "function_sid": function_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[FunctionVersionContext] = None

    @property
    def _proxy(self) -> "FunctionVersionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FunctionVersionContext for this FunctionVersionInstance
        """
        if self._context is None:
            self._context = FunctionVersionContext(
                self._version,
                service_sid=self._solution["service_sid"],
                function_sid=self._solution["function_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "FunctionVersionInstance":
        """
        Fetch the FunctionVersionInstance


        :returns: The fetched FunctionVersionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "FunctionVersionInstance":
        """
        Asynchronous coroutine to fetch the FunctionVersionInstance


        :returns: The fetched FunctionVersionInstance
        """
        return await self._proxy.fetch_async()

    @property
    def function_version_content(self) -> FunctionVersionContentList:
        """
        Access the function_version_content
        """
        return self._proxy.function_version_content

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.FunctionVersionInstance {}>".format(context)


class FunctionVersionContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, function_sid: str, sid: str):
        """
        Initialize the FunctionVersionContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Function Version resource from.
        :param function_sid: The SID of the function that is the parent of the Function Version resource to fetch.
        :param sid: The SID of the Function Version resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "function_sid": function_sid,
            "sid": sid,
        }
        self._uri = (
            "/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}".format(
                **self._solution
            )
        )

        self._function_version_content: Optional[FunctionVersionContentList] = None

    def fetch(self) -> FunctionVersionInstance:
        """
        Fetch the FunctionVersionInstance


        :returns: The fetched FunctionVersionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FunctionVersionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            function_sid=self._solution["function_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> FunctionVersionInstance:
        """
        Asynchronous coroutine to fetch the FunctionVersionInstance


        :returns: The fetched FunctionVersionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FunctionVersionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            function_sid=self._solution["function_sid"],
            sid=self._solution["sid"],
        )

    @property
    def function_version_content(self) -> FunctionVersionContentList:
        """
        Access the function_version_content
        """
        if self._function_version_content is None:
            self._function_version_content = FunctionVersionContentList(
                self._version,
                self._solution["service_sid"],
                self._solution["function_sid"],
                self._solution["sid"],
            )
        return self._function_version_content

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.FunctionVersionContext {}>".format(context)


class FunctionVersionPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> FunctionVersionInstance:
        """
        Build an instance of FunctionVersionInstance

        :param payload: Payload response from the API
        """
        return FunctionVersionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            function_sid=self._solution["function_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.FunctionVersionPage>"


class FunctionVersionList(ListResource):
    def __init__(self, version: Version, service_sid: str, function_sid: str):
        """
        Initialize the FunctionVersionList

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Function Version resources from.
        :param function_sid: The SID of the function that is the parent of the Function Version resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "function_sid": function_sid,
        }
        self._uri = "/Services/{service_sid}/Functions/{function_sid}/Versions".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[FunctionVersionInstance]:
        """
        Streams FunctionVersionInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[FunctionVersionInstance]:
        """
        Asynchronously streams FunctionVersionInstance records from the API as a generator stream.
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
    ) -> List[FunctionVersionInstance]:
        """
        Lists FunctionVersionInstance records from the API as a list.
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
    ) -> List[FunctionVersionInstance]:
        """
        Asynchronously lists FunctionVersionInstance records from the API as a list.
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
    ) -> FunctionVersionPage:
        """
        Retrieve a single page of FunctionVersionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FunctionVersionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return FunctionVersionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> FunctionVersionPage:
        """
        Asynchronously retrieve a single page of FunctionVersionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FunctionVersionInstance
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
        return FunctionVersionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> FunctionVersionPage:
        """
        Retrieve a specific page of FunctionVersionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FunctionVersionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FunctionVersionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> FunctionVersionPage:
        """
        Asynchronously retrieve a specific page of FunctionVersionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FunctionVersionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FunctionVersionPage(self._version, response, self._solution)

    def get(self, sid: str) -> FunctionVersionContext:
        """
        Constructs a FunctionVersionContext

        :param sid: The SID of the Function Version resource to fetch.
        """
        return FunctionVersionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            function_sid=self._solution["function_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> FunctionVersionContext:
        """
        Constructs a FunctionVersionContext

        :param sid: The SID of the Function Version resource to fetch.
        """
        return FunctionVersionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            function_sid=self._solution["function_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.FunctionVersionList>"
