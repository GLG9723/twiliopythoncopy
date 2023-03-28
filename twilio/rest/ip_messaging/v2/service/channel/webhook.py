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
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class WebhookInstance(InstanceResource):
    class Method(object):
        GET = "GET"
        POST = "POST"

    class Type(object):
        WEBHOOK = "webhook"
        TRIGGER = "trigger"
        STUDIO = "studio"

    """
    :ivar sid: 
    :ivar account_sid: 
    :ivar service_sid: 
    :ivar channel_sid: 
    :ivar type: 
    :ivar url: 
    :ivar configuration: 
    :ivar date_created: 
    :ivar date_updated: 
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
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.channel_sid: Optional[str] = payload.get("channel_sid")
        self.type: Optional[str] = payload.get("type")
        self.url: Optional[str] = payload.get("url")
        self.configuration: Optional[Dict[str, object]] = payload.get("configuration")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )

        self._solution = {
            "service_sid": service_sid,
            "channel_sid": channel_sid,
            "sid": sid or self.sid,
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
                service_sid=self._solution["service_sid"],
                channel_sid=self._solution["channel_sid"],
                sid=self._solution["sid"],
            )
        return self._context

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
        configuration_url: Union[str, object] = values.unset,
        configuration_method: Union["WebhookInstance.Method", object] = values.unset,
        configuration_filters: Union[List[str], object] = values.unset,
        configuration_triggers: Union[List[str], object] = values.unset,
        configuration_flow_sid: Union[str, object] = values.unset,
        configuration_retry_count: Union[int, object] = values.unset,
    ) -> "WebhookInstance":
        """
        Update the WebhookInstance

        :param configuration_url:
        :param configuration_method:
        :param configuration_filters:
        :param configuration_triggers:
        :param configuration_flow_sid:
        :param configuration_retry_count:

        :returns: The updated WebhookInstance
        """
        return self._proxy.update(
            configuration_url=configuration_url,
            configuration_method=configuration_method,
            configuration_filters=configuration_filters,
            configuration_triggers=configuration_triggers,
            configuration_flow_sid=configuration_flow_sid,
            configuration_retry_count=configuration_retry_count,
        )

    async def update_async(
        self,
        configuration_url: Union[str, object] = values.unset,
        configuration_method: Union["WebhookInstance.Method", object] = values.unset,
        configuration_filters: Union[List[str], object] = values.unset,
        configuration_triggers: Union[List[str], object] = values.unset,
        configuration_flow_sid: Union[str, object] = values.unset,
        configuration_retry_count: Union[int, object] = values.unset,
    ) -> "WebhookInstance":
        """
        Asynchronous coroutine to update the WebhookInstance

        :param configuration_url:
        :param configuration_method:
        :param configuration_filters:
        :param configuration_triggers:
        :param configuration_flow_sid:
        :param configuration_retry_count:

        :returns: The updated WebhookInstance
        """
        return await self._proxy.update_async(
            configuration_url=configuration_url,
            configuration_method=configuration_method,
            configuration_filters=configuration_filters,
            configuration_triggers=configuration_triggers,
            configuration_flow_sid=configuration_flow_sid,
            configuration_retry_count=configuration_retry_count,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.WebhookInstance {}>".format(context)


class WebhookContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, channel_sid: str, sid: str):
        """
        Initialize the WebhookContext

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
            "/Services/{service_sid}/Channels/{channel_sid}/Webhooks/{sid}".format(
                **self._solution
            )
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
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
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
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        configuration_url: Union[str, object] = values.unset,
        configuration_method: Union["WebhookInstance.Method", object] = values.unset,
        configuration_filters: Union[List[str], object] = values.unset,
        configuration_triggers: Union[List[str], object] = values.unset,
        configuration_flow_sid: Union[str, object] = values.unset,
        configuration_retry_count: Union[int, object] = values.unset,
    ) -> WebhookInstance:
        """
        Update the WebhookInstance

        :param configuration_url:
        :param configuration_method:
        :param configuration_filters:
        :param configuration_triggers:
        :param configuration_flow_sid:
        :param configuration_retry_count:

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
                "Configuration.RetryCount": configuration_retry_count,
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
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        configuration_url: Union[str, object] = values.unset,
        configuration_method: Union["WebhookInstance.Method", object] = values.unset,
        configuration_filters: Union[List[str], object] = values.unset,
        configuration_triggers: Union[List[str], object] = values.unset,
        configuration_flow_sid: Union[str, object] = values.unset,
        configuration_retry_count: Union[int, object] = values.unset,
    ) -> WebhookInstance:
        """
        Asynchronous coroutine to update the WebhookInstance

        :param configuration_url:
        :param configuration_method:
        :param configuration_filters:
        :param configuration_triggers:
        :param configuration_flow_sid:
        :param configuration_retry_count:

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
                "Configuration.RetryCount": configuration_retry_count,
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
        return "<Twilio.IpMessaging.V2.WebhookContext {}>".format(context)


class WebhookPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> WebhookInstance:
        """
        Build an instance of WebhookInstance

        :param payload: Payload response from the API
        """
        return WebhookInstance(
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
        return "<Twilio.IpMessaging.V2.WebhookPage>"


class WebhookList(ListResource):
    def __init__(self, version: Version, service_sid: str, channel_sid: str):
        """
        Initialize the WebhookList

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
        self._uri = "/Services/{service_sid}/Channels/{channel_sid}/Webhooks".format(
            **self._solution
        )

    def create(
        self,
        type: "WebhookInstance.Type",
        configuration_url: Union[str, object] = values.unset,
        configuration_method: Union["WebhookInstance.Method", object] = values.unset,
        configuration_filters: Union[List[str], object] = values.unset,
        configuration_triggers: Union[List[str], object] = values.unset,
        configuration_flow_sid: Union[str, object] = values.unset,
        configuration_retry_count: Union[int, object] = values.unset,
    ) -> WebhookInstance:
        """
        Create the WebhookInstance

        :param type:
        :param configuration_url:
        :param configuration_method:
        :param configuration_filters:
        :param configuration_triggers:
        :param configuration_flow_sid:
        :param configuration_retry_count:

        :returns: The created WebhookInstance
        """
        data = values.of(
            {
                "Type": type,
                "Configuration.Url": configuration_url,
                "Configuration.Method": configuration_method,
                "Configuration.Filters": serialize.map(
                    configuration_filters, lambda e: e
                ),
                "Configuration.Triggers": serialize.map(
                    configuration_triggers, lambda e: e
                ),
                "Configuration.FlowSid": configuration_flow_sid,
                "Configuration.RetryCount": configuration_retry_count,
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
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    async def create_async(
        self,
        type: "WebhookInstance.Type",
        configuration_url: Union[str, object] = values.unset,
        configuration_method: Union["WebhookInstance.Method", object] = values.unset,
        configuration_filters: Union[List[str], object] = values.unset,
        configuration_triggers: Union[List[str], object] = values.unset,
        configuration_flow_sid: Union[str, object] = values.unset,
        configuration_retry_count: Union[int, object] = values.unset,
    ) -> WebhookInstance:
        """
        Asynchronously create the WebhookInstance

        :param type:
        :param configuration_url:
        :param configuration_method:
        :param configuration_filters:
        :param configuration_triggers:
        :param configuration_flow_sid:
        :param configuration_retry_count:

        :returns: The created WebhookInstance
        """
        data = values.of(
            {
                "Type": type,
                "Configuration.Url": configuration_url,
                "Configuration.Method": configuration_method,
                "Configuration.Filters": serialize.map(
                    configuration_filters, lambda e: e
                ),
                "Configuration.Triggers": serialize.map(
                    configuration_triggers, lambda e: e
                ),
                "Configuration.FlowSid": configuration_flow_sid,
                "Configuration.RetryCount": configuration_retry_count,
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
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[WebhookInstance]:
        """
        Streams WebhookInstance records from the API as a generator stream.
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
    ) -> List[WebhookInstance]:
        """
        Asynchronously streams WebhookInstance records from the API as a generator stream.
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

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[WebhookInstance]:
        """
        Lists WebhookInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
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
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[WebhookInstance]:
        """
        Asynchronously lists WebhookInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
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
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> WebhookPage:
        """
        Retrieve a single page of WebhookInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

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
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> WebhookPage:
        """
        Asynchronously retrieve a single page of WebhookInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

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

    def get_page(self, target_url: str) -> WebhookPage:
        """
        Retrieve a specific page of WebhookInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of WebhookInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return WebhookPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> WebhookPage:
        """
        Asynchronously retrieve a specific page of WebhookInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of WebhookInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return WebhookPage(self._version, response, self._solution)

    def get(self, sid: str) -> WebhookContext:
        """
        Constructs a WebhookContext

        :param sid:
        """
        return WebhookContext(
            self._version,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> WebhookContext:
        """
        Constructs a WebhookContext

        :param sid:
        """
        return WebhookContext(
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
        return "<Twilio.IpMessaging.V2.WebhookList>"
