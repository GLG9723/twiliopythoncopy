"""
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


from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class WorkersRealTimeStatisticsList(ListResource):
    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkersRealTimeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the resource to fetch.

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
        }

    def get(self):
        """
        Constructs a WorkersRealTimeStatisticsContext


        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsContext
        """
        return WorkersRealTimeStatisticsContext(
            self._version, workspace_sid=self._solution["workspace_sid"]
        )

    def __call__(self):
        """
        Constructs a WorkersRealTimeStatisticsContext


        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsContext
        """
        return WorkersRealTimeStatisticsContext(
            self._version, workspace_sid=self._solution["workspace_sid"]
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Taskrouter.V1.WorkersRealTimeStatisticsList>"


class WorkersRealTimeStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str):
        """
        Initialize the WorkersRealTimeStatisticsInstance

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "activity_statistics": payload.get("activity_statistics"),
            "total_workers": deserialize.integer(payload.get("total_workers")),
            "workspace_sid": payload.get("workspace_sid"),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {
            "workspace_sid": workspace_sid,
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WorkersRealTimeStatisticsContext for this WorkersRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsContext
        """
        if self._context is None:
            self._context = WorkersRealTimeStatisticsContext(
                self._version,
                workspace_sid=self._solution["workspace_sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Worker resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def activity_statistics(self):
        """
        :returns: The number of current Workers by Activity.
        :rtype: list[object]
        """
        return self._properties["activity_statistics"]

    @property
    def total_workers(self):
        """
        :returns: The total number of Workers.
        :rtype: int
        """
        return self._properties["total_workers"]

    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the Workers.
        :rtype: str
        """
        return self._properties["workspace_sid"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Workers statistics resource.
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self, task_channel=values.unset):
        """
        Fetch the WorkersRealTimeStatisticsInstance

        :param str task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkersRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsInstance
        """
        return self._proxy.fetch(
            task_channel=task_channel,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.WorkersRealTimeStatisticsInstance {}>".format(
            context
        )


class WorkersRealTimeStatisticsContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkersRealTimeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the resource to fetch.

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Workers/RealTimeStatistics".format(
            **self._solution
        )

    def fetch(self, task_channel=values.unset):
        """
        Fetch the WorkersRealTimeStatisticsInstance

        :param str task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkersRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics.WorkersRealTimeStatisticsInstance
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

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.WorkersRealTimeStatisticsContext {}>".format(
            context
        )
