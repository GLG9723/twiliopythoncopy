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
from typing import List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UserBindingInstance(InstanceResource):
    class BindingType(object):
        GCM = "gcm"
        APN = "apn"
        FCM = "fcm"

    def __init__(
        self,
        version,
        payload,
        service_sid: str,
        user_sid: str,
        sid: Optional[str] = None,
    ):
        """
        Initialize the UserBindingInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "endpoint": payload.get("endpoint"),
            "identity": payload.get("identity"),
            "user_sid": payload.get("user_sid"),
            "credential_sid": payload.get("credential_sid"),
            "binding_type": payload.get("binding_type"),
            "message_types": payload.get("message_types"),
            "url": payload.get("url"),
        }

        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[UserBindingContext] = None

    @property
    def _proxy(self) -> "UserBindingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserBindingContext for this UserBindingInstance
        """
        if self._context is None:
            self._context = UserBindingContext(
                self._version,
                service_sid=self._solution["service_sid"],
                user_sid=self._solution["user_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> str:
        """
        :returns:
        """
        return self._properties["sid"]

    @property
    def account_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["account_sid"]

    @property
    def service_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["service_sid"]

    @property
    def date_created(self) -> datetime:
        """
        :returns:
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns:
        """
        return self._properties["date_updated"]

    @property
    def endpoint(self) -> str:
        """
        :returns:
        """
        return self._properties["endpoint"]

    @property
    def identity(self) -> str:
        """
        :returns:
        """
        return self._properties["identity"]

    @property
    def user_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["user_sid"]

    @property
    def credential_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["credential_sid"]

    @property
    def binding_type(self) -> "UserBindingInstance.BindingType":
        """
        :returns:
        """
        return self._properties["binding_type"]

    @property
    def message_types(self) -> List[str]:
        """
        :returns:
        """
        return self._properties["message_types"]

    @property
    def url(self) -> str:
        """
        :returns:
        """
        return self._properties["url"]

    def delete(self) -> bool:
        """
        Deletes the UserBindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UserBindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "UserBindingInstance":
        """
        Fetch the UserBindingInstance


        :returns: The fetched UserBindingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "UserBindingInstance":
        """
        Asynchronous coroutine to fetch the UserBindingInstance


        :returns: The fetched UserBindingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.UserBindingInstance {}>".format(context)


class UserBindingContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, user_sid: str, sid: str):
        """
        Initialize the UserBindingContext

        :param version: Version that contains the resource
        :param service_sid:
        :param user_sid:
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the UserBindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UserBindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> UserBindingInstance:
        """
        Fetch the UserBindingInstance


        :returns: The fetched UserBindingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UserBindingInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> UserBindingInstance:
        """
        Asynchronous coroutine to fetch the UserBindingInstance


        :returns: The fetched UserBindingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UserBindingInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.UserBindingContext {}>".format(context)


class UserBindingPage(Page):
    def get_instance(self, payload) -> UserBindingInstance:
        """
        Build an instance of UserBindingInstance

        :param dict payload: Payload response from the API
        """
        return UserBindingInstance(
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
        return "<Twilio.IpMessaging.V2.UserBindingPage>"


class UserBindingList(ListResource):
    def __init__(self, version: Version, service_sid: str, user_sid: str):
        """
        Initialize the UserBindingList

        :param version: Version that contains the resource
        :param service_sid:
        :param user_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
        }
        self._uri = "/Services/{service_sid}/Users/{user_sid}/Bindings".format(
            **self._solution
        )

    def stream(
        self, binding_type=values.unset, limit=None, page_size=None
    ) -> List[UserBindingInstance]:
        """
        Streams UserBindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[&quot;UserBindingInstance.BindingType&quot;] binding_type:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(binding_type=binding_type, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, binding_type=values.unset, limit=None, page_size=None
    ) -> List[UserBindingInstance]:
        """
        Asynchronously streams UserBindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[&quot;UserBindingInstance.BindingType&quot;] binding_type:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            binding_type=binding_type, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self, binding_type=values.unset, limit=None, page_size=None
    ) -> List[UserBindingInstance]:
        """
        Lists UserBindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[&quot;UserBindingInstance.BindingType&quot;] binding_type:
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
                binding_type=binding_type,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self, binding_type=values.unset, limit=None, page_size=None
    ) -> List[UserBindingInstance]:
        """
        Asynchronously lists UserBindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[&quot;UserBindingInstance.BindingType&quot;] binding_type:
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
                binding_type=binding_type,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        binding_type=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> UserBindingPage:
        """
        Retrieve a single page of UserBindingInstance records from the API.
        Request is executed immediately

        :param List[&quot;UserBindingInstance.BindingType&quot;] binding_type:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserBindingInstance
        """
        data = values.of(
            {
                "BindingType": serialize.map(binding_type, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UserBindingPage(self._version, response, self._solution)

    async def page_async(
        self,
        binding_type=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> UserBindingPage:
        """
        Asynchronously retrieve a single page of UserBindingInstance records from the API.
        Request is executed immediately

        :param List[&quot;UserBindingInstance.BindingType&quot;] binding_type:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserBindingInstance
        """
        data = values.of(
            {
                "BindingType": serialize.map(binding_type, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return UserBindingPage(self._version, response, self._solution)

    def get_page(self, target_url) -> UserBindingPage:
        """
        Retrieve a specific page of UserBindingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserBindingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UserBindingPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> UserBindingPage:
        """
        Asynchronously retrieve a specific page of UserBindingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserBindingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UserBindingPage(self._version, response, self._solution)

    def get(self, sid) -> UserBindingContext:
        """
        Constructs a UserBindingContext

        :param sid:
        """
        return UserBindingContext(
            self._version,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> UserBindingContext:
        """
        Constructs a UserBindingContext

        :param sid:
        """
        return UserBindingContext(
            self._version,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V2.UserBindingList>"
