r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SourceIpMappingInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the IP Record resource.
    :ivar ip_record_sid: The Twilio-provided string that uniquely identifies the IP Record resource to map from.
    :ivar sip_domain_sid: The SID of the SIP Domain that the IP Record is mapped to.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.ip_record_sid: Optional[str] = payload.get("ip_record_sid")
        self.sip_domain_sid: Optional[str] = payload.get("sip_domain_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[SourceIpMappingContext] = None

    @property
    def _proxy(self) -> "SourceIpMappingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SourceIpMappingContext for this SourceIpMappingInstance
        """
        if self._context is None:
            self._context = SourceIpMappingContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the SourceIpMappingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SourceIpMappingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "SourceIpMappingInstance":
        """
        Fetch the SourceIpMappingInstance


        :returns: The fetched SourceIpMappingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SourceIpMappingInstance":
        """
        Asynchronous coroutine to fetch the SourceIpMappingInstance


        :returns: The fetched SourceIpMappingInstance
        """
        return await self._proxy.fetch_async()

    def update(self, sip_domain_sid: str) -> "SourceIpMappingInstance":
        """
        Update the SourceIpMappingInstance

        :param sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.

        :returns: The updated SourceIpMappingInstance
        """
        return self._proxy.update(
            sip_domain_sid=sip_domain_sid,
        )

    async def update_async(self, sip_domain_sid: str) -> "SourceIpMappingInstance":
        """
        Asynchronous coroutine to update the SourceIpMappingInstance

        :param sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.

        :returns: The updated SourceIpMappingInstance
        """
        return await self._proxy.update_async(
            sip_domain_sid=sip_domain_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Voice.V1.SourceIpMappingInstance {context}>"


class SourceIpMappingContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the SourceIpMappingContext

        :param version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the IP Record resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/SourceIpMappings/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the SourceIpMappingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SourceIpMappingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> SourceIpMappingInstance:
        """
        Fetch the SourceIpMappingInstance


        :returns: The fetched SourceIpMappingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SourceIpMappingInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SourceIpMappingInstance:
        """
        Asynchronous coroutine to fetch the SourceIpMappingInstance


        :returns: The fetched SourceIpMappingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SourceIpMappingInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(self, sip_domain_sid: str) -> SourceIpMappingInstance:
        """
        Update the SourceIpMappingInstance

        :param sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.

        :returns: The updated SourceIpMappingInstance
        """
        data = values.of(
            {
                "SipDomainSid": sip_domain_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SourceIpMappingInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    async def update_async(self, sip_domain_sid: str) -> SourceIpMappingInstance:
        """
        Asynchronous coroutine to update the SourceIpMappingInstance

        :param sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.

        :returns: The updated SourceIpMappingInstance
        """
        data = values.of(
            {
                "SipDomainSid": sip_domain_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SourceIpMappingInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Voice.V1.SourceIpMappingContext {context}>"


class SourceIpMappingPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> SourceIpMappingInstance:
        """
        Build an instance of SourceIpMappingInstance

        :param payload: Payload response from the API
        """
        return SourceIpMappingInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Voice.V1.SourceIpMappingPage>"


class SourceIpMappingList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SourceIpMappingList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/SourceIpMappings"

    def create(
        self, ip_record_sid: str, sip_domain_sid: str
    ) -> SourceIpMappingInstance:
        """
        Create the SourceIpMappingInstance

        :param ip_record_sid: The Twilio-provided string that uniquely identifies the IP Record resource to map from.
        :param sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.

        :returns: The created SourceIpMappingInstance
        """

        data = values.of(
            {
                "IpRecordSid": ip_record_sid,
                "SipDomainSid": sip_domain_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SourceIpMappingInstance(self._version, payload)

    async def create_async(
        self, ip_record_sid: str, sip_domain_sid: str
    ) -> SourceIpMappingInstance:
        """
        Asynchronously create the SourceIpMappingInstance

        :param ip_record_sid: The Twilio-provided string that uniquely identifies the IP Record resource to map from.
        :param sip_domain_sid: The SID of the SIP Domain that the IP Record should be mapped to.

        :returns: The created SourceIpMappingInstance
        """

        data = values.of(
            {
                "IpRecordSid": ip_record_sid,
                "SipDomainSid": sip_domain_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SourceIpMappingInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SourceIpMappingInstance]:
        """
        Streams SourceIpMappingInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[SourceIpMappingInstance]:
        """
        Asynchronously streams SourceIpMappingInstance records from the API as a generator stream.
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

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SourceIpMappingInstance]:
        """
        Lists SourceIpMappingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SourceIpMappingInstance]:
        """
        Asynchronously lists SourceIpMappingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SourceIpMappingPage:
        """
        Retrieve a single page of SourceIpMappingInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SourceIpMappingInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SourceIpMappingPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SourceIpMappingPage:
        """
        Asynchronously retrieve a single page of SourceIpMappingInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SourceIpMappingInstance
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
        return SourceIpMappingPage(self._version, response)

    def get_page(self, target_url: str) -> SourceIpMappingPage:
        """
        Retrieve a specific page of SourceIpMappingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SourceIpMappingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SourceIpMappingPage(self._version, response)

    async def get_page_async(self, target_url: str) -> SourceIpMappingPage:
        """
        Asynchronously retrieve a specific page of SourceIpMappingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SourceIpMappingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SourceIpMappingPage(self._version, response)

    def get(self, sid: str) -> SourceIpMappingContext:
        """
        Constructs a SourceIpMappingContext

        :param sid: The Twilio-provided string that uniquely identifies the IP Record resource to update.
        """
        return SourceIpMappingContext(self._version, sid=sid)

    def __call__(self, sid: str) -> SourceIpMappingContext:
        """
        Constructs a SourceIpMappingContext

        :param sid: The Twilio-provided string that uniquely identifies the IP Record resource to update.
        """
        return SourceIpMappingContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Voice.V1.SourceIpMappingList>"
