r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class MessageInstance(InstanceResource):
    class OrderType(object):
        ASC = "asc"
        DESC = "desc"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    """
    :ivar sid: 
    :ivar account_sid: 
    :ivar attributes: 
    :ivar service_sid: 
    :ivar to: 
    :ivar channel_sid: 
    :ivar date_created: 
    :ivar date_updated: 
    :ivar last_updated_by: 
    :ivar was_edited: 
    :ivar _from: 
    :ivar body: 
    :ivar index: 
    :ivar type: 
    :ivar media: 
    :ivar url: 
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        channel_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.attributes: Optional[str] = payload.get("attributes")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.to: Optional[str] = payload.get("to")
        self.channel_sid: Optional[str] = payload.get("channel_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.last_updated_by: Optional[str] = payload.get("last_updated_by")
        self.was_edited: Optional[bool] = payload.get("was_edited")
        self._from: Optional[str] = payload.get("from")
        self.body: Optional[str] = payload.get("body")
        self.index: Optional[int] = deserialize.integer(payload.get("index"))
        self.type: Optional[str] = payload.get("type")
        self.media: Optional[Dict[str, object]] = payload.get("media")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "channel_sid": channel_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[MessageContext] = None

    @property
    def _proxy(self) -> "MessageContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MessageContext for this MessageInstance
        """
        if self._context is None:
            self._context = MessageContext(
                self._version,
                service_sid=self._solution["service_sid"],
                channel_sid=self._solution["channel_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self, x_twilio_webhook_enabled=values.unset) -> bool:
        """
        Deletes the MessageInstance

        :param "MessageInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    async def delete_async(self, x_twilio_webhook_enabled=values.unset) -> bool:
        """
        Asynchronous coroutine that deletes the MessageInstance

        :param "MessageInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    def fetch(self) -> "MessageInstance":
        """
        Fetch the MessageInstance


        :returns: The fetched MessageInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "MessageInstance":
        """
        Asynchronous coroutine to fetch the MessageInstance


        :returns: The fetched MessageInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        x_twilio_webhook_enabled=values.unset,
        body=values.unset,
        attributes=values.unset,
        date_created=values.unset,
        date_updated=values.unset,
        last_updated_by=values.unset,
        from_=values.unset,
    ) -> "MessageInstance":
        """
        Update the MessageInstance

        :param "MessageInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str body:
        :param str attributes:
        :param datetime date_created:
        :param datetime date_updated:
        :param str last_updated_by:
        :param str from_:

        :returns: The updated MessageInstance
        """
        return self._proxy.update(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            body=body,
            attributes=attributes,
            date_created=date_created,
            date_updated=date_updated,
            last_updated_by=last_updated_by,
            from_=from_,
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled=values.unset,
        body=values.unset,
        attributes=values.unset,
        date_created=values.unset,
        date_updated=values.unset,
        last_updated_by=values.unset,
        from_=values.unset,
    ) -> "MessageInstance":
        """
        Asynchronous coroutine to update the MessageInstance

        :param "MessageInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str body:
        :param str attributes:
        :param datetime date_created:
        :param datetime date_updated:
        :param str last_updated_by:
        :param str from_:

        :returns: The updated MessageInstance
        """
        return await self._proxy.update_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            body=body,
            attributes=attributes,
            date_created=date_created,
            date_updated=date_updated,
            last_updated_by=last_updated_by,
            from_=from_,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.MessageInstance {}>".format(context)


class MessageContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, channel_sid: str, sid: str):
        """
        Initialize the MessageContext

        :param version: Version that contains the resource
        :param service_sid:
        :param channel_sid:
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "channel_sid": channel_sid,
            "sid": sid,
        }
        self._uri = (
            "/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}".format(
                **self._solution
            )
        )

    def delete(self, x_twilio_webhook_enabled=values.unset) -> bool:
        """
        Deletes the MessageInstance

        :param &quot;MessageInstance.WebhookEnabledType&quot; x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

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
        Asynchronous coroutine that deletes the MessageInstance

        :param &quot;MessageInstance.WebhookEnabledType&quot; x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

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

    def fetch(self) -> MessageInstance:
        """
        Fetch the MessageInstance


        :returns: The fetched MessageInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> MessageInstance:
        """
        Asynchronous coroutine to fetch the MessageInstance


        :returns: The fetched MessageInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        x_twilio_webhook_enabled=values.unset,
        body=values.unset,
        attributes=values.unset,
        date_created=values.unset,
        date_updated=values.unset,
        last_updated_by=values.unset,
        from_=values.unset,
    ) -> MessageInstance:
        """
        Update the MessageInstance

        :param "MessageInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str body:
        :param str attributes:
        :param datetime date_created:
        :param datetime date_updated:
        :param str last_updated_by:
        :param str from_:

        :returns: The updated MessageInstance
        """
        data = values.of(
            {
                "Body": body,
                "Attributes": attributes,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "LastUpdatedBy": last_updated_by,
                "From": from_,
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

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled=values.unset,
        body=values.unset,
        attributes=values.unset,
        date_created=values.unset,
        date_updated=values.unset,
        last_updated_by=values.unset,
        from_=values.unset,
    ) -> MessageInstance:
        """
        Asynchronous coroutine to update the MessageInstance

        :param "MessageInstance.WebhookEnabledType" x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str body:
        :param str attributes:
        :param datetime date_created:
        :param datetime date_updated:
        :param str last_updated_by:
        :param str from_:

        :returns: The updated MessageInstance
        """
        data = values.of(
            {
                "Body": body,
                "Attributes": attributes,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "LastUpdatedBy": last_updated_by,
                "From": from_,
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

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.MessageContext {}>".format(context)


class MessagePage(Page):
    def get_instance(self, payload) -> MessageInstance:
        """
        Build an instance of MessageInstance

        :param dict payload: Payload response from the API
        """
        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V2.MessagePage>"


class MessageList(ListResource):
    def __init__(self, version: Version, service_sid: str, channel_sid: str):
        """
        Initialize the MessageList

        :param version: Version that contains the resource
        :param service_sid:
        :param channel_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "channel_sid": channel_sid,
        }
        self._uri = "/Services/{service_sid}/Channels/{channel_sid}/Messages".format(
            **self._solution
        )

    def create(
        self,
        x_twilio_webhook_enabled=values.unset,
        from_=values.unset,
        attributes=values.unset,
        date_created=values.unset,
        date_updated=values.unset,
        last_updated_by=values.unset,
        body=values.unset,
        media_sid=values.unset,
    ) -> MessageInstance:
        """
        Create the MessageInstance

        :param &quot;MessageInstance.WebhookEnabledType&quot; x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str from_:
        :param str attributes:
        :param datetime date_created:
        :param datetime date_updated:
        :param str last_updated_by:
        :param str body:
        :param str media_sid:

        :returns: The created MessageInstance
        """
        data = values.of(
            {
                "From": from_,
                "Attributes": attributes,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "LastUpdatedBy": last_updated_by,
                "Body": body,
                "MediaSid": media_sid,
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

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    async def create_async(
        self,
        x_twilio_webhook_enabled=values.unset,
        from_=values.unset,
        attributes=values.unset,
        date_created=values.unset,
        date_updated=values.unset,
        last_updated_by=values.unset,
        body=values.unset,
        media_sid=values.unset,
    ) -> MessageInstance:
        """
        Asynchronously create the MessageInstance

        :param &quot;MessageInstance.WebhookEnabledType&quot; x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str from_:
        :param str attributes:
        :param datetime date_created:
        :param datetime date_updated:
        :param str last_updated_by:
        :param str body:
        :param str media_sid:

        :returns: The created MessageInstance
        """
        data = values.of(
            {
                "From": from_,
                "Attributes": attributes,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "LastUpdatedBy": last_updated_by,
                "Body": body,
                "MediaSid": media_sid,
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

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def stream(
        self, order=values.unset, limit=None, page_size=None
    ) -> List[MessageInstance]:
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;MessageInstance.OrderType&quot; order:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(order=order, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, order=values.unset, limit=None, page_size=None
    ) -> List[MessageInstance]:
        """
        Asynchronously streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;MessageInstance.OrderType&quot; order:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(order=order, page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self, order=values.unset, limit=None, page_size=None
    ) -> List[MessageInstance]:
        """
        Lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;MessageInstance.OrderType&quot; order:
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
                order=order,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self, order=values.unset, limit=None, page_size=None
    ) -> List[MessageInstance]:
        """
        Asynchronously lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;MessageInstance.OrderType&quot; order:
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
                order=order,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        order=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> MessagePage:
        """
        Retrieve a single page of MessageInstance records from the API.
        Request is executed immediately

        :param &quot;MessageInstance.OrderType&quot; order:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        """
        data = values.of(
            {
                "Order": order,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return MessagePage(self._version, response, self._solution)

    async def page_async(
        self,
        order=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> MessagePage:
        """
        Asynchronously retrieve a single page of MessageInstance records from the API.
        Request is executed immediately

        :param &quot;MessageInstance.OrderType&quot; order:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        """
        data = values.of(
            {
                "Order": order,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return MessagePage(self._version, response, self._solution)

    def get_page(self, target_url) -> MessagePage:
        """
        Retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return MessagePage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> MessagePage:
        """
        Asynchronously retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return MessagePage(self._version, response, self._solution)

    def get(self, sid) -> MessageContext:
        """
        Constructs a MessageContext

        :param sid:
        """
        return MessageContext(
            self._version,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> MessageContext:
        """
        Constructs a MessageContext

        :param sid:
        """
        return MessageContext(
            self._version,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V2.MessageList>"
