r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.conversations.v1.service.binding import BindingList
from twilio.rest.conversations.v1.service.configuration import ConfigurationList
from twilio.rest.conversations.v1.service.conversation import ConversationList
from twilio.rest.conversations.v1.service.participant_conversation import (
    ParticipantConversationList,
)
from twilio.rest.conversations.v1.service.role import RoleList
from twilio.rest.conversations.v1.service.user import UserList


class ServiceInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the ServiceInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "sid": payload.get("sid"),
            "friendly_name": payload.get("friendly_name"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[ServiceContext] = None

    @property
    def _proxy(self) -> "ServiceContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        """
        if self._context is None:
            self._context = ServiceContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self) -> str:
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this service.
        """
        return self._properties["account_sid"]

    @property
    def sid(self) -> str:
        """
        :returns: A 34 character string that uniquely identifies this resource.
        """
        return self._properties["sid"]

    @property
    def friendly_name(self) -> str:
        """
        :returns: The human-readable name of this service, limited to 256 characters. Optional.
        """
        return self._properties["friendly_name"]

    @property
    def date_created(self) -> datetime:
        """
        :returns: The date that this resource was created.
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns: The date that this resource was last updated.
        """
        return self._properties["date_updated"]

    @property
    def url(self) -> str:
        """
        :returns: An absolute API resource URL for this service.
        """
        return self._properties["url"]

    @property
    def links(self) -> Dict[str, object]:
        """
        :returns: Contains absolute API resource URLs to access conversations, users, roles, bindings and configuration of this service.
        """
        return self._properties["links"]

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ServiceInstance":
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ServiceInstance":
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return await self._proxy.fetch_async()

    @property
    def bindings(self) -> BindingList:
        """
        Access the bindings
        """
        return self._proxy.bindings

    @property
    def configuration(self) -> ConfigurationList:
        """
        Access the configuration
        """
        return self._proxy.configuration

    @property
    def conversations(self) -> ConversationList:
        """
        Access the conversations
        """
        return self._proxy.conversations

    @property
    def participant_conversations(self) -> ParticipantConversationList:
        """
        Access the participant_conversations
        """
        return self._proxy.participant_conversations

    @property
    def roles(self) -> RoleList:
        """
        Access the roles
        """
        return self._proxy.roles

    @property
    def users(self) -> UserList:
        """
        Access the users
        """
        return self._proxy.users

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.ServiceInstance {}>".format(context)


class ServiceContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Services/{sid}".format(**self._solution)

        self._bindings: Optional[BindingList] = None
        self._configuration: Optional[ConfigurationList] = None
        self._conversations: Optional[ConversationList] = None
        self._participant_conversations: Optional[ParticipantConversationList] = None
        self._roles: Optional[RoleList] = None
        self._users: Optional[UserList] = None

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ServiceInstance:
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ServiceInstance:
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    @property
    def bindings(self) -> BindingList:
        """
        Access the bindings
        """
        if self._bindings is None:
            self._bindings = BindingList(
                self._version,
                self._solution["sid"],
            )
        return self._bindings

    @property
    def configuration(self) -> ConfigurationList:
        """
        Access the configuration
        """
        if self._configuration is None:
            self._configuration = ConfigurationList(
                self._version,
                self._solution["sid"],
            )
        return self._configuration

    @property
    def conversations(self) -> ConversationList:
        """
        Access the conversations
        """
        if self._conversations is None:
            self._conversations = ConversationList(
                self._version,
                self._solution["sid"],
            )
        return self._conversations

    @property
    def participant_conversations(self) -> ParticipantConversationList:
        """
        Access the participant_conversations
        """
        if self._participant_conversations is None:
            self._participant_conversations = ParticipantConversationList(
                self._version,
                self._solution["sid"],
            )
        return self._participant_conversations

    @property
    def roles(self) -> RoleList:
        """
        Access the roles
        """
        if self._roles is None:
            self._roles = RoleList(
                self._version,
                self._solution["sid"],
            )
        return self._roles

    @property
    def users(self) -> UserList:
        """
        Access the users
        """
        if self._users is None:
            self._users = UserList(
                self._version,
                self._solution["sid"],
            )
        return self._users

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.ServiceContext {}>".format(context)


class ServicePage(Page):
    def get_instance(self, payload) -> ServiceInstance:
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.ServicePage>"


class ServiceList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Services"

    def create(self, friendly_name) -> ServiceInstance:
        """
        Create the ServiceInstance

        :param str friendly_name: The human-readable name of this service, limited to 256 characters. Optional.

        :returns: The created ServiceInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    async def create_async(self, friendly_name) -> ServiceInstance:
        """
        Asynchronously create the ServiceInstance

        :param str friendly_name: The human-readable name of this service, limited to 256 characters. Optional.

        :returns: The created ServiceInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    def stream(self, limit=None, page_size=None) -> List[ServiceInstance]:
        """
        Streams ServiceInstance records from the API as a generator stream.
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

    async def stream_async(self, limit=None, page_size=None) -> List[ServiceInstance]:
        """
        Asynchronously streams ServiceInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[ServiceInstance]:
        """
        Lists ServiceInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[ServiceInstance]:
        """
        Asynchronously lists ServiceInstance records from the API as a list.
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
    ) -> ServicePage:
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ServicePage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> ServicePage:
        """
        Asynchronously retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
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
        return ServicePage(self._version, response)

    def get_page(self, target_url) -> ServicePage:
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ServicePage(self._version, response)

    async def get_page_async(self, target_url) -> ServicePage:
        """
        Asynchronously retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ServicePage(self._version, response)

    def get(self, sid) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.ServiceList>"
