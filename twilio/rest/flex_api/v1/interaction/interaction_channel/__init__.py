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


from typing import Dict, List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite import (
    InteractionChannelInviteList,
)
from twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant import (
    InteractionChannelParticipantList,
)


class InteractionChannelInstance(InstanceResource):
    class ChannelStatus(object):
        SETUP = "setup"
        ACTIVE = "active"
        FAILED = "failed"
        CLOSED = "closed"

    class Type(object):
        VOICE = "voice"
        SMS = "sms"
        EMAIL = "email"
        WEB = "web"
        WHATSAPP = "whatsapp"
        CHAT = "chat"
        MESSENGER = "messenger"
        GBM = "gbm"

    def __init__(
        self, version, payload, interaction_sid: str, sid: Optional[str] = None
    ):
        """
        Initialize the InteractionChannelInstance
        """
        super().__init__(version)

        self._sid: Optional[str] = payload.get("sid")
        self._interaction_sid: Optional[str] = payload.get("interaction_sid")
        self._type: Optional["InteractionChannelInstance.Type"] = payload.get("type")
        self._status: Optional[
            "InteractionChannelInstance.ChannelStatus"
        ] = payload.get("status")
        self._error_code: Optional[int] = deserialize.integer(payload.get("error_code"))
        self._error_message: Optional[str] = payload.get("error_message")
        self._url: Optional[str] = payload.get("url")
        self._links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "interaction_sid": interaction_sid,
            "sid": sid or self._sid,
        }
        self._context: Optional[InteractionChannelContext] = None

    @property
    def _proxy(self) -> "InteractionChannelContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InteractionChannelContext for this InteractionChannelInstance
        """
        if self._context is None:
            self._context = InteractionChannelContext(
                self._version,
                interaction_sid=self._solution["interaction_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
        """
        return self._sid

    @property
    def interaction_sid(self) -> Optional[str]:
        """
        :returns: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
        """
        return self._interaction_sid

    @property
    def type(self) -> Optional["InteractionChannelInstance.Type"]:
        return self._type

    @property
    def status(self) -> Optional["InteractionChannelInstance.ChannelStatus"]:
        return self._status

    @property
    def error_code(self) -> Optional[int]:
        """
        :returns: The Twilio error code for a failed channel.
        """
        return self._error_code

    @property
    def error_message(self) -> Optional[str]:
        """
        :returns: The error message for a failed channel.
        """
        return self._error_message

    @property
    def url(self) -> Optional[str]:
        return self._url

    @property
    def links(self) -> Optional[Dict[str, object]]:
        return self._links

    def fetch(self) -> "InteractionChannelInstance":
        """
        Fetch the InteractionChannelInstance


        :returns: The fetched InteractionChannelInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "InteractionChannelInstance":
        """
        Asynchronous coroutine to fetch the InteractionChannelInstance


        :returns: The fetched InteractionChannelInstance
        """
        return await self._proxy.fetch_async()

    def update(self, status, routing=values.unset) -> "InteractionChannelInstance":
        """
        Update the InteractionChannelInstance

        :param "InteractionChannelInstance.Status" status:
        :param object routing: Optional. The state of associated tasks. If not specified, all tasks will be set to `wrapping`.

        :returns: The updated InteractionChannelInstance
        """
        return self._proxy.update(
            status=status,
            routing=routing,
        )

    async def update_async(
        self, status, routing=values.unset
    ) -> "InteractionChannelInstance":
        """
        Asynchronous coroutine to update the InteractionChannelInstance

        :param "InteractionChannelInstance.Status" status:
        :param object routing: Optional. The state of associated tasks. If not specified, all tasks will be set to `wrapping`.

        :returns: The updated InteractionChannelInstance
        """
        return await self._proxy.update_async(
            status=status,
            routing=routing,
        )

    @property
    def invites(self) -> InteractionChannelInviteList:
        """
        Access the invites
        """
        return self._proxy.invites

    @property
    def participants(self) -> InteractionChannelParticipantList:
        """
        Access the participants
        """
        return self._proxy.participants

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InteractionChannelInstance {}>".format(context)


class InteractionChannelContext(InstanceContext):
    def __init__(self, version: Version, interaction_sid: str, sid: str):
        """
        Initialize the InteractionChannelContext

        :param version: Version that contains the resource
        :param interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
        :param sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "interaction_sid": interaction_sid,
            "sid": sid,
        }
        self._uri = "/Interactions/{interaction_sid}/Channels/{sid}".format(
            **self._solution
        )

        self._invites: Optional[InteractionChannelInviteList] = None
        self._participants: Optional[InteractionChannelParticipantList] = None

    def fetch(self) -> InteractionChannelInstance:
        """
        Fetch the InteractionChannelInstance


        :returns: The fetched InteractionChannelInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return InteractionChannelInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> InteractionChannelInstance:
        """
        Asynchronous coroutine to fetch the InteractionChannelInstance


        :returns: The fetched InteractionChannelInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return InteractionChannelInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            sid=self._solution["sid"],
        )

    def update(self, status, routing=values.unset) -> InteractionChannelInstance:
        """
        Update the InteractionChannelInstance

        :param "InteractionChannelInstance.Status" status:
        :param object routing: Optional. The state of associated tasks. If not specified, all tasks will be set to `wrapping`.

        :returns: The updated InteractionChannelInstance
        """
        data = values.of(
            {
                "Status": status,
                "Routing": serialize.object(routing),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionChannelInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, status, routing=values.unset
    ) -> InteractionChannelInstance:
        """
        Asynchronous coroutine to update the InteractionChannelInstance

        :param "InteractionChannelInstance.Status" status:
        :param object routing: Optional. The state of associated tasks. If not specified, all tasks will be set to `wrapping`.

        :returns: The updated InteractionChannelInstance
        """
        data = values.of(
            {
                "Status": status,
                "Routing": serialize.object(routing),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionChannelInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            sid=self._solution["sid"],
        )

    @property
    def invites(self) -> InteractionChannelInviteList:
        """
        Access the invites
        """
        if self._invites is None:
            self._invites = InteractionChannelInviteList(
                self._version,
                self._solution["interaction_sid"],
                self._solution["sid"],
            )
        return self._invites

    @property
    def participants(self) -> InteractionChannelParticipantList:
        """
        Access the participants
        """
        if self._participants is None:
            self._participants = InteractionChannelParticipantList(
                self._version,
                self._solution["interaction_sid"],
                self._solution["sid"],
            )
        return self._participants

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InteractionChannelContext {}>".format(context)


class InteractionChannelPage(Page):
    def get_instance(self, payload) -> InteractionChannelInstance:
        """
        Build an instance of InteractionChannelInstance

        :param dict payload: Payload response from the API
        """
        return InteractionChannelInstance(
            self._version, payload, interaction_sid=self._solution["interaction_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InteractionChannelPage>"


class InteractionChannelList(ListResource):
    def __init__(self, version: Version, interaction_sid: str):
        """
        Initialize the InteractionChannelList

        :param version: Version that contains the resource
        :param interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "interaction_sid": interaction_sid,
        }
        self._uri = "/Interactions/{interaction_sid}/Channels".format(**self._solution)

    def stream(self, limit=None, page_size=None) -> List[InteractionChannelInstance]:
        """
        Streams InteractionChannelInstance records from the API as a generator stream.
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

    async def stream_async(
        self, limit=None, page_size=None
    ) -> List[InteractionChannelInstance]:
        """
        Asynchronously streams InteractionChannelInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[InteractionChannelInstance]:
        """
        Lists InteractionChannelInstance records from the API as a list.
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

    async def list_async(
        self, limit=None, page_size=None
    ) -> List[InteractionChannelInstance]:
        """
        Asynchronously lists InteractionChannelInstance records from the API as a list.
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
    ) -> InteractionChannelPage:
        """
        Retrieve a single page of InteractionChannelInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionChannelInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InteractionChannelPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> InteractionChannelPage:
        """
        Asynchronously retrieve a single page of InteractionChannelInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionChannelInstance
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
        return InteractionChannelPage(self._version, response, self._solution)

    def get_page(self, target_url) -> InteractionChannelPage:
        """
        Retrieve a specific page of InteractionChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InteractionChannelInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InteractionChannelPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> InteractionChannelPage:
        """
        Asynchronously retrieve a specific page of InteractionChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InteractionChannelInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InteractionChannelPage(self._version, response, self._solution)

    def get(self, sid) -> InteractionChannelContext:
        """
        Constructs a InteractionChannelContext

        :param sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
        """
        return InteractionChannelContext(
            self._version, interaction_sid=self._solution["interaction_sid"], sid=sid
        )

    def __call__(self, sid) -> InteractionChannelContext:
        """
        Constructs a InteractionChannelContext

        :param sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
        """
        return InteractionChannelContext(
            self._version, interaction_sid=self._solution["interaction_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InteractionChannelList>"
