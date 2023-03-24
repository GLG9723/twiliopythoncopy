r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
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
from twilio.rest.events.v1.subscription.subscribed_event import SubscribedEventList


class SubscriptionInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the SubscriptionInstance
        """
        super().__init__(version)

        self._account_sid: Optional[str] = payload.get("account_sid")
        self._sid: Optional[str] = payload.get("sid")
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self._description: Optional[str] = payload.get("description")
        self._sink_sid: Optional[str] = payload.get("sink_sid")
        self._url: Optional[str] = payload.get("url")
        self._links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self._sid,
        }
        self._context: Optional[SubscriptionContext] = None

    @property
    def _proxy(self) -> "SubscriptionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SubscriptionContext for this SubscriptionInstance
        """
        if self._context is None:
            self._context = SubscriptionContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The unique SID identifier of the Account.
        """
        return self._account_sid

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: A 34 character string that uniquely identifies this Subscription.
        """
        return self._sid

    @property
    def date_created(self) -> Optional[datetime]:
        """
        :returns: The date that this Subscription was created, given in ISO 8601 format.
        """
        return self._date_created

    @property
    def date_updated(self) -> Optional[datetime]:
        """
        :returns: The date that this Subscription was updated, given in ISO 8601 format.
        """
        return self._date_updated

    @property
    def description(self) -> Optional[str]:
        """
        :returns: A human readable description for the Subscription
        """
        return self._description

    @property
    def sink_sid(self) -> Optional[str]:
        """
        :returns: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
        """
        return self._sink_sid

    @property
    def url(self) -> Optional[str]:
        """
        :returns: The URL of this resource.
        """
        return self._url

    @property
    def links(self) -> Optional[Dict[str, object]]:
        """
        :returns: Contains a dictionary of URL links to nested resources of this Subscription.
        """
        return self._links

    def delete(self) -> bool:
        """
        Deletes the SubscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SubscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "SubscriptionInstance":
        """
        Fetch the SubscriptionInstance


        :returns: The fetched SubscriptionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SubscriptionInstance":
        """
        Asynchronous coroutine to fetch the SubscriptionInstance


        :returns: The fetched SubscriptionInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, description=values.unset, sink_sid=values.unset
    ) -> "SubscriptionInstance":
        """
        Update the SubscriptionInstance

        :param str description: A human readable description for the Subscription.
        :param str sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.

        :returns: The updated SubscriptionInstance
        """
        return self._proxy.update(
            description=description,
            sink_sid=sink_sid,
        )

    async def update_async(
        self, description=values.unset, sink_sid=values.unset
    ) -> "SubscriptionInstance":
        """
        Asynchronous coroutine to update the SubscriptionInstance

        :param str description: A human readable description for the Subscription.
        :param str sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.

        :returns: The updated SubscriptionInstance
        """
        return await self._proxy.update_async(
            description=description,
            sink_sid=sink_sid,
        )

    @property
    def subscribed_events(self) -> SubscribedEventList:
        """
        Access the subscribed_events
        """
        return self._proxy.subscribed_events

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Events.V1.SubscriptionInstance {}>".format(context)


class SubscriptionContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the SubscriptionContext

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this Subscription.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Subscriptions/{sid}".format(**self._solution)

        self._subscribed_events: Optional[SubscribedEventList] = None

    def delete(self) -> bool:
        """
        Deletes the SubscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SubscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> SubscriptionInstance:
        """
        Fetch the SubscriptionInstance


        :returns: The fetched SubscriptionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SubscriptionInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SubscriptionInstance:
        """
        Asynchronous coroutine to fetch the SubscriptionInstance


        :returns: The fetched SubscriptionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SubscriptionInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self, description=values.unset, sink_sid=values.unset
    ) -> SubscriptionInstance:
        """
        Update the SubscriptionInstance

        :param str description: A human readable description for the Subscription.
        :param str sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.

        :returns: The updated SubscriptionInstance
        """
        data = values.of(
            {
                "Description": description,
                "SinkSid": sink_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SubscriptionInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self, description=values.unset, sink_sid=values.unset
    ) -> SubscriptionInstance:
        """
        Asynchronous coroutine to update the SubscriptionInstance

        :param str description: A human readable description for the Subscription.
        :param str sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.

        :returns: The updated SubscriptionInstance
        """
        data = values.of(
            {
                "Description": description,
                "SinkSid": sink_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SubscriptionInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def subscribed_events(self) -> SubscribedEventList:
        """
        Access the subscribed_events
        """
        if self._subscribed_events is None:
            self._subscribed_events = SubscribedEventList(
                self._version,
                self._solution["sid"],
            )
        return self._subscribed_events

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Events.V1.SubscriptionContext {}>".format(context)


class SubscriptionPage(Page):
    def get_instance(self, payload) -> SubscriptionInstance:
        """
        Build an instance of SubscriptionInstance

        :param dict payload: Payload response from the API
        """
        return SubscriptionInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Events.V1.SubscriptionPage>"


class SubscriptionList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the SubscriptionList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Subscriptions"

    def create(self, description, sink_sid, types) -> SubscriptionInstance:
        """
        Create the SubscriptionInstance

        :param str description: A human readable description for the Subscription **This value should not contain PII.**
        :param str sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
        :param List[object] types: An array of objects containing the subscribed Event Types

        :returns: The created SubscriptionInstance
        """
        data = values.of(
            {
                "Description": description,
                "SinkSid": sink_sid,
                "Types": serialize.map(types, lambda e: serialize.object(e)),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SubscriptionInstance(self._version, payload)

    async def create_async(self, description, sink_sid, types) -> SubscriptionInstance:
        """
        Asynchronously create the SubscriptionInstance

        :param str description: A human readable description for the Subscription **This value should not contain PII.**
        :param str sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
        :param List[object] types: An array of objects containing the subscribed Event Types

        :returns: The created SubscriptionInstance
        """
        data = values.of(
            {
                "Description": description,
                "SinkSid": sink_sid,
                "Types": serialize.map(types, lambda e: serialize.object(e)),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SubscriptionInstance(self._version, payload)

    def stream(
        self, sink_sid=values.unset, limit=None, page_size=None
    ) -> List[SubscriptionInstance]:
        """
        Streams SubscriptionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str sink_sid: The SID of the sink that the list of Subscriptions should be filtered by.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(sink_sid=sink_sid, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, sink_sid=values.unset, limit=None, page_size=None
    ) -> List[SubscriptionInstance]:
        """
        Asynchronously streams SubscriptionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str sink_sid: The SID of the sink that the list of Subscriptions should be filtered by.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(sink_sid=sink_sid, page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self, sink_sid=values.unset, limit=None, page_size=None
    ) -> List[SubscriptionInstance]:
        """
        Lists SubscriptionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str sink_sid: The SID of the sink that the list of Subscriptions should be filtered by.
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
                sink_sid=sink_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self, sink_sid=values.unset, limit=None, page_size=None
    ) -> List[SubscriptionInstance]:
        """
        Asynchronously lists SubscriptionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str sink_sid: The SID of the sink that the list of Subscriptions should be filtered by.
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
                sink_sid=sink_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        sink_sid=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> SubscriptionPage:
        """
        Retrieve a single page of SubscriptionInstance records from the API.
        Request is executed immediately

        :param str sink_sid: The SID of the sink that the list of Subscriptions should be filtered by.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SubscriptionInstance
        """
        data = values.of(
            {
                "SinkSid": sink_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SubscriptionPage(self._version, response)

    async def page_async(
        self,
        sink_sid=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> SubscriptionPage:
        """
        Asynchronously retrieve a single page of SubscriptionInstance records from the API.
        Request is executed immediately

        :param str sink_sid: The SID of the sink that the list of Subscriptions should be filtered by.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SubscriptionInstance
        """
        data = values.of(
            {
                "SinkSid": sink_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SubscriptionPage(self._version, response)

    def get_page(self, target_url) -> SubscriptionPage:
        """
        Retrieve a specific page of SubscriptionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SubscriptionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SubscriptionPage(self._version, response)

    async def get_page_async(self, target_url) -> SubscriptionPage:
        """
        Asynchronously retrieve a specific page of SubscriptionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SubscriptionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SubscriptionPage(self._version, response)

    def get(self, sid) -> SubscriptionContext:
        """
        Constructs a SubscriptionContext

        :param sid: A 34 character string that uniquely identifies this Subscription.
        """
        return SubscriptionContext(self._version, sid=sid)

    def __call__(self, sid) -> SubscriptionContext:
        """
        Constructs a SubscriptionContext

        :param sid: A 34 character string that uniquely identifies this Subscription.
        """
        return SubscriptionContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Events.V1.SubscriptionList>"
