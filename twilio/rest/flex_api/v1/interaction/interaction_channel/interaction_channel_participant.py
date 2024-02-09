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

from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InteractionChannelParticipantInstance(InstanceResource):
    class Status(object):
        CLOSED = "closed"
        WRAPUP = "wrapup"

    class Type(object):
        SUPERVISOR = "supervisor"
        CUSTOMER = "customer"
        EXTERNAL = "external"
        AGENT = "agent"
        UNKNOWN = "unknown"

    """
    :ivar sid: The unique string created by Twilio to identify an Interaction Channel Participant resource.
    :ivar type: 
    :ivar interaction_sid: The Interaction Sid for this channel.
    :ivar channel_sid: The Channel Sid for this Participant.
    :ivar url: 
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        interaction_sid: str,
        channel_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.type: Optional["InteractionChannelParticipantInstance.Type"] = payload.get(
            "type"
        )
        self.interaction_sid: Optional[str] = payload.get("interaction_sid")
        self.channel_sid: Optional[str] = payload.get("channel_sid")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "interaction_sid": interaction_sid,
            "channel_sid": channel_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[InteractionChannelParticipantContext] = None

    @property
    def _proxy(self) -> "InteractionChannelParticipantContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InteractionChannelParticipantContext for this InteractionChannelParticipantInstance
        """
        if self._context is None:
            self._context = InteractionChannelParticipantContext(
                self._version,
                interaction_sid=self._solution["interaction_sid"],
                channel_sid=self._solution["channel_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def update(
        self, status: "InteractionChannelParticipantInstance.Status"
    ) -> "InteractionChannelParticipantInstance":
        """
        Update the InteractionChannelParticipantInstance

        :param status:

        :returns: The updated InteractionChannelParticipantInstance
        """
        return self._proxy.update(
            status=status,
        )

    async def update_async(
        self, status: "InteractionChannelParticipantInstance.Status"
    ) -> "InteractionChannelParticipantInstance":
        """
        Asynchronous coroutine to update the InteractionChannelParticipantInstance

        :param status:

        :returns: The updated InteractionChannelParticipantInstance
        """
        return await self._proxy.update_async(
            status=status,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InteractionChannelParticipantInstance {}>".format(
            context
        )


class InteractionChannelParticipantContext(InstanceContext):
    def __init__(
        self, version: Version, interaction_sid: str, channel_sid: str, sid: str
    ):
        """
        Initialize the InteractionChannelParticipantContext

        :param version: Version that contains the resource
        :param interaction_sid: The Interaction Sid for this channel.
        :param channel_sid: The Channel Sid for this Participant.
        :param sid: The unique string created by Twilio to identify an Interaction Channel resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "interaction_sid": interaction_sid,
            "channel_sid": channel_sid,
            "sid": sid,
        }
        self._uri = "/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants/{sid}".format(
            **self._solution
        )

    def update(
        self, status: "InteractionChannelParticipantInstance.Status"
    ) -> InteractionChannelParticipantInstance:
        """
        Update the InteractionChannelParticipantInstance

        :param status:

        :returns: The updated InteractionChannelParticipantInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionChannelParticipantInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, status: "InteractionChannelParticipantInstance.Status"
    ) -> InteractionChannelParticipantInstance:
        """
        Asynchronous coroutine to update the InteractionChannelParticipantInstance

        :param status:

        :returns: The updated InteractionChannelParticipantInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionChannelParticipantInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InteractionChannelParticipantContext {}>".format(
            context
        )


class InteractionChannelParticipantPage(Page):
    def get_instance(
        self, payload: Dict[str, Any]
    ) -> InteractionChannelParticipantInstance:
        """
        Build an instance of InteractionChannelParticipantInstance

        :param payload: Payload response from the API
        """
        return InteractionChannelParticipantInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InteractionChannelParticipantPage>"


class InteractionChannelParticipantList(ListResource):
    def __init__(self, version: Version, interaction_sid: str, channel_sid: str):
        """
        Initialize the InteractionChannelParticipantList

        :param version: Version that contains the resource
        :param interaction_sid: The Interaction Sid for this channel.
        :param channel_sid: The Channel Sid for this Participant.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "interaction_sid": interaction_sid,
            "channel_sid": channel_sid,
        }
        self._uri = "/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants".format(
            **self._solution
        )

    def create(
        self,
        type: "InteractionChannelParticipantInstance.Type",
        media_properties: object,
    ) -> InteractionChannelParticipantInstance:
        """
        Create the InteractionChannelParticipantInstance

        :param type:
        :param media_properties: JSON representing the Media Properties for the new Participant.

        :returns: The created InteractionChannelParticipantInstance
        """
        data = values.of(
            {
                "Type": type,
                "MediaProperties": serialize.object(media_properties),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionChannelParticipantInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    async def create_async(
        self,
        type: "InteractionChannelParticipantInstance.Type",
        media_properties: object,
    ) -> InteractionChannelParticipantInstance:
        """
        Asynchronously create the InteractionChannelParticipantInstance

        :param type:
        :param media_properties: JSON representing the Media Properties for the new Participant.

        :returns: The created InteractionChannelParticipantInstance
        """
        data = values.of(
            {
                "Type": type,
                "MediaProperties": serialize.object(media_properties),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionChannelParticipantInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[InteractionChannelParticipantInstance]:
        """
        Streams InteractionChannelParticipantInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[InteractionChannelParticipantInstance]:
        """
        Asynchronously streams InteractionChannelParticipantInstance records from the API as a generator stream.
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
    ) -> List[InteractionChannelParticipantInstance]:
        """
        Lists InteractionChannelParticipantInstance records from the API as a list.
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
    ) -> List[InteractionChannelParticipantInstance]:
        """
        Asynchronously lists InteractionChannelParticipantInstance records from the API as a list.
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
    ) -> InteractionChannelParticipantPage:
        """
        Retrieve a single page of InteractionChannelParticipantInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionChannelParticipantInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InteractionChannelParticipantPage(
            self._version, response, self._solution
        )

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InteractionChannelParticipantPage:
        """
        Asynchronously retrieve a single page of InteractionChannelParticipantInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionChannelParticipantInstance
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
        return InteractionChannelParticipantPage(
            self._version, response, self._solution
        )

    def get_page(self, target_url: str) -> InteractionChannelParticipantPage:
        """
        Retrieve a specific page of InteractionChannelParticipantInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InteractionChannelParticipantInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InteractionChannelParticipantPage(
            self._version, response, self._solution
        )

    async def get_page_async(
        self, target_url: str
    ) -> InteractionChannelParticipantPage:
        """
        Asynchronously retrieve a specific page of InteractionChannelParticipantInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InteractionChannelParticipantInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InteractionChannelParticipantPage(
            self._version, response, self._solution
        )

    def get(self, sid: str) -> InteractionChannelParticipantContext:
        """
        Constructs a InteractionChannelParticipantContext

        :param sid: The unique string created by Twilio to identify an Interaction Channel resource.
        """
        return InteractionChannelParticipantContext(
            self._version,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> InteractionChannelParticipantContext:
        """
        Constructs a InteractionChannelParticipantContext

        :param sid: The unique string created by Twilio to identify an Interaction Channel resource.
        """
        return InteractionChannelParticipantContext(
            self._version,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InteractionChannelParticipantList>"
