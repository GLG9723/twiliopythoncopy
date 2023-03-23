r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Accounts
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class SecondaryAuthTokenInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the SecondaryAuthTokenInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "secondary_auth_token": payload.get("secondary_auth_token"),
            "url": payload.get("url"),
        }

        self._solution = {}
        self._context: Optional[SecondaryAuthTokenContext] = None

    @property
    def _proxy(self) -> "SecondaryAuthTokenContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SecondaryAuthTokenContext for this SecondaryAuthTokenInstance
        """
        if self._context is None:
            self._context = SecondaryAuthTokenContext(
                self._version,
            )
        return self._context

    @property
    def account_sid(self) -> str:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the secondary Auth Token was created for.
        """
        return self._properties["account_sid"]

    @property
    def date_created(self) -> datetime:
        """
        :returns: The date and time in UTC when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns: The date and time in UTC when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        """
        return self._properties["date_updated"]

    @property
    def secondary_auth_token(self) -> str:
        """
        :returns: The generated secondary Auth Token that can be used to authenticate future API requests.
        """
        return self._properties["secondary_auth_token"]

    @property
    def url(self) -> str:
        """
        :returns: The URI for this resource, relative to `https://accounts.twilio.com`
        """
        return self._properties["url"]

    def create(self) -> "SecondaryAuthTokenInstance":
        """
        Create the SecondaryAuthTokenInstance


        :returns: The created SecondaryAuthTokenInstance
        """
        return self._proxy.create()

    async def create_async(self) -> "SecondaryAuthTokenInstance":
        """
        Asynchronous coroutine to create the SecondaryAuthTokenInstance


        :returns: The created SecondaryAuthTokenInstance
        """
        return await self._proxy.create_async()

    def delete(self) -> bool:
        """
        Deletes the SecondaryAuthTokenInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SecondaryAuthTokenInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Accounts.V1.SecondaryAuthTokenInstance {}>".format(context)


class SecondaryAuthTokenContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the SecondaryAuthTokenContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/AuthTokens/Secondary"

    def create(self) -> SecondaryAuthTokenInstance:
        """
        Create the SecondaryAuthTokenInstance


        :returns: The created SecondaryAuthTokenInstance
        """
        data = values.of({})

        payload = self._version.create(method="POST", uri=self._uri, data=data)

        return SecondaryAuthTokenInstance(self._version, payload)

    async def create_async(self) -> SecondaryAuthTokenInstance:
        """
        Asynchronous coroutine to create the SecondaryAuthTokenInstance


        :returns: The created SecondaryAuthTokenInstance
        """
        data = values.of({})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data
        )

        return SecondaryAuthTokenInstance(self._version, payload)

    def delete(self) -> bool:
        """
        Deletes the SecondaryAuthTokenInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SecondaryAuthTokenInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Accounts.V1.SecondaryAuthTokenContext>"


class SecondaryAuthTokenList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the SecondaryAuthTokenList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> SecondaryAuthTokenContext:
        """
        Constructs a SecondaryAuthTokenContext

        """
        return SecondaryAuthTokenContext(self._version)

    def __call__(self) -> SecondaryAuthTokenContext:
        """
        Constructs a SecondaryAuthTokenContext

        """
        return SecondaryAuthTokenContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Accounts.V1.SecondaryAuthTokenList>"
