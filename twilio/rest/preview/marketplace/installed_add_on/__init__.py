r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension import (
    InstalledAddOnExtensionList,
)


class InstalledAddOnInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the InstalledAddOn resource. This Sid can also be found in the Console on that specific Add-ons page as the 'Available Add-on Sid'.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the InstalledAddOn resource.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar description: A short description of the Add-on's functionality.
    :ivar configuration: The JSON object that represents the current configuration of installed Add-on.
    :ivar unique_name: An application-defined string that uniquely identifies the resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the resource.
    :ivar links: The URLs of related resources.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.description: Optional[str] = payload.get("description")
        self.configuration: Optional[Dict[str, object]] = payload.get("configuration")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[InstalledAddOnContext] = None

    @property
    def _proxy(self) -> "InstalledAddOnContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InstalledAddOnContext for this InstalledAddOnInstance
        """
        if self._context is None:
            self._context = InstalledAddOnContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the InstalledAddOnInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the InstalledAddOnInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "InstalledAddOnInstance":
        """
        Fetch the InstalledAddOnInstance


        :returns: The fetched InstalledAddOnInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "InstalledAddOnInstance":
        """
        Asynchronous coroutine to fetch the InstalledAddOnInstance


        :returns: The fetched InstalledAddOnInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        configuration: Union[object, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> "InstalledAddOnInstance":
        """
        Update the InstalledAddOnInstance

        :param configuration: Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured
        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.

        :returns: The updated InstalledAddOnInstance
        """
        return self._proxy.update(
            configuration=configuration,
            unique_name=unique_name,
        )

    async def update_async(
        self,
        configuration: Union[object, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> "InstalledAddOnInstance":
        """
        Asynchronous coroutine to update the InstalledAddOnInstance

        :param configuration: Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured
        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.

        :returns: The updated InstalledAddOnInstance
        """
        return await self._proxy.update_async(
            configuration=configuration,
            unique_name=unique_name,
        )

    @property
    def extensions(self) -> InstalledAddOnExtensionList:
        """
        Access the extensions
        """
        return self._proxy.extensions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Preview.Marketplace.InstalledAddOnInstance {context}>"


class InstalledAddOnContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the InstalledAddOnContext

        :param version: Version that contains the resource
        :param sid: The SID of the InstalledAddOn resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/InstalledAddOns/{sid}".format(**self._solution)

        self._extensions: Optional[InstalledAddOnExtensionList] = None

    def delete(self) -> bool:
        """
        Deletes the InstalledAddOnInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the InstalledAddOnInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> InstalledAddOnInstance:
        """
        Fetch the InstalledAddOnInstance


        :returns: The fetched InstalledAddOnInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return InstalledAddOnInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> InstalledAddOnInstance:
        """
        Asynchronous coroutine to fetch the InstalledAddOnInstance


        :returns: The fetched InstalledAddOnInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return InstalledAddOnInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        configuration: Union[object, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> InstalledAddOnInstance:
        """
        Update the InstalledAddOnInstance

        :param configuration: Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured
        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.

        :returns: The updated InstalledAddOnInstance
        """
        data = values.of(
            {
                "Configuration": serialize.object(configuration),
                "UniqueName": unique_name,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InstalledAddOnInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        configuration: Union[object, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> InstalledAddOnInstance:
        """
        Asynchronous coroutine to update the InstalledAddOnInstance

        :param configuration: Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured
        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.

        :returns: The updated InstalledAddOnInstance
        """
        data = values.of(
            {
                "Configuration": serialize.object(configuration),
                "UniqueName": unique_name,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InstalledAddOnInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def extensions(self) -> InstalledAddOnExtensionList:
        """
        Access the extensions
        """
        if self._extensions is None:
            self._extensions = InstalledAddOnExtensionList(
                self._version,
                self._solution["sid"],
            )
        return self._extensions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Preview.Marketplace.InstalledAddOnContext {context}>"


class InstalledAddOnPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> InstalledAddOnInstance:
        """
        Build an instance of InstalledAddOnInstance

        :param payload: Payload response from the API
        """
        return InstalledAddOnInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Marketplace.InstalledAddOnPage>"


class InstalledAddOnList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InstalledAddOnList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/InstalledAddOns"

    def create(
        self,
        available_add_on_sid: str,
        accept_terms_of_service: bool,
        configuration: Union[object, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> InstalledAddOnInstance:
        """
        Create the InstalledAddOnInstance

        :param available_add_on_sid: The SID of the AvaliableAddOn to install.
        :param accept_terms_of_service: Whether the Terms of Service were accepted.
        :param configuration: The JSON object that represents the configuration of the new Add-on being installed.
        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.

        :returns: The created InstalledAddOnInstance
        """

        data = values.of(
            {
                "AvailableAddOnSid": available_add_on_sid,
                "AcceptTermsOfService": serialize.boolean_to_string(
                    accept_terms_of_service
                ),
                "Configuration": serialize.object(configuration),
                "UniqueName": unique_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InstalledAddOnInstance(self._version, payload)

    async def create_async(
        self,
        available_add_on_sid: str,
        accept_terms_of_service: bool,
        configuration: Union[object, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> InstalledAddOnInstance:
        """
        Asynchronously create the InstalledAddOnInstance

        :param available_add_on_sid: The SID of the AvaliableAddOn to install.
        :param accept_terms_of_service: Whether the Terms of Service were accepted.
        :param configuration: The JSON object that represents the configuration of the new Add-on being installed.
        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.

        :returns: The created InstalledAddOnInstance
        """

        data = values.of(
            {
                "AvailableAddOnSid": available_add_on_sid,
                "AcceptTermsOfService": serialize.boolean_to_string(
                    accept_terms_of_service
                ),
                "Configuration": serialize.object(configuration),
                "UniqueName": unique_name,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InstalledAddOnInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[InstalledAddOnInstance]:
        """
        Streams InstalledAddOnInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[InstalledAddOnInstance]:
        """
        Asynchronously streams InstalledAddOnInstance records from the API as a generator stream.
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
    ) -> List[InstalledAddOnInstance]:
        """
        Lists InstalledAddOnInstance records from the API as a list.
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
    ) -> List[InstalledAddOnInstance]:
        """
        Asynchronously lists InstalledAddOnInstance records from the API as a list.
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
    ) -> InstalledAddOnPage:
        """
        Retrieve a single page of InstalledAddOnInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InstalledAddOnInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InstalledAddOnPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InstalledAddOnPage:
        """
        Asynchronously retrieve a single page of InstalledAddOnInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InstalledAddOnInstance
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
        return InstalledAddOnPage(self._version, response)

    def get_page(self, target_url: str) -> InstalledAddOnPage:
        """
        Retrieve a specific page of InstalledAddOnInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InstalledAddOnInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InstalledAddOnPage(self._version, response)

    async def get_page_async(self, target_url: str) -> InstalledAddOnPage:
        """
        Asynchronously retrieve a specific page of InstalledAddOnInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InstalledAddOnInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InstalledAddOnPage(self._version, response)

    def get(self, sid: str) -> InstalledAddOnContext:
        """
        Constructs a InstalledAddOnContext

        :param sid: The SID of the InstalledAddOn resource to update.
        """
        return InstalledAddOnContext(self._version, sid=sid)

    def __call__(self, sid: str) -> InstalledAddOnContext:
        """
        Constructs a InstalledAddOnContext

        :param sid: The SID of the InstalledAddOn resource to update.
        """
        return InstalledAddOnContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Marketplace.InstalledAddOnList>"
