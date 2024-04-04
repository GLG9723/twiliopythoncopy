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
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class WorkerStatisticsInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Worker resource.
    :ivar cumulative: An object that contains the cumulative statistics for the Worker.
    :ivar worker_sid: The SID of the Worker that contains the WorkerChannel.
    :ivar workspace_sid: The SID of the Workspace that contains the WorkerChannel.
    :ivar url: The absolute URL of the WorkerChannel statistics resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        workspace_sid: str,
        worker_sid: str,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.cumulative: Optional[Dict[str, object]] = payload.get("cumulative")
        self.worker_sid: Optional[str] = payload.get("worker_sid")
        self.workspace_sid: Optional[str] = payload.get("workspace_sid")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "workspace_sid": workspace_sid,
            "worker_sid": worker_sid,
        }
        self._context: Optional[WorkerStatisticsContext] = None

    @property
    def _proxy(self) -> "WorkerStatisticsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WorkerStatisticsContext for this WorkerStatisticsInstance
        """
        if self._context is None:
            self._context = WorkerStatisticsContext(
                self._version,
                workspace_sid=self._solution["workspace_sid"],
                worker_sid=self._solution["worker_sid"],
            )
        return self._context

    def fetch(
        self,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
    ) -> "WorkerStatisticsInstance":
        """
        Fetch the WorkerStatisticsInstance

        :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param end_date: Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkerStatisticsInstance
        """
        return self._proxy.fetch(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
            task_channel=task_channel,
        )

    async def fetch_async(
        self,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
    ) -> "WorkerStatisticsInstance":
        """
        Asynchronous coroutine to fetch the WorkerStatisticsInstance

        :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param end_date: Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkerStatisticsInstance
        """
        return await self._proxy.fetch_async(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
            task_channel=task_channel,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.WorkerStatisticsInstance {}>".format(context)


class WorkerStatisticsContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str, worker_sid: str):
        """
        Initialize the WorkerStatisticsContext

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
        :param worker_sid: The SID of the Worker with the WorkerChannel to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
            "worker_sid": worker_sid,
        }
        self._uri = (
            "/Workspaces/{workspace_sid}/Workers/{worker_sid}/Statistics".format(
                **self._solution
            )
        )

    def fetch(
        self,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
    ) -> WorkerStatisticsInstance:
        """
        Fetch the WorkerStatisticsInstance

        :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param end_date: Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkerStatisticsInstance
        """

        data = values.of(
            {
                "Minutes": minutes,
                "StartDate": serialize.iso8601_datetime(start_date),
                "EndDate": serialize.iso8601_datetime(end_date),
                "TaskChannel": task_channel,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return WorkerStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            worker_sid=self._solution["worker_sid"],
        )

    async def fetch_async(
        self,
        minutes: Union[int, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        task_channel: Union[str, object] = values.unset,
    ) -> WorkerStatisticsInstance:
        """
        Asynchronous coroutine to fetch the WorkerStatisticsInstance

        :param minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :param start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param end_date: Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkerStatisticsInstance
        """

        data = values.of(
            {
                "Minutes": minutes,
                "StartDate": serialize.iso8601_datetime(start_date),
                "EndDate": serialize.iso8601_datetime(end_date),
                "TaskChannel": task_channel,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return WorkerStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            worker_sid=self._solution["worker_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.WorkerStatisticsContext {}>".format(context)


class WorkerStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str, worker_sid: str):
        """
        Initialize the WorkerStatisticsList

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
        :param worker_sid: The SID of the Worker with the WorkerChannel to fetch.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
            "worker_sid": worker_sid,
        }

    def get(self) -> WorkerStatisticsContext:
        """
        Constructs a WorkerStatisticsContext

        """
        return WorkerStatisticsContext(
            self._version,
            workspace_sid=self._solution["workspace_sid"],
            worker_sid=self._solution["worker_sid"],
        )

    def __call__(self) -> WorkerStatisticsContext:
        """
        Constructs a WorkerStatisticsContext

        """
        return WorkerStatisticsContext(
            self._version,
            workspace_sid=self._solution["workspace_sid"],
            worker_sid=self._solution["worker_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Taskrouter.V1.WorkerStatisticsList>"
