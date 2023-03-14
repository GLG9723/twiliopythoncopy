"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.insights.v1.conference.conference_participant import (
    ConferenceParticipantList,
)


class ConferenceList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ConferenceList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.insights.v1.conference.ConferenceList
        :rtype: twilio.rest.insights.v1.conference.ConferenceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Conferences".format(**self._solution)

    def stream(
        self,
        conference_sid=values.unset,
        friendly_name=values.unset,
        status=values.unset,
        created_after=values.unset,
        created_before=values.unset,
        mixer_region=values.unset,
        tags=values.unset,
        subaccount=values.unset,
        detected_issues=values.unset,
        end_reason=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams ConferenceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str conference_sid: The SID of the conference.
        :param str friendly_name: Custom label for the conference resource, up to 64 characters.
        :param str status: Conference status.
        :param str created_after: Conferences created after the provided timestamp specified in ISO 8601 format
        :param str created_before: Conferences created before the provided timestamp specified in ISO 8601 format.
        :param str mixer_region: Twilio region where the conference media was mixed.
        :param str tags: Tags applied by Twilio for common potential configuration, quality, or performance issues.
        :param str subaccount: Account SID for the subaccount whose resources you wish to retrieve.
        :param str detected_issues: Potential configuration, behavior, or performance issues detected during the conference.
        :param str end_reason: Conference end reason; e.g. last participant left, modified by API, etc.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.conference.ConferenceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            conference_sid=conference_sid,
            friendly_name=friendly_name,
            status=status,
            created_after=created_after,
            created_before=created_before,
            mixer_region=mixer_region,
            tags=tags,
            subaccount=subaccount,
            detected_issues=detected_issues,
            end_reason=end_reason,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    def list(
        self,
        conference_sid=values.unset,
        friendly_name=values.unset,
        status=values.unset,
        created_after=values.unset,
        created_before=values.unset,
        mixer_region=values.unset,
        tags=values.unset,
        subaccount=values.unset,
        detected_issues=values.unset,
        end_reason=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists ConferenceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str conference_sid: The SID of the conference.
        :param str friendly_name: Custom label for the conference resource, up to 64 characters.
        :param str status: Conference status.
        :param str created_after: Conferences created after the provided timestamp specified in ISO 8601 format
        :param str created_before: Conferences created before the provided timestamp specified in ISO 8601 format.
        :param str mixer_region: Twilio region where the conference media was mixed.
        :param str tags: Tags applied by Twilio for common potential configuration, quality, or performance issues.
        :param str subaccount: Account SID for the subaccount whose resources you wish to retrieve.
        :param str detected_issues: Potential configuration, behavior, or performance issues detected during the conference.
        :param str end_reason: Conference end reason; e.g. last participant left, modified by API, etc.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.conference.ConferenceInstance]
        """
        return list(
            self.stream(
                conference_sid=conference_sid,
                friendly_name=friendly_name,
                status=status,
                created_after=created_after,
                created_before=created_before,
                mixer_region=mixer_region,
                tags=tags,
                subaccount=subaccount,
                detected_issues=detected_issues,
                end_reason=end_reason,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        conference_sid=values.unset,
        friendly_name=values.unset,
        status=values.unset,
        created_after=values.unset,
        created_before=values.unset,
        mixer_region=values.unset,
        tags=values.unset,
        subaccount=values.unset,
        detected_issues=values.unset,
        end_reason=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of ConferenceInstance records from the API.
        Request is executed immediately

        :param str conference_sid: The SID of the conference.
        :param str friendly_name: Custom label for the conference resource, up to 64 characters.
        :param str status: Conference status.
        :param str created_after: Conferences created after the provided timestamp specified in ISO 8601 format
        :param str created_before: Conferences created before the provided timestamp specified in ISO 8601 format.
        :param str mixer_region: Twilio region where the conference media was mixed.
        :param str tags: Tags applied by Twilio for common potential configuration, quality, or performance issues.
        :param str subaccount: Account SID for the subaccount whose resources you wish to retrieve.
        :param str detected_issues: Potential configuration, behavior, or performance issues detected during the conference.
        :param str end_reason: Conference end reason; e.g. last participant left, modified by API, etc.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ConferenceInstance
        :rtype: twilio.rest.insights.v1.conference.ConferencePage
        """
        data = values.of(
            {
                "ConferenceSid": conference_sid,
                "FriendlyName": friendly_name,
                "Status": status,
                "CreatedAfter": created_after,
                "CreatedBefore": created_before,
                "MixerRegion": mixer_region,
                "Tags": tags,
                "Subaccount": subaccount,
                "DetectedIssues": detected_issues,
                "EndReason": end_reason,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ConferencePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ConferenceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ConferenceInstance
        :rtype: twilio.rest.insights.v1.conference.ConferencePage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ConferencePage(self._version, response, self._solution)

    def get(self, conference_sid):
        """
        Constructs a ConferenceContext

        :param conference_sid: The unique SID identifier of the Conference.

        :returns: twilio.rest.insights.v1.conference.ConferenceContext
        :rtype: twilio.rest.insights.v1.conference.ConferenceContext
        """
        return ConferenceContext(self._version, conference_sid=conference_sid)

    def __call__(self, conference_sid):
        """
        Constructs a ConferenceContext

        :param conference_sid: The unique SID identifier of the Conference.

        :returns: twilio.rest.insights.v1.conference.ConferenceContext
        :rtype: twilio.rest.insights.v1.conference.ConferenceContext
        """
        return ConferenceContext(self._version, conference_sid=conference_sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Insights.V1.ConferenceList>"


class ConferencePage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the ConferencePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.conference.ConferencePage
        :rtype: twilio.rest.insights.v1.conference.ConferencePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ConferenceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.conference.ConferenceInstance
        :rtype: twilio.rest.insights.v1.conference.ConferenceInstance
        """
        return ConferenceInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Insights.V1.ConferencePage>"


class ConferenceInstance(InstanceResource):
    class ConferenceEndReason(object):
        LAST_PARTICIPANT_LEFT = "last_participant_left"
        CONFERENCE_ENDED_VIA_API = "conference_ended_via_api"
        PARTICIPANT_WITH_END_CONFERENCE_ON_EXIT_LEFT = (
            "participant_with_end_conference_on_exit_left"
        )
        LAST_PARTICIPANT_KICKED = "last_participant_kicked"
        PARTICIPANT_WITH_END_CONFERENCE_ON_EXIT_KICKED = (
            "participant_with_end_conference_on_exit_kicked"
        )

    class ConferenceStatus(object):
        IN_PROGRESS = "in_progress"
        NOT_STARTED = "not_started"
        COMPLETED = "completed"
        SUMMARY_TIMEOUT = "summary_timeout"

    class ProcessingState(object):
        COMPLETE = "complete"
        IN_PROGRESS = "in_progress"
        TIMEOUT = "timeout"

    class Region(object):
        US1 = "us1"
        AU1 = "au1"
        BR1 = "br1"
        IE1 = "ie1"
        JP1 = "jp1"
        SG1 = "sg1"
        DE1 = "de1"

    class Tag(object):
        INVALID_REQUESTED_REGION = "invalid_requested_region"
        DUPLICATE_IDENTITY = "duplicate_identity"
        START_FAILURE = "start_failure"
        REGION_CONFIGURATION_ISSUES = "region_configuration_issues"
        QUALITY_WARNINGS = "quality_warnings"
        PARTICIPANT_BEHAVIOR_ISSUES = "participant_behavior_issues"
        HIGH_PACKET_LOSS = "high_packet_loss"
        HIGH_JITTER = "high_jitter"
        HIGH_LATENCY = "high_latency"
        LOW_MOS = "low_mos"
        DETECTED_SILENCE = "detected_silence"

    def __init__(self, version, payload, conference_sid: str = None):
        """
        Initialize the ConferenceInstance

        :returns: twilio.rest.insights.v1.conference.ConferenceInstance
        :rtype: twilio.rest.insights.v1.conference.ConferenceInstance
        """
        super().__init__(version)

        self._properties = {
            "conference_sid": payload.get("conference_sid"),
            "account_sid": payload.get("account_sid"),
            "friendly_name": payload.get("friendly_name"),
            "create_time": deserialize.iso8601_datetime(payload.get("create_time")),
            "start_time": deserialize.iso8601_datetime(payload.get("start_time")),
            "end_time": deserialize.iso8601_datetime(payload.get("end_time")),
            "duration_seconds": deserialize.integer(payload.get("duration_seconds")),
            "connect_duration_seconds": deserialize.integer(
                payload.get("connect_duration_seconds")
            ),
            "status": payload.get("status"),
            "max_participants": deserialize.integer(payload.get("max_participants")),
            "max_concurrent_participants": deserialize.integer(
                payload.get("max_concurrent_participants")
            ),
            "unique_participants": deserialize.integer(
                payload.get("unique_participants")
            ),
            "end_reason": payload.get("end_reason"),
            "ended_by": payload.get("ended_by"),
            "mixer_region": payload.get("mixer_region"),
            "mixer_region_requested": payload.get("mixer_region_requested"),
            "recording_enabled": payload.get("recording_enabled"),
            "detected_issues": payload.get("detected_issues"),
            "tags": payload.get("tags"),
            "tag_info": payload.get("tag_info"),
            "processing_state": payload.get("processing_state"),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._context = None
        self._solution = {
            "conference_sid": conference_sid or self._properties["conference_sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ConferenceContext for this ConferenceInstance
        :rtype: twilio.rest.insights.v1.conference.ConferenceContext
        """
        if self._context is None:
            self._context = ConferenceContext(
                self._version,
                conference_sid=self._solution["conference_sid"],
            )
        return self._context

    @property
    def conference_sid(self):
        """
        :returns: The unique SID identifier of the Conference.
        :rtype: str
        """
        return self._properties["conference_sid"]

    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def friendly_name(self):
        """
        :returns: Custom label for the conference resource, up to 64 characters.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def create_time(self):
        """
        :returns: Conference creation date and time in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties["create_time"]

    @property
    def start_time(self):
        """
        :returns: Timestamp in ISO 8601 format when the conference started. Conferences do not start until at least two participants join, at least one of whom has startConferenceOnEnter=true.
        :rtype: datetime
        """
        return self._properties["start_time"]

    @property
    def end_time(self):
        """
        :returns: Conference end date and time in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties["end_time"]

    @property
    def duration_seconds(self):
        """
        :returns: Conference duration in seconds.
        :rtype: int
        """
        return self._properties["duration_seconds"]

    @property
    def connect_duration_seconds(self):
        """
        :returns: Duration of the between conference start event and conference end event in seconds.
        :rtype: int
        """
        return self._properties["connect_duration_seconds"]

    @property
    def status(self):
        """
        :returns:
        :rtype: ConferenceInstance.ConferenceStatus
        """
        return self._properties["status"]

    @property
    def max_participants(self):
        """
        :returns: Maximum number of concurrent participants as specified by the configuration.
        :rtype: int
        """
        return self._properties["max_participants"]

    @property
    def max_concurrent_participants(self):
        """
        :returns: Actual maximum number of concurrent participants in the conference.
        :rtype: int
        """
        return self._properties["max_concurrent_participants"]

    @property
    def unique_participants(self):
        """
        :returns: Unique conference participants based on caller ID.
        :rtype: int
        """
        return self._properties["unique_participants"]

    @property
    def end_reason(self):
        """
        :returns:
        :rtype: ConferenceInstance.ConferenceEndReason
        """
        return self._properties["end_reason"]

    @property
    def ended_by(self):
        """
        :returns: Call SID of the participant whose actions ended the conference.
        :rtype: str
        """
        return self._properties["ended_by"]

    @property
    def mixer_region(self):
        """
        :returns:
        :rtype: ConferenceInstance.Region
        """
        return self._properties["mixer_region"]

    @property
    def mixer_region_requested(self):
        """
        :returns:
        :rtype: ConferenceInstance.Region
        """
        return self._properties["mixer_region_requested"]

    @property
    def recording_enabled(self):
        """
        :returns: Boolean. Indicates whether recording was enabled at the conference mixer.
        :rtype: bool
        """
        return self._properties["recording_enabled"]

    @property
    def detected_issues(self):
        """
        :returns: Potential issues detected by Twilio during the conference.
        :rtype: dict
        """
        return self._properties["detected_issues"]

    @property
    def tags(self):
        """
        :returns: Tags for detected conference conditions and participant behaviors which may be of interest.
        :rtype: list[ConferenceInstance.Tag]
        """
        return self._properties["tags"]

    @property
    def tag_info(self):
        """
        :returns: Object. Contains details about conference tags including severity.
        :rtype: dict
        """
        return self._properties["tag_info"]

    @property
    def processing_state(self):
        """
        :returns:
        :rtype: ConferenceInstance.ProcessingState
        """
        return self._properties["processing_state"]

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns: Contains a dictionary of URL links to nested resources of this Conference.
        :rtype: dict
        """
        return self._properties["links"]

    def fetch(self):
        """
        Fetch the ConferenceInstance


        :returns: The fetched ConferenceInstance
        :rtype: twilio.rest.insights.v1.conference.ConferenceInstance
        """
        return self._proxy.fetch()

    @property
    def conference_participants(self):
        """
        Access the conference_participants

        :returns: twilio.rest.insights.v1.conference.ConferenceParticipantList
        :rtype: twilio.rest.insights.v1.conference.ConferenceParticipantList
        """
        return self._proxy.conference_participants

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.ConferenceInstance {}>".format(context)


class ConferenceContext(InstanceContext):
    def __init__(self, version: Version, conference_sid: str):
        """
        Initialize the ConferenceContext

        :param Version version: Version that contains the resource
        :param conference_sid: The unique SID identifier of the Conference.

        :returns: twilio.rest.insights.v1.conference.ConferenceContext
        :rtype: twilio.rest.insights.v1.conference.ConferenceContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "conference_sid": conference_sid,
        }
        self._uri = "/Conferences/{conference_sid}".format(**self._solution)

        self._conference_participants = None

    def fetch(self):
        """
        Fetch the ConferenceInstance


        :returns: The fetched ConferenceInstance
        :rtype: twilio.rest.insights.v1.conference.ConferenceInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ConferenceInstance(
            self._version,
            payload,
            conference_sid=self._solution["conference_sid"],
        )

    @property
    def conference_participants(self):
        """
        Access the conference_participants

        :returns: twilio.rest.insights.v1.conference.ConferenceParticipantList
        :rtype: twilio.rest.insights.v1.conference.ConferenceParticipantList
        """
        if self._conference_participants is None:
            self._conference_participants = ConferenceParticipantList(
                self._version,
                self._solution["conference_sid"],
            )
        return self._conference_participants

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.ConferenceContext {}>".format(context)
