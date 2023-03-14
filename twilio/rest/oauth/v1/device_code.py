r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Oauth
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class DeviceCodeList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the DeviceCodeList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.oauth.v1.device_code.DeviceCodeList
        :rtype: twilio.rest.oauth.v1.device_code.DeviceCodeList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/device/code".format(**self._solution)

    def create(self, client_sid, scopes, audiences=values.unset):
        """
        Create the DeviceCodeInstance

        :param str client_sid: A 34 character string that uniquely identifies this OAuth App.
        :param list[str] scopes: An Array of scopes for authorization request
        :param list[str] audiences: An array of intended audiences for token requests

        :returns: The created DeviceCodeInstance
        :rtype: twilio.rest.oauth.v1.device_code.DeviceCodeInstance
        """
        data = values.of(
            {
                "ClientSid": client_sid,
                "Scopes": serialize.map(scopes, lambda e: e),
                "Audiences": serialize.map(audiences, lambda e: e),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceCodeInstance(self._version, payload)

    async def create_async(self, client_sid, scopes, audiences=values.unset):
        """
        Asynchronously create the DeviceCodeInstance

        :param str client_sid: A 34 character string that uniquely identifies this OAuth App.
        :param list[str] scopes: An Array of scopes for authorization request
        :param list[str] audiences: An array of intended audiences for token requests

        :returns: The created DeviceCodeInstance
        :rtype: twilio.rest.oauth.v1.device_code.DeviceCodeInstance
        """
        data = values.of(
            {
                "ClientSid": client_sid,
                "Scopes": serialize.map(scopes, lambda e: e),
                "Audiences": serialize.map(audiences, lambda e: e),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceCodeInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Oauth.V1.DeviceCodeList>"


class DeviceCodeInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the DeviceCodeInstance

        :returns: twilio.rest.oauth.v1.device_code.DeviceCodeInstance
        :rtype: twilio.rest.oauth.v1.device_code.DeviceCodeInstance
        """
        super().__init__(version)

        self._properties = {
            "device_code": payload.get("device_code"),
            "user_code": payload.get("user_code"),
            "verification_uri": payload.get("verification_uri"),
            "verification_uri_complete": payload.get("verification_uri_complete"),
            "expires_in": payload.get("expires_in"),
            "interval": deserialize.integer(payload.get("interval")),
        }

        self._context = None
        self._solution = {}

    @property
    def device_code(self):
        """
        :returns: The device verification code.
        :rtype: str
        """
        return self._properties["device_code"]

    @property
    def user_code(self):
        """
        :returns: The verification code which end user uses to verify authorization request.
        :rtype: str
        """
        return self._properties["user_code"]

    @property
    def verification_uri(self):
        """
        :returns: The URI that the end user visits to verify authorization request.
        :rtype: str
        """
        return self._properties["verification_uri"]

    @property
    def verification_uri_complete(self):
        """
        :returns: The URI with user_code that the end-user alternatively visits to verify authorization request.
        :rtype: str
        """
        return self._properties["verification_uri_complete"]

    @property
    def expires_in(self):
        """
        :returns: The expiration time of the device_code and user_code in seconds.
        :rtype: int
        """
        return self._properties["expires_in"]

    @property
    def interval(self):
        """
        :returns: The minimum amount of time in seconds that the client should wait between polling requests to the token endpoint.
        :rtype: int
        """
        return self._properties["interval"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Oauth.V1.DeviceCodeInstance {}>".format(context)
