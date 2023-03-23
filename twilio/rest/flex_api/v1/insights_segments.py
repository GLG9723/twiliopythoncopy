r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InsightsSegmentsInstance(InstanceResource):
    def __init__(self, version, payload, segment_id: Optional[str] = None):
        """
        Initialize the InsightsSegmentsInstance

        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        """
        super().__init__(version)

        self._properties = {
            "segment_id": payload.get("segment_id"),
            "external_id": payload.get("external_id"),
            "queue": payload.get("queue"),
            "external_contact": payload.get("external_contact"),
            "external_segment_link_id": payload.get("external_segment_link_id"),
            "date": payload.get("date"),
            "account_id": payload.get("account_id"),
            "external_segment_link": payload.get("external_segment_link"),
            "agent_id": payload.get("agent_id"),
            "agent_phone": payload.get("agent_phone"),
            "agent_name": payload.get("agent_name"),
            "agent_team_name": payload.get("agent_team_name"),
            "agent_team_name_in_hierarchy": payload.get("agent_team_name_in_hierarchy"),
            "agent_link": payload.get("agent_link"),
            "customer_phone": payload.get("customer_phone"),
            "customer_name": payload.get("customer_name"),
            "customer_link": payload.get("customer_link"),
            "segment_recording_offset": payload.get("segment_recording_offset"),
            "media": payload.get("media"),
            "assessment_type": payload.get("assessment_type"),
            "assessment_percentage": payload.get("assessment_percentage"),
            "url": payload.get("url"),
        }

        self._solution = {
            "segment_id": segment_id or self._properties["segment_id"],
        }
        self._context: Optional[InsightsSegmentsContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InsightsSegmentsContext for this InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        """
        if self._context is None:
            self._context = InsightsSegmentsContext(
                self._version,
                segment_id=self._solution["segment_id"],
            )
        return self._context

    @property
    def segment_id(self):
        """
        :returns: To unique id of the segment
        :rtype: str
        """
        return self._properties["segment_id"]

    @property
    def external_id(self):
        """
        :returns: The unique id for the conversation.
        :rtype: str
        """
        return self._properties["external_id"]

    @property
    def queue(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["queue"]

    @property
    def external_contact(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["external_contact"]

    @property
    def external_segment_link_id(self):
        """
        :returns: The uuid for the external_segment_link.
        :rtype: str
        """
        return self._properties["external_segment_link_id"]

    @property
    def date(self):
        """
        :returns: The date of the conversation.
        :rtype: str
        """
        return self._properties["date"]

    @property
    def account_id(self):
        """
        :returns: The unique id for the account.
        :rtype: str
        """
        return self._properties["account_id"]

    @property
    def external_segment_link(self):
        """
        :returns: The hyperlink to recording of the task event.
        :rtype: str
        """
        return self._properties["external_segment_link"]

    @property
    def agent_id(self):
        """
        :returns: The unique id for the agent.
        :rtype: str
        """
        return self._properties["agent_id"]

    @property
    def agent_phone(self):
        """
        :returns: The phone number of the agent.
        :rtype: str
        """
        return self._properties["agent_phone"]

    @property
    def agent_name(self):
        """
        :returns: The name of the agent.
        :rtype: str
        """
        return self._properties["agent_name"]

    @property
    def agent_team_name(self):
        """
        :returns: The team name to which agent belongs.
        :rtype: str
        """
        return self._properties["agent_team_name"]

    @property
    def agent_team_name_in_hierarchy(self):
        """
        :returns: he team name to which agent belongs.
        :rtype: str
        """
        return self._properties["agent_team_name_in_hierarchy"]

    @property
    def agent_link(self):
        """
        :returns: The link to the agent conversation.
        :rtype: str
        """
        return self._properties["agent_link"]

    @property
    def customer_phone(self):
        """
        :returns: The phone number of the customer.
        :rtype: str
        """
        return self._properties["customer_phone"]

    @property
    def customer_name(self):
        """
        :returns: The name of the customer.
        :rtype: str
        """
        return self._properties["customer_name"]

    @property
    def customer_link(self):
        """
        :returns: The link to the customer conversation.
        :rtype: str
        """
        return self._properties["customer_link"]

    @property
    def segment_recording_offset(self):
        """
        :returns: The offset value for the recording.
        :rtype: str
        """
        return self._properties["segment_recording_offset"]

    @property
    def media(self):
        """
        :returns: The media identifiers of the conversation.
        :rtype: dict
        """
        return self._properties["media"]

    @property
    def assessment_type(self):
        """
        :returns: The type of the assessment.
        :rtype: dict
        """
        return self._properties["assessment_type"]

    @property
    def assessment_percentage(self):
        """
        :returns: The percentage scored on the Assessments.
        :rtype: dict
        """
        return self._properties["assessment_percentage"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self, token=values.unset):
        """
        Fetch the InsightsSegmentsInstance

        :param str token: The Token HTTP request header

        :returns: The fetched InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        """
        return self._proxy.fetch(
            token=token,
        )

    async def fetch_async(self, token=values.unset):
        """
        Asynchronous coroutine to fetch the InsightsSegmentsInstance

        :param str token: The Token HTTP request header

        :returns: The fetched InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        """
        return await self._proxy.fetch_async(
            token=token,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InsightsSegmentsInstance {}>".format(context)


class InsightsSegmentsContext(InstanceContext):
    def __init__(self, version: Version, segment_id: str):
        """
        Initialize the InsightsSegmentsContext

        :param Version version: Version that contains the resource
        :param segment_id: To unique id of the segment

        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "segment_id": segment_id,
        }
        self._uri = "/Insights/Segments/{segment_id}".format(**self._solution)

    def fetch(self, token=values.unset):
        """
        Fetch the InsightsSegmentsInstance

        :param str token: The Token HTTP request header

        :returns: The fetched InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        """

        data = values.of(
            {
                "Token": token,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return InsightsSegmentsInstance(
            self._version,
            payload,
            segment_id=self._solution["segment_id"],
        )

    async def fetch_async(self, token=values.unset):
        """
        Asynchronous coroutine to fetch the InsightsSegmentsInstance

        :param str token: The Token HTTP request header

        :returns: The fetched InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        """

        data = values.of(
            {
                "Token": token,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return InsightsSegmentsInstance(
            self._version,
            payload,
            segment_id=self._solution["segment_id"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InsightsSegmentsContext {}>".format(context)


class InsightsSegmentsPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of InsightsSegmentsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        """
        return InsightsSegmentsInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsSegmentsPage>"


class InsightsSegmentsList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the InsightsSegmentsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsList
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsList
        """
        super().__init__(version)

        self._uri = "/Insights/Segments"

    def stream(
        self,
        token=values.unset,
        reservation_id=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams InsightsSegmentsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param List[str] reservation_id: The list of reservation Ids
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            token=token, reservation_id=reservation_id, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        token=values.unset,
        reservation_id=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams InsightsSegmentsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param List[str] reservation_id: The list of reservation Ids
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            token=token, reservation_id=reservation_id, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        token=values.unset,
        reservation_id=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists InsightsSegmentsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
        :param List[str] reservation_id: The list of reservation Ids
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance]
        """
        return list(
            self.stream(
                token=token,
                reservation_id=reservation_id,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        token=values.unset,
        reservation_id=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists InsightsSegmentsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
        :param List[str] reservation_id: The list of reservation Ids
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance]
        """
        return list(
            await self.stream_async(
                token=token,
                reservation_id=reservation_id,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        token=values.unset,
        reservation_id=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of InsightsSegmentsInstance records from the API.
        Request is executed immediately

        :param str token: The Token HTTP request header
        :param List[str] reservation_id: The list of reservation Ids
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsPage
        """
        data = values.of(
            {
                "Token": token,
                "ReservationId": serialize.map(reservation_id, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InsightsSegmentsPage(self._version, response)

    async def page_async(
        self,
        token=values.unset,
        reservation_id=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of InsightsSegmentsInstance records from the API.
        Request is executed immediately

        :param str token: The Token HTTP request header
        :param List[str] reservation_id: The list of reservation Ids
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsPage
        """
        data = values.of(
            {
                "Token": token,
                "ReservationId": serialize.map(reservation_id, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return InsightsSegmentsPage(self._version, response)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InsightsSegmentsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InsightsSegmentsPage(self._version, response)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of InsightsSegmentsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InsightsSegmentsPage(self._version, response)

    def get(self, segment_id):
        """
        Constructs a InsightsSegmentsContext

        :param segment_id: To unique id of the segment

        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        """
        return InsightsSegmentsContext(self._version, segment_id=segment_id)

    def __call__(self, segment_id):
        """
        Constructs a InsightsSegmentsContext

        :param segment_id: To unique id of the segment

        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        """
        return InsightsSegmentsContext(self._version, segment_id=segment_id)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.InsightsSegmentsList>"
