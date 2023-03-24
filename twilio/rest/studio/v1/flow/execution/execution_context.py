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


class ExecutionContextInstance(InstanceResource):
    def __init__(self, version, payload, flow_sid: str, execution_sid: str):
        """
        Initialize the ExecutionContextInstance
        """
        super().__init__(version)

        self._account_sid: Optional[str] = payload.get("account_sid")
        self._context: Optional[Dict[str, object]] = payload.get("context")
        self._flow_sid: Optional[str] = payload.get("flow_sid")
        self._execution_sid: Optional[str] = payload.get("execution_sid")
        self._url: Optional[str] = payload.get("url")

        self._solution = {
            "flow_sid": flow_sid,
            "execution_sid": execution_sid,
        }
        self._context: Optional[ExecutionContextContext] = None

    @property
    def _proxy(self) -> "ExecutionContextContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ExecutionContextContext for this ExecutionContextInstance
        """
        if self._context is None:
            self._context = ExecutionContextContext(
                self._version,
                flow_sid=self._solution["flow_sid"],
                execution_sid=self._solution["execution_sid"],
            )
        return self._context

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ExecutionContext resource.
        """
        return self._account_sid

    @property
    def context(self) -> Optional[Dict[str, object]]:
        """
        :returns: The current state of the Flow's Execution. As a flow executes, we save its state in this context. We save data that your widgets can access as variables in configuration fields or in text areas as variable substitution.
        """
        return self._context

    @property
    def flow_sid(self) -> Optional[str]:
        """
        :returns: The SID of the Flow.
        """
        return self._flow_sid

    @property
    def execution_sid(self) -> Optional[str]:
        """
        :returns: The SID of the context's Execution resource.
        """
        return self._execution_sid

    @property
    def url(self) -> Optional[str]:
        """
        :returns: The absolute URL of the resource.
        """
        return self._url

    def fetch(self) -> "ExecutionContextInstance":
        """
        Fetch the ExecutionContextInstance


        :returns: The fetched ExecutionContextInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ExecutionContextInstance":
        """
        Asynchronous coroutine to fetch the ExecutionContextInstance


        :returns: The fetched ExecutionContextInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V1.ExecutionContextInstance {}>".format(context)


class ExecutionContextContext(InstanceContext):
    def __init__(self, version: Version, flow_sid: str, execution_sid: str):
        """
        Initialize the ExecutionContextContext

        :param version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Execution context to fetch.
        :param execution_sid: The SID of the Execution context to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "flow_sid": flow_sid,
            "execution_sid": execution_sid,
        }
        self._uri = "/Flows/{flow_sid}/Executions/{execution_sid}/Context".format(
            **self._solution
        )

    def fetch(self) -> ExecutionContextInstance:
        """
        Fetch the ExecutionContextInstance


        :returns: The fetched ExecutionContextInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ExecutionContextInstance(
            self._version,
            payload,
            flow_sid=self._solution["flow_sid"],
            execution_sid=self._solution["execution_sid"],
        )

    async def fetch_async(self) -> ExecutionContextInstance:
        """
        Asynchronous coroutine to fetch the ExecutionContextInstance


        :returns: The fetched ExecutionContextInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ExecutionContextInstance(
            self._version,
            payload,
            flow_sid=self._solution["flow_sid"],
            execution_sid=self._solution["execution_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V1.ExecutionContextContext {}>".format(context)


class ExecutionContextList(ListResource):
    def __init__(self, version: Version, flow_sid: str, execution_sid: str):
        """
        Initialize the ExecutionContextList

        :param version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Execution context to fetch.
        :param execution_sid: The SID of the Execution context to fetch.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "flow_sid": flow_sid,
            "execution_sid": execution_sid,
        }

    def get(self) -> ExecutionContextContext:
        """
        Constructs a ExecutionContextContext

        """
        return ExecutionContextContext(
            self._version,
            flow_sid=self._solution["flow_sid"],
            execution_sid=self._solution["execution_sid"],
        )

    def __call__(self) -> ExecutionContextContext:
        """
        Constructs a ExecutionContextContext

        """
        return ExecutionContextContext(
            self._version,
            flow_sid=self._solution["flow_sid"],
            execution_sid=self._solution["execution_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Studio.V1.ExecutionContextList>"
