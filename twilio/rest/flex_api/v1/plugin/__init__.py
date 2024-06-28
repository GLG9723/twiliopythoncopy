r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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
from twilio.rest.flex_api.v1.plugin.plugin_versions import PluginVersionsList


class PluginInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the Flex Plugin resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Plugin resource and owns this resource.
    :ivar unique_name: The name that uniquely identifies this Flex Plugin resource.
    :ivar friendly_name: The friendly name this Flex Plugin resource.
    :ivar description: A descriptive string that you create to describe the plugin resource. It can be up to 500 characters long
    :ivar archived: Whether the Flex Plugin is archived. The default value is false.
    :ivar date_created: The date and time in GMT-7 when the Flex Plugin was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT-7 when the Flex Plugin was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Flex Plugin resource.
    :ivar links:
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.description: Optional[str] = payload.get("description")
        self.archived: Optional[bool] = payload.get("archived")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[PluginContext] = None

    @property
    def _proxy(self) -> "PluginContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PluginContext for this PluginInstance
        """
        if self._context is None:
            self._context = PluginContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(
        self, flex_metadata: Union[str, object] = values.unset
    ) -> "PluginInstance":
        """
        Fetch the PluginInstance

        :param flex_metadata: The Flex-Metadata HTTP request header

        :returns: The fetched PluginInstance
        """
        return self._proxy.fetch(
            flex_metadata=flex_metadata,
        )

    async def fetch_async(
        self, flex_metadata: Union[str, object] = values.unset
    ) -> "PluginInstance":
        """
        Asynchronous coroutine to fetch the PluginInstance

        :param flex_metadata: The Flex-Metadata HTTP request header

        :returns: The fetched PluginInstance
        """
        return await self._proxy.fetch_async(
            flex_metadata=flex_metadata,
        )

    def update(
        self,
        flex_metadata: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
    ) -> "PluginInstance":
        """
        Update the PluginInstance

        :param flex_metadata: The Flex-Metadata HTTP request header
        :param friendly_name: The Flex Plugin's friendly name.
        :param description: A descriptive string that you update to describe the plugin resource. It can be up to 500 characters long

        :returns: The updated PluginInstance
        """
        return self._proxy.update(
            flex_metadata=flex_metadata,
            friendly_name=friendly_name,
            description=description,
        )

    async def update_async(
        self,
        flex_metadata: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
    ) -> "PluginInstance":
        """
        Asynchronous coroutine to update the PluginInstance

        :param flex_metadata: The Flex-Metadata HTTP request header
        :param friendly_name: The Flex Plugin's friendly name.
        :param description: A descriptive string that you update to describe the plugin resource. It can be up to 500 characters long

        :returns: The updated PluginInstance
        """
        return await self._proxy.update_async(
            flex_metadata=flex_metadata,
            friendly_name=friendly_name,
            description=description,
        )

    @property
    def plugin_versions(self) -> PluginVersionsList:
        """
        Access the plugin_versions
        """
        return self._proxy.plugin_versions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.FlexApi.V1.PluginInstance {context}>"


class PluginContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the PluginContext

        :param version: Version that contains the resource
        :param sid: The SID of the Flex Plugin resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/PluginService/Plugins/{sid}".format(**self._solution)

        self._plugin_versions: Optional[PluginVersionsList] = None

    def fetch(self, flex_metadata: Union[str, object] = values.unset) -> PluginInstance:
        """
        Fetch the PluginInstance

        :param flex_metadata: The Flex-Metadata HTTP request header

        :returns: The fetched PluginInstance
        """

        data = values.of(
            {
                "Flex-Metadata": flex_metadata,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return PluginInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(
        self, flex_metadata: Union[str, object] = values.unset
    ) -> PluginInstance:
        """
        Asynchronous coroutine to fetch the PluginInstance

        :param flex_metadata: The Flex-Metadata HTTP request header

        :returns: The fetched PluginInstance
        """

        data = values.of(
            {
                "Flex-Metadata": flex_metadata,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return PluginInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        flex_metadata: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
    ) -> PluginInstance:
        """
        Update the PluginInstance

        :param flex_metadata: The Flex-Metadata HTTP request header
        :param friendly_name: The Flex Plugin's friendly name.
        :param description: A descriptive string that you update to describe the plugin resource. It can be up to 500 characters long

        :returns: The updated PluginInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Description": description,
            }
        )
        headers = values.of(
            {
                "Flex-Metadata": flex_metadata,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return PluginInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        flex_metadata: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
    ) -> PluginInstance:
        """
        Asynchronous coroutine to update the PluginInstance

        :param flex_metadata: The Flex-Metadata HTTP request header
        :param friendly_name: The Flex Plugin's friendly name.
        :param description: A descriptive string that you update to describe the plugin resource. It can be up to 500 characters long

        :returns: The updated PluginInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Description": description,
            }
        )
        headers = values.of(
            {
                "Flex-Metadata": flex_metadata,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return PluginInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def plugin_versions(self) -> PluginVersionsList:
        """
        Access the plugin_versions
        """
        if self._plugin_versions is None:
            self._plugin_versions = PluginVersionsList(
                self._version,
                self._solution["sid"],
            )
        return self._plugin_versions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.FlexApi.V1.PluginContext {context}>"


class PluginPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> PluginInstance:
        """
        Build an instance of PluginInstance

        :param payload: Payload response from the API
        """
        return PluginInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.PluginPage>"


class PluginList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the PluginList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/PluginService/Plugins"

    def create(
        self,
        unique_name: str,
        flex_metadata: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
    ) -> PluginInstance:
        """
        Create the PluginInstance

        :param unique_name: The Flex Plugin's unique name.
        :param flex_metadata: The Flex-Metadata HTTP request header
        :param friendly_name: The Flex Plugin's friendly name.
        :param description: A descriptive string that you create to describe the plugin resource. It can be up to 500 characters long

        :returns: The created PluginInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "Description": description,
            }
        )
        headers = values.of(
            {
                "Flex-Metadata": flex_metadata,
                "Content-Type": "application/x-www-form-urlencoded",
            }
        )

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return PluginInstance(self._version, payload)

    async def create_async(
        self,
        unique_name: str,
        flex_metadata: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
    ) -> PluginInstance:
        """
        Asynchronously create the PluginInstance

        :param unique_name: The Flex Plugin's unique name.
        :param flex_metadata: The Flex-Metadata HTTP request header
        :param friendly_name: The Flex Plugin's friendly name.
        :param description: A descriptive string that you create to describe the plugin resource. It can be up to 500 characters long

        :returns: The created PluginInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "Description": description,
            }
        )
        headers = values.of(
            {
                "Flex-Metadata": flex_metadata,
                "Content-Type": "application/x-www-form-urlencoded",
            }
        )

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return PluginInstance(self._version, payload)

    def stream(
        self,
        flex_metadata: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[PluginInstance]:
        """
        Streams PluginInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str flex_metadata: The Flex-Metadata HTTP request header
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(flex_metadata=flex_metadata, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        flex_metadata: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[PluginInstance]:
        """
        Asynchronously streams PluginInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str flex_metadata: The Flex-Metadata HTTP request header
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            flex_metadata=flex_metadata, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        flex_metadata: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[PluginInstance]:
        """
        Lists PluginInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str flex_metadata: The Flex-Metadata HTTP request header
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
                flex_metadata=flex_metadata,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        flex_metadata: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[PluginInstance]:
        """
        Asynchronously lists PluginInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str flex_metadata: The Flex-Metadata HTTP request header
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
                flex_metadata=flex_metadata,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        flex_metadata: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> PluginPage:
        """
        Retrieve a single page of PluginInstance records from the API.
        Request is executed immediately

        :param flex_metadata: The Flex-Metadata HTTP request header
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of PluginInstance
        """
        data = values.of(
            {
                "Flex-Metadata": flex_metadata,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return PluginPage(self._version, response)

    async def page_async(
        self,
        flex_metadata: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> PluginPage:
        """
        Asynchronously retrieve a single page of PluginInstance records from the API.
        Request is executed immediately

        :param flex_metadata: The Flex-Metadata HTTP request header
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of PluginInstance
        """
        data = values.of(
            {
                "Flex-Metadata": flex_metadata,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return PluginPage(self._version, response)

    def get_page(self, target_url: str) -> PluginPage:
        """
        Retrieve a specific page of PluginInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of PluginInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return PluginPage(self._version, response)

    async def get_page_async(self, target_url: str) -> PluginPage:
        """
        Asynchronously retrieve a specific page of PluginInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of PluginInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return PluginPage(self._version, response)

    def get(self, sid: str) -> PluginContext:
        """
        Constructs a PluginContext

        :param sid: The SID of the Flex Plugin resource to update.
        """
        return PluginContext(self._version, sid=sid)

    def __call__(self, sid: str) -> PluginContext:
        """
        Constructs a PluginContext

        :param sid: The SID of the Flex Plugin resource to update.
        """
        return PluginContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.PluginList>"
