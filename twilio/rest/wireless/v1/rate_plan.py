r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Wireless
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


class RatePlanInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the RatePlanInstance
        """
        super().__init__(version)

        self._sid: Optional[str] = payload.get("sid")
        self._unique_name: Optional[str] = payload.get("unique_name")
        self._account_sid: Optional[str] = payload.get("account_sid")
        self._friendly_name: Optional[str] = payload.get("friendly_name")
        self._data_enabled: Optional[bool] = payload.get("data_enabled")
        self._data_metering: Optional[str] = payload.get("data_metering")
        self._data_limit: Optional[int] = deserialize.integer(payload.get("data_limit"))
        self._messaging_enabled: Optional[bool] = payload.get("messaging_enabled")
        self._voice_enabled: Optional[bool] = payload.get("voice_enabled")
        self._national_roaming_enabled: Optional[bool] = payload.get(
            "national_roaming_enabled"
        )
        self._national_roaming_data_limit: Optional[int] = deserialize.integer(
            payload.get("national_roaming_data_limit")
        )
        self._international_roaming: Optional[List[str]] = payload.get(
            "international_roaming"
        )
        self._international_roaming_data_limit: Optional[int] = deserialize.integer(
            payload.get("international_roaming_data_limit")
        )
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self._url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self._sid,
        }
        self._context: Optional[RatePlanContext] = None

    @property
    def _proxy(self) -> "RatePlanContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RatePlanContext for this RatePlanInstance
        """
        if self._context is None:
            self._context = RatePlanContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that we created to identify the RatePlan resource.
        """
        return self._sid

    @property
    def unique_name(self) -> Optional[str]:
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        """
        return self._unique_name

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the RatePlan resource.
        """
        return self._account_sid

    @property
    def friendly_name(self) -> Optional[str]:
        """
        :returns: The string that you assigned to describe the resource.
        """
        return self._friendly_name

    @property
    def data_enabled(self) -> Optional[bool]:
        """
        :returns: Whether SIMs can use GPRS/3G/4G/LTE data connectivity.
        """
        return self._data_enabled

    @property
    def data_metering(self) -> Optional[str]:
        """
        :returns: The model used to meter data usage. Can be: `payg` and `quota-1`, `quota-10`, and `quota-50`. Learn more about the available [data metering models](https://www.twilio.com/docs/wireless/api/rateplan-resource#payg-vs-quota-data-plans).
        """
        return self._data_metering

    @property
    def data_limit(self) -> Optional[int]:
        """
        :returns: The total data usage (download and upload combined) in Megabytes that the Network allows during one month on the home network (T-Mobile USA). The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB.
        """
        return self._data_limit

    @property
    def messaging_enabled(self) -> Optional[bool]:
        """
        :returns: Whether SIMs can make, send, and receive SMS using [Commands](https://www.twilio.com/docs/wireless/api/command-resource).
        """
        return self._messaging_enabled

    @property
    def voice_enabled(self) -> Optional[bool]:
        """
        :returns: Deprecated. Whether SIMs can make and receive voice calls.
        """
        return self._voice_enabled

    @property
    def national_roaming_enabled(self) -> Optional[bool]:
        """
        :returns: Whether SIMs can roam on networks other than the home network (T-Mobile USA) in the United States. See [national roaming](https://www.twilio.com/docs/wireless/api/rateplan-resource#national-roaming).
        """
        return self._national_roaming_enabled

    @property
    def national_roaming_data_limit(self) -> Optional[int]:
        """
        :returns: The total data usage (download and upload combined) in Megabytes that the Network allows during one month on non-home networks in the United States. The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB.
        """
        return self._national_roaming_data_limit

    @property
    def international_roaming(self) -> Optional[List[str]]:
        """
        :returns: The list of services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States. Can contain: `data` and `messaging`.
        """
        return self._international_roaming

    @property
    def international_roaming_data_limit(self) -> Optional[int]:
        """
        :returns: The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States. Can be up to 2TB.
        """
        return self._international_roaming_data_limit

    @property
    def date_created(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        """
        return self._date_created

    @property
    def date_updated(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        """
        return self._date_updated

    @property
    def url(self) -> Optional[str]:
        """
        :returns: The absolute URL of the resource.
        """
        return self._url

    def delete(self) -> bool:
        """
        Deletes the RatePlanInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RatePlanInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "RatePlanInstance":
        """
        Fetch the RatePlanInstance


        :returns: The fetched RatePlanInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RatePlanInstance":
        """
        Asynchronous coroutine to fetch the RatePlanInstance


        :returns: The fetched RatePlanInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, unique_name=values.unset, friendly_name=values.unset
    ) -> "RatePlanInstance":
        """
        Update the RatePlanInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param str friendly_name: A descriptive string that you create to describe the resource. It does not have to be unique.

        :returns: The updated RatePlanInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
            friendly_name=friendly_name,
        )

    async def update_async(
        self, unique_name=values.unset, friendly_name=values.unset
    ) -> "RatePlanInstance":
        """
        Asynchronous coroutine to update the RatePlanInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param str friendly_name: A descriptive string that you create to describe the resource. It does not have to be unique.

        :returns: The updated RatePlanInstance
        """
        return await self._proxy.update_async(
            unique_name=unique_name,
            friendly_name=friendly_name,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Wireless.V1.RatePlanInstance {}>".format(context)


class RatePlanContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the RatePlanContext

        :param version: Version that contains the resource
        :param sid: The SID of the RatePlan resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/RatePlans/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the RatePlanInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RatePlanInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> RatePlanInstance:
        """
        Fetch the RatePlanInstance


        :returns: The fetched RatePlanInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RatePlanInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> RatePlanInstance:
        """
        Asynchronous coroutine to fetch the RatePlanInstance


        :returns: The fetched RatePlanInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RatePlanInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self, unique_name=values.unset, friendly_name=values.unset
    ) -> RatePlanInstance:
        """
        Update the RatePlanInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param str friendly_name: A descriptive string that you create to describe the resource. It does not have to be unique.

        :returns: The updated RatePlanInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RatePlanInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self, unique_name=values.unset, friendly_name=values.unset
    ) -> RatePlanInstance:
        """
        Asynchronous coroutine to update the RatePlanInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param str friendly_name: A descriptive string that you create to describe the resource. It does not have to be unique.

        :returns: The updated RatePlanInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RatePlanInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Wireless.V1.RatePlanContext {}>".format(context)


class RatePlanPage(Page):
    def get_instance(self, payload) -> RatePlanInstance:
        """
        Build an instance of RatePlanInstance

        :param dict payload: Payload response from the API
        """
        return RatePlanInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Wireless.V1.RatePlanPage>"


class RatePlanList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the RatePlanList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/RatePlans"

    def create(
        self,
        unique_name=values.unset,
        friendly_name=values.unset,
        data_enabled=values.unset,
        data_limit=values.unset,
        data_metering=values.unset,
        messaging_enabled=values.unset,
        voice_enabled=values.unset,
        national_roaming_enabled=values.unset,
        international_roaming=values.unset,
        national_roaming_data_limit=values.unset,
        international_roaming_data_limit=values.unset,
    ) -> RatePlanInstance:
        """
        Create the RatePlanInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param str friendly_name: A descriptive string that you create to describe the resource. It does not have to be unique.
        :param bool data_enabled: Whether SIMs can use GPRS/3G/4G/LTE data connectivity.
        :param int data_limit: The total data usage (download and upload combined) in Megabytes that the Network allows during one month on the home network (T-Mobile USA). The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB and the default value is `1000`.
        :param str data_metering: The model used to meter data usage. Can be: `payg` and `quota-1`, `quota-10`, and `quota-50`. Learn more about the available [data metering models](https://www.twilio.com/docs/wireless/api/rateplan-resource#payg-vs-quota-data-plans).
        :param bool messaging_enabled: Whether SIMs can make, send, and receive SMS using [Commands](https://www.twilio.com/docs/wireless/api/command-resource).
        :param bool voice_enabled: Deprecated.
        :param bool national_roaming_enabled: Whether SIMs can roam on networks other than the home network (T-Mobile USA) in the United States. See [national roaming](https://www.twilio.com/docs/wireless/api/rateplan-resource#national-roaming).
        :param List[str] international_roaming: The list of services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States. Can contain: `data` and `messaging`.
        :param int national_roaming_data_limit: The total data usage (download and upload combined) in Megabytes that the Network allows during one month on non-home networks in the United States. The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB. See [national roaming](https://www.twilio.com/docs/wireless/api/rateplan-resource#national-roaming) for more info.
        :param int international_roaming_data_limit: The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States. Can be up to 2TB.

        :returns: The created RatePlanInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "DataEnabled": data_enabled,
                "DataLimit": data_limit,
                "DataMetering": data_metering,
                "MessagingEnabled": messaging_enabled,
                "VoiceEnabled": voice_enabled,
                "NationalRoamingEnabled": national_roaming_enabled,
                "InternationalRoaming": serialize.map(
                    international_roaming, lambda e: e
                ),
                "NationalRoamingDataLimit": national_roaming_data_limit,
                "InternationalRoamingDataLimit": international_roaming_data_limit,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RatePlanInstance(self._version, payload)

    async def create_async(
        self,
        unique_name=values.unset,
        friendly_name=values.unset,
        data_enabled=values.unset,
        data_limit=values.unset,
        data_metering=values.unset,
        messaging_enabled=values.unset,
        voice_enabled=values.unset,
        national_roaming_enabled=values.unset,
        international_roaming=values.unset,
        national_roaming_data_limit=values.unset,
        international_roaming_data_limit=values.unset,
    ) -> RatePlanInstance:
        """
        Asynchronously create the RatePlanInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param str friendly_name: A descriptive string that you create to describe the resource. It does not have to be unique.
        :param bool data_enabled: Whether SIMs can use GPRS/3G/4G/LTE data connectivity.
        :param int data_limit: The total data usage (download and upload combined) in Megabytes that the Network allows during one month on the home network (T-Mobile USA). The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB and the default value is `1000`.
        :param str data_metering: The model used to meter data usage. Can be: `payg` and `quota-1`, `quota-10`, and `quota-50`. Learn more about the available [data metering models](https://www.twilio.com/docs/wireless/api/rateplan-resource#payg-vs-quota-data-plans).
        :param bool messaging_enabled: Whether SIMs can make, send, and receive SMS using [Commands](https://www.twilio.com/docs/wireless/api/command-resource).
        :param bool voice_enabled: Deprecated.
        :param bool national_roaming_enabled: Whether SIMs can roam on networks other than the home network (T-Mobile USA) in the United States. See [national roaming](https://www.twilio.com/docs/wireless/api/rateplan-resource#national-roaming).
        :param List[str] international_roaming: The list of services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States. Can contain: `data` and `messaging`.
        :param int national_roaming_data_limit: The total data usage (download and upload combined) in Megabytes that the Network allows during one month on non-home networks in the United States. The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB. See [national roaming](https://www.twilio.com/docs/wireless/api/rateplan-resource#national-roaming) for more info.
        :param int international_roaming_data_limit: The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States. Can be up to 2TB.

        :returns: The created RatePlanInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "DataEnabled": data_enabled,
                "DataLimit": data_limit,
                "DataMetering": data_metering,
                "MessagingEnabled": messaging_enabled,
                "VoiceEnabled": voice_enabled,
                "NationalRoamingEnabled": national_roaming_enabled,
                "InternationalRoaming": serialize.map(
                    international_roaming, lambda e: e
                ),
                "NationalRoamingDataLimit": national_roaming_data_limit,
                "InternationalRoamingDataLimit": international_roaming_data_limit,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RatePlanInstance(self._version, payload)

    def stream(self, limit=None, page_size=None) -> List[RatePlanInstance]:
        """
        Streams RatePlanInstance records from the API as a generator stream.
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

    async def stream_async(self, limit=None, page_size=None) -> List[RatePlanInstance]:
        """
        Asynchronously streams RatePlanInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[RatePlanInstance]:
        """
        Lists RatePlanInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[RatePlanInstance]:
        """
        Asynchronously lists RatePlanInstance records from the API as a list.
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
    ) -> RatePlanPage:
        """
        Retrieve a single page of RatePlanInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RatePlanInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return RatePlanPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> RatePlanPage:
        """
        Asynchronously retrieve a single page of RatePlanInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RatePlanInstance
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
        return RatePlanPage(self._version, response)

    def get_page(self, target_url) -> RatePlanPage:
        """
        Retrieve a specific page of RatePlanInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RatePlanInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RatePlanPage(self._version, response)

    async def get_page_async(self, target_url) -> RatePlanPage:
        """
        Asynchronously retrieve a specific page of RatePlanInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RatePlanInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RatePlanPage(self._version, response)

    def get(self, sid) -> RatePlanContext:
        """
        Constructs a RatePlanContext

        :param sid: The SID of the RatePlan resource to update.
        """
        return RatePlanContext(self._version, sid=sid)

    def __call__(self, sid) -> RatePlanContext:
        """
        Constructs a RatePlanContext

        :param sid: The SID of the RatePlan resource to update.
        """
        return RatePlanContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Wireless.V1.RatePlanList>"
