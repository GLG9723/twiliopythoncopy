r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class WebhookInstance(InstanceResource):
    class Methods(object):
        GET = "GET"
        POST = "POST"

    class Status(object):
        ENABLED = "enabled"
        DISABLED = "disabled"

    class Version(object):
        V1 = "v1"
        V2 = "v2"

    def __init__(self, version, payload, service_sid: str, sid: Optional[str] = None):
        """
        Initialize the WebhookInstance
        """
        super().__init__(version)

        self._sid: Optional[str] = payload.get("sid")
        self._service_sid: Optional[str] = payload.get("service_sid")
        self._account_sid: Optional[str] = payload.get("account_sid")
        self._friendly_name: Optional[str] = payload.get("friendly_name")
        self._event_types: Optional[List[str]] = payload.get("event_types")
        self._status: Optional["WebhookInstance.Status"] = payload.get("status")
        self._version: Optional["WebhookInstance.Version"] = payload.get("version")
        self._webhook_url: Optional[str] = payload.get("webhook_url")
        self._webhook_method: Optional["WebhookInstance.Methods"] = payload.get(
            "webhook_method"
        )
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self._url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self._sid,
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
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that we created to identify the Webhook resource.
        """
        return self._sid

    @property
    def service_sid(self) -> Optional[str]:
        """
        :returns: The unique SID identifier of the Service.
        """
        return self._service_sid

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
        """
        return self._account_sid

    @property
    def friendly_name(self) -> Optional[str]:
        """
        :returns: The string that you assigned to describe the webhook. **This value should not contain PII.**
        """
        return self._friendly_name

    @property
    def event_types(self) -> Optional[List[str]]:
        """
        :returns: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        """
        return self._event_types

    @property
    def status(self) -> Optional["WebhookInstance.Status"]:
        return self._status

    @property
    def version(self) -> Optional["WebhookInstance.Version"]:
        return self._version

    @property
    def webhook_url(self) -> Optional[str]:
        """
        :returns: The URL associated with this Webhook.
        """
        return self._webhook_url

    @property
    def webhook_method(self) -> Optional["WebhookInstance.Methods"]:
        return self._webhook_method

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
        :returns: The absolute URL of the Webhook resource.
        """
        return self._url

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
        friendly_name=values.unset,
        event_types=values.unset,
        webhook_url=values.unset,
        status=values.unset,
        version=values.unset,
    ) -> "WebhookInstance":
        """
        Update the WebhookInstance

        :param str friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param List[str] event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param str webhook_url: The URL associated with this Webhook.
        :param "WebhookInstance.Status" status:
        :param "WebhookInstance.Version" version:

        :returns: The updated WebhookInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            event_types=event_types,
            webhook_url=webhook_url,
            status=status,
            version=version,
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        event_types=values.unset,
        webhook_url=values.unset,
        status=values.unset,
        version=values.unset,
    ) -> "WebhookInstance":
        """
        Asynchronous coroutine to update the WebhookInstance

        :param str friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param List[str] event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param str webhook_url: The URL associated with this Webhook.
        :param "WebhookInstance.Status" status:
        :param "WebhookInstance.Version" version:

        :returns: The updated WebhookInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            event_types=event_types,
            webhook_url=webhook_url,
            status=status,
            version=version,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.WebhookInstance {}>".format(context)


class WebhookContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the WebhookContext

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Webhooks/{sid}".format(**self._solution)

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
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name=values.unset,
        event_types=values.unset,
        webhook_url=values.unset,
        status=values.unset,
        version=values.unset,
    ) -> WebhookInstance:
        """
        Update the WebhookInstance

        :param str friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param List[str] event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param str webhook_url: The URL associated with this Webhook.
        :param "WebhookInstance.Status" status:
        :param "WebhookInstance.Version" version:

        :returns: The updated WebhookInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "EventTypes": serialize.map(event_types, lambda e: e),
                "WebhookUrl": webhook_url,
                "Status": status,
                "Version": version,
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
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        event_types=values.unset,
        webhook_url=values.unset,
        status=values.unset,
        version=values.unset,
    ) -> WebhookInstance:
        """
        Asynchronous coroutine to update the WebhookInstance

        :param str friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param List[str] event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param str webhook_url: The URL associated with this Webhook.
        :param "WebhookInstance.Status" status:
        :param "WebhookInstance.Version" version:

        :returns: The updated WebhookInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "EventTypes": serialize.map(event_types, lambda e: e),
                "WebhookUrl": webhook_url,
                "Status": status,
                "Version": version,
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
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.WebhookContext {}>".format(context)


class WebhookPage(Page):
    def get_instance(self, payload) -> WebhookInstance:
        """
        Build an instance of WebhookInstance

        :param dict payload: Payload response from the API
        """
        return WebhookInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.WebhookPage>"


class WebhookList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the WebhookList

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Webhooks".format(**self._solution)

    def create(
        self,
        friendly_name,
        event_types,
        webhook_url,
        status=values.unset,
        version=values.unset,
    ) -> WebhookInstance:
        """
        Create the WebhookInstance

        :param str friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param List[str] event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param str webhook_url: The URL associated with this Webhook.
        :param &quot;WebhookInstance.Status&quot; status:
        :param &quot;WebhookInstance.Version&quot; version:

        :returns: The created WebhookInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "EventTypes": serialize.map(event_types, lambda e: e),
                "WebhookUrl": webhook_url,
                "Status": status,
                "Version": version,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        friendly_name,
        event_types,
        webhook_url,
        status=values.unset,
        version=values.unset,
    ) -> WebhookInstance:
        """
        Asynchronously create the WebhookInstance

        :param str friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param List[str] event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param str webhook_url: The URL associated with this Webhook.
        :param &quot;WebhookInstance.Status&quot; status:
        :param &quot;WebhookInstance.Version&quot; version:

        :returns: The created WebhookInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "EventTypes": serialize.map(event_types, lambda e: e),
                "WebhookUrl": webhook_url,
                "Status": status,
                "Version": version,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
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

        :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
        """
        return WebhookContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid) -> WebhookContext:
        """
        Constructs a WebhookContext

        :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
        """
        return WebhookContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.WebhookList>"
