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
from typing import Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.conversations.v1.service.user.user_conversation import (
    UserConversationList,
)


class UserInstance(InstanceResource):
    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(
        self, version, payload, chat_service_sid: str, sid: Optional[str] = None
    ):
        """
        Initialize the UserInstance
        """
        super().__init__(version)

        self._sid: Optional[str] = payload.get("sid")
        self._account_sid: Optional[str] = payload.get("account_sid")
        self._chat_service_sid: Optional[str] = payload.get("chat_service_sid")
        self._role_sid: Optional[str] = payload.get("role_sid")
        self._identity: Optional[str] = payload.get("identity")
        self._friendly_name: Optional[str] = payload.get("friendly_name")
        self._attributes: Optional[str] = payload.get("attributes")
        self._is_online: Optional[bool] = payload.get("is_online")
        self._is_notifiable: Optional[bool] = payload.get("is_notifiable")
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self._url: Optional[str] = payload.get("url")
        self._links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "chat_service_sid": chat_service_sid,
            "sid": sid or self._sid,
        }
        self._context: Optional[UserContext] = None

    @property
    def _proxy(self) -> "UserContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserContext for this UserInstance
        """
        if self._context is None:
            self._context = UserContext(
                self._version,
                chat_service_sid=self._solution["chat_service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that we created to identify the User resource.
        """
        return self._sid

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the User resource.
        """
        return self._account_sid

    @property
    def chat_service_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with.
        """
        return self._chat_service_sid

    @property
    def role_sid(self) -> Optional[str]:
        """
        :returns: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) assigned to the user.
        """
        return self._role_sid

    @property
    def identity(self) -> Optional[str]:
        """
        :returns: The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
        """
        return self._identity

    @property
    def friendly_name(self) -> Optional[str]:
        """
        :returns: The string that you assigned to describe the resource.
        """
        return self._friendly_name

    @property
    def attributes(self) -> Optional[str]:
        """
        :returns: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        """
        return self._attributes

    @property
    def is_online(self) -> Optional[bool]:
        """
        :returns: Whether the User is actively connected to this Conversations Service and online. This value is only returned by Fetch actions that return a single resource and `null` is always returned by a Read action. This value is `null` if the Service's `reachability_enabled` is `false`, if the User has never been online for this Conversations Service, even if the Service's `reachability_enabled` is `true`.
        """
        return self._is_online

    @property
    def is_notifiable(self) -> Optional[bool]:
        """
        :returns: Whether the User has a potentially valid Push Notification registration (APN or GCM) for this Conversations Service. If at least one registration exists, `true`; otherwise `false`. This value is only returned by Fetch actions that return a single resource and `null` is always returned by a Read action. This value is `null` if the Service's `reachability_enabled` is `false`, and if the User has never had a notification registration, even if the Service's `reachability_enabled` is `true`.
        """
        return self._is_notifiable

    @property
    def date_created(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        """
        return self._date_created

    @property
    def date_updated(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        """
        return self._date_updated

    @property
    def url(self) -> Optional[str]:
        """
        :returns: An absolute API resource URL for this user.
        """
        return self._url

    @property
    def links(self) -> Optional[Dict[str, object]]:
        return self._links

    def delete(self, x_twilio_webhook_enabled=values.unset) -> bool:
        """
        Deletes the UserInstance

        :param "UserInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    async def delete_async(self, x_twilio_webhook_enabled=values.unset) -> bool:
        """
        Asynchronous coroutine that deletes the UserInstance

        :param "UserInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    def fetch(self) -> "UserInstance":
        """
        Fetch the UserInstance


        :returns: The fetched UserInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "UserInstance":
        """
        Asynchronous coroutine to fetch the UserInstance


        :returns: The fetched UserInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        x_twilio_webhook_enabled=values.unset,
        friendly_name=values.unset,
        attributes=values.unset,
        role_sid=values.unset,
    ) -> "UserInstance":
        """
        Update the UserInstance

        :param "UserInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param str role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The updated UserInstance
        """
        return self._proxy.update(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            attributes=attributes,
            role_sid=role_sid,
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled=values.unset,
        friendly_name=values.unset,
        attributes=values.unset,
        role_sid=values.unset,
    ) -> "UserInstance":
        """
        Asynchronous coroutine to update the UserInstance

        :param "UserInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param str role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The updated UserInstance
        """
        return await self._proxy.update_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            attributes=attributes,
            role_sid=role_sid,
        )

    @property
    def user_conversations(self) -> UserConversationList:
        """
        Access the user_conversations
        """
        return self._proxy.user_conversations

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.UserInstance {}>".format(context)


class UserContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str, sid: str):
        """
        Initialize the UserContext

        :param version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with.
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{chat_service_sid}/Users/{sid}".format(**self._solution)

        self._user_conversations: Optional[UserConversationList] = None

    def delete(self, x_twilio_webhook_enabled=values.unset) -> bool:
        """
        Deletes the UserInstance

        :param &quot;UserInstance.WebhookEnabledType&quot; x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(self, x_twilio_webhook_enabled=values.unset) -> bool:
        """
        Asynchronous coroutine that deletes the UserInstance

        :param &quot;UserInstance.WebhookEnabledType&quot; x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

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

    def fetch(self) -> UserInstance:
        """
        Fetch the UserInstance


        :returns: The fetched UserInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UserInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> UserInstance:
        """
        Asynchronous coroutine to fetch the UserInstance


        :returns: The fetched UserInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UserInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        x_twilio_webhook_enabled=values.unset,
        friendly_name=values.unset,
        attributes=values.unset,
        role_sid=values.unset,
    ) -> UserInstance:
        """
        Update the UserInstance

        :param "UserInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param str role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The updated UserInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Attributes": attributes,
                "RoleSid": role_sid,
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

        return UserInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled=values.unset,
        friendly_name=values.unset,
        attributes=values.unset,
        role_sid=values.unset,
    ) -> UserInstance:
        """
        Asynchronous coroutine to update the UserInstance

        :param "UserInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param str role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The updated UserInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Attributes": attributes,
                "RoleSid": role_sid,
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

        return UserInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def user_conversations(self) -> UserConversationList:
        """
        Access the user_conversations
        """
        if self._user_conversations is None:
            self._user_conversations = UserConversationList(
                self._version,
                self._solution["chat_service_sid"],
                self._solution["sid"],
            )
        return self._user_conversations

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.UserContext {}>".format(context)


class UserPage(Page):
    def get_instance(self, payload) -> UserInstance:
        """
        Build an instance of UserInstance

        :param dict payload: Payload response from the API
        """
        return UserInstance(
            self._version, payload, chat_service_sid=self._solution["chat_service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.UserPage>"


class UserList(ListResource):
    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the UserList

        :param version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to read the User resources from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
        }
        self._uri = "/Services/{chat_service_sid}/Users".format(**self._solution)

    def create(
        self,
        identity,
        x_twilio_webhook_enabled=values.unset,
        friendly_name=values.unset,
        attributes=values.unset,
        role_sid=values.unset,
    ) -> UserInstance:
        """
        Create the UserInstance

        :param str identity: The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
        :param &quot;UserInstance.WebhookEnabledType&quot; x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param str role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The created UserInstance
        """
        data = values.of(
            {
                "Identity": identity,
                "FriendlyName": friendly_name,
                "Attributes": attributes,
                "RoleSid": role_sid,
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

        return UserInstance(
            self._version, payload, chat_service_sid=self._solution["chat_service_sid"]
        )

    async def create_async(
        self,
        identity,
        x_twilio_webhook_enabled=values.unset,
        friendly_name=values.unset,
        attributes=values.unset,
        role_sid=values.unset,
    ) -> UserInstance:
        """
        Asynchronously create the UserInstance

        :param str identity: The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
        :param &quot;UserInstance.WebhookEnabledType&quot; x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param str role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The created UserInstance
        """
        data = values.of(
            {
                "Identity": identity,
                "FriendlyName": friendly_name,
                "Attributes": attributes,
                "RoleSid": role_sid,
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

        return UserInstance(
            self._version, payload, chat_service_sid=self._solution["chat_service_sid"]
        )

    def stream(self, limit=None, page_size=None) -> List[UserInstance]:
        """
        Streams UserInstance records from the API as a generator stream.
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

    async def stream_async(self, limit=None, page_size=None) -> List[UserInstance]:
        """
        Asynchronously streams UserInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[UserInstance]:
        """
        Lists UserInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[UserInstance]:
        """
        Asynchronously lists UserInstance records from the API as a list.
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
    ) -> UserPage:
        """
        Retrieve a single page of UserInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UserPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> UserPage:
        """
        Asynchronously retrieve a single page of UserInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
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
        return UserPage(self._version, response, self._solution)

    def get_page(self, target_url) -> UserPage:
        """
        Retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UserPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> UserPage:
        """
        Asynchronously retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UserPage(self._version, response, self._solution)

    def get(self, sid) -> UserContext:
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        return UserContext(
            self._version, chat_service_sid=self._solution["chat_service_sid"], sid=sid
        )

    def __call__(self, sid) -> UserContext:
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        return UserContext(
            self._version, chat_service_sid=self._solution["chat_service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.UserList>"
