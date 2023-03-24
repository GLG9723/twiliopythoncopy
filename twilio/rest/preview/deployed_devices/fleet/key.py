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
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class KeyInstance(InstanceResource):

    """
    :ivar sid: Contains a 34 character string that uniquely identifies this Key credential resource.
    :ivar url: Contains an absolute URL for this Key credential resource.
    :ivar friendly_name: Contains a human readable descriptive text for this Key credential, up to 256 characters long.
    :ivar fleet_sid: Specifies the unique string identifier of the Fleet that the given Key credential belongs to.
    :ivar account_sid: Specifies the unique string identifier of the Account responsible for this Key credential.
    :ivar device_sid: Specifies the unique string identifier of a Device authenticated with this Key credential.
    :ivar secret: Contains the automatically generated secret belonging to this Key credential, used to authenticate the Device.
    :ivar date_created: Specifies the date this Key credential was created, given in UTC ISO 8601 format.
    :ivar date_updated: Specifies the date this Key credential was last updated, given in UTC ISO 8601 format.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        fleet_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.url: Optional[str] = payload.get("url")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.fleet_sid: Optional[str] = payload.get("fleet_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.device_sid: Optional[str] = payload.get("device_sid")
        self.secret: Optional[str] = payload.get("secret")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )

        self._solution = {
            "fleet_sid": fleet_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[KeyContext] = None

    @property
    def _proxy(self) -> "KeyContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: KeyContext for this KeyInstance
        """
        if self._context is None:
            self._context = KeyContext(
                self._version,
                fleet_sid=self._solution["fleet_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the KeyInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the KeyInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "KeyInstance":
        """
        Fetch the KeyInstance


        :returns: The fetched KeyInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "KeyInstance":
        """
        Asynchronous coroutine to fetch the KeyInstance


        :returns: The fetched KeyInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, friendly_name=values.unset, device_sid=values.unset
    ) -> "KeyInstance":
        """
        Update the KeyInstance

        :param str friendly_name: Provides a human readable descriptive text for this Key credential, up to 256 characters long.
        :param str device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Key credential.

        :returns: The updated KeyInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            device_sid=device_sid,
        )

    async def update_async(
        self, friendly_name=values.unset, device_sid=values.unset
    ) -> "KeyInstance":
        """
        Asynchronous coroutine to update the KeyInstance

        :param str friendly_name: Provides a human readable descriptive text for this Key credential, up to 256 characters long.
        :param str device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Key credential.

        :returns: The updated KeyInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            device_sid=device_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.DeployedDevices.KeyInstance {}>".format(context)


class KeyContext(InstanceContext):
    def __init__(self, version: Version, fleet_sid: str, sid: str):
        """
        Initialize the KeyContext

        :param version: Version that contains the resource
        :param fleet_sid:
        :param sid: Provides a 34 character string that uniquely identifies the requested Key credential resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "fleet_sid": fleet_sid,
            "sid": sid,
        }
        self._uri = "/Fleets/{fleet_sid}/Keys/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the KeyInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the KeyInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> KeyInstance:
        """
        Fetch the KeyInstance


        :returns: The fetched KeyInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return KeyInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> KeyInstance:
        """
        Asynchronous coroutine to fetch the KeyInstance


        :returns: The fetched KeyInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return KeyInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self, friendly_name=values.unset, device_sid=values.unset
    ) -> KeyInstance:
        """
        Update the KeyInstance

        :param str friendly_name: Provides a human readable descriptive text for this Key credential, up to 256 characters long.
        :param str device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Key credential.

        :returns: The updated KeyInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DeviceSid": device_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return KeyInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, friendly_name=values.unset, device_sid=values.unset
    ) -> KeyInstance:
        """
        Asynchronous coroutine to update the KeyInstance

        :param str friendly_name: Provides a human readable descriptive text for this Key credential, up to 256 characters long.
        :param str device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Key credential.

        :returns: The updated KeyInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DeviceSid": device_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return KeyInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.DeployedDevices.KeyContext {}>".format(context)


class KeyPage(Page):
    def get_instance(self, payload) -> KeyInstance:
        """
        Build an instance of KeyInstance

        :param dict payload: Payload response from the API
        """
        return KeyInstance(
            self._version, payload, fleet_sid=self._solution["fleet_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.DeployedDevices.KeyPage>"


class KeyList(ListResource):
    def __init__(self, version: Version, fleet_sid: str):
        """
        Initialize the KeyList

        :param version: Version that contains the resource
        :param fleet_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "fleet_sid": fleet_sid,
        }
        self._uri = "/Fleets/{fleet_sid}/Keys".format(**self._solution)

    def create(
        self, friendly_name=values.unset, device_sid=values.unset
    ) -> KeyInstance:
        """
        Create the KeyInstance

        :param str friendly_name: Provides a human readable descriptive text for this Key credential, up to 256 characters long.
        :param str device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Key credential.

        :returns: The created KeyInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DeviceSid": device_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return KeyInstance(
            self._version, payload, fleet_sid=self._solution["fleet_sid"]
        )

    async def create_async(
        self, friendly_name=values.unset, device_sid=values.unset
    ) -> KeyInstance:
        """
        Asynchronously create the KeyInstance

        :param str friendly_name: Provides a human readable descriptive text for this Key credential, up to 256 characters long.
        :param str device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Key credential.

        :returns: The created KeyInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DeviceSid": device_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return KeyInstance(
            self._version, payload, fleet_sid=self._solution["fleet_sid"]
        )

    def stream(
        self, device_sid=values.unset, limit=None, page_size=None
    ) -> List[KeyInstance]:
        """
        Streams KeyInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str device_sid: Filters the resulting list of Keys by a unique string identifier of an authenticated Device.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(device_sid=device_sid, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, device_sid=values.unset, limit=None, page_size=None
    ) -> List[KeyInstance]:
        """
        Asynchronously streams KeyInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str device_sid: Filters the resulting list of Keys by a unique string identifier of an authenticated Device.
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
            device_sid=device_sid, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self, device_sid=values.unset, limit=None, page_size=None
    ) -> List[KeyInstance]:
        """
        Lists KeyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str device_sid: Filters the resulting list of Keys by a unique string identifier of an authenticated Device.
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
                device_sid=device_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self, device_sid=values.unset, limit=None, page_size=None
    ) -> List[KeyInstance]:
        """
        Asynchronously lists KeyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str device_sid: Filters the resulting list of Keys by a unique string identifier of an authenticated Device.
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
                device_sid=device_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        device_sid=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> KeyPage:
        """
        Retrieve a single page of KeyInstance records from the API.
        Request is executed immediately

        :param str device_sid: Filters the resulting list of Keys by a unique string identifier of an authenticated Device.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of KeyInstance
        """
        data = values.of(
            {
                "DeviceSid": device_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return KeyPage(self._version, response, self._solution)

    async def page_async(
        self,
        device_sid=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> KeyPage:
        """
        Asynchronously retrieve a single page of KeyInstance records from the API.
        Request is executed immediately

        :param str device_sid: Filters the resulting list of Keys by a unique string identifier of an authenticated Device.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of KeyInstance
        """
        data = values.of(
            {
                "DeviceSid": device_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return KeyPage(self._version, response, self._solution)

    def get_page(self, target_url) -> KeyPage:
        """
        Retrieve a specific page of KeyInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of KeyInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return KeyPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> KeyPage:
        """
        Asynchronously retrieve a specific page of KeyInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of KeyInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return KeyPage(self._version, response, self._solution)

    def get(self, sid) -> KeyContext:
        """
        Constructs a KeyContext

        :param sid: Provides a 34 character string that uniquely identifies the requested Key credential resource.
        """
        return KeyContext(self._version, fleet_sid=self._solution["fleet_sid"], sid=sid)

    def __call__(self, sid) -> KeyContext:
        """
        Constructs a KeyContext

        :param sid: Provides a 34 character string that uniquely identifies the requested Key credential resource.
        """
        return KeyContext(self._version, fleet_sid=self._solution["fleet_sid"], sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.DeployedDevices.KeyList>"
