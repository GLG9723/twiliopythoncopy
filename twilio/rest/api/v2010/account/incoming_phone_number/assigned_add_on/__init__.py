r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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
from twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension import (
    AssignedAddOnExtensionList,
)


class AssignedAddOnInstance(InstanceResource):
    """
    :ivar sid: The unique string that that we created to identify the resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource.
    :ivar resource_sid: The SID of the Phone Number to which the Add-on is assigned.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar description: A short description of the functionality that the Add-on provides.
    :ivar configuration: A JSON string that represents the current configuration of this Add-on installation.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar uri: The URI of the resource, relative to `https://api.twilio.com`.
    :ivar subresource_uris: A list of related resources identified by their relative URIs.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        resource_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.resource_sid: Optional[str] = payload.get("resource_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.description: Optional[str] = payload.get("description")
        self.configuration: Optional[Dict[str, object]] = payload.get("configuration")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.uri: Optional[str] = payload.get("uri")
        self.subresource_uris: Optional[Dict[str, object]] = payload.get(
            "subresource_uris"
        )

        self._solution = {
            "account_sid": account_sid,
            "resource_sid": resource_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[AssignedAddOnContext] = None

    @property
    def _proxy(self) -> "AssignedAddOnContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssignedAddOnContext for this AssignedAddOnInstance
        """
        if self._context is None:
            self._context = AssignedAddOnContext(
                self._version,
                account_sid=self._solution["account_sid"],
                resource_sid=self._solution["resource_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the AssignedAddOnInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AssignedAddOnInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "AssignedAddOnInstance":
        """
        Fetch the AssignedAddOnInstance


        :returns: The fetched AssignedAddOnInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AssignedAddOnInstance":
        """
        Asynchronous coroutine to fetch the AssignedAddOnInstance


        :returns: The fetched AssignedAddOnInstance
        """
        return await self._proxy.fetch_async()

    @property
    def extensions(self) -> AssignedAddOnExtensionList:
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
        return f"<Twilio.Api.V2010.AssignedAddOnInstance {context}>"


class AssignedAddOnContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, resource_sid: str, sid: str):
        """
        Initialize the AssignedAddOnContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.
        :param resource_sid: The SID of the Phone Number to which the Add-on is assigned.
        :param sid: The Twilio-provided string that uniquely identifies the resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "resource_sid": resource_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{sid}.json".format(
            **self._solution
        )

        self._extensions: Optional[AssignedAddOnExtensionList] = None

    def delete(self) -> bool:
        """
        Deletes the AssignedAddOnInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AssignedAddOnInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> AssignedAddOnInstance:
        """
        Fetch the AssignedAddOnInstance


        :returns: The fetched AssignedAddOnInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AssignedAddOnInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AssignedAddOnInstance:
        """
        Asynchronous coroutine to fetch the AssignedAddOnInstance


        :returns: The fetched AssignedAddOnInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AssignedAddOnInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
            sid=self._solution["sid"],
        )

    @property
    def extensions(self) -> AssignedAddOnExtensionList:
        """
        Access the extensions
        """
        if self._extensions is None:
            self._extensions = AssignedAddOnExtensionList(
                self._version,
                self._solution["account_sid"],
                self._solution["resource_sid"],
                self._solution["sid"],
            )
        return self._extensions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Api.V2010.AssignedAddOnContext {context}>"


class AssignedAddOnPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> AssignedAddOnInstance:
        """
        Build an instance of AssignedAddOnInstance

        :param payload: Payload response from the API
        """
        return AssignedAddOnInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AssignedAddOnPage>"


class AssignedAddOnList(ListResource):

    def __init__(self, version: Version, account_sid: str, resource_sid: str):
        """
        Initialize the AssignedAddOnList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
        :param resource_sid: The SID of the Phone Number to which the Add-on is assigned.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "resource_sid": resource_sid,
        }
        self._uri = "/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns.json".format(
            **self._solution
        )

    def create(self, installed_add_on_sid: str) -> AssignedAddOnInstance:
        """
        Create the AssignedAddOnInstance

        :param installed_add_on_sid: The SID that identifies the Add-on installation.

        :returns: The created AssignedAddOnInstance
        """

        data = values.of(
            {
                "InstalledAddOnSid": installed_add_on_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssignedAddOnInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
        )

    async def create_async(self, installed_add_on_sid: str) -> AssignedAddOnInstance:
        """
        Asynchronously create the AssignedAddOnInstance

        :param installed_add_on_sid: The SID that identifies the Add-on installation.

        :returns: The created AssignedAddOnInstance
        """

        data = values.of(
            {
                "InstalledAddOnSid": installed_add_on_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssignedAddOnInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[AssignedAddOnInstance]:
        """
        Streams AssignedAddOnInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[AssignedAddOnInstance]:
        """
        Asynchronously streams AssignedAddOnInstance records from the API as a generator stream.
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
    ) -> List[AssignedAddOnInstance]:
        """
        Lists AssignedAddOnInstance records from the API as a list.
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
    ) -> List[AssignedAddOnInstance]:
        """
        Asynchronously lists AssignedAddOnInstance records from the API as a list.
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
    ) -> AssignedAddOnPage:
        """
        Retrieve a single page of AssignedAddOnInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssignedAddOnInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AssignedAddOnPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AssignedAddOnPage:
        """
        Asynchronously retrieve a single page of AssignedAddOnInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssignedAddOnInstance
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
        return AssignedAddOnPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> AssignedAddOnPage:
        """
        Retrieve a specific page of AssignedAddOnInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssignedAddOnInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AssignedAddOnPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> AssignedAddOnPage:
        """
        Asynchronously retrieve a specific page of AssignedAddOnInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssignedAddOnInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AssignedAddOnPage(self._version, response, self._solution)

    def get(self, sid: str) -> AssignedAddOnContext:
        """
        Constructs a AssignedAddOnContext

        :param sid: The Twilio-provided string that uniquely identifies the resource to fetch.
        """
        return AssignedAddOnContext(
            self._version,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> AssignedAddOnContext:
        """
        Constructs a AssignedAddOnContext

        :param sid: The Twilio-provided string that uniquely identifies the resource to fetch.
        """
        return AssignedAddOnContext(
            self._version,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AssignedAddOnList>"
