r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
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


class IpAccessControlListInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlList resource.
    :ivar sid: The unique string that we created to identify the IpAccessControlList resource.
    :ivar trunk_sid: The SID of the Trunk the resource is associated with.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        trunk_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.trunk_sid: Optional[str] = payload.get("trunk_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "trunk_sid": trunk_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[IpAccessControlListContext] = None

    @property
    def _proxy(self) -> "IpAccessControlListContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: IpAccessControlListContext for this IpAccessControlListInstance
        """
        if self._context is None:
            self._context = IpAccessControlListContext(
                self._version,
                trunk_sid=self._solution["trunk_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the IpAccessControlListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the IpAccessControlListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "IpAccessControlListInstance":
        """
        Fetch the IpAccessControlListInstance


        :returns: The fetched IpAccessControlListInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "IpAccessControlListInstance":
        """
        Asynchronous coroutine to fetch the IpAccessControlListInstance


        :returns: The fetched IpAccessControlListInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Trunking.V1.IpAccessControlListInstance {context}>"


class IpAccessControlListContext(InstanceContext):

    def __init__(self, version: Version, trunk_sid: str, sid: str):
        """
        Initialize the IpAccessControlListContext

        :param version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to fetch the IP Access Control List.
        :param sid: The unique string that we created to identify the IpAccessControlList resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
            "sid": sid,
        }
        self._uri = "/Trunks/{trunk_sid}/IpAccessControlLists/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the IpAccessControlListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the IpAccessControlListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> IpAccessControlListInstance:
        """
        Fetch the IpAccessControlListInstance


        :returns: The fetched IpAccessControlListInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return IpAccessControlListInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> IpAccessControlListInstance:
        """
        Asynchronous coroutine to fetch the IpAccessControlListInstance


        :returns: The fetched IpAccessControlListInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return IpAccessControlListInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Trunking.V1.IpAccessControlListContext {context}>"


class IpAccessControlListPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> IpAccessControlListInstance:
        """
        Build an instance of IpAccessControlListInstance

        :param payload: Payload response from the API
        """
        return IpAccessControlListInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.IpAccessControlListPage>"


class IpAccessControlListList(ListResource):

    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the IpAccessControlListList

        :param version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to read the IP Access Control Lists.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
        }
        self._uri = "/Trunks/{trunk_sid}/IpAccessControlLists".format(**self._solution)

    def create(self, ip_access_control_list_sid: str) -> IpAccessControlListInstance:
        """
        Create the IpAccessControlListInstance

        :param ip_access_control_list_sid: The SID of the [IP Access Control List](https://www.twilio.com/docs/voice/sip/api/sip-ipaccesscontrollist-resource) that you want to associate with the trunk.

        :returns: The created IpAccessControlListInstance
        """

        data = values.of(
            {
                "IpAccessControlListSid": ip_access_control_list_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return IpAccessControlListInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    async def create_async(
        self, ip_access_control_list_sid: str
    ) -> IpAccessControlListInstance:
        """
        Asynchronously create the IpAccessControlListInstance

        :param ip_access_control_list_sid: The SID of the [IP Access Control List](https://www.twilio.com/docs/voice/sip/api/sip-ipaccesscontrollist-resource) that you want to associate with the trunk.

        :returns: The created IpAccessControlListInstance
        """

        data = values.of(
            {
                "IpAccessControlListSid": ip_access_control_list_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return IpAccessControlListInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[IpAccessControlListInstance]:
        """
        Streams IpAccessControlListInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[IpAccessControlListInstance]:
        """
        Asynchronously streams IpAccessControlListInstance records from the API as a generator stream.
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
    ) -> List[IpAccessControlListInstance]:
        """
        Lists IpAccessControlListInstance records from the API as a list.
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
    ) -> List[IpAccessControlListInstance]:
        """
        Asynchronously lists IpAccessControlListInstance records from the API as a list.
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
    ) -> IpAccessControlListPage:
        """
        Retrieve a single page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of IpAccessControlListInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return IpAccessControlListPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> IpAccessControlListPage:
        """
        Asynchronously retrieve a single page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of IpAccessControlListInstance
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
        return IpAccessControlListPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> IpAccessControlListPage:
        """
        Retrieve a specific page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of IpAccessControlListInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return IpAccessControlListPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> IpAccessControlListPage:
        """
        Asynchronously retrieve a specific page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of IpAccessControlListInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return IpAccessControlListPage(self._version, response, self._solution)

    def get(self, sid: str) -> IpAccessControlListContext:
        """
        Constructs a IpAccessControlListContext

        :param sid: The unique string that we created to identify the IpAccessControlList resource to fetch.
        """
        return IpAccessControlListContext(
            self._version, trunk_sid=self._solution["trunk_sid"], sid=sid
        )

    def __call__(self, sid: str) -> IpAccessControlListContext:
        """
        Constructs a IpAccessControlListContext

        :param sid: The unique string that we created to identify the IpAccessControlList resource to fetch.
        """
        return IpAccessControlListContext(
            self._version, trunk_sid=self._solution["trunk_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.IpAccessControlListList>"
