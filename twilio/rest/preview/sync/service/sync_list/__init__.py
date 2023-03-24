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
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.sync.service.sync_list.sync_list_item import SyncListItemList
from twilio.rest.preview.sync.service.sync_list.sync_list_permission import (
    SyncListPermissionList,
)


class SyncListInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, sid: Optional[str] = None):
        """
        Initialize the SyncListInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "unique_name": payload.get("unique_name"),
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "url": payload.get("url"),
            "links": payload.get("links"),
            "revision": payload.get("revision"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "created_by": payload.get("created_by"),
        }

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[SyncListContext] = None

    @property
    def _proxy(self) -> "SyncListContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncListContext for this SyncListInstance
        """
        if self._context is None:
            self._context = SyncListContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> str:
        """
        :returns:
        """
        return self._properties["sid"]

    @property
    def unique_name(self) -> str:
        """
        :returns:
        """
        return self._properties["unique_name"]

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
    def url(self) -> str:
        """
        :returns:
        """
        return self._properties["url"]

    @property
    def links(self) -> dict:
        """
        :returns:
        """
        return self._properties["links"]

    @property
    def revision(self) -> str:
        """
        :returns:
        """
        return self._properties["revision"]

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

    def delete(self) -> bool:
        """
        Deletes the SyncListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SyncListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "SyncListInstance":
        """
        Fetch the SyncListInstance


        :returns: The fetched SyncListInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SyncListInstance":
        """
        Asynchronous coroutine to fetch the SyncListInstance


        :returns: The fetched SyncListInstance
        """
        return await self._proxy.fetch_async()

    @property
    def sync_list_items(self) -> SyncListItemList:
        """
        Access the sync_list_items
        """
        return self._proxy.sync_list_items

    @property
    def sync_list_permissions(self) -> SyncListPermissionList:
        """
        Access the sync_list_permissions
        """
        return self._proxy.sync_list_permissions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.SyncListInstance {}>".format(context)


class SyncListContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the SyncListContext

        :param version: Version that contains the resource
        :param service_sid:
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Lists/{sid}".format(**self._solution)

        self._sync_list_items: Optional[SyncListItemList] = None
        self._sync_list_permissions: Optional[SyncListPermissionList] = None

    def delete(self) -> bool:
        """
        Deletes the SyncListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SyncListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> SyncListInstance:
        """
        Fetch the SyncListInstance


        :returns: The fetched SyncListInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SyncListInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SyncListInstance:
        """
        Asynchronous coroutine to fetch the SyncListInstance


        :returns: The fetched SyncListInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SyncListInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def sync_list_items(self) -> SyncListItemList:
        """
        Access the sync_list_items
        """
        if self._sync_list_items is None:
            self._sync_list_items = SyncListItemList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._sync_list_items

    @property
    def sync_list_permissions(self) -> SyncListPermissionList:
        """
        Access the sync_list_permissions
        """
        if self._sync_list_permissions is None:
            self._sync_list_permissions = SyncListPermissionList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._sync_list_permissions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.SyncListContext {}>".format(context)


class SyncListPage(Page):
    def get_instance(self, payload) -> SyncListInstance:
        """
        Build an instance of SyncListInstance

        :param dict payload: Payload response from the API
        """
        return SyncListInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncListPage>"


class SyncListList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the SyncListList

        :param version: Version that contains the resource
        :param service_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Lists".format(**self._solution)

    def create(self, unique_name=values.unset) -> SyncListInstance:
        """
        Create the SyncListInstance

        :param str unique_name:

        :returns: The created SyncListInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncListInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(self, unique_name=values.unset) -> SyncListInstance:
        """
        Asynchronously create the SyncListInstance

        :param str unique_name:

        :returns: The created SyncListInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncListInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(self, limit=None, page_size=None) -> List[SyncListInstance]:
        """
        Streams SyncListInstance records from the API as a generator stream.
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

    async def stream_async(self, limit=None, page_size=None) -> List[SyncListInstance]:
        """
        Asynchronously streams SyncListInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[SyncListInstance]:
        """
        Lists SyncListInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[SyncListInstance]:
        """
        Asynchronously lists SyncListInstance records from the API as a list.
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
    ) -> SyncListPage:
        """
        Retrieve a single page of SyncListInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncListInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SyncListPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> SyncListPage:
        """
        Asynchronously retrieve a single page of SyncListInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncListInstance
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
        return SyncListPage(self._version, response, self._solution)

    def get_page(self, target_url) -> SyncListPage:
        """
        Retrieve a specific page of SyncListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncListInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SyncListPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> SyncListPage:
        """
        Asynchronously retrieve a specific page of SyncListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncListInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SyncListPage(self._version, response, self._solution)

    def get(self, sid) -> SyncListContext:
        """
        Constructs a SyncListContext

        :param sid:
        """
        return SyncListContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid) -> SyncListContext:
        """
        Constructs a SyncListContext

        :param sid:
        """
        return SyncListContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncListList>"
