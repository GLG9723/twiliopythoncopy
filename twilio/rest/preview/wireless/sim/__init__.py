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
from typing import List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.wireless.sim.usage import UsageList


class SimInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the SimInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "unique_name": payload.get("unique_name"),
            "account_sid": payload.get("account_sid"),
            "rate_plan_sid": payload.get("rate_plan_sid"),
            "friendly_name": payload.get("friendly_name"),
            "iccid": payload.get("iccid"),
            "e_id": payload.get("e_id"),
            "status": payload.get("status"),
            "commands_callback_url": payload.get("commands_callback_url"),
            "commands_callback_method": payload.get("commands_callback_method"),
            "sms_fallback_method": payload.get("sms_fallback_method"),
            "sms_fallback_url": payload.get("sms_fallback_url"),
            "sms_method": payload.get("sms_method"),
            "sms_url": payload.get("sms_url"),
            "voice_fallback_method": payload.get("voice_fallback_method"),
            "voice_fallback_url": payload.get("voice_fallback_url"),
            "voice_method": payload.get("voice_method"),
            "voice_url": payload.get("voice_url"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[SimContext] = None

    @property
    def _proxy(self) -> "SimContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SimContext for this SimInstance
        """
        if self._context is None:
            self._context = SimContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> str:
        """
        :returns:
        """
        return self._properties["sid"]

    @property
    def unique_name(self) -> str:
        """
        :returns:
        """
        return self._properties["unique_name"]

    @property
    def account_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["account_sid"]

    @property
    def rate_plan_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["rate_plan_sid"]

    @property
    def friendly_name(self) -> str:
        """
        :returns:
        """
        return self._properties["friendly_name"]

    @property
    def iccid(self) -> str:
        """
        :returns:
        """
        return self._properties["iccid"]

    @property
    def e_id(self) -> str:
        """
        :returns:
        """
        return self._properties["e_id"]

    @property
    def status(self) -> str:
        """
        :returns:
        """
        return self._properties["status"]

    @property
    def commands_callback_url(self) -> str:
        """
        :returns:
        """
        return self._properties["commands_callback_url"]

    @property
    def commands_callback_method(self) -> str:
        """
        :returns:
        """
        return self._properties["commands_callback_method"]

    @property
    def sms_fallback_method(self) -> str:
        """
        :returns:
        """
        return self._properties["sms_fallback_method"]

    @property
    def sms_fallback_url(self) -> str:
        """
        :returns:
        """
        return self._properties["sms_fallback_url"]

    @property
    def sms_method(self) -> str:
        """
        :returns:
        """
        return self._properties["sms_method"]

    @property
    def sms_url(self) -> str:
        """
        :returns:
        """
        return self._properties["sms_url"]

    @property
    def voice_fallback_method(self) -> str:
        """
        :returns:
        """
        return self._properties["voice_fallback_method"]

    @property
    def voice_fallback_url(self) -> str:
        """
        :returns:
        """
        return self._properties["voice_fallback_url"]

    @property
    def voice_method(self) -> str:
        """
        :returns:
        """
        return self._properties["voice_method"]

    @property
    def voice_url(self) -> str:
        """
        :returns:
        """
        return self._properties["voice_url"]

    @property
    def date_created(self) -> datetime:
        """
        :returns:
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns:
        """
        return self._properties["date_updated"]

    @property
    def url(self) -> str:
        """
        :returns:
        """
        return self._properties["url"]

    @property
    def links(self) -> dict:
        """
        :returns:
        """
        return self._properties["links"]

    def fetch(self) -> "SimInstance":
        """
        Fetch the SimInstance


        :returns: The fetched SimInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SimInstance":
        """
        Asynchronous coroutine to fetch the SimInstance


        :returns: The fetched SimInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        unique_name=values.unset,
        callback_method=values.unset,
        callback_url=values.unset,
        friendly_name=values.unset,
        rate_plan=values.unset,
        status=values.unset,
        commands_callback_method=values.unset,
        commands_callback_url=values.unset,
        sms_fallback_method=values.unset,
        sms_fallback_url=values.unset,
        sms_method=values.unset,
        sms_url=values.unset,
        voice_fallback_method=values.unset,
        voice_fallback_url=values.unset,
        voice_method=values.unset,
        voice_url=values.unset,
    ) -> "SimInstance":
        """
        Update the SimInstance

        :param str unique_name:
        :param str callback_method:
        :param str callback_url:
        :param str friendly_name:
        :param str rate_plan:
        :param str status:
        :param str commands_callback_method:
        :param str commands_callback_url:
        :param str sms_fallback_method:
        :param str sms_fallback_url:
        :param str sms_method:
        :param str sms_url:
        :param str voice_fallback_method:
        :param str voice_fallback_url:
        :param str voice_method:
        :param str voice_url:

        :returns: The updated SimInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
            callback_method=callback_method,
            callback_url=callback_url,
            friendly_name=friendly_name,
            rate_plan=rate_plan,
            status=status,
            commands_callback_method=commands_callback_method,
            commands_callback_url=commands_callback_url,
            sms_fallback_method=sms_fallback_method,
            sms_fallback_url=sms_fallback_url,
            sms_method=sms_method,
            sms_url=sms_url,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
        )

    async def update_async(
        self,
        unique_name=values.unset,
        callback_method=values.unset,
        callback_url=values.unset,
        friendly_name=values.unset,
        rate_plan=values.unset,
        status=values.unset,
        commands_callback_method=values.unset,
        commands_callback_url=values.unset,
        sms_fallback_method=values.unset,
        sms_fallback_url=values.unset,
        sms_method=values.unset,
        sms_url=values.unset,
        voice_fallback_method=values.unset,
        voice_fallback_url=values.unset,
        voice_method=values.unset,
        voice_url=values.unset,
    ) -> "SimInstance":
        """
        Asynchronous coroutine to update the SimInstance

        :param str unique_name:
        :param str callback_method:
        :param str callback_url:
        :param str friendly_name:
        :param str rate_plan:
        :param str status:
        :param str commands_callback_method:
        :param str commands_callback_url:
        :param str sms_fallback_method:
        :param str sms_fallback_url:
        :param str sms_method:
        :param str sms_url:
        :param str voice_fallback_method:
        :param str voice_fallback_url:
        :param str voice_method:
        :param str voice_url:

        :returns: The updated SimInstance
        """
        return await self._proxy.update_async(
            unique_name=unique_name,
            callback_method=callback_method,
            callback_url=callback_url,
            friendly_name=friendly_name,
            rate_plan=rate_plan,
            status=status,
            commands_callback_method=commands_callback_method,
            commands_callback_url=commands_callback_url,
            sms_fallback_method=sms_fallback_method,
            sms_fallback_url=sms_fallback_url,
            sms_method=sms_method,
            sms_url=sms_url,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
        )

    @property
    def usage(self) -> UsageList:
        """
        Access the usage
        """
        return self._proxy.usage

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Wireless.SimInstance {}>".format(context)


class SimContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the SimContext

        :param version: Version that contains the resource
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Sims/{sid}".format(**self._solution)

        self._usage: Optional[UsageList] = None

    def fetch(self) -> SimInstance:
        """
        Fetch the SimInstance


        :returns: The fetched SimInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SimInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SimInstance:
        """
        Asynchronous coroutine to fetch the SimInstance


        :returns: The fetched SimInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SimInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        unique_name=values.unset,
        callback_method=values.unset,
        callback_url=values.unset,
        friendly_name=values.unset,
        rate_plan=values.unset,
        status=values.unset,
        commands_callback_method=values.unset,
        commands_callback_url=values.unset,
        sms_fallback_method=values.unset,
        sms_fallback_url=values.unset,
        sms_method=values.unset,
        sms_url=values.unset,
        voice_fallback_method=values.unset,
        voice_fallback_url=values.unset,
        voice_method=values.unset,
        voice_url=values.unset,
    ) -> SimInstance:
        """
        Update the SimInstance

        :param str unique_name:
        :param str callback_method:
        :param str callback_url:
        :param str friendly_name:
        :param str rate_plan:
        :param str status:
        :param str commands_callback_method:
        :param str commands_callback_url:
        :param str sms_fallback_method:
        :param str sms_fallback_url:
        :param str sms_method:
        :param str sms_url:
        :param str voice_fallback_method:
        :param str voice_fallback_url:
        :param str voice_method:
        :param str voice_url:

        :returns: The updated SimInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "CallbackMethod": callback_method,
                "CallbackUrl": callback_url,
                "FriendlyName": friendly_name,
                "RatePlan": rate_plan,
                "Status": status,
                "CommandsCallbackMethod": commands_callback_method,
                "CommandsCallbackUrl": commands_callback_url,
                "SmsFallbackMethod": sms_fallback_method,
                "SmsFallbackUrl": sms_fallback_url,
                "SmsMethod": sms_method,
                "SmsUrl": sms_url,
                "VoiceFallbackMethod": voice_fallback_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceMethod": voice_method,
                "VoiceUrl": voice_url,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SimInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        unique_name=values.unset,
        callback_method=values.unset,
        callback_url=values.unset,
        friendly_name=values.unset,
        rate_plan=values.unset,
        status=values.unset,
        commands_callback_method=values.unset,
        commands_callback_url=values.unset,
        sms_fallback_method=values.unset,
        sms_fallback_url=values.unset,
        sms_method=values.unset,
        sms_url=values.unset,
        voice_fallback_method=values.unset,
        voice_fallback_url=values.unset,
        voice_method=values.unset,
        voice_url=values.unset,
    ) -> SimInstance:
        """
        Asynchronous coroutine to update the SimInstance

        :param str unique_name:
        :param str callback_method:
        :param str callback_url:
        :param str friendly_name:
        :param str rate_plan:
        :param str status:
        :param str commands_callback_method:
        :param str commands_callback_url:
        :param str sms_fallback_method:
        :param str sms_fallback_url:
        :param str sms_method:
        :param str sms_url:
        :param str voice_fallback_method:
        :param str voice_fallback_url:
        :param str voice_method:
        :param str voice_url:

        :returns: The updated SimInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "CallbackMethod": callback_method,
                "CallbackUrl": callback_url,
                "FriendlyName": friendly_name,
                "RatePlan": rate_plan,
                "Status": status,
                "CommandsCallbackMethod": commands_callback_method,
                "CommandsCallbackUrl": commands_callback_url,
                "SmsFallbackMethod": sms_fallback_method,
                "SmsFallbackUrl": sms_fallback_url,
                "SmsMethod": sms_method,
                "SmsUrl": sms_url,
                "VoiceFallbackMethod": voice_fallback_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceMethod": voice_method,
                "VoiceUrl": voice_url,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SimInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def usage(self) -> UsageList:
        """
        Access the usage
        """
        if self._usage is None:
            self._usage = UsageList(
                self._version,
                self._solution["sid"],
            )
        return self._usage

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Wireless.SimContext {}>".format(context)


