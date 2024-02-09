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

from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class TaskQueueCumulativeStatisticsInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskQueue resource.
    :ivar avg_task_acceptance_time: The average time in seconds between Task creation and acceptance.
    :ivar start_time: The beginning of the interval during which these statistics were calculated, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar end_time: The end of the interval during which these statistics were calculated, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar reservations_created: The total number of Reservations created for Tasks in the TaskQueue.
    :ivar reservations_accepted: The total number of Reservations accepted for Tasks in the TaskQueue.
    :ivar reservations_rejected: The total number of Reservations rejected for Tasks in the TaskQueue.
    :ivar reservations_timed_out: The total number of Reservations that timed out for Tasks in the TaskQueue.
    :ivar reservations_canceled: The total number of Reservations canceled for Tasks in the TaskQueue.
    :ivar reservations_rescinded: The total number of Reservations rescinded.
    :ivar split_by_wait_time: A list of objects that describe the number of Tasks canceled and reservations accepted above and below the thresholds specified in seconds.
    :ivar task_queue_sid: The SID of the TaskQueue from which these statistics were calculated.
    :ivar wait_duration_until_accepted: The wait duration statistics (`avg`, `min`, `max`, `total`) for Tasks accepted while in the TaskQueue. Calculation is based on the time when the Tasks were created. For transfers, the wait duration is counted from the moment ***the Task was created***, and not from when the transfer was initiated.
    :ivar wait_duration_until_canceled: The wait duration statistics (`avg`, `min`, `max`, `total`) for Tasks canceled while in the TaskQueue.
    :ivar wait_duration_in_queue_until_accepted: The relative wait duration statistics (`avg`, `min`, `max`, `total`) for Tasks accepted while in the TaskQueue. Calculation is based on the time when the Tasks entered the TaskQueue.
    :ivar tasks_canceled: The total number of Tasks canceled in the TaskQueue.
    :ivar tasks_completed: The total number of Tasks completed in the TaskQueue.
    :ivar tasks_deleted: The total number of Tasks deleted in the TaskQueue.
    :ivar tasks_entered: The total number of Tasks entered into the TaskQueue.
    :ivar tasks_moved: The total number of Tasks that were moved from one queue to another.
    :ivar workspace_sid: The SID of the Workspace that contains the TaskQueue.
    :ivar url: The absolute URL of the TaskQueue statistics resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        workspace_sid: str,
        task_queue_sid: str,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.avg_task_acceptance_time: Optional[int] = deserialize.integer(
            payload.get("avg_task_acceptance_time")
        )
        self.start_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("start_time")
        )
        self.end_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("end_time")
        )
        self.reservations_created: Optional[int] = deserialize.integer(
            payload.get("reservations_created")
        )
        self.reservations_accepted: Optional[int] = deserialize.integer(
            payload.get("reservations_accepted")
        )
        self.reservations_rejected: Optional[int] = deserialize.integer(
            payload.get("reservations_rejected")
        )
        self.reservations_timed_out: Optional[int] = deserialize.integer(
            payload.get("reservations_timed_out")
        )
        self.reservations_canceled: Optional[int] = deserialize.integer(
            payload.get("reservations_canceled")
        )
        self.reservations_rescinded: Optional[int] = deserialize.integer(
            payload.get("reservations_rescinded")
        )
        self.split_by_wait_time: Optional[Dict[str, object]] = payload.get(
            "split_by_wait_time"
        )
        self.task_queue_sid: Optional[str] = payload.get("task_queue_sid")
        self.wait_duration_until_accepted: Optional[Dict[str, object]] = payload.get(
            "wait_duration_until_accepted"
        )
        self.wait_duration_until_canceled: Optional[Dict[str, object]] = payload.get(
            "wait_duration_until_canceled"
        )
        self.wait_duration_in_queue_until_accepted: Optional[Dict[str, object]] = (
            payload.get("wait_duration_in_queue_until_accepted")
        )
        self.tasks_canceled: Optional[int] = deserialize.integer(
            payload.get("tasks_canceled")
        )
        self.tasks_completed: Optional[int] = deserialize.integer(
            payload.get("tasks_completed")
        )
        self.tasks_deleted: Optional[int] = deserialize.integer(
            payload.get("tasks_deleted")
        )
        self.tasks_entered: Optional[int] = deserialize.integer(
            payload.get("tasks_entered")
        )
        self.tasks_moved: Optional[int] = deserialize.integer(
            payload.get("tasks_moved")
        )
        self.workspace_sid: Optional[str] = payload.get("workspace_sid")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "workspace_sid": workspace_sid,
            "task_queue_sid": task_queue_sid,
        }
        self._context: Optional[TaskQueueCumulativeStatisticsContext] = None

    @property
    def _proxy(self) -> "TaskQueueCumulativeStatisticsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskQueueCumulativeStatisticsContext for this TaskQueueCumulativeStatisticsInstance
        """
        if self._context is None:
            self._context = TaskQueueCumulativeStatisticsContext(
                self._version,
                workspace_sid=self._solution["workspace_sid"],
                task_queue_sid=self._solution["task_queue_sid"],
            )
        return self._context

    def fetch(
        self,
        end_date: Union[datetime, object] = values.unset,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> "TaskQueueCumulativeStatisticsInstance":
        """
        Fetch the TaskQueueCumulativeStatisticsInstance

        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. TaskRouter will calculate statistics on up to 10,000 Tasks/Reservations for any given threshold.

        :returns: The fetched TaskQueueCumulativeStatisticsInstance
        """
        return self._proxy.fetch(
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
        )

    async def fetch_async(
        self,
        end_date: Union[datetime, object] = values.unset,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> "TaskQueueCumulativeStatisticsInstance":
        """
        Asynchronous coroutine to fetch the TaskQueueCumulativeStatisticsInstance

        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. TaskRouter will calculate statistics on up to 10,000 Tasks/Reservations for any given threshold.

        :returns: The fetched TaskQueueCumulativeStatisticsInstance
        """
        return await self._proxy.fetch_async(
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.TaskQueueCumulativeStatisticsInstance {}>".format(
            context
        )


class TaskQueueCumulativeStatisticsContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str, task_queue_sid: str):
        """
        Initialize the TaskQueueCumulativeStatisticsContext

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
        :param task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
            "task_queue_sid": task_queue_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/CumulativeStatistics".format(
            **self._solution
        )

    def fetch(
        self,
        end_date: Union[datetime, object] = values.unset,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> TaskQueueCumulativeStatisticsInstance:
        """
        Fetch the TaskQueueCumulativeStatisticsInstance

        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. TaskRouter will calculate statistics on up to 10,000 Tasks/Reservations for any given threshold.

        :returns: The fetched TaskQueueCumulativeStatisticsInstance
        """

        data = values.of(
            {
                "EndDate": serialize.iso8601_datetime(end_date),
                "Minutes": minutes,
                "StartDate": serialize.iso8601_datetime(start_date),
                "TaskChannel": task_channel,
                "SplitByWaitTime": split_by_wait_time,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return TaskQueueCumulativeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            task_queue_sid=self._solution["task_queue_sid"],
        )

    async def fetch_async(
        self,
        end_date: Union[datetime, object] = values.unset,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
        split_by_wait_time: Union[str, object] = values.unset,
    ) -> TaskQueueCumulativeStatisticsInstance:
        """
        Asynchronous coroutine to fetch the TaskQueueCumulativeStatisticsInstance

        :param end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. TaskRouter will calculate statistics on up to 10,000 Tasks/Reservations for any given threshold.

        :returns: The fetched TaskQueueCumulativeStatisticsInstance
        """

        data = values.of(
            {
                "EndDate": serialize.iso8601_datetime(end_date),
                "Minutes": minutes,
                "StartDate": serialize.iso8601_datetime(start_date),
                "TaskChannel": task_channel,
                "SplitByWaitTime": split_by_wait_time,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return TaskQueueCumulativeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            task_queue_sid=self._solution["task_queue_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.TaskQueueCumulativeStatisticsContext {}>".format(
            context
        )


class TaskQueueCumulativeStatisticsList(ListResource):
    def __init__(self, version: Version, workspace_sid: str, task_queue_sid: str):
        """
        Initialize the TaskQueueCumulativeStatisticsList

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
        :param task_queue_sid: The SID of the TaskQueue for which to fetch statistics.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
            "task_queue_sid": task_queue_sid,
        }

    def get(self) -> TaskQueueCumulativeStatisticsContext:
        """
        Constructs a TaskQueueCumulativeStatisticsContext

        """
        return TaskQueueCumulativeStatisticsContext(
            self._version,
            workspace_sid=self._solution["workspace_sid"],
            task_queue_sid=self._solution["task_queue_sid"],
        )

    def __call__(self) -> TaskQueueCumulativeStatisticsContext:
        """
        Constructs a TaskQueueCumulativeStatisticsContext

        """
        return TaskQueueCumulativeStatisticsContext(
            self._version,
            workspace_sid=self._solution["workspace_sid"],
            task_queue_sid=self._solution["task_queue_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Taskrouter.V1.TaskQueueCumulativeStatisticsList>"
