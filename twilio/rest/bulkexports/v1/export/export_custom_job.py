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

from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ExportCustomJobInstance(InstanceResource):
    """
    :ivar friendly_name: The friendly name specified when creating the job
    :ivar resource_type: The type of communication – Messages, Calls, Conferences, and Participants
    :ivar start_day: The start day for the custom export specified when creating the job
    :ivar end_day: The end day for the export specified when creating the job
    :ivar webhook_url: The optional webhook url called on completion of the job. If this is supplied, `WebhookMethod` must also be supplied.
    :ivar webhook_method: This is the method used to call the webhook on completion of the job. If this is supplied, `WebhookUrl` must also be supplied.
    :ivar email: The optional email to send the completion notification to
    :ivar job_sid: The unique job_sid returned when the custom export was created
    :ivar details: The details of a job which is an object that contains an array of status grouped by `status` state.  Each `status` object has a `status` string, a count which is the number of days in that `status`, and list of days in that `status`. The day strings are in the format yyyy-MM-dd. As an example, a currently running job may have a status object for COMPLETED and a `status` object for SUBMITTED each with its own count and list of days.
    :ivar job_queue_position: This is the job position from the 1st in line. Your queue position will never increase. As jobs ahead of yours in the queue are processed, the queue position number will decrease
    :ivar estimated_completion_time: this is the time estimated until your job is complete. This is calculated each time you request the job list. The time is calculated based on the current rate of job completion (which may vary) and your job queue position
    """

    def __init__(self, version: Version, payload: Dict[str, Any], resource_type: str):
        super().__init__(version)

        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.resource_type: Optional[str] = payload.get("resource_type")
        self.start_day: Optional[str] = payload.get("start_day")
        self.end_day: Optional[str] = payload.get("end_day")
        self.webhook_url: Optional[str] = payload.get("webhook_url")
        self.webhook_method: Optional[str] = payload.get("webhook_method")
        self.email: Optional[str] = payload.get("email")
        self.job_sid: Optional[str] = payload.get("job_sid")
        self.details: Optional[Dict[str, object]] = payload.get("details")
        self.job_queue_position: Optional[str] = payload.get("job_queue_position")
        self.estimated_completion_time: Optional[str] = payload.get(
            "estimated_completion_time"
        )

        self._solution = {
            "resource_type": resource_type,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Bulkexports.V1.ExportCustomJobInstance {context}>"


class ExportCustomJobPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> ExportCustomJobInstance:
        """
        Build an instance of ExportCustomJobInstance

        :param payload: Payload response from the API
        """
        return ExportCustomJobInstance(
            self._version, payload, resource_type=self._solution["resource_type"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Bulkexports.V1.ExportCustomJobPage>"


class ExportCustomJobList(ListResource):

    def __init__(self, version: Version, resource_type: str):
        """
        Initialize the ExportCustomJobList

        :param version: Version that contains the resource
        :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "resource_type": resource_type,
        }
        self._uri = "/Exports/{resource_type}/Jobs".format(**self._solution)

    def create(
        self,
        start_day: str,
        end_day: str,
        friendly_name: str,
        webhook_url: Union[str, object] = values.unset,
        webhook_method: Union[str, object] = values.unset,
        email: Union[str, object] = values.unset,
    ) -> ExportCustomJobInstance:
        """
        Create the ExportCustomJobInstance

        :param start_day: The start day for the custom export specified as a string in the format of yyyy-mm-dd
        :param end_day: The end day for the custom export specified as a string in the format of yyyy-mm-dd. End day is inclusive and must be 2 days earlier than the current UTC day.
        :param friendly_name: The friendly name specified when creating the job
        :param webhook_url: The optional webhook url called on completion of the job. If this is supplied, `WebhookMethod` must also be supplied. If you set neither webhook nor email, you will have to check your job's status manually.
        :param webhook_method: This is the method used to call the webhook on completion of the job. If this is supplied, `WebhookUrl` must also be supplied.
        :param email: The optional email to send the completion notification to. You can set both webhook, and email, or one or the other. If you set neither, the job will run but you will have to query to determine your job's status.

        :returns: The created ExportCustomJobInstance
        """

        data = values.of(
            {
                "StartDay": start_day,
                "EndDay": end_day,
                "FriendlyName": friendly_name,
                "WebhookUrl": webhook_url,
                "WebhookMethod": webhook_method,
                "Email": email,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ExportCustomJobInstance(
            self._version, payload, resource_type=self._solution["resource_type"]
        )

    async def create_async(
        self,
        start_day: str,
        end_day: str,
        friendly_name: str,
        webhook_url: Union[str, object] = values.unset,
        webhook_method: Union[str, object] = values.unset,
        email: Union[str, object] = values.unset,
    ) -> ExportCustomJobInstance:
        """
        Asynchronously create the ExportCustomJobInstance

        :param start_day: The start day for the custom export specified as a string in the format of yyyy-mm-dd
        :param end_day: The end day for the custom export specified as a string in the format of yyyy-mm-dd. End day is inclusive and must be 2 days earlier than the current UTC day.
        :param friendly_name: The friendly name specified when creating the job
        :param webhook_url: The optional webhook url called on completion of the job. If this is supplied, `WebhookMethod` must also be supplied. If you set neither webhook nor email, you will have to check your job's status manually.
        :param webhook_method: This is the method used to call the webhook on completion of the job. If this is supplied, `WebhookUrl` must also be supplied.
        :param email: The optional email to send the completion notification to. You can set both webhook, and email, or one or the other. If you set neither, the job will run but you will have to query to determine your job's status.

        :returns: The created ExportCustomJobInstance
        """

        data = values.of(
            {
                "StartDay": start_day,
                "EndDay": end_day,
                "FriendlyName": friendly_name,
                "WebhookUrl": webhook_url,
                "WebhookMethod": webhook_method,
                "Email": email,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ExportCustomJobInstance(
            self._version, payload, resource_type=self._solution["resource_type"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ExportCustomJobInstance]:
        """
        Streams ExportCustomJobInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ExportCustomJobInstance]:
        """
        Asynchronously streams ExportCustomJobInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ExportCustomJobInstance]:
        """
        Lists ExportCustomJobInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ExportCustomJobInstance]:
        """
        Asynchronously lists ExportCustomJobInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ExportCustomJobPage:
        """
        Retrieve a single page of ExportCustomJobInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ExportCustomJobInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ExportCustomJobPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ExportCustomJobPage:
        """
        Asynchronously retrieve a single page of ExportCustomJobInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ExportCustomJobInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ExportCustomJobPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ExportCustomJobPage:
        """
        Retrieve a specific page of ExportCustomJobInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ExportCustomJobInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ExportCustomJobPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ExportCustomJobPage:
        """
        Asynchronously retrieve a specific page of ExportCustomJobInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ExportCustomJobInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ExportCustomJobPage(self._version, response, self._solution)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Bulkexports.V1.ExportCustomJobList>"
