r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ValidationRequestInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str):
        """
        Initialize the ValidationRequestInstance
        """
        super().__init__(version)

        self._account_sid: Optional[str] = payload.get("account_sid")
        self._call_sid: Optional[str] = payload.get("call_sid")
        self._friendly_name: Optional[str] = payload.get("friendly_name")
        self._phone_number: Optional[str] = payload.get("phone_number")
        self._validation_code: Optional[str] = payload.get("validation_code")

        self._solution = {
            "account_sid": account_sid,
        }

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the Caller ID.
        """
        return self._account_sid

    @property
    def call_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Caller ID is associated with.
        """
        return self._call_sid

    @property
    def friendly_name(self) -> Optional[str]:
        """
        :returns: The string that you assigned to describe the resource.
        """
        return self._friendly_name

    @property
    def phone_number(self) -> Optional[str]:
        """
        :returns: The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        """
        return self._phone_number

    @property
    def validation_code(self) -> Optional[str]:
        """
        :returns: The 6 digit validation code that someone must enter to validate the Caller ID  when `phone_number` is called.
        """
        return self._validation_code

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.ValidationRequestInstance {}>".format(context)


class ValidationRequestList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the ValidationRequestList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the new caller ID resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/OutgoingCallerIds.json".format(
            **self._solution
        )

    def create(
        self,
        phone_number,
        friendly_name=values.unset,
        call_delay=values.unset,
        extension=values.unset,
        status_callback=values.unset,
        status_callback_method=values.unset,
    ) -> ValidationRequestInstance:
        """
        Create the ValidationRequestInstance

        :param str phone_number: The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        :param str friendly_name: A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number.
        :param int call_delay: The number of seconds to delay before initiating the verification call. Can be an integer between `0` and `60`, inclusive. The default is `0`.
        :param str extension: The digits to dial after connecting the verification call.
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information about the verification process to your application.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`, and the default is `POST`.

        :returns: The created ValidationRequestInstance
        """
        data = values.of(
            {
                "PhoneNumber": phone_number,
                "FriendlyName": friendly_name,
                "CallDelay": call_delay,
                "Extension": extension,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ValidationRequestInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def create_async(
        self,
        phone_number,
        friendly_name=values.unset,
        call_delay=values.unset,
        extension=values.unset,
        status_callback=values.unset,
        status_callback_method=values.unset,
    ) -> ValidationRequestInstance:
        """
        Asynchronously create the ValidationRequestInstance

        :param str phone_number: The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        :param str friendly_name: A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number.
        :param int call_delay: The number of seconds to delay before initiating the verification call. Can be an integer between `0` and `60`, inclusive. The default is `0`.
        :param str extension: The digits to dial after connecting the verification call.
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information about the verification process to your application.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`, and the default is `POST`.

        :returns: The created ValidationRequestInstance
        """
        data = values.of(
            {
                "PhoneNumber": phone_number,
                "FriendlyName": friendly_name,
                "CallDelay": call_delay,
                "Extension": extension,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ValidationRequestInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.ValidationRequestList>"
