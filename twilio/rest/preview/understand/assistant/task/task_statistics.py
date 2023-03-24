r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class TaskStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskStatisticsInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "assistant_sid": payload.get("assistant_sid"),
            "task_sid": payload.get("task_sid"),
            "samples_count": deserialize.integer(payload.get("samples_count")),
            "fields_count": deserialize.integer(payload.get("fields_count")),
            "url": payload.get("url"),
        }

        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }
        self._context: Optional[TaskStatisticsContext] = None

    @property
    def _proxy(self) -> "TaskStatisticsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskStatisticsContext for this TaskStatisticsInstance
        """
        if self._context is None:
            self._context = TaskStatisticsContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                task_sid=self._solution["task_sid"],
            )
        return self._context

    @property
    def account_sid(self) -> str:
        """
        :returns: The unique ID of the Account that created this Field.
        """
        return self._properties["account_sid"]

    @property
    def assistant_sid(self) -> str:
        """
        :returns: The unique ID of the parent Assistant.
        """
        return self._properties["assistant_sid"]

    @property
    def task_sid(self) -> str:
        """
        :returns: The unique ID of the Task associated with this Field.
        """
        return self._properties["task_sid"]

    @property
    def samples_count(self) -> int:
        """
        :returns: The total number of Samples associated with this Task.
        """
        return self._properties["samples_count"]

    @property
    def fields_count(self) -> int:
        """
        :returns: The total number of Fields associated with this Task.
        """
        return self._properties["fields_count"]

    @property
    def url(self) -> str:
        """
        :returns:
        """
        return self._properties["url"]

    def fetch(self) -> "TaskStatisticsInstance":
        """
        Fetch the TaskStatisticsInstance


        :returns: The fetched TaskStatisticsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "TaskStatisticsInstance":
        """
        Asynchronous coroutine to fetch the TaskStatisticsInstance


        :returns: The fetched TaskStatisticsInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.TaskStatisticsInstance {}>".format(context)


class TaskStatisticsContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskStatisticsContext

        :param version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.
        :param task_sid: The unique ID of the Task associated with this Field.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks/{task_sid}/Statistics".format(
            **self._solution
        )

    def fetch(self) -> TaskStatisticsInstance:
        """
        Fetch the TaskStatisticsInstance


        :returns: The fetched TaskStatisticsInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TaskStatisticsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    async def fetch_async(self) -> TaskStatisticsInstance:
        """
        Asynchronous coroutine to fetch the TaskStatisticsInstance


        :returns: The fetched TaskStatisticsInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TaskStatisticsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.TaskStatisticsContext {}>".format(context)


class TaskStatisticsList(ListResource):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskStatisticsList

        :param version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.
        :param task_sid: The unique ID of the Task associated with this Field.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }

    def get(self) -> TaskStatisticsContext:
        """
        Constructs a TaskStatisticsContext

        """
        return TaskStatisticsContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __call__(self) -> TaskStatisticsContext:
        """
        Constructs a TaskStatisticsContext

        """
        return TaskStatisticsContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Understand.TaskStatisticsList>"
