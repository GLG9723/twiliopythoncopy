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
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class MessagingConfigurationInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
    :ivar service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.
    :ivar country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.
    :ivar messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to be used to send SMS to the country of this configuration.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar url: The URL of this resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        country: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.country: Optional[str] = payload.get("country")
        self.messaging_service_sid: Optional[str] = payload.get("messaging_service_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "country": country or self.country,
        }
        self._context: Optional[MessagingConfigurationContext] = None

    @property
    def _proxy(self) -> "MessagingConfigurationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MessagingConfigurationContext for this MessagingConfigurationInstance
        """
        if self._context is None:
            self._context = MessagingConfigurationContext(
                self._version,
                service_sid=self._solution["service_sid"],
                country=self._solution["country"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the MessagingConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the MessagingConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "MessagingConfigurationInstance":
        """
        Fetch the MessagingConfigurationInstance


        :returns: The fetched MessagingConfigurationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "MessagingConfigurationInstance":
        """
        Asynchronous coroutine to fetch the MessagingConfigurationInstance


        :returns: The fetched MessagingConfigurationInstance
        """
        return await self._proxy.fetch_async()

    def update(self, messaging_service_sid: str) -> "MessagingConfigurationInstance":
        """
        Update the MessagingConfigurationInstance

        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to be used to send SMS to the country of this configuration.

        :returns: The updated MessagingConfigurationInstance
        """
        return self._proxy.update(
            messaging_service_sid=messaging_service_sid,
        )

    async def update_async(
        self, messaging_service_sid: str
    ) -> "MessagingConfigurationInstance":
        """
        Asynchronous coroutine to update the MessagingConfigurationInstance

        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to be used to send SMS to the country of this configuration.

        :returns: The updated MessagingConfigurationInstance
        """
        return await self._proxy.update_async(
            messaging_service_sid=messaging_service_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Verify.V2.MessagingConfigurationInstance {context}>"


class MessagingConfigurationContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, country: str):
        """
        Initialize the MessagingConfigurationContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.
        :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "country": country,
        }
        self._uri = "/Services/{service_sid}/MessagingConfigurations/{country}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the MessagingConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the MessagingConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> MessagingConfigurationInstance:
        """
        Fetch the MessagingConfigurationInstance


        :returns: The fetched MessagingConfigurationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return MessagingConfigurationInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            country=self._solution["country"],
        )

    async def fetch_async(self) -> MessagingConfigurationInstance:
        """
        Asynchronous coroutine to fetch the MessagingConfigurationInstance


        :returns: The fetched MessagingConfigurationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return MessagingConfigurationInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            country=self._solution["country"],
        )

    def update(self, messaging_service_sid: str) -> MessagingConfigurationInstance:
        """
        Update the MessagingConfigurationInstance

        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to be used to send SMS to the country of this configuration.

        :returns: The updated MessagingConfigurationInstance
        """
        data = values.of(
            {
                "MessagingServiceSid": messaging_service_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MessagingConfigurationInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            country=self._solution["country"],
        )

    async def update_async(
        self, messaging_service_sid: str
    ) -> MessagingConfigurationInstance:
        """
        Asynchronous coroutine to update the MessagingConfigurationInstance

        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to be used to send SMS to the country of this configuration.

        :returns: The updated MessagingConfigurationInstance
        """
        data = values.of(
            {
                "MessagingServiceSid": messaging_service_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MessagingConfigurationInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            country=self._solution["country"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Verify.V2.MessagingConfigurationContext {context}>"


class MessagingConfigurationPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> MessagingConfigurationInstance:
        """
        Build an instance of MessagingConfigurationInstance

        :param payload: Payload response from the API
        """
        return MessagingConfigurationInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.MessagingConfigurationPage>"


class MessagingConfigurationList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the MessagingConfigurationList

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/MessagingConfigurations".format(
            **self._solution
        )

    def create(
        self, country: str, messaging_service_sid: str
    ) -> MessagingConfigurationInstance:
        """
        Create the MessagingConfigurationInstance

        :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.
        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to be used to send SMS to the country of this configuration.

        :returns: The created MessagingConfigurationInstance
        """

        data = values.of(
            {
                "Country": country,
                "MessagingServiceSid": messaging_service_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MessagingConfigurationInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self, country: str, messaging_service_sid: str
    ) -> MessagingConfigurationInstance:
        """
        Asynchronously create the MessagingConfigurationInstance

        :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.
        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to be used to send SMS to the country of this configuration.

        :returns: The created MessagingConfigurationInstance
        """

        data = values.of(
            {
                "Country": country,
                "MessagingServiceSid": messaging_service_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MessagingConfigurationInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[MessagingConfigurationInstance]:
        """
        Streams MessagingConfigurationInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[MessagingConfigurationInstance]:
        """
        Asynchronously streams MessagingConfigurationInstance records from the API as a generator stream.
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
    ) -> List[MessagingConfigurationInstance]:
        """
        Lists MessagingConfigurationInstance records from the API as a list.
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
    ) -> List[MessagingConfigurationInstance]:
        """
        Asynchronously lists MessagingConfigurationInstance records from the API as a list.
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
    ) -> MessagingConfigurationPage:
        """
        Retrieve a single page of MessagingConfigurationInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MessagingConfigurationInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return MessagingConfigurationPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> MessagingConfigurationPage:
        """
        Asynchronously retrieve a single page of MessagingConfigurationInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MessagingConfigurationInstance
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
        return MessagingConfigurationPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> MessagingConfigurationPage:
        """
        Retrieve a specific page of MessagingConfigurationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MessagingConfigurationInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return MessagingConfigurationPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> MessagingConfigurationPage:
        """
        Asynchronously retrieve a specific page of MessagingConfigurationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MessagingConfigurationInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return MessagingConfigurationPage(self._version, response, self._solution)

    def get(self, country: str) -> MessagingConfigurationContext:
        """
        Constructs a MessagingConfigurationContext

        :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.
        """
        return MessagingConfigurationContext(
            self._version, service_sid=self._solution["service_sid"], country=country
        )

    def __call__(self, country: str) -> MessagingConfigurationContext:
        """
        Constructs a MessagingConfigurationContext

        :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.
        """
        return MessagingConfigurationContext(
            self._version, service_sid=self._solution["service_sid"], country=country
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.MessagingConfigurationList>"
