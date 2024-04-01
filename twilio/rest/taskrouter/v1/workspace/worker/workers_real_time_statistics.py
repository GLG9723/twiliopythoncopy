r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class WorkersRealTimeStatisticsInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Worker resource.
    :ivar activity_statistics: The number of current Workers by Activity.
    :ivar total_workers: The total number of Workers.
    :ivar workspace_sid: The SID of the Workspace that contains the Workers.
    :ivar url: The absolute URL of the Workers statistics resource.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], workspace_sid: str):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.activity_statistics: Optional[List[Dict[str, object]]] = payload.get(
            "activity_statistics"
        )
        self.total_workers: Optional[int] = deserialize.integer(
            payload.get("total_workers")
        )
        self.workspace_sid: Optional[str] = payload.get("workspace_sid")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "workspace_sid": workspace_sid,
        }
        self._context: Optional[WorkersRealTimeStatisticsContext] = None

    @property
    def _proxy(self) -> "WorkersRealTimeStatisticsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WorkersRealTimeStatisticsContext for this WorkersRealTimeStatisticsInstance
        """
        if self._context is None:
            self._context = WorkersRealTimeStatisticsContext(
                self._version,
                workspace_sid=self._solution["workspace_sid"],
            )
        return self._context

    def fetch(
        self, task_channel: Union[str, object] = values.unset
    ) -> "WorkersRealTimeStatisticsInstance":
        """
        Fetch the WorkersRealTimeStatisticsInstance

        :param task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkersRealTimeStatisticsInstance
        """
        return self._proxy.fetch(
            task_channel=task_channel,
        )

    async def fetch_async(
        self, task_channel: Union[str, object] = values.unset
    ) -> "WorkersRealTimeStatisticsInstance":
        """
        Asynchronous coroutine to fetch the WorkersRealTimeStatisticsInstance

        :param task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkersRealTimeStatisticsInstance
        """
        return await self._proxy.fetch_async(
            task_channel=task_channel,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.WorkersRealTimeStatisticsInstance {}>".format(
            context
        )


class WorkersRealTimeStatisticsContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkersRealTimeStatisticsContext

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Workers/RealTimeStatistics".format(
            **self._solution
        )

    def fetch(
        self, task_channel: Union[str, object] = values.unset
    ) -> WorkersRealTimeStatisticsInstance:
        """
        Fetch the WorkersRealTimeStatisticsInstance

        :param task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkersRealTimeStatisticsInstance
        """

        data = values.of(
            {
                "TaskChannel": task_channel,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return WorkersRealTimeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
        )

    async def fetch_async(
        self, task_channel: Union[str, object] = values.unset
    ) -> WorkersRealTimeStatisticsInstance:
        """
        Asynchronous coroutine to fetch the WorkersRealTimeStatisticsInstance

        :param task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkersRealTimeStatisticsInstance
        """

        data = values.of(
            {
                "TaskChannel": task_channel,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return WorkersRealTimeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.WorkersRealTimeStatisticsContext {}>".format(
            context
        )


class WorkersRealTimeStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkersRealTimeStatisticsList

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the resource to fetch.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
        }

    def get(self) -> WorkersRealTimeStatisticsContext:
        """
        Constructs a WorkersRealTimeStatisticsContext

        """
        return WorkersRealTimeStatisticsContext(
            self._version, workspace_sid=self._solution["workspace_sid"]
        )

    def __call__(self) -> WorkersRealTimeStatisticsContext:
        """
        Constructs a WorkersRealTimeStatisticsContext

        """
        return WorkersRealTimeStatisticsContext(
            self._version, workspace_sid=self._solution["workspace_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Taskrouter.V1.WorkersRealTimeStatisticsList>"
