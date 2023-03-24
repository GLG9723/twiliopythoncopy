r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class SettingInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the SettingInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "advanced_features": payload.get("advanced_features"),
            "voice_trace": payload.get("voice_trace"),
            "url": payload.get("url"),
        }

        self._solution = {}
        self._context: Optional[SettingContext] = None

    @property
    def _proxy(self) -> "SettingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SettingContext for this SettingInstance
        """
        if self._context is None:
            self._context = SettingContext(
                self._version,
            )
        return self._context

    @property
    def account_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["account_sid"]

    @property
    def advanced_features(self) -> bool:
        """
        :returns:
        """
        return self._properties["advanced_features"]

    @property
    def voice_trace(self) -> bool:
        """
        :returns:
        """
        return self._properties["voice_trace"]

    @property
    def url(self) -> str:
        """
        :returns:
        """
        return self._properties["url"]

    def fetch(self, subaccount_sid=values.unset) -> "SettingInstance":
        """
        Fetch the SettingInstance

        :param str subaccount_sid:

        :returns: The fetched SettingInstance
        """
        return self._proxy.fetch(
            subaccount_sid=subaccount_sid,
        )

    async def fetch_async(self, subaccount_sid=values.unset) -> "SettingInstance":
        """
        Asynchronous coroutine to fetch the SettingInstance

        :param str subaccount_sid:

        :returns: The fetched SettingInstance
        """
        return await self._proxy.fetch_async(
            subaccount_sid=subaccount_sid,
        )

    def update(
        self,
        advanced_features=values.unset,
        voice_trace=values.unset,
        subaccount_sid=values.unset,
    ) -> "SettingInstance":
        """
        Update the SettingInstance

        :param bool advanced_features:
        :param bool voice_trace:
        :param str subaccount_sid:

        :returns: The updated SettingInstance
        """
        return self._proxy.update(
            advanced_features=advanced_features,
            voice_trace=voice_trace,
            subaccount_sid=subaccount_sid,
        )

    async def update_async(
        self,
        advanced_features=values.unset,
        voice_trace=values.unset,
        subaccount_sid=values.unset,
    ) -> "SettingInstance":
        """
        Asynchronous coroutine to update the SettingInstance

        :param bool advanced_features:
        :param bool voice_trace:
        :param str subaccount_sid:

        :returns: The updated SettingInstance
        """
        return await self._proxy.update_async(
            advanced_features=advanced_features,
            voice_trace=voice_trace,
            subaccount_sid=subaccount_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.SettingInstance {}>".format(context)


class SettingContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the SettingContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/Voice/Settings"

    def fetch(self, subaccount_sid=values.unset) -> SettingInstance:
        """
        Fetch the SettingInstance

        :param str subaccount_sid:

        :returns: The fetched SettingInstance
        """

        data = values.of(
            {
                "SubaccountSid": subaccount_sid,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return SettingInstance(
            self._version,
            payload,
        )

    async def fetch_async(self, subaccount_sid=values.unset) -> SettingInstance:
        """
        Asynchronous coroutine to fetch the SettingInstance

        :param str subaccount_sid:

        :returns: The fetched SettingInstance
        """

        data = values.of(
            {
                "SubaccountSid": subaccount_sid,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return SettingInstance(
            self._version,
            payload,
        )

    def update(
        self,
        advanced_features=values.unset,
        voice_trace=values.unset,
        subaccount_sid=values.unset,
    ) -> SettingInstance:
        """
        Update the SettingInstance

        :param bool advanced_features:
        :param bool voice_trace:
        :param str subaccount_sid:

        :returns: The updated SettingInstance
        """
        data = values.of(
            {
                "AdvancedFeatures": advanced_features,
                "VoiceTrace": voice_trace,
                "SubaccountSid": subaccount_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SettingInstance(self._version, payload)

    async def update_async(
        self,
        advanced_features=values.unset,
        voice_trace=values.unset,
        subaccount_sid=values.unset,
    ) -> SettingInstance:
        """
        Asynchronous coroutine to update the SettingInstance

        :param bool advanced_features:
        :param bool voice_trace:
        :param str subaccount_sid:

        :returns: The updated SettingInstance
        """
        data = values.of(
            {
                "AdvancedFeatures": advanced_features,
                "VoiceTrace": voice_trace,
                "SubaccountSid": subaccount_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SettingInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Insights.V1.SettingContext>"


class SettingList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the SettingList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> SettingContext:
        """
        Constructs a SettingContext

        """
        return SettingContext(self._version)

    def __call__(self) -> SettingContext:
        """
        Constructs a SettingContext

        """
        return SettingContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.SettingList>"
