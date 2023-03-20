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

        :returns: twilio.rest.oauth.v1.user_info.UserInfoInstance
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoInstance
        """
        super().__init__(version)

        self._properties = {
            "user_sid": payload.get("user_sid"),
            "first_name": payload.get("first_name"),
            "last_name": payload.get("last_name"),
            "friendly_name": payload.get("friendly_name"),
            "email": payload.get("email"),
            "url": payload.get("url"),
        }

        self._solution = {}
        self._context: Optional[UserInfoContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserInfoContext for this UserInfoInstance
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoContext
        """
        if self._context is None:
            self._context = UserInfoContext(
                self._version,
            )
        return self._context

    @property
    def user_sid(self):
        """
        :returns: The URL of the party that will create the token and sign it with its private key.
        :rtype: str
        """
        return self._properties["user_sid"]

    @property
    def first_name(self):
        """
        :returns: The first name of the end-user.
        :rtype: str
        """
        return self._properties["first_name"]

    @property
    def last_name(self):
        """
        :returns: The last name of the end-user.
        :rtype: str
        """
        return self._properties["last_name"]

    @property
    def friendly_name(self):
        """
        :returns: The friendly name of the end-user.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def email(self):
        """
        :returns: The end-user's preferred email address.
        :rtype: str
        """
        return self._properties["email"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self):
        """
        Fetch the UserInfoInstance


        :returns: The fetched UserInfoInstance
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the UserInfoInstance


        :returns: The fetched UserInfoInstance
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Oauth.V1.UserInfoInstance {}>".format(context)


class UserInfoContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the UserInfoContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.oauth.v1.user_info.UserInfoContext
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoContext
        """
        super().__init__(version)

        self._uri = "/userinfo"

    def fetch(self):
        """
        Fetch the UserInfoInstance


        :returns: The fetched UserInfoInstance
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UserInfoInstance(
            self._version,
            payload,
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the UserInfoInstance


        :returns: The fetched UserInfoInstance
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UserInfoInstance(
            self._version,
            payload,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """

        return "<Twilio.Oauth.V1.UserInfoContext>"


class UserInfoList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the UserInfoList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.oauth.v1.user_info.UserInfoList
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoList
        """
        super().__init__(version)

    def get(self):
        """
        Constructs a UserInfoContext


        :returns: twilio.rest.oauth.v1.user_info.UserInfoContext
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoContext
        """
        return UserInfoContext(self._version)

    def __call__(self):
        """
        Constructs a UserInfoContext


        :returns: twilio.rest.oauth.v1.user_info.UserInfoContext
        :rtype: twilio.rest.oauth.v1.user_info.UserInfoContext
        """
        return UserInfoContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Oauth.V1.UserInfoList>"
