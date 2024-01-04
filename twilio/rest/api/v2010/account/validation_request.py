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


from typing import Any, Dict, Optional, Union
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ValidationRequestInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the Caller ID.
    :ivar call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Caller ID is associated with.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar phone_number: The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
    :ivar validation_code: The 6 digit validation code that someone must enter to validate the Caller ID  when `phone_number` is called.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], account_sid: str):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.phone_number: Optional[str] = payload.get("phone_number")
        self.validation_code: Optional[str] = payload.get("validation_code")

        self._solution = {
            "account_sid": account_sid,
        }

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
        phone_number: str,
        friendly_name: Union[str, object] = values.unset,
        call_delay: Union[int, object] = values.unset,
        extension: Union[str, object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
    ) -> ValidationRequestInstance:
        """
        Create the ValidationRequestInstance

        :param phone_number: The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        :param friendly_name: A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number.
        :param call_delay: The number of seconds to delay before initiating the verification call. Can be an integer between `0` and `60`, inclusive. The default is `0`.
        :param extension: The digits to dial after connecting the verification call.
        :param status_callback: The URL we should call using the `status_callback_method` to send status information about the verification process to your application.
        :param status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`, and the default is `POST`.

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
        phone_number: str,
        friendly_name: Union[str, object] = values.unset,
        call_delay: Union[int, object] = values.unset,
        extension: Union[str, object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
    ) -> ValidationRequestInstance:
        """
        Asynchronously create the ValidationRequestInstance

        :param phone_number: The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        :param friendly_name: A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number.
        :param call_delay: The number of seconds to delay before initiating the verification call. Can be an integer between `0` and `60`, inclusive. The default is `0`.
        :param extension: The digits to dial after connecting the verification call.
        :param status_callback: The URL we should call using the `status_callback_method` to send status information about the verification process to your application.
        :param status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`, and the default is `POST`.

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
