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
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.deployed_devices.fleet.certificate import CertificateList
from twilio.rest.preview.deployed_devices.fleet.deployment import DeploymentList
from twilio.rest.preview.deployed_devices.fleet.device import DeviceList
from twilio.rest.preview.deployed_devices.fleet.key import KeyList


class FleetInstance(InstanceResource):

    """
    :ivar sid: Contains a 34 character string that uniquely identifies this Fleet resource.
    :ivar url: Contains an absolute URL for this Fleet resource.
    :ivar unique_name: Contains a unique and addressable name of this Fleet, e.g. 'default', up to 128 characters long.
    :ivar friendly_name: Contains a human readable descriptive text for this Fleet, up to 256 characters long.
    :ivar account_sid: Speicifies the unique string identifier of the Account responsible for this Fleet.
    :ivar default_deployment_sid: Contains the string identifier of the automatically provisioned default Deployment of this Fleet.
    :ivar date_created: Specifies the date this Fleet was created, given in UTC ISO 8601 format.
    :ivar date_updated: Specifies the date this Fleet was last updated, given in UTC ISO 8601 format.
    :ivar links: Contains a dictionary of URL links to nested resources of this Fleet.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.url: Optional[str] = payload.get("url")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.default_deployment_sid: Optional[str] = payload.get(
            "default_deployment_sid"
        )
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[FleetContext] = None

    @property
    def _proxy(self) -> "FleetContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FleetContext for this FleetInstance
        """
        if self._context is None:
            self._context = FleetContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the FleetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FleetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "FleetInstance":
        """
        Fetch the FleetInstance


        :returns: The fetched FleetInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "FleetInstance":
        """
        Asynchronous coroutine to fetch the FleetInstance


        :returns: The fetched FleetInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        default_deployment_sid: Union[str, object] = values.unset,
    ) -> "FleetInstance":
        """
        Update the FleetInstance

        :param friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
        :param default_deployment_sid: Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.

        :returns: The updated FleetInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            default_deployment_sid=default_deployment_sid,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        default_deployment_sid: Union[str, object] = values.unset,
    ) -> "FleetInstance":
        """
        Asynchronous coroutine to update the FleetInstance

        :param friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
        :param default_deployment_sid: Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.

        :returns: The updated FleetInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            default_deployment_sid=default_deployment_sid,
        )

    @property
    def certificates(self) -> CertificateList:
        """
        Access the certificates
        """
        return self._proxy.certificates

    @property
    def deployments(self) -> DeploymentList:
        """
        Access the deployments
        """
        return self._proxy.deployments

    @property
    def devices(self) -> DeviceList:
        """
        Access the devices
        """
        return self._proxy.devices

    @property
    def keys(self) -> KeyList:
        """
        Access the keys
        """
        return self._proxy.keys

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.DeployedDevices.FleetInstance {}>".format(context)


class FleetContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the FleetContext

        :param version: Version that contains the resource
        :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Fleets/{sid}".format(**self._solution)

        self._certificates: Optional[CertificateList] = None
        self._deployments: Optional[DeploymentList] = None
        self._devices: Optional[DeviceList] = None
        self._keys: Optional[KeyList] = None

    def delete(self) -> bool:
        """
        Deletes the FleetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FleetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> FleetInstance:
        """
        Fetch the FleetInstance


        :returns: The fetched FleetInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FleetInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> FleetInstance:
        """
        Asynchronous coroutine to fetch the FleetInstance


        :returns: The fetched FleetInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FleetInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        default_deployment_sid: Union[str, object] = values.unset,
    ) -> FleetInstance:
        """
        Update the FleetInstance

        :param friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
        :param default_deployment_sid: Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.

        :returns: The updated FleetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DefaultDeploymentSid": default_deployment_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        default_deployment_sid: Union[str, object] = values.unset,
    ) -> FleetInstance:
        """
        Asynchronous coroutine to update the FleetInstance

        :param friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
        :param default_deployment_sid: Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.

        :returns: The updated FleetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DefaultDeploymentSid": default_deployment_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def certificates(self) -> CertificateList:
        """
        Access the certificates
        """
        if self._certificates is None:
            self._certificates = CertificateList(
                self._version,
                self._solution["sid"],
            )
        return self._certificates

    @property
    def deployments(self) -> DeploymentList:
        """
        Access the deployments
        """
        if self._deployments is None:
            self._deployments = DeploymentList(
                self._version,
                self._solution["sid"],
            )
        return self._deployments

    @property
    def devices(self) -> DeviceList:
        """
        Access the devices
        """
        if self._devices is None:
            self._devices = DeviceList(
                self._version,
                self._solution["sid"],
            )
        return self._devices

    @property
    def keys(self) -> KeyList:
        """
        Access the keys
        """
        if self._keys is None:
            self._keys = KeyList(
                self._version,
                self._solution["sid"],
            )
        return self._keys

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.DeployedDevices.FleetContext {}>".format(context)


class FleetPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> FleetInstance:
        """
        Build an instance of FleetInstance

        :param payload: Payload response from the API
        """
        return FleetInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.DeployedDevices.FleetPage>"


class FleetList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the FleetList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Fleets"

    def create(self, friendly_name: Union[str, object] = values.unset) -> FleetInstance:
        """
        Create the FleetInstance

        :param friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.

        :returns: The created FleetInstance
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

        return FleetInstance(self._version, payload)

    async def create_async(
        self, friendly_name: Union[str, object] = values.unset
    ) -> FleetInstance:
        """
        Asynchronously create the FleetInstance

        :param friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.

        :returns: The created FleetInstance
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

        return FleetInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[FleetInstance]:
        """
        Streams FleetInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[FleetInstance]:
        """
        Asynchronously streams FleetInstance records from the API as a generator stream.
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
    ) -> List[FleetInstance]:
        """
        Lists FleetInstance records from the API as a list.
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
    ) -> List[FleetInstance]:
        """
        Asynchronously lists FleetInstance records from the API as a list.
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
    ) -> FleetPage:
        """
        Retrieve a single page of FleetInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FleetInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return FleetPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> FleetPage:
        """
        Asynchronously retrieve a single page of FleetInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FleetInstance
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
        return FleetPage(self._version, response)

    def get_page(self, target_url: str) -> FleetPage:
        """
        Retrieve a specific page of FleetInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FleetInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FleetPage(self._version, response)

    async def get_page_async(self, target_url: str) -> FleetPage:
        """
        Asynchronously retrieve a specific page of FleetInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FleetInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FleetPage(self._version, response)

    def get(self, sid: str) -> FleetContext:
        """
        Constructs a FleetContext

        :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.
        """
        return FleetContext(self._version, sid=sid)

    def __call__(self, sid: str) -> FleetContext:
        """
        Constructs a FleetContext

        :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.
        """
        return FleetContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.DeployedDevices.FleetList>"
