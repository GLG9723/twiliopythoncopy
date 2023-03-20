r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class FlowTestUserInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        """
        Initialize the FlowTestUserInstance

        :returns: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "test_users": payload.get("test_users"),
            "url": payload.get("url"),
        }

        self._solution = {
            "sid": sid,
        }
        self._context: Optional[FlowTestUserContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FlowTestUserContext for this FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserContext
        """
        if self._context is None:
            self._context = FlowTestUserContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: Unique identifier of the flow.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def test_users(self):
        """
        :returns: List of test user identities that can test draft versions of the flow.
        :rtype: list[str]
        """
        return self._properties["test_users"]

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self):
        """
        Fetch the FlowTestUserInstance


        :returns: The fetched FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FlowTestUserInstance


        :returns: The fetched FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserInstance
        """
        return await self._proxy.fetch_async()

    def update(self, test_users):
        """
        Update the FlowTestUserInstance

        :param list[str] test_users: List of test user identities that can test draft versions of the flow.

        :returns: The updated FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserInstance
        """
        return self._proxy.update(
            test_users=test_users,
        )

    async def update_async(self, test_users):
        """
        Asynchronous coroutine to update the FlowTestUserInstance

        :param list[str] test_users: List of test user identities that can test draft versions of the flow.

        :returns: The updated FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserInstance
        """
        return await self._proxy.update_async(
            test_users=test_users,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V2.FlowTestUserInstance {}>".format(context)


class FlowTestUserContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the FlowTestUserContext

        :param Version version: Version that contains the resource
        :param sid: Unique identifier of the flow.

        :returns: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserContext
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Flows/{sid}/TestUsers".format(**self._solution)

    def fetch(self):
        """
        Fetch the FlowTestUserInstance


        :returns: The fetched FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FlowTestUserInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FlowTestUserInstance


        :returns: The fetched FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FlowTestUserInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(self, test_users):
        """
        Update the FlowTestUserInstance

        :param list[str] test_users: List of test user identities that can test draft versions of the flow.

        :returns: The updated FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserInstance
        """
        data = values.of(
            {
                "TestUsers": serialize.map(test_users, lambda e: e),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FlowTestUserInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(self, test_users):
        """
        Asynchronous coroutine to update the FlowTestUserInstance

        :param list[str] test_users: List of test user identities that can test draft versions of the flow.

        :returns: The updated FlowTestUserInstance
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserInstance
        """
        data = values.of(
            {
                "TestUsers": serialize.map(test_users, lambda e: e),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FlowTestUserInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V2.FlowTestUserContext {}>".format(context)


class FlowTestUserList(ListResource):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the FlowTestUserList

        :param Version version: Version that contains the resource
        :param sid: Unique identifier of the flow.

        :returns: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserList
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }

    def get(self):
        """
        Constructs a FlowTestUserContext


        :returns: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserContext
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserContext
        """
        return FlowTestUserContext(self._version, sid=self._solution["sid"])

    def __call__(self):
        """
        Constructs a FlowTestUserContext


        :returns: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserContext
        :rtype: twilio.rest.studio.v2.flow.flow_test_user.FlowTestUserContext
        """
        return FlowTestUserContext(self._version, sid=self._solution["sid"])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Studio.V2.FlowTestUserList>"
