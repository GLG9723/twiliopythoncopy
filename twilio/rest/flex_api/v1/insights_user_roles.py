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


from typing import Any, Dict, List, Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class InsightsUserRolesInstance(InstanceResource):

    """
    :ivar roles: Flex Insights roles for the user
    :ivar url:
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.roles: Optional[List[str]] = payload.get("roles")
        self.url: Optional[str] = payload.get("url")

        self._solution = {}
        self._context: Optional[InsightsUserRolesContext] = None

    @property
    def _proxy(self) -> "InsightsUserRolesContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InsightsUserRolesContext for this InsightsUserRolesInstance
        """
        if self._context is None:
            self._context = InsightsUserRolesContext(
                self._version,
            )
        return self._context

    def fetch(self, authorization=values.unset) -> "InsightsUserRolesInstance":
        """
        Fetch the InsightsUserRolesInstance

        :param str authorization: The Authorization HTTP request header

        :returns: The fetched InsightsUserRolesInstance
        """
        return self._proxy.fetch(
            authorization=authorization,
        )

    async def fetch_async(
        self, authorization=values.unset
    ) -> "InsightsUserRolesInstance":
        """
        Asynchronous coroutine to fetch the InsightsUserRolesInstance

        :param str authorization: The Authorization HTTP request header

        :returns: The fetched InsightsUserRolesInstance
        """
        return await self._proxy.fetch_async(
            authorization=authorization,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InsightsUserRolesInstance {}>".format(context)


class InsightsUserRolesContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the InsightsUserRolesContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/Insights/UserRoles"

    def fetch(self, authorization=values.unset) -> InsightsUserRolesInstance:
        """
        Fetch the InsightsUserRolesInstance

        :param str authorization: The Authorization HTTP request header

        :returns: The fetched InsightsUserRolesInstance
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

    async def fetch_async(
        self, authorization=values.unset
    ) -> InsightsUserRolesInstance:
        """
        Asynchronous coroutine to fetch the InsightsUserRolesInstance

        :param str authorization: The Authorization HTTP request header

        :returns: The fetched InsightsUserRolesInstance
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

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.FlexApi.V1.InsightsUserRolesContext>"


class InsightsUserRolesList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the InsightsUserRolesList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> InsightsUserRolesContext:
        """
        Constructs a InsightsUserRolesContext

        """
        return InsightsUserRolesContext(self._version)

    def __call__(self) -> InsightsUserRolesContext:
        """
        Constructs a InsightsUserRolesContext

        """
        return InsightsUserRolesContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsUserRolesList>"