class SimPage(Page):
    def get_instance(self, payload) -> SimInstance:
        """
        Build an instance of SimInstance

        :param dict payload: Payload response from the API
        """
        return SimInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Wireless.SimPage>"


class SimList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the SimList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Sims"

    def stream(
        self,
        status=values.unset,
        iccid=values.unset,
        rate_plan=values.unset,
        e_id=values.unset,
        sim_registration_code=values.unset,
        limit=None,
        page_size=None,
    ) -> List[SimInstance]:
        """
        Streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str status:
        :param str iccid:
        :param str rate_plan:
        :param str e_id:
        :param str sim_registration_code:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            iccid=iccid,
            rate_plan=rate_plan,
            e_id=e_id,
            sim_registration_code=sim_registration_code,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status=values.unset,
        iccid=values.unset,
        rate_plan=values.unset,
        e_id=values.unset,
        sim_registration_code=values.unset,
        limit=None,
        page_size=None,
    ) -> List[SimInstance]:
        """
        Asynchronously streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str status:
        :param str iccid:
        :param str rate_plan:
        :param str e_id:
        :param str sim_registration_code:
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
            status=status,
            iccid=iccid,
            rate_plan=rate_plan,
            e_id=e_id,
            sim_registration_code=sim_registration_code,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status=values.unset,
        iccid=values.unset,
        rate_plan=values.unset,
        e_id=values.unset,
        sim_registration_code=values.unset,
        limit=None,
        page_size=None,
    ) -> List[SimInstance]:
        """
        Lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str status:
        :param str iccid:
        :param str rate_plan:
        :param str e_id:
        :param str sim_registration_code:
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
                status=status,
                iccid=iccid,
                rate_plan=rate_plan,
                e_id=e_id,
                sim_registration_code=sim_registration_code,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status=values.unset,
        iccid=values.unset,
        rate_plan=values.unset,
        e_id=values.unset,
        sim_registration_code=values.unset,
        limit=None,
        page_size=None,
    ) -> List[SimInstance]:
        """
        Asynchronously lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str status:
        :param str iccid:
        :param str rate_plan:
        :param str e_id:
        :param str sim_registration_code:
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
                status=status,
                iccid=iccid,
                rate_plan=rate_plan,
                e_id=e_id,
                sim_registration_code=sim_registration_code,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        status=values.unset,
        iccid=values.unset,
        rate_plan=values.unset,
        e_id=values.unset,
        sim_registration_code=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> SimPage:
        """
        Retrieve a single page of SimInstance records from the API.
        Request is executed immediately

        :param str status:
        :param str iccid:
        :param str rate_plan:
        :param str e_id:
        :param str sim_registration_code:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        """
        data = values.of(
            {
                "Status": status,
                "Iccid": iccid,
                "RatePlan": rate_plan,
                "EId": e_id,
                "SimRegistrationCode": sim_registration_code,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SimPage(self._version, response)

    async def page_async(
        self,
        status=values.unset,
        iccid=values.unset,
        rate_plan=values.unset,
        e_id=values.unset,
        sim_registration_code=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> SimPage:
        """
        Asynchronously retrieve a single page of SimInstance records from the API.
        Request is executed immediately

        :param str status:
        :param str iccid:
        :param str rate_plan:
        :param str e_id:
        :param str sim_registration_code:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        """
        data = values.of(
            {
                "Status": status,
                "Iccid": iccid,
                "RatePlan": rate_plan,
                "EId": e_id,
                "SimRegistrationCode": sim_registration_code,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SimPage(self._version, response)

    def get_page(self, target_url) -> SimPage:
        """
        Retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SimPage(self._version, response)

    async def get_page_async(self, target_url) -> SimPage:
        """
        Asynchronously retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SimPage(self._version, response)

    def get(self, sid) -> SimContext:
        """
        Constructs a SimContext

        :param sid:
        """
        return SimContext(self._version, sid=sid)

    def __call__(self, sid) -> SimContext:
        """
        Constructs a SimContext

        :param sid:
        """
        return SimContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Wireless.SimList>"
