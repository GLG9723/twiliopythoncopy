r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
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


class ByocTrunkInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the ByocTrunkInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "sid": payload.get("sid"),
            "friendly_name": payload.get("friendly_name"),
            "voice_url": payload.get("voice_url"),
            "voice_method": payload.get("voice_method"),
            "voice_fallback_url": payload.get("voice_fallback_url"),
            "voice_fallback_method": payload.get("voice_fallback_method"),
            "status_callback_url": payload.get("status_callback_url"),
            "status_callback_method": payload.get("status_callback_method"),
            "cnam_lookup_enabled": payload.get("cnam_lookup_enabled"),
            "connection_policy_sid": payload.get("connection_policy_sid"),
            "from_domain_sid": payload.get("from_domain_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[ByocTrunkContext] = None

    @property
    def _proxy(self) -> "ByocTrunkContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ByocTrunkContext for this ByocTrunkInstance
        """
        if self._context is None:
            self._context = ByocTrunkContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self) -> str:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the BYOC Trunk resource.
        """
        return self._properties["account_sid"]

    @property
    def sid(self) -> str:
        """
        :returns: The unique string that that we created to identify the BYOC Trunk resource.
        """
        return self._properties["sid"]

    @property
    def friendly_name(self) -> str:
        """
        :returns: The string that you assigned to describe the resource.
        """
        return self._properties["friendly_name"]

    @property
    def voice_url(self) -> str:
        """
        :returns: The URL we call using the `voice_method` when the BYOC Trunk receives a call.
        """
        return self._properties["voice_url"]

    @property
    def voice_method(self) -> str:
        """
        :returns: The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`.
        """
        return self._properties["voice_method"]

    @property
    def voice_fallback_url(self) -> str:
        """
        :returns: The URL that we call when an error occurs while retrieving or executing the TwiML requested from `voice_url`.
        """
        return self._properties["voice_fallback_url"]

    @property
    def voice_fallback_method(self) -> str:
        """
        :returns: The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        """
        return self._properties["voice_fallback_method"]

    @property
    def status_callback_url(self) -> str:
        """
        :returns: The URL that we call to pass status parameters (such as call ended) to your application.
        """
        return self._properties["status_callback_url"]

    @property
    def status_callback_method(self) -> str:
        """
        :returns: The HTTP method we use to call `status_callback_url`. Either `GET` or `POST`.
        """
        return self._properties["status_callback_method"]

    @property
    def cnam_lookup_enabled(self) -> bool:
        """
        :returns: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        """
        return self._properties["cnam_lookup_enabled"]

    @property
    def connection_policy_sid(self) -> str:
        """
        :returns: The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
        """
        return self._properties["connection_policy_sid"]

    @property
    def from_domain_sid(self) -> str:
        """
        :returns: The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \"call back\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \"sip.twilio.com\".
        """
        return self._properties["from_domain_sid"]

    @property
    def date_created(self) -> datetime:
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._properties["date_updated"]

    @property
    def url(self) -> str:
        """
        :returns: The absolute URL of the resource.
        """
        return self._properties["url"]

    def delete(self) -> bool:
        """
        Deletes the ByocTrunkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ByocTrunkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ByocTrunkInstance":
        """
        Fetch the ByocTrunkInstance


        :returns: The fetched ByocTrunkInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ByocTrunkInstance":
        """
        Asynchronous coroutine to fetch the ByocTrunkInstance


        :returns: The fetched ByocTrunkInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name=values.unset,
        voice_url=values.unset,
        voice_method=values.unset,
        voice_fallback_url=values.unset,
        voice_fallback_method=values.unset,
        status_callback_url=values.unset,
        status_callback_method=values.unset,
        cnam_lookup_enabled=values.unset,
        connection_policy_sid=values.unset,
        from_domain_sid=values.unset,
    ) -> "ByocTrunkInstance":
        """
        Update the ByocTrunkInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param str voice_url: The URL we should call when the BYOC Trunk receives a call.
        :param str voice_method: The HTTP method we should use to call `voice_url`
        :param str voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.
        :param str voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :param str status_callback_url: The URL that we should call to pass status parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
        :param bool cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param str connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
        :param str from_domain_sid: The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\"call back\\\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\"sip.twilio.com\\\".

        :returns: The updated ByocTrunkInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            voice_url=voice_url,
            voice_method=voice_method,
            voice_fallback_url=voice_fallback_url,
            voice_fallback_method=voice_fallback_method,
            status_callback_url=status_callback_url,
            status_callback_method=status_callback_method,
            cnam_lookup_enabled=cnam_lookup_enabled,
            connection_policy_sid=connection_policy_sid,
            from_domain_sid=from_domain_sid,
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        voice_url=values.unset,
        voice_method=values.unset,
        voice_fallback_url=values.unset,
        voice_fallback_method=values.unset,
        status_callback_url=values.unset,
        status_callback_method=values.unset,
        cnam_lookup_enabled=values.unset,
        connection_policy_sid=values.unset,
        from_domain_sid=values.unset,
    ) -> "ByocTrunkInstance":
        """
        Asynchronous coroutine to update the ByocTrunkInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param str voice_url: The URL we should call when the BYOC Trunk receives a call.
        :param str voice_method: The HTTP method we should use to call `voice_url`
        :param str voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.
        :param str voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :param str status_callback_url: The URL that we should call to pass status parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
        :param bool cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param str connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
        :param str from_domain_sid: The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\"call back\\\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\"sip.twilio.com\\\".

        :returns: The updated ByocTrunkInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            voice_url=voice_url,
            voice_method=voice_method,
            voice_fallback_url=voice_fallback_url,
            voice_fallback_method=voice_fallback_method,
            status_callback_url=status_callback_url,
            status_callback_method=status_callback_method,
            cnam_lookup_enabled=cnam_lookup_enabled,
            connection_policy_sid=connection_policy_sid,
            from_domain_sid=from_domain_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Voice.V1.ByocTrunkInstance {}>".format(context)


class ByocTrunkContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the ByocTrunkContext

        :param version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/ByocTrunks/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the ByocTrunkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ByocTrunkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ByocTrunkInstance:
        """
        Fetch the ByocTrunkInstance


        :returns: The fetched ByocTrunkInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ByocTrunkInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ByocTrunkInstance:
        """
        Asynchronous coroutine to fetch the ByocTrunkInstance


        :returns: The fetched ByocTrunkInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ByocTrunkInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name=values.unset,
        voice_url=values.unset,
        voice_method=values.unset,
        voice_fallback_url=values.unset,
        voice_fallback_method=values.unset,
        status_callback_url=values.unset,
        status_callback_method=values.unset,
        cnam_lookup_enabled=values.unset,
        connection_policy_sid=values.unset,
        from_domain_sid=values.unset,
    ) -> ByocTrunkInstance:
        """
        Update the ByocTrunkInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param str voice_url: The URL we should call when the BYOC Trunk receives a call.
        :param str voice_method: The HTTP method we should use to call `voice_url`
        :param str voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.
        :param str voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :param str status_callback_url: The URL that we should call to pass status parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
        :param bool cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param str connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
        :param str from_domain_sid: The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\"call back\\\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\"sip.twilio.com\\\".

        :returns: The updated ByocTrunkInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "VoiceUrl": voice_url,
                "VoiceMethod": voice_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceFallbackMethod": voice_fallback_method,
                "StatusCallbackUrl": status_callback_url,
                "StatusCallbackMethod": status_callback_method,
                "CnamLookupEnabled": cnam_lookup_enabled,
                "ConnectionPolicySid": connection_policy_sid,
                "FromDomainSid": from_domain_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ByocTrunkInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        friendly_name=values.unset,
        voice_url=values.unset,
        voice_method=values.unset,
        voice_fallback_url=values.unset,
        voice_fallback_method=values.unset,
        status_callback_url=values.unset,
        status_callback_method=values.unset,
        cnam_lookup_enabled=values.unset,
        connection_policy_sid=values.unset,
        from_domain_sid=values.unset,
    ) -> ByocTrunkInstance:
        """
        Asynchronous coroutine to update the ByocTrunkInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param str voice_url: The URL we should call when the BYOC Trunk receives a call.
        :param str voice_method: The HTTP method we should use to call `voice_url`
        :param str voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.
        :param str voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :param str status_callback_url: The URL that we should call to pass status parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
        :param bool cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param str connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
        :param str from_domain_sid: The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\"call back\\\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\"sip.twilio.com\\\".

        :returns: The updated ByocTrunkInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "VoiceUrl": voice_url,
                "VoiceMethod": voice_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceFallbackMethod": voice_fallback_method,
                "StatusCallbackUrl": status_callback_url,
                "StatusCallbackMethod": status_callback_method,
                "CnamLookupEnabled": cnam_lookup_enabled,
                "ConnectionPolicySid": connection_policy_sid,
                "FromDomainSid": from_domain_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ByocTrunkInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Voice.V1.ByocTrunkContext {}>".format(context)


class ByocTrunkPage(Page):
    def get_instance(self, payload) -> ByocTrunkInstance:
        """
        Build an instance of ByocTrunkInstance

        :param dict payload: Payload response from the API
        """
        return ByocTrunkInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Voice.V1.ByocTrunkPage>"


class ByocTrunkList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ByocTrunkList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/ByocTrunks"

    def create(
        self,
        friendly_name=values.unset,
        voice_url=values.unset,
        voice_method=values.unset,
        voice_fallback_url=values.unset,
        voice_fallback_method=values.unset,
        status_callback_url=values.unset,
        status_callback_method=values.unset,
        cnam_lookup_enabled=values.unset,
        connection_policy_sid=values.unset,
        from_domain_sid=values.unset,
    ) -> ByocTrunkInstance:
        """
        Create the ByocTrunkInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param str voice_url: The URL we should call when the BYOC Trunk receives a call.
        :param str voice_method: The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
        :param str voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML from `voice_url`.
        :param str voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :param str status_callback_url: The URL that we should call to pass status parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
        :param bool cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param str connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
        :param str from_domain_sid: The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\"call back\\\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\"sip.twilio.com\\\".

        :returns: The created ByocTrunkInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "VoiceUrl": voice_url,
                "VoiceMethod": voice_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceFallbackMethod": voice_fallback_method,
                "StatusCallbackUrl": status_callback_url,
                "StatusCallbackMethod": status_callback_method,
                "CnamLookupEnabled": cnam_lookup_enabled,
                "ConnectionPolicySid": connection_policy_sid,
                "FromDomainSid": from_domain_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ByocTrunkInstance(self._version, payload)

    async def create_async(
        self,
        friendly_name=values.unset,
        voice_url=values.unset,
        voice_method=values.unset,
        voice_fallback_url=values.unset,
        voice_fallback_method=values.unset,
        status_callback_url=values.unset,
        status_callback_method=values.unset,
        cnam_lookup_enabled=values.unset,
        connection_policy_sid=values.unset,
        from_domain_sid=values.unset,
    ) -> ByocTrunkInstance:
        """
        Asynchronously create the ByocTrunkInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param str voice_url: The URL we should call when the BYOC Trunk receives a call.
        :param str voice_method: The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
        :param str voice_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML from `voice_url`.
        :param str voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :param str status_callback_url: The URL that we should call to pass status parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
        :param bool cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param str connection_policy_sid: The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
        :param str from_domain_sid: The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\"call back\\\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\"sip.twilio.com\\\".

        :returns: The created ByocTrunkInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "VoiceUrl": voice_url,
                "VoiceMethod": voice_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceFallbackMethod": voice_fallback_method,
                "StatusCallbackUrl": status_callback_url,
                "StatusCallbackMethod": status_callback_method,
                "CnamLookupEnabled": cnam_lookup_enabled,
                "ConnectionPolicySid": connection_policy_sid,
                "FromDomainSid": from_domain_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ByocTrunkInstance(self._version, payload)

    def stream(self, limit=None, page_size=None) -> List[ByocTrunkInstance]:
        """
        Streams ByocTrunkInstance records from the API as a generator stream.
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

    async def stream_async(self, limit=None, page_size=None) -> List[ByocTrunkInstance]:
        """
        Asynchronously streams ByocTrunkInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[ByocTrunkInstance]:
        """
        Lists ByocTrunkInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[ByocTrunkInstance]:
        """
        Asynchronously lists ByocTrunkInstance records from the API as a list.
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
    ) -> ByocTrunkPage:
        """
        Retrieve a single page of ByocTrunkInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ByocTrunkInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ByocTrunkPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> ByocTrunkPage:
        """
        Asynchronously retrieve a single page of ByocTrunkInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ByocTrunkInstance
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
        return ByocTrunkPage(self._version, response)

    def get_page(self, target_url) -> ByocTrunkPage:
        """
        Retrieve a specific page of ByocTrunkInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ByocTrunkInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ByocTrunkPage(self._version, response)

    async def get_page_async(self, target_url) -> ByocTrunkPage:
        """
        Asynchronously retrieve a specific page of ByocTrunkInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ByocTrunkInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ByocTrunkPage(self._version, response)

    def get(self, sid) -> ByocTrunkContext:
        """
        Constructs a ByocTrunkContext

        :param sid: The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update.
        """
        return ByocTrunkContext(self._version, sid=sid)

    def __call__(self, sid) -> ByocTrunkContext:
        """
        Constructs a ByocTrunkContext

        :param sid: The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update.
        """
        return ByocTrunkContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Voice.V1.ByocTrunkList>"
