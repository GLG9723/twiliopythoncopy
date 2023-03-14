r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class InsightsUserRolesList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the InsightsUserRolesList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesList
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a InsightsUserRolesContext


        :returns: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesContext
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesContext
        """
        return InsightsUserRolesContext(self._version)

    def __call__(self):
        """
        Constructs a InsightsUserRolesContext


        :returns: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesContext
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesContext
        """
        return InsightsUserRolesContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.InsightsUserRolesList>"


class InsightsUserRolesInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the InsightsUserRolesInstance

        :returns: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesInstance
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesInstance
        """
        super().__init__(version)

        self._properties = {
            "roles": payload.get("roles"),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InsightsUserRolesContext for this InsightsUserRolesInstance
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesContext
        """
        if self._context is None:
            self._context = InsightsUserRolesContext(
                self._version,
            )
        return self._context

    @property
    def roles(self):
        """
        :returns: Flex Insights roles for the user
        :rtype: list[str]
        """
        return self._properties["roles"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self, authorization=values.unset):
        """
        Fetch the InsightsUserRolesInstance

        :param str authorization: The Authorization HTTP request header

        :returns: The fetched InsightsUserRolesInstance
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesInstance
        """
        return self._proxy.fetch(
            authorization=authorization,
        )

    async def fetch_async(self, authorization=values.unset):
        """
        Asynchronous coroutine to fetch the InsightsUserRolesInstance

        :param str authorization: The Authorization HTTP request header

        :returns: The fetched InsightsUserRolesInstance
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesInstance
        """
        return await self._proxy.fetch_async(
            authorization=authorization,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InsightsUserRolesInstance {}>".format(context)


class InsightsUserRolesContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the InsightsUserRolesContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesContext
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Insights/UserRoles".format(**self._solution)

    def fetch(self, authorization=values.unset):
        """
        Fetch the InsightsUserRolesInstance

        :param str authorization: The Authorization HTTP request header

        :returns: The fetched InsightsUserRolesInstance
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesInstance
        """

        data = values.of(
            {
                "Authorization": authorization,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return InsightsUserRolesInstance(
            self._version,
            payload,
        )

    async def fetch_async(self, authorization=values.unset):
        """
        Asynchronous coroutine to fetch the InsightsUserRolesInstance

        :param str authorization: The Authorization HTTP request header

        :returns: The fetched InsightsUserRolesInstance
        :rtype: twilio.rest.flex_api.v1.insights_user_roles.InsightsUserRolesInstance
        """

        data = values.of(
            {
                "Authorization": authorization,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return InsightsUserRolesInstance(
            self._version,
            payload,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InsightsUserRolesContext {}>".format(context)
