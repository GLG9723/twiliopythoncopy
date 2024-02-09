r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Routes
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class PhoneNumberInstance(InstanceResource):
    """
    :ivar phone_number: The phone number in E.164 format
    :ivar url: The absolute URL of the resource.
    :ivar sid: A 34 character string that uniquely identifies the Inbound Processing Region assignments for this phone number.
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar friendly_name: A human readable description of the Inbound Processing Region assignments for this phone number, up to 64 characters.
    :ivar voice_region: The Inbound Processing Region used for this phone number for voice.
    :ivar date_created: The date that this phone number was assigned an Inbound Processing Region, given in ISO 8601 format.
    :ivar date_updated: The date that the Inbound Processing Region was updated for this phone number, given in ISO 8601 format.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        phone_number: Optional[str] = None,
    ):
        super().__init__(version)

        self.phone_number: Optional[str] = payload.get("phone_number")
        self.url: Optional[str] = payload.get("url")
        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.voice_region: Optional[str] = payload.get("voice_region")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )

        self._solution = {
            "phone_number": phone_number or self.phone_number,
        }
        self._context: Optional[PhoneNumberContext] = None

    @property
    def _proxy(self) -> "PhoneNumberContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        """
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                phone_number=self._solution["phone_number"],
            )
        return self._context

    def fetch(self) -> "PhoneNumberInstance":
        """
        Fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "PhoneNumberInstance":
        """
        Asynchronous coroutine to fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        voice_region: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> "PhoneNumberInstance":
        """
        Update the PhoneNumberInstance

        :param voice_region: The Inbound Processing Region used for this phone number for voice
        :param friendly_name: A human readable description of this resource, up to 64 characters.

        :returns: The updated PhoneNumberInstance
        """
        return self._proxy.update(
            voice_region=voice_region,
            friendly_name=friendly_name,
        )

    async def update_async(
        self,
        voice_region: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> "PhoneNumberInstance":
        """
        Asynchronous coroutine to update the PhoneNumberInstance

        :param voice_region: The Inbound Processing Region used for this phone number for voice
        :param friendly_name: A human readable description of this resource, up to 64 characters.

        :returns: The updated PhoneNumberInstance
        """
        return await self._proxy.update_async(
            voice_region=voice_region,
            friendly_name=friendly_name,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Routes.V2.PhoneNumberInstance {}>".format(context)


class PhoneNumberContext(InstanceContext):
    def __init__(self, version: Version, phone_number: str):
        """
        Initialize the PhoneNumberContext

        :param version: Version that contains the resource
        :param phone_number: The phone number in E.164 format
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "phone_number": phone_number,
        }
        self._uri = "/PhoneNumbers/{phone_number}".format(**self._solution)

    def fetch(self) -> PhoneNumberInstance:
        """
        Fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            phone_number=self._solution["phone_number"],
        )

    async def fetch_async(self) -> PhoneNumberInstance:
        """
        Asynchronous coroutine to fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            phone_number=self._solution["phone_number"],
        )

    def update(
        self,
        voice_region: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> PhoneNumberInstance:
        """
        Update the PhoneNumberInstance

        :param voice_region: The Inbound Processing Region used for this phone number for voice
        :param friendly_name: A human readable description of this resource, up to 64 characters.

        :returns: The updated PhoneNumberInstance
        """
        data = values.of(
            {
                "VoiceRegion": voice_region,
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PhoneNumberInstance(
            self._version, payload, phone_number=self._solution["phone_number"]
        )

    async def update_async(
        self,
        voice_region: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
    ) -> PhoneNumberInstance:
        """
        Asynchronous coroutine to update the PhoneNumberInstance

        :param voice_region: The Inbound Processing Region used for this phone number for voice
        :param friendly_name: A human readable description of this resource, up to 64 characters.

        :returns: The updated PhoneNumberInstance
        """
        data = values.of(
            {
                "VoiceRegion": voice_region,
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PhoneNumberInstance(
            self._version, payload, phone_number=self._solution["phone_number"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Routes.V2.PhoneNumberContext {}>".format(context)


class PhoneNumberList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the PhoneNumberList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, phone_number: str) -> PhoneNumberContext:
        """
        Constructs a PhoneNumberContext

        :param phone_number: The phone number in E.164 format
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __call__(self, phone_number: str) -> PhoneNumberContext:
        """
        Constructs a PhoneNumberContext

        :param phone_number: The phone number in E.164 format
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Routes.V2.PhoneNumberList>"
