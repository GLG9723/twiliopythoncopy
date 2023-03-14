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


from twilio.base import deserialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InsightsAssessmentsCommentList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the InsightsAssessmentsCommentList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentList
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Insights/QM/Assessments/Comments".format(**self._solution)

    def create(
        self,
        category_id,
        category_name,
        comment,
        segment_id,
        user_name,
        user_email,
        agent_id,
        offset,
        token=values.unset,
    ):
        """
        Create the InsightsAssessmentsCommentInstance

        :param str category_id: The ID of the category
        :param str category_name: The name of the category
        :param str comment: The Assessment comment.
        :param str segment_id: The id of the segment.
        :param str user_name: The name of the user.
        :param str user_email: The email id of the user.
        :param str agent_id: The id of the agent.
        :param float offset: The offset
        :param str token: The Token HTTP request header

        :returns: The created InsightsAssessmentsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentInstance
        """
        data = values.of(
            {
                "CategoryId": category_id,
                "CategoryName": category_name,
                "Comment": comment,
                "SegmentId": segment_id,
                "UserName": user_name,
                "UserEmail": user_email,
                "AgentId": agent_id,
                "Offset": offset,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )
        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsAssessmentsCommentInstance(self._version, payload)

    async def create_async(
        self,
        category_id,
        category_name,
        comment,
        segment_id,
        user_name,
        user_email,
        agent_id,
        offset,
        token=values.unset,
    ):
        """
        Asynchronously create the InsightsAssessmentsCommentInstance

        :param str category_id: The ID of the category
        :param str category_name: The name of the category
        :param str comment: The Assessment comment.
        :param str segment_id: The id of the segment.
        :param str user_name: The name of the user.
        :param str user_email: The email id of the user.
        :param str agent_id: The id of the agent.
        :param float offset: The offset
        :param str token: The Token HTTP request header

        :returns: The created InsightsAssessmentsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentInstance
        """
        data = values.of(
            {
                "CategoryId": category_id,
                "CategoryName": category_name,
                "Comment": comment,
                "SegmentId": segment_id,
                "UserName": user_name,
                "UserEmail": user_email,
                "AgentId": agent_id,
                "Offset": offset,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )
        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsAssessmentsCommentInstance(self._version, payload)

    def stream(
        self,
        token=values.unset,
        segment_id=values.unset,
        agent_id=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams InsightsAssessmentsCommentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str agent_id: The id of the agent.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            token=token,
            segment_id=segment_id,
            agent_id=agent_id,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        token=values.unset,
        segment_id=values.unset,
        agent_id=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams InsightsAssessmentsCommentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str agent_id: The id of the agent.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            token=token,
            segment_id=segment_id,
            agent_id=agent_id,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        token=values.unset,
        segment_id=values.unset,
        agent_id=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists InsightsAssessmentsCommentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str agent_id: The id of the agent.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentInstance]
        """
        return list(
            self.stream(
                token=token,
                segment_id=segment_id,
                agent_id=agent_id,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        token=values.unset,
        segment_id=values.unset,
        agent_id=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists InsightsAssessmentsCommentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str agent_id: The id of the agent.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentInstance]
        """
        return list(
            await self.stream_async(
                token=token,
                segment_id=segment_id,
                agent_id=agent_id,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        token=values.unset,
        segment_id=values.unset,
        agent_id=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of InsightsAssessmentsCommentInstance records from the API.
        Request is executed immediately

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str agent_id: The id of the agent.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsAssessmentsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentPage
        """
        data = values.of(
            {
                "Token": token,
                "SegmentId": segment_id,
                "AgentId": agent_id,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InsightsAssessmentsCommentPage(self._version, response, self._solution)

    async def page_async(
        self,
        token=values.unset,
        segment_id=values.unset,
        agent_id=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of InsightsAssessmentsCommentInstance records from the API.
        Request is executed immediately

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str agent_id: The id of the agent.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsAssessmentsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentPage
        """
        data = values.of(
            {
                "Token": token,
                "SegmentId": segment_id,
                "AgentId": agent_id,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return InsightsAssessmentsCommentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InsightsAssessmentsCommentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InsightsAssessmentsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InsightsAssessmentsCommentPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of InsightsAssessmentsCommentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InsightsAssessmentsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InsightsAssessmentsCommentPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.InsightsAssessmentsCommentList>"


class InsightsAssessmentsCommentPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the InsightsAssessmentsCommentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentPage
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InsightsAssessmentsCommentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentInstance
        """
        return InsightsAssessmentsCommentInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.InsightsAssessmentsCommentPage>"


class InsightsAssessmentsCommentInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the InsightsAssessmentsCommentInstance

        :returns: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentInstance
        :rtype: twilio.rest.flex_api.v1.insights_assessments_comment.InsightsAssessmentsCommentInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "assessment_id": payload.get("assessment_id"),
            "comment": payload.get("comment"),
            "offset": deserialize.decimal(payload.get("offset")),
            "report": payload.get("report"),
            "weight": deserialize.decimal(payload.get("weight")),
            "agent_id": payload.get("agent_id"),
            "segment_id": payload.get("segment_id"),
            "user_name": payload.get("user_name"),
            "user_email": payload.get("user_email"),
            "timestamp": deserialize.decimal(payload.get("timestamp")),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {}

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Insights resource and owns this resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def assessment_id(self):
        """
        :returns: The unique ID of the assessment.
        :rtype: str
        """
        return self._properties["assessment_id"]

    @property
    def comment(self):
        """
        :returns: The comment added for assessment.
        :rtype: dict
        """
        return self._properties["comment"]

    @property
    def offset(self):
        """
        :returns: The offset
        :rtype: float
        """
        return self._properties["offset"]

    @property
    def report(self):
        """
        :returns: The flag indicating if this assessment is part of report
        :rtype: bool
        """
        return self._properties["report"]

    @property
    def weight(self):
        """
        :returns: The weightage given to this comment
        :rtype: float
        """
        return self._properties["weight"]

    @property
    def agent_id(self):
        """
        :returns: The id of the agent.
        :rtype: str
        """
        return self._properties["agent_id"]

    @property
    def segment_id(self):
        """
        :returns: The id of the segment.
        :rtype: str
        """
        return self._properties["segment_id"]

    @property
    def user_name(self):
        """
        :returns: The name of the user.
        :rtype: str
        """
        return self._properties["user_name"]

    @property
    def user_email(self):
        """
        :returns: The email id of the user.
        :rtype: str
        """
        return self._properties["user_email"]

    @property
    def timestamp(self):
        """
        :returns: The timestamp when the record is inserted
        :rtype: float
        """
        return self._properties["timestamp"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InsightsAssessmentsCommentInstance {}>".format(
            context
        )
