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


from typing import Dict, Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class StepContextInstance(InstanceResource):
    def __init__(
        self, version, payload, flow_sid: str, engagement_sid: str, step_sid: str
    ):
        """
        Initialize the StepContextInstance
        """
        super().__init__(version)

        self._account_sid: Optional[str] = payload.get("account_sid")
        self._context: Optional[Dict[str, object]] = payload.get("context")
        self._engagement_sid: Optional[str] = payload.get("engagement_sid")
        self._flow_sid: Optional[str] = payload.get("flow_sid")
        self._step_sid: Optional[str] = payload.get("step_sid")
        self._url: Optional[str] = payload.get("url")

        self._solution = {
            "flow_sid": flow_sid,
            "engagement_sid": engagement_sid,
            "step_sid": step_sid,
        }
        self._context: Optional[StepContextContext] = None

    @property
    def _proxy(self) -> "StepContextContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: StepContextContext for this StepContextInstance
        """
        if self._context is None:
            self._context = StepContextContext(
                self._version,
                flow_sid=self._solution["flow_sid"],
                engagement_sid=self._solution["engagement_sid"],
                step_sid=self._solution["step_sid"],
            )
        return self._context

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the StepContext resource.
        """
        return self._account_sid

    @property
    def context(self) -> Optional[Dict[str, object]]:
        """
        :returns: The current state of the Flow's Execution. As a flow executes, we save its state in this context. We save data that your widgets can access as variables in configuration fields or in text areas as variable substitution.
        """
        return self._context

    @property
    def engagement_sid(self) -> Optional[str]:
        """
        :returns: The SID of the Engagement.
        """
        return self._engagement_sid

    @property
    def flow_sid(self) -> Optional[str]:
        """
        :returns: The SID of the Flow.
        """
        return self._flow_sid

    @property
    def step_sid(self) -> Optional[str]:
        """
        :returns: The SID of the Step the context is associated with.
        """
        return self._step_sid

    @property
    def url(self) -> Optional[str]:
        """
        :returns: The absolute URL of the resource.
        """
        return self._url

    def fetch(self) -> "StepContextInstance":
        """
        Fetch the StepContextInstance


        :returns: The fetched StepContextInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "StepContextInstance":
        """
        Asynchronous coroutine to fetch the StepContextInstance


        :returns: The fetched StepContextInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V1.StepContextInstance {}>".format(context)


class StepContextContext(InstanceContext):
    def __init__(
        self, version: Version, flow_sid: str, engagement_sid: str, step_sid: str
    ):
        """
        Initialize the StepContextContext

        :param version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Step to fetch.
        :param engagement_sid: The SID of the Engagement with the Step to fetch.
        :param step_sid: The SID of the Step to fetch
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "flow_sid": flow_sid,
            "engagement_sid": engagement_sid,
            "step_sid": step_sid,
        }
        self._uri = "/Flows/{flow_sid}/Engagements/{engagement_sid}/Steps/{step_sid}/Context".format(
            **self._solution
        )

    def fetch(self) -> StepContextInstance:
        """
        Fetch the StepContextInstance


        :returns: The fetched StepContextInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return StepContextInstance(
            self._version,
            payload,
            flow_sid=self._solution["flow_sid"],
            engagement_sid=self._solution["engagement_sid"],
            step_sid=self._solution["step_sid"],
        )

    async def fetch_async(self) -> StepContextInstance:
        """
        Asynchronous coroutine to fetch the StepContextInstance


        :returns: The fetched StepContextInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return StepContextInstance(
            self._version,
            payload,
            flow_sid=self._solution["flow_sid"],
            engagement_sid=self._solution["engagement_sid"],
            step_sid=self._solution["step_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V1.StepContextContext {}>".format(context)


class StepContextList(ListResource):
    def __init__(
        self, version: Version, flow_sid: str, engagement_sid: str, step_sid: str
    ):
        """
        Initialize the StepContextList

        :param version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Step to fetch.
        :param engagement_sid: The SID of the Engagement with the Step to fetch.
        :param step_sid: The SID of the Step to fetch

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "flow_sid": flow_sid,
            "engagement_sid": engagement_sid,
            "step_sid": step_sid,
        }

    def get(self) -> StepContextContext:
        """
        Constructs a StepContextContext

        """
        return StepContextContext(
            self._version,
            flow_sid=self._solution["flow_sid"],
            engagement_sid=self._solution["engagement_sid"],
            step_sid=self._solution["step_sid"],
        )

    def __call__(self) -> StepContextContext:
        """
        Constructs a StepContextContext

        """
        return StepContextContext(
            self._version,
            flow_sid=self._solution["flow_sid"],
            engagement_sid=self._solution["engagement_sid"],
            step_sid=self._solution["step_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Studio.V1.StepContextList>"
