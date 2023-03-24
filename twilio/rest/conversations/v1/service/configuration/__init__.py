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


from typing import Dict, Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.conversations.v1.service.configuration.notification import (
    NotificationList,
)
from twilio.rest.conversations.v1.service.configuration.webhook import WebhookList


class ConfigurationInstance(InstanceResource):
    def __init__(self, version, payload, chat_service_sid: str):
        """
        Initialize the ConfigurationInstance
        """
        super().__init__(version)

        self._properties = {
            "chat_service_sid": payload.get("chat_service_sid"),
            "default_conversation_creator_role_sid": payload.get(
                "default_conversation_creator_role_sid"
            ),
            "default_conversation_role_sid": payload.get(
                "default_conversation_role_sid"
            ),
            "default_chat_service_role_sid": payload.get(
                "default_chat_service_role_sid"
            ),
            "url": payload.get("url"),
            "links": payload.get("links"),
            "reachability_enabled": payload.get("reachability_enabled"),
        }

        self._solution = {
            "chat_service_sid": chat_service_sid,
        }
        self._context: Optional[ConfigurationContext] = None

    @property
    def _proxy(self) -> "ConfigurationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ConfigurationContext for this ConfigurationInstance
        """
        if self._context is None:
            self._context = ConfigurationContext(
                self._version,
                chat_service_sid=self._solution["chat_service_sid"],
            )
        return self._context

    @property
    def chat_service_sid(self) -> str:
        """
        :returns: The unique string that we created to identify the Service configuration resource.
        """
        return self._properties["chat_service_sid"]

    @property
    def default_conversation_creator_role_sid(self) -> str:
        """
        :returns: The conversation-level role assigned to a conversation creator user when they join a new conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        """
        return self._properties["default_conversation_creator_role_sid"]

    @property
    def default_conversation_role_sid(self) -> str:
        """
        :returns: The conversation-level role assigned to users when they are added to a conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        """
        return self._properties["default_conversation_role_sid"]

    @property
    def default_chat_service_role_sid(self) -> str:
        """
        :returns: The service-level role assigned to users when they are added to the service. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        """
        return self._properties["default_chat_service_role_sid"]

    @property
    def url(self) -> str:
        """
        :returns: An absolute API resource URL for this service configuration.
        """
        return self._properties["url"]

    @property
    def links(self) -> Dict[str, object]:
        """
        :returns: Contains an absolute API resource URL to access the push notifications configuration of this service.
        """
        return self._properties["links"]

    @property
    def reachability_enabled(self) -> bool:
        """
        :returns: Whether the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) is enabled for this Conversations Service. The default is `false`.
        """
        return self._properties["reachability_enabled"]

    def fetch(self) -> "ConfigurationInstance":
        """
        Fetch the ConfigurationInstance


        :returns: The fetched ConfigurationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ConfigurationInstance":
        """
        Asynchronous coroutine to fetch the ConfigurationInstance


        :returns: The fetched ConfigurationInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        default_conversation_creator_role_sid=values.unset,
        default_conversation_role_sid=values.unset,
        default_chat_service_role_sid=values.unset,
        reachability_enabled=values.unset,
    ) -> "ConfigurationInstance":
        """
        Update the ConfigurationInstance

        :param str default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when they join a new conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param str default_conversation_role_sid: The conversation-level role assigned to users when they are added to a conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param str default_chat_service_role_sid: The service-level role assigned to users when they are added to the service. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param bool reachability_enabled: Whether the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) is enabled for this Conversations Service. The default is `false`.

        :returns: The updated ConfigurationInstance
        """
        return self._proxy.update(
            default_conversation_creator_role_sid=default_conversation_creator_role_sid,
            default_conversation_role_sid=default_conversation_role_sid,
            default_chat_service_role_sid=default_chat_service_role_sid,
            reachability_enabled=reachability_enabled,
        )

    async def update_async(
        self,
        default_conversation_creator_role_sid=values.unset,
        default_conversation_role_sid=values.unset,
        default_chat_service_role_sid=values.unset,
        reachability_enabled=values.unset,
    ) -> "ConfigurationInstance":
        """
        Asynchronous coroutine to update the ConfigurationInstance

        :param str default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when they join a new conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param str default_conversation_role_sid: The conversation-level role assigned to users when they are added to a conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param str default_chat_service_role_sid: The service-level role assigned to users when they are added to the service. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param bool reachability_enabled: Whether the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) is enabled for this Conversations Service. The default is `false`.

        :returns: The updated ConfigurationInstance
        """
        return await self._proxy.update_async(
            default_conversation_creator_role_sid=default_conversation_creator_role_sid,
            default_conversation_role_sid=default_conversation_role_sid,
            default_chat_service_role_sid=default_chat_service_role_sid,
            reachability_enabled=reachability_enabled,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.ConfigurationInstance {}>".format(context)


class ConfigurationContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the ConfigurationContext

        :param version: Version that contains the resource
        :param chat_service_sid: The SID of the Service configuration resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
        }
        self._uri = "/Services/{chat_service_sid}/Configuration".format(
            **self._solution
        )

    def fetch(self) -> ConfigurationInstance:
        """
        Fetch the ConfigurationInstance


        :returns: The fetched ConfigurationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ConfigurationInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
        )

    async def fetch_async(self) -> ConfigurationInstance:
        """
        Asynchronous coroutine to fetch the ConfigurationInstance


        :returns: The fetched ConfigurationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ConfigurationInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
        )

    def update(
        self,
        default_conversation_creator_role_sid=values.unset,
        default_conversation_role_sid=values.unset,
        default_chat_service_role_sid=values.unset,
        reachability_enabled=values.unset,
    ) -> ConfigurationInstance:
        """
        Update the ConfigurationInstance

        :param str default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when they join a new conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param str default_conversation_role_sid: The conversation-level role assigned to users when they are added to a conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param str default_chat_service_role_sid: The service-level role assigned to users when they are added to the service. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param bool reachability_enabled: Whether the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) is enabled for this Conversations Service. The default is `false`.

        :returns: The updated ConfigurationInstance
        """
        data = values.of(
            {
                "DefaultConversationCreatorRoleSid": default_conversation_creator_role_sid,
                "DefaultConversationRoleSid": default_conversation_role_sid,
                "DefaultChatServiceRoleSid": default_chat_service_role_sid,
                "ReachabilityEnabled": reachability_enabled,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ConfigurationInstance(
            self._version, payload, chat_service_sid=self._solution["chat_service_sid"]
        )

    async def update_async(
        self,
        default_conversation_creator_role_sid=values.unset,
        default_conversation_role_sid=values.unset,
        default_chat_service_role_sid=values.unset,
        reachability_enabled=values.unset,
    ) -> ConfigurationInstance:
        """
        Asynchronous coroutine to update the ConfigurationInstance

        :param str default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when they join a new conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param str default_conversation_role_sid: The conversation-level role assigned to users when they are added to a conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param str default_chat_service_role_sid: The service-level role assigned to users when they are added to the service. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :param bool reachability_enabled: Whether the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) is enabled for this Conversations Service. The default is `false`.

        :returns: The updated ConfigurationInstance
        """
        data = values.of(
            {
                "DefaultConversationCreatorRoleSid": default_conversation_creator_role_sid,
                "DefaultConversationRoleSid": default_conversation_role_sid,
                "DefaultChatServiceRoleSid": default_chat_service_role_sid,
                "ReachabilityEnabled": reachability_enabled,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ConfigurationInstance(
            self._version, payload, chat_service_sid=self._solution["chat_service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.ConfigurationContext {}>".format(context)


class ConfigurationList(ListResource):
    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the ConfigurationList

        :param version: Version that contains the resource
        :param chat_service_sid: The SID of the Service configuration resource to fetch.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
        }

        self._notifications: Optional[NotificationList] = None
        self._webhooks: Optional[WebhookList] = None

    @property
    def notifications(self) -> NotificationList:
        """
        Access the notifications
        """
        if self._notifications is None:
            self._notifications = NotificationList(
                self._version, chat_service_sid=self._solution["chat_service_sid"]
            )
        return self._notifications

    @property
    def webhooks(self) -> WebhookList:
        """
        Access the webhooks
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(
                self._version, chat_service_sid=self._solution["chat_service_sid"]
            )
        return self._webhooks

    def get(self) -> ConfigurationContext:
        """
        Constructs a ConfigurationContext

        """
        return ConfigurationContext(
            self._version, chat_service_sid=self._solution["chat_service_sid"]
        )

    def __call__(self) -> ConfigurationContext:
        """
        Constructs a ConfigurationContext

        """
        return ConfigurationContext(
            self._version, chat_service_sid=self._solution["chat_service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.ConfigurationList>"
