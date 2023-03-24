r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Bulkexports
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


class JobInstance(InstanceResource):
    def __init__(self, version, payload, job_sid: Optional[str] = None):
        """
        Initialize the JobInstance
        """
        super().__init__(version)

        self._properties = {
            "resource_type": payload.get("resource_type"),
            "friendly_name": payload.get("friendly_name"),
            "details": payload.get("details"),
            "start_day": payload.get("start_day"),
            "end_day": payload.get("end_day"),
            "job_sid": payload.get("job_sid"),
            "webhook_url": payload.get("webhook_url"),
            "webhook_method": payload.get("webhook_method"),
            "email": payload.get("email"),
            "url": payload.get("url"),
            "job_queue_position": payload.get("job_queue_position"),
            "estimated_completion_time": payload.get("estimated_completion_time"),
        }

        self._solution = {
            "job_sid": job_sid or self._properties["job_sid"],
        }
        self._context: Optional[JobContext] = None

    @property
    def _proxy(self) -> "JobContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: JobContext for this JobInstance
        """
        if self._context is None:
            self._context = JobContext(
                self._version,
                job_sid=self._solution["job_sid"],
            )
        return self._context

    @property
    def resource_type(self) -> str:
        """
        :returns: The type of communication – Messages, Calls, Conferences, and Participants
        """
        return self._properties["resource_type"]

    @property
    def friendly_name(self) -> str:
        """
        :returns: The friendly name specified when creating the job
        """
        return self._properties["friendly_name"]

    @property
    def details(self) -> Dict[str, object]:
        """
        :returns: The details of a job which is an object that contains an array of status grouped by `status` state.  Each `status` object has a `status` string, a count which is the number of days in that `status`, and list of days in that `status`. The day strings are in the format yyyy-MM-dd. As an example, a currently running job may have a status object for COMPLETED and a `status` object for SUBMITTED each with its own count and list of days.
        """
        return self._properties["details"]

    @property
    def start_day(self) -> str:
        """
        :returns: The start time for the export specified when creating the job
        """
        return self._properties["start_day"]

    @property
    def end_day(self) -> str:
        """
        :returns: The end time for the export specified when creating the job
        """
        return self._properties["end_day"]

    @property
    def job_sid(self) -> str:
        """
        :returns: The job_sid returned when the export was created
        """
        return self._properties["job_sid"]

    @property
    def webhook_url(self) -> str:
        """
        :returns: The optional webhook url called on completion
        """
        return self._properties["webhook_url"]

    @property
    def webhook_method(self) -> str:
        """
        :returns: This is the method used to call the webhook
        """
        return self._properties["webhook_method"]

    @property
    def email(self) -> str:
        """
        :returns: The optional email to send the completion notification to
        """
        return self._properties["email"]

    @property
    def url(self) -> str:
        """
        :returns:
        """
        return self._properties["url"]

    @property
    def job_queue_position(self) -> str:
        """
        :returns: This is the job position from the 1st in line. Your queue position will never increase. As jobs ahead of yours in the queue are processed, the queue position number will decrease
        """
        return self._properties["job_queue_position"]

    @property
    def estimated_completion_time(self) -> str:
        """
        :returns: this is the time estimated until your job is complete. This is calculated each time you request the job list. The time is calculated based on the current rate of job completion (which may vary) and your job queue position
        """
        return self._properties["estimated_completion_time"]

    def delete(self) -> bool:
        """
        Deletes the JobInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the JobInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "JobInstance":
        """
        Fetch the JobInstance


        :returns: The fetched JobInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "JobInstance":
        """
        Asynchronous coroutine to fetch the JobInstance


        :returns: The fetched JobInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Bulkexports.V1.JobInstance {}>".format(context)


class JobContext(InstanceContext):
    def __init__(self, version: Version, job_sid: str):
        """
        Initialize the JobContext

        :param version: Version that contains the resource
        :param job_sid: The unique string that that we created to identify the Bulk Export job
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "job_sid": job_sid,
        }
        self._uri = "/Exports/Jobs/{job_sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the JobInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the JobInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> JobInstance:
        """
        Fetch the JobInstance


        :returns: The fetched JobInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return JobInstance(
            self._version,
            payload,
            job_sid=self._solution["job_sid"],
        )

    async def fetch_async(self) -> JobInstance:
        """
        Asynchronous coroutine to fetch the JobInstance


        :returns: The fetched JobInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return JobInstance(
            self._version,
            payload,
            job_sid=self._solution["job_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Bulkexports.V1.JobContext {}>".format(context)


class JobList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the JobList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, job_sid) -> JobContext:
        """
        Constructs a JobContext

        :param job_sid: The unique string that that we created to identify the Bulk Export job
        """
        return JobContext(self._version, job_sid=job_sid)

    def __call__(self, job_sid) -> JobContext:
        """
        Constructs a JobContext

        :param job_sid: The unique string that that we created to identify the Bulk Export job
        """
        return JobContext(self._version, job_sid=job_sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Bulkexports.V1.JobList>"
