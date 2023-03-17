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


from typing import Optional
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UserChannelList(ListResource):
    def __init__(self, version: Version, service_sid: str, user_sid: str):
        """
        Initialize the UserChannelList

        :param Version version: Version that contains the resource
        :param service_sid:
        :param user_sid:

        :returns: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelList
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
        }
        self._uri = "/Services/{service_sid}/Users/{user_sid}/Channels".format(
            **self._solution
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams UserChannelInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams UserChannelInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists UserChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists UserChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of UserChannelInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UserChannelPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of UserChannelInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelPage
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
        return UserChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UserChannelPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of UserChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UserChannelPage(self._version, response, self._solution)

    def get(self, channel_sid):
        """
        Constructs a UserChannelContext

        :param channel_sid:

        :returns: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelContext
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelContext
        """
        return UserChannelContext(
            self._version,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=channel_sid,
        )

    def __call__(self, channel_sid):
        """
        Constructs a UserChannelContext

        :param channel_sid:

        :returns: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelContext
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelContext
        """
        return UserChannelContext(
            self._version,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=channel_sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.IpMessaging.V2.UserChannelList>"


class UserChannelPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of UserChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        """
        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V2.UserChannelPage>"


class UserChannelInstance(InstanceResource):
    class ChannelStatus(object):
        JOINED = "joined"
        INVITED = "invited"
        NOT_PARTICIPATING = "not_participating"

    class NotificationLevel(object):
        DEFAULT = "default"
        MUTED = "muted"

    def __init__(
        self,
        version,
        payload,
        service_sid: str,
        user_sid: str,
        channel_sid: Optional[str] = None,
    ):
        """
        Initialize the UserChannelInstance

        :returns: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "channel_sid": payload.get("channel_sid"),
            "user_sid": payload.get("user_sid"),
            "member_sid": payload.get("member_sid"),
            "status": payload.get("status"),
            "last_consumed_message_index": deserialize.integer(
                payload.get("last_consumed_message_index")
            ),
            "unread_messages_count": deserialize.integer(
                payload.get("unread_messages_count")
            ),
            "links": payload.get("links"),
            "url": payload.get("url"),
            "notification_level": payload.get("notification_level"),
        }

        self._context = None
        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
            "channel_sid": channel_sid or self._properties["channel_sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserChannelContext for this UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelContext
        """
        if self._context is None:
            self._context = UserChannelContext(
                self._version,
                service_sid=self._solution["service_sid"],
                user_sid=self._solution["user_sid"],
                channel_sid=self._solution["channel_sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def service_sid(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["service_sid"]

    @property
    def channel_sid(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["channel_sid"]

    @property
    def user_sid(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["user_sid"]

    @property
    def member_sid(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["member_sid"]

    @property
    def status(self):
        """
        :returns:
        :rtype: UserChannelInstance.ChannelStatus
        """
        return self._properties["status"]

    @property
    def last_consumed_message_index(self):
        """
        :returns:
        :rtype: int
        """
        return self._properties["last_consumed_message_index"]

    @property
    def unread_messages_count(self):
        """
        :returns:
        :rtype: int
        """
        return self._properties["unread_messages_count"]

    @property
    def links(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["links"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    @property
    def notification_level(self):
        """
        :returns:
        :rtype: UserChannelInstance.NotificationLevel
        """
        return self._properties["notification_level"]

    def delete(self):
        """
        Deletes the UserChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the UserChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the UserChannelInstance


        :returns: The fetched UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the UserChannelInstance


        :returns: The fetched UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        notification_level=values.unset,
        last_consumed_message_index=values.unset,
        last_consumption_timestamp=values.unset,
    ):
        """
        Update the UserChannelInstance

        :param UserChannelInstance.NotificationLevel notification_level:
        :param int last_consumed_message_index:
        :param datetime last_consumption_timestamp:

        :returns: The updated UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        """
        return self._proxy.update(
            notification_level=notification_level,
            last_consumed_message_index=last_consumed_message_index,
            last_consumption_timestamp=last_consumption_timestamp,
        )

    async def update_async(
        self,
        notification_level=values.unset,
        last_consumed_message_index=values.unset,
        last_consumption_timestamp=values.unset,
    ):
        """
        Asynchronous coroutine to update the UserChannelInstance

        :param UserChannelInstance.NotificationLevel notification_level:
        :param int last_consumed_message_index:
        :param datetime last_consumption_timestamp:

        :returns: The updated UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        """
        return await self._proxy.update_async(
            notification_level=notification_level,
            last_consumed_message_index=last_consumed_message_index,
            last_consumption_timestamp=last_consumption_timestamp,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.UserChannelInstance {}>".format(context)


class UserChannelContext(InstanceContext):
    def __init__(
        self, version: Version, service_sid: str, user_sid: str, channel_sid: str
    ):
        """
        Initialize the UserChannelContext

        :param Version version: Version that contains the resource
        :param service_sid:
        :param user_sid:
        :param channel_sid:

        :returns: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelContext
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
            "channel_sid": channel_sid,
        }
        self._uri = (
            "/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}".format(
                **self._solution
            )
        )

    def delete(self):
        """
        Deletes the UserChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the UserChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the UserChannelInstance


        :returns: The fetched UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the UserChannelInstance


        :returns: The fetched UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def update(
        self,
        notification_level=values.unset,
        last_consumed_message_index=values.unset,
        last_consumption_timestamp=values.unset,
    ):
        """
        Update the UserChannelInstance

        :param UserChannelInstance.NotificationLevel notification_level:
        :param int last_consumed_message_index:
        :param datetime last_consumption_timestamp:

        :returns: The updated UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        """
        data = values.of(
            {
                "NotificationLevel": notification_level,
                "LastConsumedMessageIndex": last_consumed_message_index,
                "LastConsumptionTimestamp": serialize.iso8601_datetime(
                    last_consumption_timestamp
                ),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    async def update_async(
        self,
        notification_level=values.unset,
        last_consumed_message_index=values.unset,
        last_consumption_timestamp=values.unset,
    ):
        """
        Asynchronous coroutine to update the UserChannelInstance

        :param UserChannelInstance.NotificationLevel notification_level:
        :param int last_consumed_message_index:
        :param datetime last_consumption_timestamp:

        :returns: The updated UserChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.user.user_channel.UserChannelInstance
        """
        data = values.of(
            {
                "NotificationLevel": notification_level,
                "LastConsumedMessageIndex": last_consumed_message_index,
                "LastConsumptionTimestamp": serialize.iso8601_datetime(
                    last_consumption_timestamp
                ),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.UserChannelContext {}>".format(context)
