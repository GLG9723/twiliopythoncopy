r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
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


class RoleInstance(InstanceResource):
    class RoleType(object):
        CHANNEL = "channel"
        DEPLOYMENT = "deployment"

    def __init__(self, version, payload, service_sid: str, sid: Optional[str] = None):
        """
        Initialize the RoleInstance
        """
        super().__init__(version)

        self._sid: Optional[str] = payload.get("sid")
        self._account_sid: Optional[str] = payload.get("account_sid")
        self._service_sid: Optional[str] = payload.get("service_sid")
        self._friendly_name: Optional[str] = payload.get("friendly_name")
        self._type: Optional["RoleInstance.RoleType"] = payload.get("type")
        self._permissions: Optional[List[str]] = payload.get("permissions")
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self._url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self._sid,
        }
        self._context: Optional[RoleContext] = None

    @property
    def _proxy(self) -> "RoleContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RoleContext for this RoleInstance
        """
        if self._context is None:
            self._context = RoleContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that we created to identify the Role resource.
        """
        return self._sid

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Role resource.
        """
        return self._account_sid

    @property
    def service_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Role resource is associated with.
        """
        return self._service_sid

    @property
    def friendly_name(self) -> Optional[str]:
        """
        :returns: The string that you assigned to describe the resource.
        """
        return self._friendly_name

    @property
    def type(self) -> Optional["RoleInstance.RoleType"]:
        return self._type

    @property
    def permissions(self) -> Optional[List[str]]:
        """
        :returns: An array of the permissions the role has been granted.
        """
        return self._permissions

    @property
    def date_created(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        """
        return self._date_created

    @property
    def date_updated(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        """
        return self._date_updated

    @property
    def url(self) -> Optional[str]:
        """
        :returns: The absolute URL of the Role resource.
        """
        return self._url

    def delete(self) -> bool:
        """
        Deletes the RoleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RoleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "RoleInstance":
        """
        Fetch the RoleInstance


        :returns: The fetched RoleInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RoleInstance":
        """
        Asynchronous coroutine to fetch the RoleInstance


        :returns: The fetched RoleInstance
        """
        return await self._proxy.fetch_async()

    def update(self, permission) -> "RoleInstance":
        """
        Update the RoleInstance

        :param List[str] permission: A permission that you grant to the role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. Note that the update action replaces all previously assigned permissions with those defined in the update action. To remove a permission, do not include it in the subsequent update action. The values for this parameter depend on the role's `type`.

        :returns: The updated RoleInstance
        """
        return self._proxy.update(
            permission=permission,
        )

    async def update_async(self, permission) -> "RoleInstance":
        """
        Asynchronous coroutine to update the RoleInstance

        :param List[str] permission: A permission that you grant to the role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. Note that the update action replaces all previously assigned permissions with those defined in the update action. To remove a permission, do not include it in the subsequent update action. The values for this parameter depend on the role's `type`.

        :returns: The updated RoleInstance
        """
        return await self._proxy.update_async(
            permission=permission,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Chat.V2.RoleInstance {}>".format(context)


class RoleContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the RoleContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Role resource in.
        :param sid: The SID of the Role resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Roles/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the RoleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RoleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> RoleInstance:
        """
        Fetch the RoleInstance


        :returns: The fetched RoleInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> RoleInstance:
        """
        Asynchronous coroutine to fetch the RoleInstance


        :returns: The fetched RoleInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(self, permission) -> RoleInstance:
        """
        Update the RoleInstance

        :param List[str] permission: A permission that you grant to the role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. Note that the update action replaces all previously assigned permissions with those defined in the update action. To remove a permission, do not include it in the subsequent update action. The values for this parameter depend on the role's `type`.

        :returns: The updated RoleInstance
        """
        data = values.of(
            {
                "Permission": serialize.map(permission, lambda e: e),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(self, permission) -> RoleInstance:
        """
        Asynchronous coroutine to update the RoleInstance

        :param List[str] permission: A permission that you grant to the role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. Note that the update action replaces all previously assigned permissions with those defined in the update action. To remove a permission, do not include it in the subsequent update action. The values for this parameter depend on the role's `type`.

        :returns: The updated RoleInstance
        """
        data = values.of(
            {
                "Permission": serialize.map(permission, lambda e: e),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoleInstance(
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
        return "<Twilio.Chat.V2.RoleContext {}>".format(context)


class RolePage(Page):
    def get_instance(self, payload) -> RoleInstance:
        """
        Build an instance of RoleInstance

        :param dict payload: Payload response from the API
        """
        return RoleInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Chat.V2.RolePage>"


class RoleList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the RoleList

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Role resources from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Roles".format(**self._solution)

    def create(self, friendly_name, type, permission) -> RoleInstance:
        """
        Create the RoleInstance

        :param str friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
        :param &quot;RoleInstance.RoleType&quot; type:
        :param List[str] permission: A permission that you grant to the new role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. The values for this parameter depend on the role's `type`.

        :returns: The created RoleInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Type": type,
                "Permission": serialize.map(permission, lambda e: e),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoleInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(self, friendly_name, type, permission) -> RoleInstance:
        """
        Asynchronously create the RoleInstance

        :param str friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
        :param &quot;RoleInstance.RoleType&quot; type:
        :param List[str] permission: A permission that you grant to the new role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. The values for this parameter depend on the role's `type`.

        :returns: The created RoleInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Type": type,
                "Permission": serialize.map(permission, lambda e: e),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoleInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(self, limit=None, page_size=None) -> List[RoleInstance]:
        """
        Streams RoleInstance records from the API as a generator stream.
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

    async def stream_async(self, limit=None, page_size=None) -> List[RoleInstance]:
        """
        Asynchronously streams RoleInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[RoleInstance]:
        """
        Lists RoleInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[RoleInstance]:
        """
        Asynchronously lists RoleInstance records from the API as a list.
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
    ) -> RolePage:
        """
        Retrieve a single page of RoleInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoleInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return RolePage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> RolePage:
        """
        Asynchronously retrieve a single page of RoleInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoleInstance
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
        return RolePage(self._version, response, self._solution)

    def get_page(self, target_url) -> RolePage:
        """
        Retrieve a specific page of RoleInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoleInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RolePage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> RolePage:
        """
        Asynchronously retrieve a specific page of RoleInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoleInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RolePage(self._version, response, self._solution)

    def get(self, sid) -> RoleContext:
        """
        Constructs a RoleContext

        :param sid: The SID of the Role resource to update.
        """
        return RoleContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid) -> RoleContext:
        """
        Constructs a RoleContext

        :param sid: The SID of the Role resource to update.
        """
        return RoleContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Chat.V2.RoleList>"
