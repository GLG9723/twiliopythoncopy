r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.conversations.v1.conversation.message import MessageList
from twilio.rest.conversations.v1.conversation.participant import ParticipantList
from twilio.rest.conversations.v1.conversation.webhook import WebhookList


class ConversationInstance(InstanceResource):
    class State(object):
        INACTIVE = "inactive"
        ACTIVE = "active"
        CLOSED = "closed"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    """
    :ivar account_sid: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation.
    :ivar chat_service_sid: The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
    :ivar messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this conversation belongs to.
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
    :ivar attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \"{}\" will be returned.
    :ivar state: 
    :ivar date_created: The date that this resource was created.
    :ivar date_updated: The date that this resource was last updated.
    :ivar timers: Timer date values representing state update for this conversation.
    :ivar url: An absolute API resource URL for this conversation.
    :ivar links: Contains absolute URLs to access the [participants](https://www.twilio.com/docs/conversations/api/conversation-participant-resource), [messages](https://www.twilio.com/docs/conversations/api/conversation-message-resource) and [webhooks](https://www.twilio.com/docs/conversations/api/conversation-scoped-webhook-resource) of this conversation.
    :ivar bindings: 
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.chat_service_sid: Optional[str] = payload.get("chat_service_sid")
        self.messaging_service_sid: Optional[str] = payload.get("messaging_service_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.attributes: Optional[str] = payload.get("attributes")
        self.state: Optional["ConversationInstance.State"] = payload.get("state")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.timers: Optional[Dict[str, object]] = payload.get("timers")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")
        self.bindings: Optional[Dict[str, object]] = payload.get("bindings")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[ConversationContext] = None

    @property
    def _proxy(self) -> "ConversationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ConversationContext for this ConversationInstance
        """
        if self._context is None:
            self._context = ConversationContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(
        self,
        x_twilio_webhook_enabled: Union[
            "ConversationInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Deletes the ConversationInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    async def delete_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ConversationInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Asynchronous coroutine that deletes the ConversationInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    def fetch(self) -> "ConversationInstance":
        """
        Fetch the ConversationInstance


        :returns: The fetched ConversationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ConversationInstance":
        """
        Asynchronous coroutine to fetch the ConversationInstance


        :returns: The fetched ConversationInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "ConversationInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        messaging_service_sid: Union[str, object] = values.unset,
        state: Union["ConversationInstance.State", object] = values.unset,
        timers_inactive: Union[str, object] = values.unset,
        timers_closed: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> "ConversationInstance":
        """
        Update the ConversationInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated.
        :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this conversation belongs to.
        :param state:
        :param timers_inactive: ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
        :param timers_closed: ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.

        :returns: The updated ConversationInstance
        """
        return self._proxy.update(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            messaging_service_sid=messaging_service_sid,
            state=state,
            timers_inactive=timers_inactive,
            timers_closed=timers_closed,
            unique_name=unique_name,
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ConversationInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        messaging_service_sid: Union[str, object] = values.unset,
        state: Union["ConversationInstance.State", object] = values.unset,
        timers_inactive: Union[str, object] = values.unset,
        timers_closed: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> "ConversationInstance":
        """
        Asynchronous coroutine to update the ConversationInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated.
        :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this conversation belongs to.
        :param state:
        :param timers_inactive: ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
        :param timers_closed: ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.

        :returns: The updated ConversationInstance
        """
        return await self._proxy.update_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
            messaging_service_sid=messaging_service_sid,
            state=state,
            timers_inactive=timers_inactive,
            timers_closed=timers_closed,
            unique_name=unique_name,
        )

    @property
    def messages(self) -> MessageList:
        """
        Access the messages
        """
        return self._proxy.messages

    @property
    def participants(self) -> ParticipantList:
        """
        Access the participants
        """
        return self._proxy.participants

    @property
    def webhooks(self) -> WebhookList:
        """
        Access the webhooks
        """
        return self._proxy.webhooks

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.ConversationInstance {}>".format(context)


class ConversationContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the ConversationContext

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Conversations/{sid}".format(**self._solution)

        self._messages: Optional[MessageList] = None
        self._participants: Optional[ParticipantList] = None
        self._webhooks: Optional[WebhookList] = None

    def delete(
        self,
        x_twilio_webhook_enabled: Union[
            "ConversationInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Deletes the ConversationInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ConversationInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Asynchronous coroutine that deletes the ConversationInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def fetch(self) -> ConversationInstance:
        """
        Fetch the ConversationInstance


        :returns: The fetched ConversationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ConversationInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ConversationInstance:
        """
        Asynchronous coroutine to fetch the ConversationInstance


        :returns: The fetched ConversationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ConversationInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "ConversationInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        messaging_service_sid: Union[str, object] = values.unset,
        state: Union["ConversationInstance.State", object] = values.unset,
        timers_inactive: Union[str, object] = values.unset,
        timers_closed: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> ConversationInstance:
        """
        Update the ConversationInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated.
        :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this conversation belongs to.
        :param state:
        :param timers_inactive: ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
        :param timers_closed: ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.

        :returns: The updated ConversationInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "Attributes": attributes,
                "MessagingServiceSid": messaging_service_sid,
                "State": state,
                "Timers.Inactive": timers_inactive,
                "Timers.Closed": timers_closed,
                "UniqueName": unique_name,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ConversationInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ConversationInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        messaging_service_sid: Union[str, object] = values.unset,
        state: Union["ConversationInstance.State", object] = values.unset,
        timers_inactive: Union[str, object] = values.unset,
        timers_closed: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> ConversationInstance:
        """
        Asynchronous coroutine to update the ConversationInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated.
        :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this conversation belongs to.
        :param state:
        :param timers_inactive: ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
        :param timers_closed: ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.

        :returns: The updated ConversationInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "Attributes": attributes,
                "MessagingServiceSid": messaging_service_sid,
                "State": state,
                "Timers.Inactive": timers_inactive,
                "Timers.Closed": timers_closed,
                "UniqueName": unique_name,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ConversationInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def messages(self) -> MessageList:
        """
        Access the messages
        """
        if self._messages is None:
            self._messages = MessageList(
                self._version,
                self._solution["sid"],
            )
        return self._messages

    @property
    def participants(self) -> ParticipantList:
        """
        Access the participants
        """
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
                self._solution["sid"],
            )
        return self._participants

    @property
    def webhooks(self) -> WebhookList:
        """
        Access the webhooks
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(
                self._version,
                self._solution["sid"],
            )
        return self._webhooks

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.ConversationContext {}>".format(context)


class ConversationPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> ConversationInstance:
        """
        Build an instance of ConversationInstance

        :param payload: Payload response from the API
        """
        return ConversationInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.ConversationPage>"


class ConversationList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ConversationList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Conversations"

    def create(
        self,
        x_twilio_webhook_enabled: Union[
            "ConversationInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        messaging_service_sid: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        state: Union["ConversationInstance.State", object] = values.unset,
        timers_inactive: Union[str, object] = values.unset,
        timers_closed: Union[str, object] = values.unset,
    ) -> ConversationInstance:
        """
        Create the ConversationInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated.
        :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this conversation belongs to.
        :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param state:
        :param timers_inactive: ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
        :param timers_closed: ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.

        :returns: The created ConversationInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "MessagingServiceSid": messaging_service_sid,
                "Attributes": attributes,
                "State": state,
                "Timers.Inactive": timers_inactive,
                "Timers.Closed": timers_closed,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )
        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ConversationInstance(self._version, payload)

    async def create_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ConversationInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        messaging_service_sid: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        state: Union["ConversationInstance.State", object] = values.unset,
        timers_inactive: Union[str, object] = values.unset,
        timers_closed: Union[str, object] = values.unset,
    ) -> ConversationInstance:
        """
        Asynchronously create the ConversationInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
        :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
        :param date_created: The date that this resource was created.
        :param date_updated: The date that this resource was last updated.
        :param messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this conversation belongs to.
        :param attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param state:
        :param timers_inactive: ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
        :param timers_closed: ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.

        :returns: The created ConversationInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "MessagingServiceSid": messaging_service_sid,
                "Attributes": attributes,
                "State": state,
                "Timers.Inactive": timers_inactive,
                "Timers.Closed": timers_closed,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )
        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ConversationInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ConversationInstance]:
        """
        Streams ConversationInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[ConversationInstance]:
        """
        Asynchronously streams ConversationInstance records from the API as a generator stream.
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
    ) -> List[ConversationInstance]:
        """
        Lists ConversationInstance records from the API as a list.
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
    ) -> List[ConversationInstance]:
        """
        Asynchronously lists ConversationInstance records from the API as a list.
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
    ) -> ConversationPage:
        """
        Retrieve a single page of ConversationInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ConversationInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ConversationPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ConversationPage:
        """
        Asynchronously retrieve a single page of ConversationInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ConversationInstance
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
        return ConversationPage(self._version, response)

    def get_page(self, target_url: str) -> ConversationPage:
        """
        Retrieve a specific page of ConversationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ConversationInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ConversationPage(self._version, response)

    async def get_page_async(self, target_url: str) -> ConversationPage:
        """
        Asynchronously retrieve a specific page of ConversationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ConversationInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ConversationPage(self._version, response)

    def get(self, sid: str) -> ConversationContext:
        """
        Constructs a ConversationContext

        :param sid: A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
        """
        return ConversationContext(self._version, sid=sid)

    def __call__(self, sid: str) -> ConversationContext:
        """
        Constructs a ConversationContext

        :param sid: A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
        """
        return ConversationContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.ConversationList>"
