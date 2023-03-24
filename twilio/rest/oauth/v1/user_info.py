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


from typing import Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class UserInfoInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the UserInfoInstance
        """
        super().__init__(version)

        self._user_sid: Optional[str] = payload.get("user_sid")
        self._first_name: Optional[str] = payload.get("first_name")
        self._last_name: Optional[str] = payload.get("last_name")
        self._friendly_name: Optional[str] = payload.get("friendly_name")
        self._email: Optional[str] = payload.get("email")
        self._url: Optional[str] = payload.get("url")

        self._solution = {}
        self._context: Optional[UserInfoContext] = None

    @property
    def _proxy(self) -> "UserInfoContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserInfoContext for this UserInfoInstance
        """
        if self._context is None:
            self._context = UserInfoContext(
                self._version,
            )
        return self._context

    @property
    def user_sid(self) -> Optional[str]:
        """
        :returns: The URL of the party that will create the token and sign it with its private key.
        """
        return self._user_sid

    @property
    def first_name(self) -> Optional[str]:
        """
        :returns: The first name of the end-user.
        """
        return self._first_name

    @property
    def last_name(self) -> Optional[str]:
        """
        :returns: The last name of the end-user.
        """
        return self._last_name

    @property
    def friendly_name(self) -> Optional[str]:
        """
        :returns: The friendly name of the end-user.
        """
        return self._friendly_name

    @property
    def email(self) -> Optional[str]:
        """
        :returns: The end-user's preferred email address.
        """
        return self._email

    @property
    def url(self) -> Optional[str]:
        return self._url

    def fetch(self) -> "UserInfoInstance":
        """
        Fetch the UserInfoInstance


        :returns: The fetched UserInfoInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "UserInfoInstance":
        """
        Asynchronous coroutine to fetch the UserInfoInstance


        :returns: The fetched UserInfoInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Oauth.V1.UserInfoInstance {}>".format(context)


class UserInfoContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the UserInfoContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/userinfo"

    def fetch(self) -> UserInfoInstance:
        """
        Fetch the UserInfoInstance


        :returns: The fetched UserInfoInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UserInfoInstance(
            self._version,
            payload,
        )

    async def fetch_async(self) -> UserInfoInstance:
        """
        Asynchronous coroutine to fetch the UserInfoInstance


        :returns: The fetched UserInfoInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UserInfoInstance(
            self._version,
            payload,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Oauth.V1.UserInfoContext>"


class UserInfoList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the UserInfoList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> UserInfoContext:
        """
        Constructs a UserInfoContext

        """
        return UserInfoContext(self._version)

    def __call__(self) -> UserInfoContext:
        """
        Constructs a UserInfoContext

        """
        return UserInfoContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Oauth.V1.UserInfoList>"
