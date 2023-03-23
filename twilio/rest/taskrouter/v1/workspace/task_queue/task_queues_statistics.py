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


from typing import List
from twilio.base import serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class TaskQueuesStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str):
        """
        Initialize the TaskQueuesStatisticsInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "cumulative": payload.get("cumulative"),
            "realtime": payload.get("realtime"),
            "task_queue_sid": payload.get("task_queue_sid"),
            "workspace_sid": payload.get("workspace_sid"),
        }

        self._solution = {
            "workspace_sid": workspace_sid,
        }

    @property
    def account_sid(self) -> str:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskQueue resource.
        """
        return self._properties["account_sid"]

    @property
    def cumulative(self) -> dict:
        """
        :returns: An object that contains the cumulative statistics for the TaskQueues.
        """
        return self._properties["cumulative"]

    @property
    def realtime(self) -> dict:
        """
        :returns: An object that contains the real-time statistics for the TaskQueues.
        """
        return self._properties["realtime"]

    @property
    def task_queue_sid(self) -> str:
        """
        :returns: The SID of the TaskQueue from which these statistics were calculated.
        """
        return self._properties["task_queue_sid"]

    @property
    def workspace_sid(self) -> str:
        """
        :returns: The SID of the Workspace that contains the TaskQueues.
        """
        return self._properties["workspace_sid"]

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.TaskQueuesStatisticsInstance {}>".format(context)


class TaskQueuesStatisticsPage(Page):
    def get_instance(self, payload) -> TaskQueuesStatisticsInstance:
        """
        Build an instance of TaskQueuesStatisticsInstance

        :param dict payload: Payload response from the API
        """
        return TaskQueuesStatisticsInstance(
            self._version, payload, workspace_sid=self._solution["workspace_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Taskrouter.V1.TaskQueuesStatisticsPage>"


class TaskQueuesStatisticsList(ListResource):
    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the TaskQueuesStatisticsList

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the TaskQueues to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/TaskQueues/Statistics".format(
            **self._solution
        )

    def stream(
        self,
        end_date=values.unset,
        friendly_name=values.unset,
        minutes=values.unset,
        start_date=values.unset,
        task_channel=values.unset,
        split_by_wait_time=values.unset,
        limit=None,
        page_size=None,
    ) -> List[TaskQueuesStatisticsInstance]:
        """
        Streams TaskQueuesStatisticsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param str friendly_name: The `friendly_name` of the TaskQueue statistics to read.
        :param int minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param str task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            end_date=end_date,
            friendly_name=friendly_name,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        end_date=values.unset,
        friendly_name=values.unset,
        minutes=values.unset,
        start_date=values.unset,
        task_channel=values.unset,
        split_by_wait_time=values.unset,
        limit=None,
        page_size=None,
    ) -> List[TaskQueuesStatisticsInstance]:
        """
        Asynchronously streams TaskQueuesStatisticsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param str friendly_name: The `friendly_name` of the TaskQueue statistics to read.
        :param int minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param str task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            end_date=end_date,
            friendly_name=friendly_name,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        end_date=values.unset,
        friendly_name=values.unset,
        minutes=values.unset,
        start_date=values.unset,
        task_channel=values.unset,
        split_by_wait_time=values.unset,
        limit=None,
        page_size=None,
    ) -> List[TaskQueuesStatisticsInstance]:
        """
        Lists TaskQueuesStatisticsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param str friendly_name: The `friendly_name` of the TaskQueue statistics to read.
        :param int minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param str task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            self.stream(
                end_date=end_date,
                friendly_name=friendly_name,
                minutes=minutes,
                start_date=start_date,
                task_channel=task_channel,
                split_by_wait_time=split_by_wait_time,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        end_date=values.unset,
        friendly_name=values.unset,
        minutes=values.unset,
        start_date=values.unset,
        task_channel=values.unset,
        split_by_wait_time=values.unset,
        limit=None,
        page_size=None,
    ) -> List[TaskQueuesStatisticsInstance]:
        """
        Asynchronously lists TaskQueuesStatisticsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param str friendly_name: The `friendly_name` of the TaskQueue statistics to read.
        :param int minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param str task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            await self.stream_async(
                end_date=end_date,
                friendly_name=friendly_name,
                minutes=minutes,
                start_date=start_date,
                task_channel=task_channel,
                split_by_wait_time=split_by_wait_time,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        end_date=values.unset,
        friendly_name=values.unset,
        minutes=values.unset,
        start_date=values.unset,
        task_channel=values.unset,
        split_by_wait_time=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> TaskQueuesStatisticsPage:
        """
        Retrieve a single page of TaskQueuesStatisticsInstance records from the API.
        Request is executed immediately

        :param datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param str friendly_name: The `friendly_name` of the TaskQueue statistics to read.
        :param int minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param str task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TaskQueuesStatisticsInstance
        """
        data = values.of(
            {
                "EndDate": serialize.iso8601_datetime(end_date),
                "FriendlyName": friendly_name,
                "Minutes": minutes,
                "StartDate": serialize.iso8601_datetime(start_date),
                "TaskChannel": task_channel,
                "SplitByWaitTime": split_by_wait_time,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return TaskQueuesStatisticsPage(self._version, response, self._solution)

    async def page_async(
        self,
        end_date=values.unset,
        friendly_name=values.unset,
        minutes=values.unset,
        start_date=values.unset,
        task_channel=values.unset,
        split_by_wait_time=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> TaskQueuesStatisticsPage:
        """
        Asynchronously retrieve a single page of TaskQueuesStatisticsInstance records from the API.
        Request is executed immediately

        :param datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param str friendly_name: The `friendly_name` of the TaskQueue statistics to read.
        :param int minutes: Only calculate statistics since this many minutes in the past. The default is 15 minutes.
        :param datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param str task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :param str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TaskQueuesStatisticsInstance
        """
        data = values.of(
            {
                "EndDate": serialize.iso8601_datetime(end_date),
                "FriendlyName": friendly_name,
                "Minutes": minutes,
                "StartDate": serialize.iso8601_datetime(start_date),
                "TaskChannel": task_channel,
                "SplitByWaitTime": split_by_wait_time,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return TaskQueuesStatisticsPage(self._version, response, self._solution)

    def get_page(self, target_url) -> TaskQueuesStatisticsPage:
        """
        Retrieve a specific page of TaskQueuesStatisticsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TaskQueuesStatisticsInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return TaskQueuesStatisticsPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> TaskQueuesStatisticsPage:
        """
        Asynchronously retrieve a specific page of TaskQueuesStatisticsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TaskQueuesStatisticsInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return TaskQueuesStatisticsPage(self._version, response, self._solution)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Taskrouter.V1.TaskQueuesStatisticsList>"
