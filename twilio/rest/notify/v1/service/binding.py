r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Notify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date, datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class BindingInstance(InstanceResource):
    class BindingType(object):
        APN = "apn"
        GCM = "gcm"
        SMS = "sms"
        FCM = "fcm"
        FACEBOOK_MESSENGER = "facebook-messenger"
        ALEXA = "alexa"

    """
    :ivar sid: The unique string that we created to identify the Binding resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Binding resource.
    :ivar service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) the resource is associated with.
    :ivar credential_sid: The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applicable only to `apn`, `fcm`, and `gcm` type Bindings.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar notification_protocol_version: The protocol version to use to send the notification. This defaults to the value of `default_xxxx_notification_protocol_version` in the [Service](https://www.twilio.com/docs/notify/api/service-resource) for the protocol. The current version is `\"3\"` for `apn`, `fcm`, and `gcm` type Bindings. The parameter is not applicable to `sms` and `facebook-messenger` type Bindings as the data format is fixed.
    :ivar endpoint: Deprecated.
    :ivar identity: The `identity` value that uniquely identifies the resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service.
    :ivar binding_type: The transport technology to use for the Binding. Can be: `apn`, `fcm`, `gcm`, `sms`, or `facebook-messenger`.
    :ivar address: The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format.
    :ivar tags: The list of tags associated with this Binding. Tags can be used to select the Bindings to use when sending a notification. Maximum 20 tags are allowed.
    :ivar url: The absolute URL of the Binding resource.
    :ivar links: The URLs of related resources.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.credential_sid: Optional[str] = payload.get("credential_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.notification_protocol_version: Optional[str] = payload.get(
            "notification_protocol_version"
        )
        self.endpoint: Optional[str] = payload.get("endpoint")
        self.identity: Optional[str] = payload.get("identity")
        self.binding_type: Optional[str] = payload.get("binding_type")
        self.address: Optional[str] = payload.get("address")
        self.tags: Optional[List[str]] = payload.get("tags")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[BindingContext] = None

    @property
    def _proxy(self) -> "BindingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BindingContext for this BindingInstance
        """
        if self._context is None:
            self._context = BindingContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the BindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the BindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "BindingInstance":
        """
        Fetch the BindingInstance


        :returns: The fetched BindingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "BindingInstance":
        """
        Asynchronous coroutine to fetch the BindingInstance


        :returns: The fetched BindingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Notify.V1.BindingInstance {}>".format(context)


class BindingContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the BindingContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to fetch the resource from.
        :param sid: The Twilio-provided string that uniquely identifies the Binding resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Bindings/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the BindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the BindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> BindingInstance:
        """
        Fetch the BindingInstance


        :returns: The fetched BindingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return BindingInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> BindingInstance:
        """
        Asynchronous coroutine to fetch the BindingInstance


        :returns: The fetched BindingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return BindingInstance(
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
        return "<Twilio.Notify.V1.BindingContext {}>".format(context)


class BindingPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> BindingInstance:
        """
        Build an instance of BindingInstance

        :param payload: Payload response from the API
        """
        return BindingInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Notify.V1.BindingPage>"


class BindingList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the BindingList

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to read the resource from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Bindings".format(**self._solution)

    def create(
        self,
        identity: str,
        binding_type: "BindingInstance.BindingType",
        address: str,
        tag: Union[List[str], object] = values.unset,
        notification_protocol_version: Union[str, object] = values.unset,
        credential_sid: Union[str, object] = values.unset,
        endpoint: Union[str, object] = values.unset,
    ) -> BindingInstance:
        """
        Create the BindingInstance

        :param identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service.
        :param binding_type:
        :param address: The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format.
        :param tag: A tag that can be used to select the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 20 tags.
        :param notification_protocol_version: The protocol version to use to send the notification. This defaults to the value of `default_xxxx_notification_protocol_version` for the protocol in the [Service](https://www.twilio.com/docs/notify/api/service-resource). The current version is `\\\"3\\\"` for `apn`, `fcm`, and `gcm` type Bindings. The parameter is not applicable to `sms` and `facebook-messenger` type Bindings as the data format is fixed.
        :param credential_sid: The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applies to only `apn`, `fcm`, and `gcm` type Bindings.
        :param endpoint: Deprecated.

        :returns: The created BindingInstance
        """

        data = values.of(
            {
                "Identity": identity,
                "BindingType": binding_type,
                "Address": address,
                "Tag": serialize.map(tag, lambda e: e),
                "NotificationProtocolVersion": notification_protocol_version,
                "CredentialSid": credential_sid,
                "Endpoint": endpoint,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BindingInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        identity: str,
        binding_type: "BindingInstance.BindingType",
        address: str,
        tag: Union[List[str], object] = values.unset,
        notification_protocol_version: Union[str, object] = values.unset,
        credential_sid: Union[str, object] = values.unset,
        endpoint: Union[str, object] = values.unset,
    ) -> BindingInstance:
        """
        Asynchronously create the BindingInstance

        :param identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service.
        :param binding_type:
        :param address: The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format.
        :param tag: A tag that can be used to select the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 20 tags.
        :param notification_protocol_version: The protocol version to use to send the notification. This defaults to the value of `default_xxxx_notification_protocol_version` for the protocol in the [Service](https://www.twilio.com/docs/notify/api/service-resource). The current version is `\\\"3\\\"` for `apn`, `fcm`, and `gcm` type Bindings. The parameter is not applicable to `sms` and `facebook-messenger` type Bindings as the data format is fixed.
        :param credential_sid: The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applies to only `apn`, `fcm`, and `gcm` type Bindings.
        :param endpoint: Deprecated.

        :returns: The created BindingInstance
        """

        data = values.of(
            {
                "Identity": identity,
                "BindingType": binding_type,
                "Address": address,
                "Tag": serialize.map(tag, lambda e: e),
                "NotificationProtocolVersion": notification_protocol_version,
                "CredentialSid": credential_sid,
                "Endpoint": endpoint,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BindingInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        start_date: Union[date, object] = values.unset,
        end_date: Union[date, object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        tag: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[BindingInstance]:
        """
        Streams BindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param List[str] identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
        :param List[str] tag: Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            start_date=start_date,
            end_date=end_date,
            identity=identity,
            tag=tag,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        start_date: Union[date, object] = values.unset,
        end_date: Union[date, object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        tag: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[BindingInstance]:
        """
        Asynchronously streams BindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param List[str] identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
        :param List[str] tag: Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            start_date=start_date,
            end_date=end_date,
            identity=identity,
            tag=tag,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        start_date: Union[date, object] = values.unset,
        end_date: Union[date, object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        tag: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BindingInstance]:
        """
        Lists BindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param List[str] identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
        :param List[str] tag: Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
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
                start_date=start_date,
                end_date=end_date,
                identity=identity,
                tag=tag,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        start_date: Union[date, object] = values.unset,
        end_date: Union[date, object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        tag: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BindingInstance]:
        """
        Asynchronously lists BindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param List[str] identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
        :param List[str] tag: Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
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
                start_date=start_date,
                end_date=end_date,
                identity=identity,
                tag=tag,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        start_date: Union[date, object] = values.unset,
        end_date: Union[date, object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        tag: Union[List[str], object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BindingPage:
        """
        Retrieve a single page of BindingInstance records from the API.
        Request is executed immediately

        :param start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
        :param tag: Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BindingInstance
        """
        data = values.of(
            {
                "StartDate": serialize.iso8601_date(start_date),
                "EndDate": serialize.iso8601_date(end_date),
                "Identity": serialize.map(identity, lambda e: e),
                "Tag": serialize.map(tag, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return BindingPage(self._version, response, self._solution)

    async def page_async(
        self,
        start_date: Union[date, object] = values.unset,
        end_date: Union[date, object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        tag: Union[List[str], object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BindingPage:
        """
        Asynchronously retrieve a single page of BindingInstance records from the API.
        Request is executed immediately

        :param start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
        :param identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
        :param tag: Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BindingInstance
        """
        data = values.of(
            {
                "StartDate": serialize.iso8601_date(start_date),
                "EndDate": serialize.iso8601_date(end_date),
                "Identity": serialize.map(identity, lambda e: e),
                "Tag": serialize.map(tag, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return BindingPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> BindingPage:
        """
        Retrieve a specific page of BindingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BindingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return BindingPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> BindingPage:
        """
        Asynchronously retrieve a specific page of BindingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BindingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return BindingPage(self._version, response, self._solution)

    def get(self, sid: str) -> BindingContext:
        """
        Constructs a BindingContext

        :param sid: The Twilio-provided string that uniquely identifies the Binding resource to fetch.
        """
        return BindingContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> BindingContext:
        """
        Constructs a BindingContext

        :param sid: The Twilio-provided string that uniquely identifies the Binding resource to fetch.
        """
        return BindingContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Notify.V1.BindingList>"
