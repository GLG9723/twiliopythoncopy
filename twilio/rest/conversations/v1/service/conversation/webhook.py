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
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class WebhookInstance(InstanceResource):
    def __init__(
        self,
        version,
        payload,
        chat_service_sid: str,
        conversation_sid: str,
        sid: Optional[str] = None,
    ):
        """
        Initialize the WebhookInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "chat_service_sid": payload.get("chat_service_sid"),
            "conversation_sid": payload.get("conversation_sid"),
            "target": payload.get("target"),
            "url": payload.get("url"),
            "configuration": payload.get("configuration"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
        }

        self._solution = {
            "chat_service_sid": chat_service_sid,
            "conversation_sid": conversation_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[WebhookContext] = None

    @property
    def _proxy(self) -> "WebhookContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WebhookContext for this WebhookInstance
        """
        if self._context is None:
            self._context = WebhookContext(
                self._version,
                chat_service_sid=self._solution["chat_service_sid"],
                conversation_sid=self._solution["conversation_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> str:
        """
        :returns: A 34 character string that uniquely identifies this resource.
        """
        return self._properties["sid"]

    @property
    def account_sid(self) -> str:
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation.
        """
        return self._properties["account_sid"]

    @property
    def chat_service_sid(self) -> str:
        """
        :returns: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
        """
        return self._properties["chat_service_sid"]

    @property
    def conversation_sid(self) -> str:
        """
        :returns: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
        """
        return self._properties["conversation_sid"]

    @property
    def target(self) -> str:
        """
        :returns: The target of this webhook: `webhook`, `studio`, `trigger`
        """
        return self._properties["target"]

    @property
    def url(self) -> str:
        """
        :returns: An absolute API resource URL for this webhook.
        """
        return self._properties["url"]

    @property
    def configuration(self) -> Dict[str, object]:
        """
        :returns: The configuration of this webhook. Is defined based on target.
        """
        return self._properties["configuration"]

    @property
    def date_created(self) -> datetime:
        """
        :returns: The date that this resource was created.
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns: The date that this resource was last updated.
        """
        return self._properties["date_updated"]

    def delete(self) -> bool:
        """
        Deletes the WebhookInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the WebhookInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "WebhookInstance":
        """
        Fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "WebhookInstance":
        """
        Asynchronous coroutine to fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        configuration_url=values.unset,
        configuration_method=values.unset,
        configuration_filters=values.unset,
        configuration_triggers=values.unset,
        configuration_flow_sid=values.unset,
    ) -> "WebhookInstance":
        """
        Update the WebhookInstance

        :param str configuration_url: The absolute url the webhook request should be sent to.
        :param "WebhookInstance.Method" configuration_method:
        :param List[str] configuration_filters: The list of events, firing webhook event for this Conversation.
        :param List[str] configuration_triggers: The list of keywords, firing webhook event for this Conversation.
        :param str configuration_flow_sid: The studio flow SID, where the webhook should be sent to.

        :returns: The updated WebhookInstance
        """
        return self._proxy.update(
            configuration_url=configuration_url,
            configuration_method=configuration_method,
            configuration_filters=configuration_filters,
            configuration_triggers=configuration_triggers,
            configuration_flow_sid=configuration_flow_sid,
        )

    async def update_async(
        self,
        configuration_url=values.unset,
        configuration_method=values.unset,
        configuration_filters=values.unset,
        configuration_triggers=values.unset,
        configuration_flow_sid=values.unset,
    ) -> "WebhookInstance":
        """
        Asynchronous coroutine to update the WebhookInstance

        :param str configuration_url: The absolute url the webhook request should be sent to.
        :param "WebhookInstance.Method" configuration_method:
        :param List[str] configuration_filters: The list of events, firing webhook event for this Conversation.
        :param List[str] configuration_triggers: The list of keywords, firing webhook event for this Conversation.
        :param str configuration_flow_sid: The studio flow SID, where the webhook should be sent to.

        :returns: The updated WebhookInstance
        """
        return await self._proxy.update_async(
            configuration_url=configuration_url,
            configuration_method=configuration_method,
            configuration_filters=configuration_filters,
            configuration_triggers=configuration_triggers,
            configuration_flow_sid=configuration_flow_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.WebhookInstance {}>".format(context)


class WebhookContext(InstanceContext):
    def __init__(
        self, version: Version, chat_service_sid: str, conversation_sid: str, sid: str
    ):
        """
        Initialize the WebhookContext

        :param version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
        :param sid: A 34 character string that uniquely identifies this resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
            "conversation_sid": conversation_sid,
            "sid": sid,
        }
        self._uri = "/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the WebhookInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the WebhookInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> WebhookInstance:
        """
        Fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return WebhookInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> WebhookInstance:
        """
        Asynchronous coroutine to fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return WebhookInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        configuration_url=values.unset,
        configuration_method=values.unset,
        configuration_filters=values.unset,
        configuration_triggers=values.unset,
        configuration_flow_sid=values.unset,
    ) -> WebhookInstance:
        """
        Update the WebhookInstance

        :param str configuration_url: The absolute url the webhook request should be sent to.
        :param "WebhookInstance.Method" configuration_method:
        :param List[str] configuration_filters: The list of events, firing webhook event for this Conversation.
        :param List[str] configuration_triggers: The list of keywords, firing webhook event for this Conversation.
        :param str configuration_flow_sid: The studio flow SID, where the webhook should be sent to.

        :returns: The updated WebhookInstance
        """
        data = values.of(
            {
                "Configuration.Url": configuration_url,
                "Configuration.Method": configuration_method,
                "Configuration.Filters": serialize.map(
                    configuration_filters, lambda e: e
                ),
                "Configuration.Triggers": serialize.map(
                    configuration_triggers, lambda e: e
                ),
                "Configuration.FlowSid": configuration_flow_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        configuration_url=values.unset,
        configuration_method=values.unset,
        configuration_filters=values.unset,
        configuration_triggers=values.unset,
        configuration_flow_sid=values.unset,
    ) -> WebhookInstance:
        """
        Asynchronous coroutine to update the WebhookInstance

        :param str configuration_url: The absolute url the webhook request should be sent to.
        :param "WebhookInstance.Method" configuration_method:
        :param List[str] configuration_filters: The list of events, firing webhook event for this Conversation.
        :param List[str] configuration_triggers: The list of keywords, firing webhook event for this Conversation.
        :param str configuration_flow_sid: The studio flow SID, where the webhook should be sent to.

        :returns: The updated WebhookInstance
        """
        data = values.of(
            {
                "Configuration.Url": configuration_url,
                "Configuration.Method": configuration_method,
                "Configuration.Filters": serialize.map(
                    configuration_filters, lambda e: e
                ),
                "Configuration.Triggers": serialize.map(
                    configuration_triggers, lambda e: e
                ),
                "Configuration.FlowSid": configuration_flow_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.WebhookContext {}>".format(context)


class WebhookPage(Page):
    def get_instance(self, payload) -> WebhookInstance:
        """
        Build an instance of WebhookInstance

        :param dict payload: Payload response from the API
        """
        return WebhookInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.WebhookPage>"


class WebhookList(ListResource):
    def __init__(self, version: Version, chat_service_sid: str, conversation_sid: str):
        """
        Initialize the WebhookList

        :param version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
            "conversation_sid": conversation_sid,
        }
        self._uri = "/Services/{chat_service_sid}/Conversations/{conversation_sid}/Webhooks".format(
            **self._solution
        )

    def create(
        self,
        target,
        configuration_url=values.unset,
        configuration_method=values.unset,
        configuration_filters=values.unset,
        configuration_triggers=values.unset,
        configuration_flow_sid=values.unset,
        configuration_replay_after=values.unset,
    ) -> WebhookInstance:
        """
        Create the WebhookInstance

        :param &quot;WebhookInstance.Target&quot; target:
        :param str configuration_url: The absolute url the webhook request should be sent to.
        :param &quot;WebhookInstance.Method&quot; configuration_method:
        :param List[str] configuration_filters: The list of events, firing webhook event for this Conversation.
        :param List[str] configuration_triggers: The list of keywords, firing webhook event for this Conversation.
        :param str configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
        :param int configuration_replay_after: The message index for which and it's successors the webhook will be replayed. Not set by default

        :returns: The created WebhookInstance
        """
        data = values.of(
            {
                "Target": target,
                "Configuration.Url": configuration_url,
                "Configuration.Method": configuration_method,
                "Configuration.Filters": serialize.map(
                    configuration_filters, lambda e: e
                ),
                "Configuration.Triggers": serialize.map(
                    configuration_triggers, lambda e: e
                ),
                "Configuration.FlowSid": configuration_flow_sid,
                "Configuration.ReplayAfter": configuration_replay_after,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
        )

    async def create_async(
        self,
        target,
        configuration_url=values.unset,
        configuration_method=values.unset,
        configuration_filters=values.unset,
        configuration_triggers=values.unset,
        configuration_flow_sid=values.unset,
        configuration_replay_after=values.unset,
    ) -> WebhookInstance:
        """
        Asynchronously create the WebhookInstance

        :param &quot;WebhookInstance.Target&quot; target:
        :param str configuration_url: The absolute url the webhook request should be sent to.
        :param &quot;WebhookInstance.Method&quot; configuration_method:
        :param List[str] configuration_filters: The list of events, firing webhook event for this Conversation.
        :param List[str] configuration_triggers: The list of keywords, firing webhook event for this Conversation.
        :param str configuration_flow_sid: The studio flow SID, where the webhook should be sent to.
        :param int configuration_replay_after: The message index for which and it's successors the webhook will be replayed. Not set by default

        :returns: The created WebhookInstance
        """
        data = values.of(
            {
                "Target": target,
                "Configuration.Url": configuration_url,
                "Configuration.Method": configuration_method,
                "Configuration.Filters": serialize.map(
                    configuration_filters, lambda e: e
                ),
                "Configuration.Triggers": serialize.map(
                    configuration_triggers, lambda e: e
                ),
                "Configuration.FlowSid": configuration_flow_sid,
                "Configuration.ReplayAfter": configuration_replay_after,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
        )

    def stream(self, limit=None, page_size=None) -> List[WebhookInstance]:
        """
        Streams WebhookInstance records from the API as a generator stream.
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

    async def stream_async(self, limit=None, page_size=None) -> List[WebhookInstance]:
        """
        Asynchronously streams WebhookInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[WebhookInstance]:
        """
        Lists WebhookInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[WebhookInstance]:
        """
        Asynchronously lists WebhookInstance records from the API as a list.
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
    ) -> WebhookPage:
        """
        Retrieve a single page of WebhookInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WebhookInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return WebhookPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> WebhookPage:
        """
        Asynchronously retrieve a single page of WebhookInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WebhookInstance
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
        return WebhookPage(self._version, response, self._solution)

    def get_page(self, target_url) -> WebhookPage:
        """
        Retrieve a specific page of WebhookInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WebhookInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return WebhookPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> WebhookPage:
        """
        Asynchronously retrieve a specific page of WebhookInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WebhookInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return WebhookPage(self._version, response, self._solution)

    def get(self, sid) -> WebhookContext:
        """
        Constructs a WebhookContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return WebhookContext(
            self._version,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> WebhookContext:
        """
        Constructs a WebhookContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return WebhookContext(
            self._version,
            chat_service_sid=self._solution["chat_service_sid"],
            conversation_sid=self._solution["conversation_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.WebhookList>"
