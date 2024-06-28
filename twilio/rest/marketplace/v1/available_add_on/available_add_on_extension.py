r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Marketplace
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class AvailableAddOnExtensionInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the AvailableAddOnExtension resource.
    :ivar available_add_on_sid: The SID of the AvailableAddOn resource to which this extension applies.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar product_name: The name of the Product this Extension is used within.
    :ivar unique_name: An application-defined string that uniquely identifies the resource.
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        available_add_on_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.available_add_on_sid: Optional[str] = payload.get("available_add_on_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.product_name: Optional[str] = payload.get("product_name")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "available_add_on_sid": available_add_on_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[AvailableAddOnExtensionContext] = None

    @property
    def _proxy(self) -> "AvailableAddOnExtensionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AvailableAddOnExtensionContext for this AvailableAddOnExtensionInstance
        """
        if self._context is None:
            self._context = AvailableAddOnExtensionContext(
                self._version,
                available_add_on_sid=self._solution["available_add_on_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "AvailableAddOnExtensionInstance":
        """
        Fetch the AvailableAddOnExtensionInstance


        :returns: The fetched AvailableAddOnExtensionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AvailableAddOnExtensionInstance":
        """
        Asynchronous coroutine to fetch the AvailableAddOnExtensionInstance


        :returns: The fetched AvailableAddOnExtensionInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return "<Twilio.Marketplace.V1.AvailableAddOnExtensionInstance {}>".format(
            context
        )


class AvailableAddOnExtensionContext(InstanceContext):

    def __init__(self, version: Version, available_add_on_sid: str, sid: str):
        """
        Initialize the AvailableAddOnExtensionContext

        :param version: Version that contains the resource
        :param available_add_on_sid: The SID of the AvailableAddOn resource with the extension to fetch.
        :param sid: The SID of the AvailableAddOn Extension resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "available_add_on_sid": available_add_on_sid,
            "sid": sid,
        }
        self._uri = "/AvailableAddOns/{available_add_on_sid}/Extensions/{sid}".format(
            **self._solution
        )

    def fetch(self) -> AvailableAddOnExtensionInstance:
        """
        Fetch the AvailableAddOnExtensionInstance


        :returns: The fetched AvailableAddOnExtensionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AvailableAddOnExtensionInstance(
            self._version,
            payload,
            available_add_on_sid=self._solution["available_add_on_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AvailableAddOnExtensionInstance:
        """
        Asynchronous coroutine to fetch the AvailableAddOnExtensionInstance


        :returns: The fetched AvailableAddOnExtensionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AvailableAddOnExtensionInstance(
            self._version,
            payload,
            available_add_on_sid=self._solution["available_add_on_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return "<Twilio.Marketplace.V1.AvailableAddOnExtensionContext {}>".format(
            context
        )


class AvailableAddOnExtensionPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> AvailableAddOnExtensionInstance:
        """
        Build an instance of AvailableAddOnExtensionInstance

        :param payload: Payload response from the API
        """
        return AvailableAddOnExtensionInstance(
            self._version,
            payload,
            available_add_on_sid=self._solution["available_add_on_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Marketplace.V1.AvailableAddOnExtensionPage>"


class AvailableAddOnExtensionList(ListResource):

    def __init__(self, version: Version, available_add_on_sid: str):
        """
        Initialize the AvailableAddOnExtensionList

        :param version: Version that contains the resource
        :param available_add_on_sid: The SID of the AvailableAddOn resource with the extensions to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "available_add_on_sid": available_add_on_sid,
        }
        self._uri = "/AvailableAddOns/{available_add_on_sid}/Extensions".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[AvailableAddOnExtensionInstance]:
        """
        Streams AvailableAddOnExtensionInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[AvailableAddOnExtensionInstance]:
        """
        Asynchronously streams AvailableAddOnExtensionInstance records from the API as a generator stream.
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
    ) -> List[AvailableAddOnExtensionInstance]:
        """
        Lists AvailableAddOnExtensionInstance records from the API as a list.
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
    ) -> List[AvailableAddOnExtensionInstance]:
        """
        Asynchronously lists AvailableAddOnExtensionInstance records from the API as a list.
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
    ) -> AvailableAddOnExtensionPage:
        """
        Retrieve a single page of AvailableAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AvailableAddOnExtensionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AvailableAddOnExtensionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AvailableAddOnExtensionPage:
        """
        Asynchronously retrieve a single page of AvailableAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AvailableAddOnExtensionInstance
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
        return AvailableAddOnExtensionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> AvailableAddOnExtensionPage:
        """
        Retrieve a specific page of AvailableAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AvailableAddOnExtensionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AvailableAddOnExtensionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> AvailableAddOnExtensionPage:
        """
        Asynchronously retrieve a specific page of AvailableAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AvailableAddOnExtensionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AvailableAddOnExtensionPage(self._version, response, self._solution)

    def get(self, sid: str) -> AvailableAddOnExtensionContext:
        """
        Constructs a AvailableAddOnExtensionContext

        :param sid: The SID of the AvailableAddOn Extension resource to fetch.
        """
        return AvailableAddOnExtensionContext(
            self._version,
            available_add_on_sid=self._solution["available_add_on_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> AvailableAddOnExtensionContext:
        """
        Constructs a AvailableAddOnExtensionContext

        :param sid: The SID of the AvailableAddOn Extension resource to fetch.
        """
        return AvailableAddOnExtensionContext(
            self._version,
            available_add_on_sid=self._solution["available_add_on_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Marketplace.V1.AvailableAddOnExtensionList>"
