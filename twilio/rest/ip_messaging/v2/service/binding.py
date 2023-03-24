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


class BindingInstance(InstanceResource):
    class BindingType(object):
        GCM = "gcm"
        APN = "apn"
        FCM = "fcm"

    """
    :ivar sid: 
    :ivar account_sid: 
    :ivar service_sid: 
    :ivar date_created: 
    :ivar date_updated: 
    :ivar endpoint: 
    :ivar identity: 
    :ivar credential_sid: 
    :ivar binding_type: 
    :ivar message_types: 
    :ivar url: 
    :ivar links: 
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
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.endpoint: Optional[str] = payload.get("endpoint")
        self.identity: Optional[str] = payload.get("identity")
        self.credential_sid: Optional[str] = payload.get("credential_sid")
        self.binding_type: Optional["BindingInstance.BindingType"] = payload.get(
            "binding_type"
        )
        self.message_types: Optional[List[str]] = payload.get("message_types")
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
        return "<Twilio.IpMessaging.V2.BindingInstance {}>".format(context)


class BindingContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the BindingContext

        :param version: Version that contains the resource
        :param service_sid:
        :param sid:
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
        return "<Twilio.IpMessaging.V2.BindingContext {}>".format(context)


class BindingPage(Page):
    def get_instance(self, payload) -> BindingInstance:
        """
        Build an instance of BindingInstance

        :param dict payload: Payload response from the API
        """
        return BindingInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V2.BindingPage>"


class BindingList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the BindingList

        :param version: Version that contains the resource
        :param service_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Bindings".format(**self._solution)

    def stream(
        self,
        binding_type=values.unset,
        identity=values.unset,
        limit=None,
        page_size=None,
    ) -> List[BindingInstance]:
        """
        Streams BindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[&quot;BindingInstance.BindingType&quot;] binding_type:
        :param List[str] identity:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            binding_type=binding_type, identity=identity, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        binding_type=values.unset,
        identity=values.unset,
        limit=None,
        page_size=None,
    ) -> List[BindingInstance]:
        """
        Asynchronously streams BindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[&quot;BindingInstance.BindingType&quot;] binding_type:
        :param List[str] identity:
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
            binding_type=binding_type, identity=identity, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        binding_type=values.unset,
        identity=values.unset,
        limit=None,
        page_size=None,
    ) -> List[BindingInstance]:
        """
        Lists BindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[&quot;BindingInstance.BindingType&quot;] binding_type:
        :param List[str] identity:
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
                identity=identity,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        binding_type=values.unset,
        identity=values.unset,
        limit=None,
        page_size=None,
    ) -> List[BindingInstance]:
        """
        Asynchronously lists BindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[&quot;BindingInstance.BindingType&quot;] binding_type:
        :param List[str] identity:
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
                identity=identity,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        binding_type=values.unset,
        identity=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> BindingPage:
        """
        Retrieve a single page of BindingInstance records from the API.
        Request is executed immediately

        :param List[&quot;BindingInstance.BindingType&quot;] binding_type:
        :param List[str] identity:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BindingInstance
        """
        data = values.of(
            {
                "BindingType": serialize.map(binding_type, lambda e: e),
                "Identity": serialize.map(identity, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return BindingPage(self._version, response, self._solution)

    async def page_async(
        self,
        binding_type=values.unset,
        identity=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> BindingPage:
        """
        Asynchronously retrieve a single page of BindingInstance records from the API.
        Request is executed immediately

        :param List[&quot;BindingInstance.BindingType&quot;] binding_type:
        :param List[str] identity:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BindingInstance
        """
        data = values.of(
            {
                "BindingType": serialize.map(binding_type, lambda e: e),
                "Identity": serialize.map(identity, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return BindingPage(self._version, response, self._solution)

    def get_page(self, target_url) -> BindingPage:
        """
        Retrieve a specific page of BindingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BindingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return BindingPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> BindingPage:
        """
        Asynchronously retrieve a specific page of BindingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BindingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return BindingPage(self._version, response, self._solution)

    def get(self, sid) -> BindingContext:
        """
        Constructs a BindingContext

        :param sid:
        """
        return BindingContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid) -> BindingContext:
        """
        Constructs a BindingContext

        :param sid:
        """
        return BindingContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V2.BindingList>"
