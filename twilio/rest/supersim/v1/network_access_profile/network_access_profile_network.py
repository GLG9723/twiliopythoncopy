r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
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


class NetworkAccessProfileNetworkInstance(InstanceResource):
    """
    :ivar sid: The unique string that identifies the Network resource.
    :ivar network_access_profile_sid: The unique string that identifies the Network resource's Network Access Profile resource.
    :ivar friendly_name: A human readable identifier of the Network this resource refers to.
    :ivar iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resource.
    :ivar identifiers: Array of objects identifying the [MCC-MNCs](https://en.wikipedia.org/wiki/Mobile_country_code) that are included in the Network resource.
    :ivar url: The absolute URL of the Network resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        network_access_profile_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.network_access_profile_sid: Optional[str] = payload.get(
            "network_access_profile_sid"
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.iso_country: Optional[str] = payload.get("iso_country")
        self.identifiers: Optional[List[Dict[str, object]]] = payload.get("identifiers")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "network_access_profile_sid": network_access_profile_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[NetworkAccessProfileNetworkContext] = None

    @property
    def _proxy(self) -> "NetworkAccessProfileNetworkContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: NetworkAccessProfileNetworkContext for this NetworkAccessProfileNetworkInstance
        """
        if self._context is None:
            self._context = NetworkAccessProfileNetworkContext(
                self._version,
                network_access_profile_sid=self._solution["network_access_profile_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the NetworkAccessProfileNetworkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the NetworkAccessProfileNetworkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "NetworkAccessProfileNetworkInstance":
        """
        Fetch the NetworkAccessProfileNetworkInstance


        :returns: The fetched NetworkAccessProfileNetworkInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "NetworkAccessProfileNetworkInstance":
        """
        Asynchronous coroutine to fetch the NetworkAccessProfileNetworkInstance


        :returns: The fetched NetworkAccessProfileNetworkInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.NetworkAccessProfileNetworkInstance {}>".format(
            context
        )


class NetworkAccessProfileNetworkContext(InstanceContext):

    def __init__(self, version: Version, network_access_profile_sid: str, sid: str):
        """
        Initialize the NetworkAccessProfileNetworkContext

        :param version: Version that contains the resource
        :param network_access_profile_sid: The unique string that identifies the Network Access Profile resource.
        :param sid: The SID of the Network resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "network_access_profile_sid": network_access_profile_sid,
            "sid": sid,
        }
        self._uri = (
            "/NetworkAccessProfiles/{network_access_profile_sid}/Networks/{sid}".format(
                **self._solution
            )
        )

    def delete(self) -> bool:
        """
        Deletes the NetworkAccessProfileNetworkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the NetworkAccessProfileNetworkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> NetworkAccessProfileNetworkInstance:
        """
        Fetch the NetworkAccessProfileNetworkInstance


        :returns: The fetched NetworkAccessProfileNetworkInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return NetworkAccessProfileNetworkInstance(
            self._version,
            payload,
            network_access_profile_sid=self._solution["network_access_profile_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> NetworkAccessProfileNetworkInstance:
        """
        Asynchronous coroutine to fetch the NetworkAccessProfileNetworkInstance


        :returns: The fetched NetworkAccessProfileNetworkInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return NetworkAccessProfileNetworkInstance(
            self._version,
            payload,
            network_access_profile_sid=self._solution["network_access_profile_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.NetworkAccessProfileNetworkContext {}>".format(
            context
        )


class NetworkAccessProfileNetworkPage(Page):

    def get_instance(
        self, payload: Dict[str, Any]
    ) -> NetworkAccessProfileNetworkInstance:
        """
        Build an instance of NetworkAccessProfileNetworkInstance

        :param payload: Payload response from the API
        """
        return NetworkAccessProfileNetworkInstance(
            self._version,
            payload,
            network_access_profile_sid=self._solution["network_access_profile_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.NetworkAccessProfileNetworkPage>"


class NetworkAccessProfileNetworkList(ListResource):

    def __init__(self, version: Version, network_access_profile_sid: str):
        """
        Initialize the NetworkAccessProfileNetworkList

        :param version: Version that contains the resource
        :param network_access_profile_sid: The unique string that identifies the Network Access Profile resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "network_access_profile_sid": network_access_profile_sid,
        }
        self._uri = (
            "/NetworkAccessProfiles/{network_access_profile_sid}/Networks".format(
                **self._solution
            )
        )

    def create(self, network: str) -> NetworkAccessProfileNetworkInstance:
        """
        Create the NetworkAccessProfileNetworkInstance

        :param network: The SID of the Network resource to be added to the Network Access Profile resource.

        :returns: The created NetworkAccessProfileNetworkInstance
        """

        data = values.of(
            {
                "Network": network,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return NetworkAccessProfileNetworkInstance(
            self._version,
            payload,
            network_access_profile_sid=self._solution["network_access_profile_sid"],
        )

    async def create_async(self, network: str) -> NetworkAccessProfileNetworkInstance:
        """
        Asynchronously create the NetworkAccessProfileNetworkInstance

        :param network: The SID of the Network resource to be added to the Network Access Profile resource.

        :returns: The created NetworkAccessProfileNetworkInstance
        """

        data = values.of(
            {
                "Network": network,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return NetworkAccessProfileNetworkInstance(
            self._version,
            payload,
            network_access_profile_sid=self._solution["network_access_profile_sid"],
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[NetworkAccessProfileNetworkInstance]:
        """
        Streams NetworkAccessProfileNetworkInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[NetworkAccessProfileNetworkInstance]:
        """
        Asynchronously streams NetworkAccessProfileNetworkInstance records from the API as a generator stream.
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
    ) -> List[NetworkAccessProfileNetworkInstance]:
        """
        Lists NetworkAccessProfileNetworkInstance records from the API as a list.
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
    ) -> List[NetworkAccessProfileNetworkInstance]:
        """
        Asynchronously lists NetworkAccessProfileNetworkInstance records from the API as a list.
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
    ) -> NetworkAccessProfileNetworkPage:
        """
        Retrieve a single page of NetworkAccessProfileNetworkInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkAccessProfileNetworkInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return NetworkAccessProfileNetworkPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> NetworkAccessProfileNetworkPage:
        """
        Asynchronously retrieve a single page of NetworkAccessProfileNetworkInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkAccessProfileNetworkInstance
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
        return NetworkAccessProfileNetworkPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> NetworkAccessProfileNetworkPage:
        """
        Retrieve a specific page of NetworkAccessProfileNetworkInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of NetworkAccessProfileNetworkInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return NetworkAccessProfileNetworkPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> NetworkAccessProfileNetworkPage:
        """
        Asynchronously retrieve a specific page of NetworkAccessProfileNetworkInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of NetworkAccessProfileNetworkInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return NetworkAccessProfileNetworkPage(self._version, response, self._solution)

    def get(self, sid: str) -> NetworkAccessProfileNetworkContext:
        """
        Constructs a NetworkAccessProfileNetworkContext

        :param sid: The SID of the Network resource to fetch.
        """
        return NetworkAccessProfileNetworkContext(
            self._version,
            network_access_profile_sid=self._solution["network_access_profile_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> NetworkAccessProfileNetworkContext:
        """
        Constructs a NetworkAccessProfileNetworkContext

        :param sid: The SID of the Network resource to fetch.
        """
        return NetworkAccessProfileNetworkContext(
            self._version,
            network_access_profile_sid=self._solution["network_access_profile_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.NetworkAccessProfileNetworkList>"
