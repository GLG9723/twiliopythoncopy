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


from typing import Dict, Optional
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.flex_api.v1.interaction.interaction_channel import (
    InteractionChannelList,
)


class InteractionInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the InteractionInstance
        """
        super().__init__(version)

        self._sid: Optional[str] = payload.get("sid")
        self._channel: Optional[Dict[str, object]] = payload.get("channel")
        self._routing: Optional[Dict[str, object]] = payload.get("routing")
        self._url: Optional[str] = payload.get("url")
        self._links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self._sid,
        }
        self._context: Optional[InteractionContext] = None

    @property
    def _proxy(self) -> "InteractionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InteractionContext for this InteractionInstance
        """
        if self._context is None:
            self._context = InteractionContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
        """
        return self._sid

    @property
    def channel(self) -> Optional[Dict[str, object]]:
        """
        :returns: A JSON object that defines the Interaction’s communication channel and includes details about the channel. See the [Outbound SMS](https://www.twilio.com/docs/flex/developer/conversations/interactions-api/interactions#agent-initiated-outbound-interactions) and [inbound (API-initiated)](https://www.twilio.com/docs/flex/developer/conversations/interactions-api/interactions#api-initiated-contact) Channel object examples.
        """
        return self._channel

    @property
    def routing(self) -> Optional[Dict[str, object]]:
        """
        :returns: A JSON Object representing the routing rules for the Interaction Channel. See [Outbound SMS Example](https://www.twilio.com/docs/flex/developer/conversations/interactions-api/interactions#agent-initiated-outbound-interactions) for an example Routing object. The Interactions resource uses TaskRouter for all routing functionality.   All attributes in the Routing object on your Interaction request body are added “as is” to the task. For a list of known attributes consumed by the Flex UI and/or Flex Insights, see [Known Task Attributes](https://www.twilio.com/docs/flex/developer/conversations/interactions-api#task-attributes).
        """
        return self._routing

    @property
    def url(self) -> Optional[str]:
        return self._url

    @property
    def links(self) -> Optional[Dict[str, object]]:
        return self._links

    def fetch(self) -> "InteractionInstance":
        """
        Fetch the InteractionInstance


        :returns: The fetched InteractionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "InteractionInstance":
        """
        Asynchronous coroutine to fetch the InteractionInstance


        :returns: The fetched InteractionInstance
        """
        return await self._proxy.fetch_async()

    @property
    def channels(self) -> InteractionChannelList:
        """
        Access the channels
        """
        return self._proxy.channels

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InteractionInstance {}>".format(context)


class InteractionContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the InteractionContext

        :param version: Version that contains the resource
        :param sid: The SID of the Interaction resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Interactions/{sid}".format(**self._solution)

        self._channels: Optional[InteractionChannelList] = None

    def fetch(self) -> InteractionInstance:
        """
        Fetch the InteractionInstance


        :returns: The fetched InteractionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return InteractionInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> InteractionInstance:
        """
        Asynchronous coroutine to fetch the InteractionInstance


        :returns: The fetched InteractionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return InteractionInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    @property
    def channels(self) -> InteractionChannelList:
        """
        Access the channels
        """
        if self._channels is None:
            self._channels = InteractionChannelList(
                self._version,
                self._solution["sid"],
            )
        return self._channels

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InteractionContext {}>".format(context)


class InteractionList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the InteractionList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Interactions"

    def create(self, channel, routing) -> InteractionInstance:
        """
        Create the InteractionInstance

        :param object channel: The Interaction's channel.
        :param object routing: The Interaction's routing logic.

        :returns: The created InteractionInstance
        """
        data = values.of(
            {
                "Channel": serialize.object(channel),
                "Routing": serialize.object(routing),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionInstance(self._version, payload)

    async def create_async(self, channel, routing) -> InteractionInstance:
        """
        Asynchronously create the InteractionInstance

        :param object channel: The Interaction's channel.
        :param object routing: The Interaction's routing logic.

        :returns: The created InteractionInstance
        """
        data = values.of(
            {
                "Channel": serialize.object(channel),
                "Routing": serialize.object(routing),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionInstance(self._version, payload)

    def get(self, sid) -> InteractionContext:
        """
        Constructs a InteractionContext

        :param sid: The SID of the Interaction resource to fetch.
        """
        return InteractionContext(self._version, sid=sid)

    def __call__(self, sid) -> InteractionContext:
        """
        Constructs a InteractionContext

        :param sid: The SID of the Interaction resource to fetch.
        """
        return InteractionContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InteractionList>"
