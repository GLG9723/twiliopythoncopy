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


class CertificateInstance(InstanceResource):
    """
    :ivar sid: Contains a 34 character string that uniquely identifies this Certificate credential resource.
    :ivar url: Contains an absolute URL for this Certificate credential resource.
    :ivar friendly_name: Contains a human readable descriptive text for this Certificate credential, up to 256 characters long.
    :ivar fleet_sid: Specifies the unique string identifier of the Fleet that the given Certificate credential belongs to.
    :ivar account_sid: Specifies the unique string identifier of the Account responsible for this Certificate credential.
    :ivar device_sid: Specifies the unique string identifier of a Device authenticated with this Certificate credential.
    :ivar thumbprint: Contains a unique hash of the payload of this Certificate credential, used to authenticate the Device.
    :ivar date_created: Specifies the date this Certificate credential was created, given in UTC ISO 8601 format.
    :ivar date_updated: Specifies the date this Certificate credential was last updated, given in UTC ISO 8601 format.
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
        self.thumbprint: Optional[str] = payload.get("thumbprint")
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
        self._context: Optional[CertificateContext] = None

    @property
    def _proxy(self) -> "CertificateContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CertificateContext for this CertificateInstance
        """
        if self._context is None:
            self._context = CertificateContext(
                self._version,
                fleet_sid=self._solution["fleet_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the CertificateInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CertificateInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "CertificateInstance":
        """
        Fetch the CertificateInstance


        :returns: The fetched CertificateInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CertificateInstance":
        """
        Asynchronous coroutine to fetch the CertificateInstance


        :returns: The fetched CertificateInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        device_sid: Union[str, object] = values.unset,
    ) -> "CertificateInstance":
        """
        Update the CertificateInstance

        :param friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
        :param device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.

        :returns: The updated CertificateInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            device_sid=device_sid,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        device_sid: Union[str, object] = values.unset,
    ) -> "CertificateInstance":
        """
        Asynchronous coroutine to update the CertificateInstance

        :param friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
        :param device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.

        :returns: The updated CertificateInstance
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
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Preview.DeployedDevices.CertificateInstance {context}>"


class CertificateContext(InstanceContext):

    def __init__(self, version: Version, fleet_sid: str, sid: str):
        """
        Initialize the CertificateContext

        :param version: Version that contains the resource
        :param fleet_sid:
        :param sid: Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "fleet_sid": fleet_sid,
            "sid": sid,
        }
        self._uri = "/Fleets/{fleet_sid}/Certificates/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the CertificateInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CertificateInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> CertificateInstance:
        """
        Fetch the CertificateInstance


        :returns: The fetched CertificateInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CertificateInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CertificateInstance:
        """
        Asynchronous coroutine to fetch the CertificateInstance


        :returns: The fetched CertificateInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CertificateInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        device_sid: Union[str, object] = values.unset,
    ) -> CertificateInstance:
        """
        Update the CertificateInstance

        :param friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
        :param device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.

        :returns: The updated CertificateInstance
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

        return CertificateInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        device_sid: Union[str, object] = values.unset,
    ) -> CertificateInstance:
        """
        Asynchronous coroutine to update the CertificateInstance

        :param friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
        :param device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.

        :returns: The updated CertificateInstance
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

        return CertificateInstance(
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
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Preview.DeployedDevices.CertificateContext {context}>"


class CertificatePage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> CertificateInstance:
        """
        Build an instance of CertificateInstance

        :param payload: Payload response from the API
        """
        return CertificateInstance(
            self._version, payload, fleet_sid=self._solution["fleet_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.DeployedDevices.CertificatePage>"


class CertificateList(ListResource):

    def __init__(self, version: Version, fleet_sid: str):
        """
        Initialize the CertificateList

        :param version: Version that contains the resource
        :param fleet_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "fleet_sid": fleet_sid,
        }
        self._uri = "/Fleets/{fleet_sid}/Certificates".format(**self._solution)

    def create(
        self,
        certificate_data: str,
        friendly_name: Union[str, object] = values.unset,
        device_sid: Union[str, object] = values.unset,
    ) -> CertificateInstance:
        """
        Create the CertificateInstance

        :param certificate_data: Provides a URL encoded representation of the public certificate in PEM format.
        :param friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
        :param device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.

        :returns: The created CertificateInstance
        """

        data = values.of(
            {
                "CertificateData": certificate_data,
                "FriendlyName": friendly_name,
                "DeviceSid": device_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CertificateInstance(
            self._version, payload, fleet_sid=self._solution["fleet_sid"]
        )

    async def create_async(
        self,
        certificate_data: str,
        friendly_name: Union[str, object] = values.unset,
        device_sid: Union[str, object] = values.unset,
    ) -> CertificateInstance:
        """
        Asynchronously create the CertificateInstance

        :param certificate_data: Provides a URL encoded representation of the public certificate in PEM format.
        :param friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
        :param device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.

        :returns: The created CertificateInstance
        """

        data = values.of(
            {
                "CertificateData": certificate_data,
                "FriendlyName": friendly_name,
                "DeviceSid": device_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CertificateInstance(
            self._version, payload, fleet_sid=self._solution["fleet_sid"]
        )

    def stream(
        self,
        device_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[CertificateInstance]:
        """
        Streams CertificateInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str device_sid: Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(device_sid=device_sid, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        device_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[CertificateInstance]:
        """
        Asynchronously streams CertificateInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str device_sid: Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            device_sid=device_sid, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        device_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CertificateInstance]:
        """
        Lists CertificateInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str device_sid: Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
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
                device_sid=device_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        device_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CertificateInstance]:
        """
        Asynchronously lists CertificateInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str device_sid: Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
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
                device_sid=device_sid,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        device_sid: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CertificatePage:
        """
        Retrieve a single page of CertificateInstance records from the API.
        Request is executed immediately

        :param device_sid: Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CertificateInstance
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
        return CertificatePage(self._version, response, self._solution)

    async def page_async(
        self,
        device_sid: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CertificatePage:
        """
        Asynchronously retrieve a single page of CertificateInstance records from the API.
        Request is executed immediately

        :param device_sid: Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CertificateInstance
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
        return CertificatePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> CertificatePage:
        """
        Retrieve a specific page of CertificateInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CertificateInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CertificatePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> CertificatePage:
        """
        Asynchronously retrieve a specific page of CertificateInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CertificateInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CertificatePage(self._version, response, self._solution)

    def get(self, sid: str) -> CertificateContext:
        """
        Constructs a CertificateContext

        :param sid: Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
        """
        return CertificateContext(
            self._version, fleet_sid=self._solution["fleet_sid"], sid=sid
        )

    def __call__(self, sid: str) -> CertificateContext:
        """
        Constructs a CertificateContext

        :param sid: Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
        """
        return CertificateContext(
            self._version, fleet_sid=self._solution["fleet_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.DeployedDevices.CertificateList>"
