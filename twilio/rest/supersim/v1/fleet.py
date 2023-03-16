r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class FleetList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the FleetList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.supersim.v1.fleet.FleetList
        :rtype: twilio.rest.supersim.v1.fleet.FleetList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Fleets".format(**self._solution)

    def create(
        self,
        network_access_profile,
        unique_name=values.unset,
        data_enabled=values.unset,
        data_limit=values.unset,
        ip_commands_url=values.unset,
        ip_commands_method=values.unset,
        sms_commands_enabled=values.unset,
        sms_commands_url=values.unset,
        sms_commands_method=values.unset,
    ):
        """
        Create the FleetInstance

        :param str network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param bool data_enabled: Defines whether SIMs in the Fleet are capable of using 2G/3G/4G/LTE/CAT-M data connectivity. Defaults to `true`.
        :param int data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).
        :param str ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param bool sms_commands_enabled: Defines whether SIMs in the Fleet are capable of sending and receiving machine-to-machine SMS via Commands. Defaults to `true`.
        :param str sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.

        :returns: The created FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
        """
        data = values.of(
            {
                "NetworkAccessProfile": network_access_profile,
                "UniqueName": unique_name,
                "DataEnabled": data_enabled,
                "DataLimit": data_limit,
                "IpCommandsUrl": ip_commands_url,
                "IpCommandsMethod": ip_commands_method,
                "SmsCommandsEnabled": sms_commands_enabled,
                "SmsCommandsUrl": sms_commands_url,
                "SmsCommandsMethod": sms_commands_method,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload)

    async def create_async(
        self,
        network_access_profile,
        unique_name=values.unset,
        data_enabled=values.unset,
        data_limit=values.unset,
        ip_commands_url=values.unset,
        ip_commands_method=values.unset,
        sms_commands_enabled=values.unset,
        sms_commands_url=values.unset,
        sms_commands_method=values.unset,
    ):
        """
        Asynchronously create the FleetInstance

        :param str network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param bool data_enabled: Defines whether SIMs in the Fleet are capable of using 2G/3G/4G/LTE/CAT-M data connectivity. Defaults to `true`.
        :param int data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).
        :param str ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param bool sms_commands_enabled: Defines whether SIMs in the Fleet are capable of sending and receiving machine-to-machine SMS via Commands. Defaults to `true`.
        :param str sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.

        :returns: The created FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
        """
        data = values.of(
            {
                "NetworkAccessProfile": network_access_profile,
                "UniqueName": unique_name,
                "DataEnabled": data_enabled,
                "DataLimit": data_limit,
                "IpCommandsUrl": ip_commands_url,
                "IpCommandsMethod": ip_commands_method,
                "SmsCommandsEnabled": sms_commands_enabled,
                "SmsCommandsUrl": sms_commands_url,
                "SmsCommandsMethod": sms_commands_method,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload)

    def stream(self, network_access_profile=values.unset, limit=None, page_size=None):
        """
        Streams FleetInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.fleet.FleetInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            network_access_profile=network_access_profile, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, network_access_profile=values.unset, limit=None, page_size=None
    ):
        """
        Asynchronously streams FleetInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.fleet.FleetInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            network_access_profile=network_access_profile, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(self, network_access_profile=values.unset, limit=None, page_size=None):
        """
        Lists FleetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.fleet.FleetInstance]
        """
        return list(
            self.stream(
                network_access_profile=network_access_profile,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self, network_access_profile=values.unset, limit=None, page_size=None
    ):
        """
        Asynchronously lists FleetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.fleet.FleetInstance]
        """
        return list(
            await self.stream_async(
                network_access_profile=network_access_profile,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        network_access_profile=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of FleetInstance records from the API.
        Request is executed immediately

        :param str network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetPage
        """
        data = values.of(
            {
                "NetworkAccessProfile": network_access_profile,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return FleetPage(self._version, response, self._solution)

    async def page_async(
        self,
        network_access_profile=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of FleetInstance records from the API.
        Request is executed immediately

        :param str network_access_profile: The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetPage
        """
        data = values.of(
            {
                "NetworkAccessProfile": network_access_profile,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return FleetPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FleetInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FleetPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of FleetInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FleetPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a FleetContext

        :param sid: The SID of the Fleet resource to update.

        :returns: twilio.rest.supersim.v1.fleet.FleetContext
        :rtype: twilio.rest.supersim.v1.fleet.FleetContext
        """
        return FleetContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a FleetContext

        :param sid: The SID of the Fleet resource to update.

        :returns: twilio.rest.supersim.v1.fleet.FleetContext
        :rtype: twilio.rest.supersim.v1.fleet.FleetContext
        """
        return FleetContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Supersim.V1.FleetList>"


class FleetPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the FleetPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.fleet.FleetPage
        :rtype: twilio.rest.supersim.v1.fleet.FleetPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FleetInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.fleet.FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
        """
        return FleetInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Supersim.V1.FleetPage>"


class FleetInstance(InstanceResource):
    class DataMetering(object):
        PAYG = "payg"

    def __init__(self, version, payload, sid: str | None = None):
        """
        Initialize the FleetInstance

        :returns: twilio.rest.supersim.v1.fleet.FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "sid": payload.get("sid"),
            "unique_name": payload.get("unique_name"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
            "data_enabled": payload.get("data_enabled"),
            "data_limit": deserialize.integer(payload.get("data_limit")),
            "data_metering": payload.get("data_metering"),
            "sms_commands_enabled": payload.get("sms_commands_enabled"),
            "sms_commands_url": payload.get("sms_commands_url"),
            "sms_commands_method": payload.get("sms_commands_method"),
            "network_access_profile_sid": payload.get("network_access_profile_sid"),
            "ip_commands_url": payload.get("ip_commands_url"),
            "ip_commands_method": payload.get("ip_commands_method"),
        }

        self._context = None
        self._solution = {
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FleetContext for this FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetContext
        """
        if self._context is None:
            self._context = FleetContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Fleet resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Fleet resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :rtype: str
        """
        return self._properties["unique_name"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Fleet resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def data_enabled(self):
        """
        :returns: Defines whether SIMs in the Fleet are capable of using 2G/3G/4G/LTE/CAT-M data connectivity. Defaults to `true`.
        :rtype: bool
        """
        return self._properties["data_enabled"]

    @property
    def data_limit(self):
        """
        :returns: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).
        :rtype: int
        """
        return self._properties["data_limit"]

    @property
    def data_metering(self):
        """
        :returns:
        :rtype: FleetInstance.DataMetering
        """
        return self._properties["data_metering"]

    @property
    def sms_commands_enabled(self):
        """
        :returns: Defines whether SIMs in the Fleet are capable of sending and receiving machine-to-machine SMS via Commands. Defaults to `true`.
        :rtype: bool
        """
        return self._properties["sms_commands_enabled"]

    @property
    def sms_commands_url(self):
        """
        :returns: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :rtype: str
        """
        return self._properties["sms_commands_url"]

    @property
    def sms_commands_method(self):
        """
        :returns: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :rtype: str
        """
        return self._properties["sms_commands_method"]

    @property
    def network_access_profile_sid(self):
        """
        :returns: The SID of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
        :rtype: str
        """
        return self._properties["network_access_profile_sid"]

    @property
    def ip_commands_url(self):
        """
        :returns: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :rtype: str
        """
        return self._properties["ip_commands_url"]

    @property
    def ip_commands_method(self):
        """
        :returns: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :rtype: str
        """
        return self._properties["ip_commands_method"]

    def fetch(self):
        """
        Fetch the FleetInstance


        :returns: The fetched FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FleetInstance


        :returns: The fetched FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        unique_name=values.unset,
        network_access_profile=values.unset,
        ip_commands_url=values.unset,
        ip_commands_method=values.unset,
        sms_commands_url=values.unset,
        sms_commands_method=values.unset,
        data_limit=values.unset,
    ):
        """
        Update the FleetInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param str network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param str ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param str sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param int data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).

        :returns: The updated FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
            network_access_profile=network_access_profile,
            ip_commands_url=ip_commands_url,
            ip_commands_method=ip_commands_method,
            sms_commands_url=sms_commands_url,
            sms_commands_method=sms_commands_method,
            data_limit=data_limit,
        )

    async def update_async(
        self,
        unique_name=values.unset,
        network_access_profile=values.unset,
        ip_commands_url=values.unset,
        ip_commands_method=values.unset,
        sms_commands_url=values.unset,
        sms_commands_method=values.unset,
        data_limit=values.unset,
    ):
        """
        Asynchronous coroutine to update the FleetInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param str network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param str ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param str sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param int data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).

        :returns: The updated FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
        """
        return await self._proxy.update_async(
            unique_name=unique_name,
            network_access_profile=network_access_profile,
            ip_commands_url=ip_commands_url,
            ip_commands_method=ip_commands_method,
            sms_commands_url=sms_commands_url,
            sms_commands_method=sms_commands_method,
            data_limit=data_limit,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.FleetInstance {}>".format(context)


class FleetContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the FleetContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Fleet resource to update.

        :returns: twilio.rest.supersim.v1.fleet.FleetContext
        :rtype: twilio.rest.supersim.v1.fleet.FleetContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Fleets/{sid}".format(**self._solution)

    def fetch(self):
        """
        Fetch the FleetInstance


        :returns: The fetched FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
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

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FleetInstance


        :returns: The fetched FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
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
        unique_name=values.unset,
        network_access_profile=values.unset,
        ip_commands_url=values.unset,
        ip_commands_method=values.unset,
        sms_commands_url=values.unset,
        sms_commands_method=values.unset,
        data_limit=values.unset,
    ):
        """
        Update the FleetInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param str network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param str ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param str sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param int data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).

        :returns: The updated FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "NetworkAccessProfile": network_access_profile,
                "IpCommandsUrl": ip_commands_url,
                "IpCommandsMethod": ip_commands_method,
                "SmsCommandsUrl": sms_commands_url,
                "SmsCommandsMethod": sms_commands_method,
                "DataLimit": data_limit,
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
        unique_name=values.unset,
        network_access_profile=values.unset,
        ip_commands_url=values.unset,
        ip_commands_method=values.unset,
        sms_commands_url=values.unset,
        sms_commands_method=values.unset,
        data_limit=values.unset,
    ):
        """
        Asynchronous coroutine to update the FleetInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param str network_access_profile: The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
        :param str ip_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str ip_commands_method: A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param str sms_commands_url: The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
        :param str sms_commands_method: A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
        :param int data_limit: The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).

        :returns: The updated FleetInstance
        :rtype: twilio.rest.supersim.v1.fleet.FleetInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "NetworkAccessProfile": network_access_profile,
                "IpCommandsUrl": ip_commands_url,
                "IpCommandsMethod": ip_commands_method,
                "SmsCommandsUrl": sms_commands_url,
                "SmsCommandsMethod": sms_commands_method,
                "DataLimit": data_limit,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FleetInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.FleetContext {}>".format(context)
