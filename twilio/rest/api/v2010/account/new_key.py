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


from datetime import datetime
from typing import Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class NewKeyInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str):
        """
        Initialize the NewKeyInstance
        """
        super().__init__(version)

        self._sid: Optional[str] = payload.get("sid")
        self._friendly_name: Optional[str] = payload.get("friendly_name")
        self._date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self._secret: Optional[str] = payload.get("secret")

        self._solution = {
            "account_sid": account_sid,
        }

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that that we created to identify the NewKey resource. You will use this as the basic-auth `user` when authenticating to the API.
        """
        return self._sid

    @property
    def friendly_name(self) -> Optional[str]:
        """
        :returns: The string that you assigned to describe the resource.
        """
        return self._friendly_name

    @property
    def date_created(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT that the API Key was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._date_created

    @property
    def date_updated(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT that the new API Key was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._date_updated

    @property
    def secret(self) -> Optional[str]:
        """
        :returns: The secret your application uses to sign Access Tokens and to authenticate to the REST API (you will use this as the basic-auth `password`).  **Note that for security reasons, this field is ONLY returned when the API Key is first created.**
        """
        return self._secret

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.NewKeyInstance {}>".format(context)


class NewKeyList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the NewKeyList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Key resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Keys.json".format(**self._solution)

    def create(self, friendly_name=values.unset) -> NewKeyInstance:
        """
        Create the NewKeyInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The created NewKeyInstance
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

        return NewKeyInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def create_async(self, friendly_name=values.unset) -> NewKeyInstance:
        """
        Asynchronously create the NewKeyInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The created NewKeyInstance
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

        return NewKeyInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.NewKeyList>"
