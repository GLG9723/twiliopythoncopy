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
from typing import Dict, List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SyncMapItemInstance(InstanceResource):
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
        map_sid: str,
        key: Optional[str] = None,
    ):
        """
        Initialize the SyncMapItemInstance
        """
        super().__init__(version)

        self._key: Optional[str] = payload.get("key")
        self._account_sid: Optional[str] = payload.get("account_sid")
        self._service_sid: Optional[str] = payload.get("service_sid")
        self._map_sid: Optional[str] = payload.get("map_sid")
        self._url: Optional[str] = payload.get("url")
        self._revision: Optional[str] = payload.get("revision")
        self._data: Optional[Dict[str, object]] = payload.get("data")
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self._created_by: Optional[str] = payload.get("created_by")

        self._solution = {
            "service_sid": service_sid,
            "map_sid": map_sid,
            "key": key or self._key,
        }
        self._context: Optional[SyncMapItemContext] = None

    @property
    def _proxy(self) -> "SyncMapItemContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncMapItemContext for this SyncMapItemInstance
        """
        if self._context is None:
            self._context = SyncMapItemContext(
                self._version,
                service_sid=self._solution["service_sid"],
                map_sid=self._solution["map_sid"],
                key=self._solution["key"],
            )
        return self._context

    @property
    def key(self) -> Optional[str]:
        return self._key

    @property
    def account_sid(self) -> Optional[str]:
        return self._account_sid

    @property
    def service_sid(self) -> Optional[str]:
        return self._service_sid

    @property
    def map_sid(self) -> Optional[str]:
        return self._map_sid

    @property
    def url(self) -> Optional[str]:
        return self._url

    @property
    def revision(self) -> Optional[str]:
        return self._revision

    @property
    def data(self) -> Optional[Dict[str, object]]:
        return self._data

    @property
    def date_created(self) -> Optional[datetime]:
        return self._date_created

    @property
    def date_updated(self) -> Optional[datetime]:
        return self._date_updated

    @property
    def created_by(self) -> Optional[str]:
        return self._created_by

    def delete(self, if_match=values.unset) -> bool:
        """
        Deletes the SyncMapItemInstance

        :param str if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            if_match=if_match,
        )

    async def delete_async(self, if_match=values.unset) -> bool:
        """
        Asynchronous coroutine that deletes the SyncMapItemInstance

        :param str if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            if_match=if_match,
        )

    def fetch(self) -> "SyncMapItemInstance":
        """
        Fetch the SyncMapItemInstance


        :returns: The fetched SyncMapItemInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SyncMapItemInstance":
        """
        Asynchronous coroutine to fetch the SyncMapItemInstance


        :returns: The fetched SyncMapItemInstance
        """
        return await self._proxy.fetch_async()

    def update(self, data, if_match=values.unset) -> "SyncMapItemInstance":
        """
        Update the SyncMapItemInstance

        :param object data:
        :param str if_match: The If-Match HTTP request header

        :returns: The updated SyncMapItemInstance
        """
        return self._proxy.update(
            data=data,
            if_match=if_match,
        )

    async def update_async(self, data, if_match=values.unset) -> "SyncMapItemInstance":
        """
        Asynchronous coroutine to update the SyncMapItemInstance

        :param object data:
        :param str if_match: The If-Match HTTP request header

        :returns: The updated SyncMapItemInstance
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
        return "<Twilio.Preview.Sync.SyncMapItemInstance {}>".format(context)


class SyncMapItemContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, map_sid: str, key: str):
        """
        Initialize the SyncMapItemContext

        :param version: Version that contains the resource
        :param service_sid:
        :param map_sid:
        :param key:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "map_sid": map_sid,
            "key": key,
        }
        self._uri = "/Services/{service_sid}/Maps/{map_sid}/Items/{key}".format(
            **self._solution
        )

    def delete(self, if_match=values.unset) -> bool:
        """
        Deletes the SyncMapItemInstance

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
        Asynchronous coroutine that deletes the SyncMapItemInstance

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

    def fetch(self) -> SyncMapItemInstance:
        """
        Fetch the SyncMapItemInstance


        :returns: The fetched SyncMapItemInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=self._solution["key"],
        )

    async def fetch_async(self) -> SyncMapItemInstance:
        """
        Asynchronous coroutine to fetch the SyncMapItemInstance


        :returns: The fetched SyncMapItemInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=self._solution["key"],
        )

    def update(self, data, if_match=values.unset) -> SyncMapItemInstance:
        """
        Update the SyncMapItemInstance

        :param object data:
        :param str if_match: The If-Match HTTP request header

        :returns: The updated SyncMapItemInstance
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

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=self._solution["key"],
        )

    async def update_async(self, data, if_match=values.unset) -> SyncMapItemInstance:
        """
        Asynchronous coroutine to update the SyncMapItemInstance

        :param object data:
        :param str if_match: The If-Match HTTP request header

        :returns: The updated SyncMapItemInstance
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

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=self._solution["key"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.SyncMapItemContext {}>".format(context)


class SyncMapItemPage(Page):
    def get_instance(self, payload) -> SyncMapItemInstance:
        """
        Build an instance of SyncMapItemInstance

        :param dict payload: Payload response from the API
        """
        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncMapItemPage>"


class SyncMapItemList(ListResource):
    def __init__(self, version: Version, service_sid: str, map_sid: str):
        """
        Initialize the SyncMapItemList

        :param version: Version that contains the resource
        :param service_sid:
        :param map_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "map_sid": map_sid,
        }
        self._uri = "/Services/{service_sid}/Maps/{map_sid}/Items".format(
            **self._solution
        )

    def create(self, key, data) -> SyncMapItemInstance:
        """
        Create the SyncMapItemInstance

        :param str key:
        :param object data:

        :returns: The created SyncMapItemInstance
        """
        data = values.of(
            {
                "Key": key,
                "Data": serialize.object(data),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
        )

    async def create_async(self, key, data) -> SyncMapItemInstance:
        """
        Asynchronously create the SyncMapItemInstance

        :param str key:
        :param object data:

        :returns: The created SyncMapItemInstance
        """
        data = values.of(
            {
                "Key": key,
                "Data": serialize.object(data),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
        )

    def stream(
        self,
        order=values.unset,
        from_=values.unset,
        bounds=values.unset,
        limit=None,
        page_size=None,
    ) -> List[SyncMapItemInstance]:
        """
        Streams SyncMapItemInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;SyncMapItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncMapItemInstance.QueryFromBoundType&quot; bounds:
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
    ) -> List[SyncMapItemInstance]:
        """
        Asynchronously streams SyncMapItemInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;SyncMapItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncMapItemInstance.QueryFromBoundType&quot; bounds:
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
    ) -> List[SyncMapItemInstance]:
        """
        Lists SyncMapItemInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;SyncMapItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncMapItemInstance.QueryFromBoundType&quot; bounds:
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
    ) -> List[SyncMapItemInstance]:
        """
        Asynchronously lists SyncMapItemInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;SyncMapItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncMapItemInstance.QueryFromBoundType&quot; bounds:
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
    ) -> SyncMapItemPage:
        """
        Retrieve a single page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param &quot;SyncMapItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncMapItemInstance.QueryFromBoundType&quot; bounds:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapItemInstance
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
        return SyncMapItemPage(self._version, response, self._solution)

    async def page_async(
        self,
        order=values.unset,
        from_=values.unset,
        bounds=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> SyncMapItemPage:
        """
        Asynchronously retrieve a single page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param &quot;SyncMapItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncMapItemInstance.QueryFromBoundType&quot; bounds:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapItemInstance
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
        return SyncMapItemPage(self._version, response, self._solution)

    def get_page(self, target_url) -> SyncMapItemPage:
        """
        Retrieve a specific page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapItemInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SyncMapItemPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> SyncMapItemPage:
        """
        Asynchronously retrieve a specific page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapItemInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SyncMapItemPage(self._version, response, self._solution)

    def get(self, key) -> SyncMapItemContext:
        """
        Constructs a SyncMapItemContext

        :param key:
        """
        return SyncMapItemContext(
            self._version,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=key,
        )

    def __call__(self, key) -> SyncMapItemContext:
        """
        Constructs a SyncMapItemContext

        :param key:
        """
        return SyncMapItemContext(
            self._version,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=key,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncMapItemList>"
