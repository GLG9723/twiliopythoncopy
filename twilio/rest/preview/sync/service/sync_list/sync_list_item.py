r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SyncListItemInstance(InstanceResource):
    class QueryFromBoundType(object):
        INCLUSIVE = "inclusive"
        EXCLUSIVE = "exclusive"

    class QueryResultOrder(object):
        ASC = "asc"
        DESC = "desc"

    def __init__(
        self,
        version,
        payload,
        service_sid: str,
        list_sid: str,
        index: Optional[int] = None,
    ):
        """
        Initialize the SyncListItemInstance
        """
        super().__init__(version)

        self._properties = {
            "index": deserialize.integer(payload.get("index")),
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "list_sid": payload.get("list_sid"),
            "url": payload.get("url"),
            "revision": payload.get("revision"),
            "data": payload.get("data"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "created_by": payload.get("created_by"),
        }

        self._solution = {
            "service_sid": service_sid,
            "list_sid": list_sid,
            "index": index or self._properties["index"],
        }
        self._context: Optional[SyncListItemContext] = None

    @property
    def _proxy(self) -> "SyncListItemContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncListItemContext for this SyncListItemInstance
        """
        if self._context is None:
            self._context = SyncListItemContext(
                self._version,
                service_sid=self._solution["service_sid"],
                list_sid=self._solution["list_sid"],
                index=self._solution["index"],
            )
        return self._context

    @property
    def index(self) -> int:
        """
        :returns:
        """
        return self._properties["index"]

    @property
    def account_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["account_sid"]

    @property
    def service_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["service_sid"]

    @property
    def list_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["list_sid"]

    @property
    def url(self) -> str:
        """
        :returns:
        """
        return self._properties["url"]

    @property
    def revision(self) -> str:
        """
        :returns:
        """
        return self._properties["revision"]

    @property
    def data(self) -> dict:
        """
        :returns:
        """
        return self._properties["data"]

    @property
    def date_created(self) -> datetime:
        """
        :returns:
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns:
        """
        return self._properties["date_updated"]

    @property
    def created_by(self) -> str:
        """
        :returns:
        """
        return self._properties["created_by"]

    def delete(self, if_match=values.unset) -> bool:
        """
        Deletes the SyncListItemInstance

        :param str if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            if_match=if_match,
        )

    async def delete_async(self, if_match=values.unset) -> bool:
        """
        Asynchronous coroutine that deletes the SyncListItemInstance

        :param str if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            if_match=if_match,
        )

    def fetch(self) -> "SyncListItemInstance":
        """
        Fetch the SyncListItemInstance


        :returns: The fetched SyncListItemInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SyncListItemInstance":
        """
        Asynchronous coroutine to fetch the SyncListItemInstance


        :returns: The fetched SyncListItemInstance
        """
        return await self._proxy.fetch_async()

    def update(self, data, if_match=values.unset) -> "SyncListItemInstance":
        """
        Update the SyncListItemInstance

        :param object data:
        :param str if_match: The If-Match HTTP request header

        :returns: The updated SyncListItemInstance
        """
        return self._proxy.update(
            data=data,
            if_match=if_match,
        )

    async def update_async(self, data, if_match=values.unset) -> "SyncListItemInstance":
        """
        Asynchronous coroutine to update the SyncListItemInstance

        :param object data:
        :param str if_match: The If-Match HTTP request header

        :returns: The updated SyncListItemInstance
        """
        return await self._proxy.update_async(
            data=data,
            if_match=if_match,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.SyncListItemInstance {}>".format(context)


class SyncListItemContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, list_sid: str, index: int):
        """
        Initialize the SyncListItemContext

        :param version: Version that contains the resource
        :param service_sid:
        :param list_sid:
        :param index:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "list_sid": list_sid,
            "index": index,
        }
        self._uri = "/Services/{service_sid}/Lists/{list_sid}/Items/{index}".format(
            **self._solution
        )

    def delete(self, if_match=values.unset) -> bool:
        """
        Deletes the SyncListItemInstance

        :param str if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(self, if_match=values.unset) -> bool:
        """
        Asynchronous coroutine that deletes the SyncListItemInstance

        :param str if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def fetch(self) -> SyncListItemInstance:
        """
        Fetch the SyncListItemInstance


        :returns: The fetched SyncListItemInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            index=self._solution["index"],
        )

    async def fetch_async(self) -> SyncListItemInstance:
        """
        Asynchronous coroutine to fetch the SyncListItemInstance


        :returns: The fetched SyncListItemInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            index=self._solution["index"],
        )

    def update(self, data, if_match=values.unset) -> SyncListItemInstance:
        """
        Update the SyncListItemInstance

        :param object data:
        :param str if_match: The If-Match HTTP request header

        :returns: The updated SyncListItemInstance
        """
        data = values.of(
            {
                "Data": serialize.object(data),
            }
        )
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            index=self._solution["index"],
        )

    async def update_async(self, data, if_match=values.unset) -> SyncListItemInstance:
        """
        Asynchronous coroutine to update the SyncListItemInstance

        :param object data:
        :param str if_match: The If-Match HTTP request header

        :returns: The updated SyncListItemInstance
        """
        data = values.of(
            {
                "Data": serialize.object(data),
            }
        )
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            index=self._solution["index"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.SyncListItemContext {}>".format(context)


class SyncListItemPage(Page):
    def get_instance(self, payload) -> SyncListItemInstance:
        """
        Build an instance of SyncListItemInstance

        :param dict payload: Payload response from the API
        """
        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncListItemPage>"


class SyncListItemList(ListResource):
    def __init__(self, version: Version, service_sid: str, list_sid: str):
        """
        Initialize the SyncListItemList

        :param version: Version that contains the resource
        :param service_sid:
        :param list_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "list_sid": list_sid,
        }
        self._uri = "/Services/{service_sid}/Lists/{list_sid}/Items".format(
            **self._solution
        )

    def create(self, data) -> SyncListItemInstance:
        """
        Create the SyncListItemInstance

        :param object data:

        :returns: The created SyncListItemInstance
        """
        data = values.of(
            {
                "Data": serialize.object(data),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
        )

    async def create_async(self, data) -> SyncListItemInstance:
        """
        Asynchronously create the SyncListItemInstance

        :param object data:

        :returns: The created SyncListItemInstance
        """
        data = values.of(
            {
                "Data": serialize.object(data),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncListItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
        )

    def stream(
        self,
        order=values.unset,
        from_=values.unset,
        bounds=values.unset,
        limit=None,
        page_size=None,
    ) -> List[SyncListItemInstance]:
        """
        Streams SyncListItemInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;SyncListItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncListItemInstance.QueryFromBoundType&quot; bounds:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            order=order, from_=from_, bounds=bounds, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        order=values.unset,
        from_=values.unset,
        bounds=values.unset,
        limit=None,
        page_size=None,
    ) -> List[SyncListItemInstance]:
        """
        Asynchronously streams SyncListItemInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;SyncListItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncListItemInstance.QueryFromBoundType&quot; bounds:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            order=order, from_=from_, bounds=bounds, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        order=values.unset,
        from_=values.unset,
        bounds=values.unset,
        limit=None,
        page_size=None,
    ) -> List[SyncListItemInstance]:
        """
        Lists SyncListItemInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;SyncListItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncListItemInstance.QueryFromBoundType&quot; bounds:
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
                order=order,
                from_=from_,
                bounds=bounds,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        order=values.unset,
        from_=values.unset,
        bounds=values.unset,
        limit=None,
        page_size=None,
    ) -> List[SyncListItemInstance]:
        """
        Asynchronously lists SyncListItemInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;SyncListItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncListItemInstance.QueryFromBoundType&quot; bounds:
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
                order=order,
                from_=from_,
                bounds=bounds,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        order=values.unset,
        from_=values.unset,
        bounds=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> SyncListItemPage:
        """
        Retrieve a single page of SyncListItemInstance records from the API.
        Request is executed immediately

        :param &quot;SyncListItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncListItemInstance.QueryFromBoundType&quot; bounds:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncListItemInstance
        """
        data = values.of(
            {
                "Order": order,
                "From": from_,
                "Bounds": bounds,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SyncListItemPage(self._version, response, self._solution)

    async def page_async(
        self,
        order=values.unset,
        from_=values.unset,
        bounds=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> SyncListItemPage:
        """
        Asynchronously retrieve a single page of SyncListItemInstance records from the API.
        Request is executed immediately

        :param &quot;SyncListItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncListItemInstance.QueryFromBoundType&quot; bounds:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncListItemInstance
        """
        data = values.of(
            {
                "Order": order,
                "From": from_,
                "Bounds": bounds,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SyncListItemPage(self._version, response, self._solution)

    def get_page(self, target_url) -> SyncListItemPage:
        """
        Retrieve a specific page of SyncListItemInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncListItemInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SyncListItemPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> SyncListItemPage:
        """
        Asynchronously retrieve a specific page of SyncListItemInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncListItemInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SyncListItemPage(self._version, response, self._solution)

    def get(self, index) -> SyncListItemContext:
        """
        Constructs a SyncListItemContext

        :param index:
        """
        return SyncListItemContext(
            self._version,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            index=index,
        )

    def __call__(self, index) -> SyncListItemContext:
        """
        Constructs a SyncListItemContext

        :param index:
        """
        return SyncListItemContext(
            self._version,
            service_sid=self._solution["service_sid"],
            list_sid=self._solution["list_sid"],
            index=index,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncListItemList>"
