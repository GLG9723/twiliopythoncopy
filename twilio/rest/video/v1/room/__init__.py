r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Dict, List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.video.v1.room.participant import ParticipantList
from twilio.rest.video.v1.room.recording_rules import RecordingRulesList
from twilio.rest.video.v1.room.room_recording import RoomRecordingList


class RoomInstance(InstanceResource):
    class RoomStatus(object):
        IN_PROGRESS = "in-progress"
        COMPLETED = "completed"
        FAILED = "failed"

    class RoomType(object):
        GO = "go"
        PEER_TO_PEER = "peer-to-peer"
        GROUP = "group"
        GROUP_SMALL = "group-small"

    class VideoCodec(object):
        VP8 = "VP8"
        H264 = "H264"

    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the RoomInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "status": payload.get("status"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "account_sid": payload.get("account_sid"),
            "enable_turn": payload.get("enable_turn"),
            "unique_name": payload.get("unique_name"),
            "status_callback": payload.get("status_callback"),
            "status_callback_method": payload.get("status_callback_method"),
            "end_time": deserialize.iso8601_datetime(payload.get("end_time")),
            "duration": deserialize.integer(payload.get("duration")),
            "type": payload.get("type"),
            "max_participants": deserialize.integer(payload.get("max_participants")),
            "max_participant_duration": deserialize.integer(
                payload.get("max_participant_duration")
            ),
            "max_concurrent_published_tracks": deserialize.integer(
                payload.get("max_concurrent_published_tracks")
            ),
            "record_participants_on_connect": payload.get(
                "record_participants_on_connect"
            ),
            "video_codecs": payload.get("video_codecs"),
            "media_region": payload.get("media_region"),
            "audio_only": payload.get("audio_only"),
            "empty_room_timeout": deserialize.integer(
                payload.get("empty_room_timeout")
            ),
            "unused_room_timeout": deserialize.integer(
                payload.get("unused_room_timeout")
            ),
            "large_room": payload.get("large_room"),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[RoomContext] = None

    @property
    def _proxy(self) -> "RoomContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RoomContext for this RoomInstance
        """
        if self._context is None:
            self._context = RoomContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> str:
        """
        :returns: The unique string that we created to identify the Room resource.
        """
        return self._properties["sid"]

    @property
    def status(self) -> "RoomInstance.RoomStatus":
        """
        :returns:
        """
        return self._properties["status"]

    @property
    def date_created(self) -> datetime:
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        """
        return self._properties["date_updated"]

    @property
    def account_sid(self) -> str:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Room resource.
        """
        return self._properties["account_sid"]

    @property
    def enable_turn(self) -> bool:
        """
        :returns: Deprecated, now always considered to be true.
        """
        return self._properties["enable_turn"]

    @property
    def unique_name(self) -> str:
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used as a `room_sid` in place of the resource's `sid` in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for `in-progress` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is `in-progress`.
        """
        return self._properties["unique_name"]

    @property
    def status_callback(self) -> str:
        """
        :returns: The URL we call using the `status_callback_method` to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
        """
        return self._properties["status_callback"]

    @property
    def status_callback_method(self) -> str:
        """
        :returns: The HTTP method we use to call `status_callback`. Can be `POST` or `GET` and defaults to `POST`.
        """
        return self._properties["status_callback_method"]

    @property
    def end_time(self) -> datetime:
        """
        :returns: The UTC end time of the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        """
        return self._properties["end_time"]

    @property
    def duration(self) -> int:
        """
        :returns: The duration of the room in seconds.
        """
        return self._properties["duration"]

    @property
    def type(self) -> "RoomInstance.RoomType":
        """
        :returns:
        """
        return self._properties["type"]

    @property
    def max_participants(self) -> int:
        """
        :returns: The maximum number of concurrent Participants allowed in the room.
        """
        return self._properties["max_participants"]

    @property
    def max_participant_duration(self) -> int:
        """
        :returns: The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
        """
        return self._properties["max_participant_duration"]

    @property
    def max_concurrent_published_tracks(self) -> int:
        """
        :returns: The maximum number of published audio, video, and data tracks all participants combined are allowed to publish in the room at the same time. Check [Programmable Video Limits](https://www.twilio.com/docs/video/programmable-video-limits) for more details. If it is set to 0 it means unconstrained.
        """
        return self._properties["max_concurrent_published_tracks"]

    @property
    def record_participants_on_connect(self) -> bool:
        """
        :returns: Whether to start recording when Participants connect. ***This feature is not available in `peer-to-peer` rooms.***
        """
        return self._properties["record_participants_on_connect"]

    @property
    def video_codecs(self) -> List["RoomInstance.VideoCodec"]:
        """
        :returns: An array of the video codecs that are supported when publishing a track in the room.  Can be: `VP8` and `H264`.  ***This feature is not available in `peer-to-peer` rooms***
        """
        return self._properties["video_codecs"]

    @property
    def media_region(self) -> str:
        """
        :returns: The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-address-whitelisting#media-servers). ***This feature is not available in `peer-to-peer` rooms.***
        """
        return self._properties["media_region"]

    @property
    def audio_only(self) -> bool:
        """
        :returns: When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only.
        """
        return self._properties["audio_only"]

    @property
    def empty_room_timeout(self) -> int:
        """
        :returns: Specifies how long (in minutes) a room will remain active after last participant leaves. Can be configured when creating a room via REST API. For Ad-Hoc rooms this value cannot be changed.
        """
        return self._properties["empty_room_timeout"]

    @property
    def unused_room_timeout(self) -> int:
        """
        :returns: Specifies how long (in minutes) a room will remain active if no one joins. Can be configured when creating a room via REST API. For Ad-Hoc rooms this value cannot be changed.
        """
        return self._properties["unused_room_timeout"]

    @property
    def large_room(self) -> bool:
        """
        :returns: Indicates if this is a large room.
        """
        return self._properties["large_room"]

    @property
    def url(self) -> str:
        """
        :returns: The absolute URL of the resource.
        """
        return self._properties["url"]

    @property
    def links(self) -> Dict[str, object]:
        """
        :returns: The URLs of related resources.
        """
        return self._properties["links"]

    def fetch(self) -> "RoomInstance":
        """
        Fetch the RoomInstance


        :returns: The fetched RoomInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RoomInstance":
        """
        Asynchronous coroutine to fetch the RoomInstance


        :returns: The fetched RoomInstance
        """
        return await self._proxy.fetch_async()

    def update(self, status) -> "RoomInstance":
        """
        Update the RoomInstance

        :param "RoomInstance.RoomStatus" status:

        :returns: The updated RoomInstance
        """
        return self._proxy.update(
            status=status,
        )

    async def update_async(self, status) -> "RoomInstance":
        """
        Asynchronous coroutine to update the RoomInstance

        :param "RoomInstance.RoomStatus" status:

        :returns: The updated RoomInstance
        """
        return await self._proxy.update_async(
            status=status,
        )

    @property
    def participants(self) -> ParticipantList:
        """
        Access the participants
        """
        return self._proxy.participants

    @property
    def recording_rules(self) -> RecordingRulesList:
        """
        Access the recording_rules
        """
        return self._proxy.recording_rules

    @property
    def recordings(self) -> RoomRecordingList:
        """
        Access the recordings
        """
        return self._proxy.recordings

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.RoomInstance {}>".format(context)


class RoomContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the RoomContext

        :param version: Version that contains the resource
        :param sid: The SID of the Room resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Rooms/{sid}".format(**self._solution)

        self._participants: Optional[ParticipantList] = None
        self._recording_rules: Optional[RecordingRulesList] = None
        self._recordings: Optional[RoomRecordingList] = None

    def fetch(self) -> RoomInstance:
        """
        Fetch the RoomInstance


        :returns: The fetched RoomInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RoomInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> RoomInstance:
        """
        Asynchronous coroutine to fetch the RoomInstance


        :returns: The fetched RoomInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RoomInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(self, status) -> RoomInstance:
        """
        Update the RoomInstance

        :param "RoomInstance.RoomStatus" status:

        :returns: The updated RoomInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoomInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(self, status) -> RoomInstance:
        """
        Asynchronous coroutine to update the RoomInstance

        :param "RoomInstance.RoomStatus" status:

        :returns: The updated RoomInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoomInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def participants(self) -> ParticipantList:
        """
        Access the participants
        """
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
                self._solution["sid"],
            )
        return self._participants

    @property
    def recording_rules(self) -> RecordingRulesList:
        """
        Access the recording_rules
        """
        if self._recording_rules is None:
            self._recording_rules = RecordingRulesList(
                self._version,
                self._solution["sid"],
            )
        return self._recording_rules

    @property
    def recordings(self) -> RoomRecordingList:
        """
        Access the recordings
        """
        if self._recordings is None:
            self._recordings = RoomRecordingList(
                self._version,
                self._solution["sid"],
            )
        return self._recordings

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.RoomContext {}>".format(context)


class RoomPage(Page):
    def get_instance(self, payload) -> RoomInstance:
        """
        Build an instance of RoomInstance

        :param dict payload: Payload response from the API
        """
        return RoomInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.RoomPage>"


class RoomList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the RoomList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Rooms"

    def create(
        self,
        enable_turn=values.unset,
        type=values.unset,
        unique_name=values.unset,
        status_callback=values.unset,
        status_callback_method=values.unset,
        max_participants=values.unset,
        record_participants_on_connect=values.unset,
        video_codecs=values.unset,
        media_region=values.unset,
        recording_rules=values.unset,
        audio_only=values.unset,
        max_participant_duration=values.unset,
        empty_room_timeout=values.unset,
        unused_room_timeout=values.unset,
        large_room=values.unset,
    ) -> RoomInstance:
        """
        Create the RoomInstance

        :param bool enable_turn: Deprecated, now always considered to be true.
        :param &quot;RoomInstance.RoomType&quot; type:
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used as a `room_sid` in place of the resource's `sid` in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for `in-progress` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is `in-progress`.
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be `POST` or `GET`.
        :param int max_participants: The maximum number of concurrent Participants allowed in the room. Peer-to-peer rooms can have up to 10 Participants. Small Group rooms can have up to 4 Participants. Group rooms can have up to 50 Participants.
        :param bool record_participants_on_connect: Whether to start recording when Participants connect. ***This feature is not available in `peer-to-peer` rooms.***
        :param List[&quot;RoomInstance.VideoCodec&quot;] video_codecs: An array of the video codecs that are supported when publishing a track in the room.  Can be: `VP8` and `H264`.  ***This feature is not available in `peer-to-peer` rooms***
        :param str media_region: The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-address-whitelisting#group-rooms-media-servers). ***This feature is not available in `peer-to-peer` rooms.***
        :param object recording_rules: A collection of Recording Rules that describe how to include or exclude matching tracks for recording
        :param bool audio_only: When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only.
        :param int max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
        :param int empty_room_timeout: Configures how long (in minutes) a room will remain active after last participant leaves. Valid values range from 1 to 60 minutes (no fractions).
        :param int unused_room_timeout: Configures how long (in minutes) a room will remain active if no one joins. Valid values range from 1 to 60 minutes (no fractions).
        :param bool large_room: When set to true, indicated that this is the large room.

        :returns: The created RoomInstance
        """
        data = values.of(
            {
                "EnableTurn": enable_turn,
                "Type": type,
                "UniqueName": unique_name,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "MaxParticipants": max_participants,
                "RecordParticipantsOnConnect": record_participants_on_connect,
                "VideoCodecs": serialize.map(video_codecs, lambda e: e),
                "MediaRegion": media_region,
                "RecordingRules": serialize.object(recording_rules),
                "AudioOnly": audio_only,
                "MaxParticipantDuration": max_participant_duration,
                "EmptyRoomTimeout": empty_room_timeout,
                "UnusedRoomTimeout": unused_room_timeout,
                "LargeRoom": large_room,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoomInstance(self._version, payload)

    async def create_async(
        self,
        enable_turn=values.unset,
        type=values.unset,
        unique_name=values.unset,
        status_callback=values.unset,
        status_callback_method=values.unset,
        max_participants=values.unset,
        record_participants_on_connect=values.unset,
        video_codecs=values.unset,
        media_region=values.unset,
        recording_rules=values.unset,
        audio_only=values.unset,
        max_participant_duration=values.unset,
        empty_room_timeout=values.unset,
        unused_room_timeout=values.unset,
        large_room=values.unset,
    ) -> RoomInstance:
        """
        Asynchronously create the RoomInstance

        :param bool enable_turn: Deprecated, now always considered to be true.
        :param &quot;RoomInstance.RoomType&quot; type:
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used as a `room_sid` in place of the resource's `sid` in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for `in-progress` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is `in-progress`.
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be `POST` or `GET`.
        :param int max_participants: The maximum number of concurrent Participants allowed in the room. Peer-to-peer rooms can have up to 10 Participants. Small Group rooms can have up to 4 Participants. Group rooms can have up to 50 Participants.
        :param bool record_participants_on_connect: Whether to start recording when Participants connect. ***This feature is not available in `peer-to-peer` rooms.***
        :param List[&quot;RoomInstance.VideoCodec&quot;] video_codecs: An array of the video codecs that are supported when publishing a track in the room.  Can be: `VP8` and `H264`.  ***This feature is not available in `peer-to-peer` rooms***
        :param str media_region: The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-address-whitelisting#group-rooms-media-servers). ***This feature is not available in `peer-to-peer` rooms.***
        :param object recording_rules: A collection of Recording Rules that describe how to include or exclude matching tracks for recording
        :param bool audio_only: When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only.
        :param int max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
        :param int empty_room_timeout: Configures how long (in minutes) a room will remain active after last participant leaves. Valid values range from 1 to 60 minutes (no fractions).
        :param int unused_room_timeout: Configures how long (in minutes) a room will remain active if no one joins. Valid values range from 1 to 60 minutes (no fractions).
        :param bool large_room: When set to true, indicated that this is the large room.

        :returns: The created RoomInstance
        """
        data = values.of(
            {
                "EnableTurn": enable_turn,
                "Type": type,
                "UniqueName": unique_name,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "MaxParticipants": max_participants,
                "RecordParticipantsOnConnect": record_participants_on_connect,
                "VideoCodecs": serialize.map(video_codecs, lambda e: e),
                "MediaRegion": media_region,
                "RecordingRules": serialize.object(recording_rules),
                "AudioOnly": audio_only,
                "MaxParticipantDuration": max_participant_duration,
                "EmptyRoomTimeout": empty_room_timeout,
                "UnusedRoomTimeout": unused_room_timeout,
                "LargeRoom": large_room,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoomInstance(self._version, payload)

    def stream(
        self,
        status=values.unset,
        unique_name=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        limit=None,
        page_size=None,
    ) -> List[RoomInstance]:
        """
        Streams RoomInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;RoomInstance.RoomStatus&quot; status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
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
            status=status,
            unique_name=unique_name,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status=values.unset,
        unique_name=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        limit=None,
        page_size=None,
    ) -> List[RoomInstance]:
        """
        Asynchronously streams RoomInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;RoomInstance.RoomStatus&quot; status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
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
            status=status,
            unique_name=unique_name,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status=values.unset,
        unique_name=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        limit=None,
        page_size=None,
    ) -> List[RoomInstance]:
        """
        Lists RoomInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;RoomInstance.RoomStatus&quot; status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
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
                status=status,
                unique_name=unique_name,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status=values.unset,
        unique_name=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        limit=None,
        page_size=None,
    ) -> List[RoomInstance]:
        """
        Asynchronously lists RoomInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;RoomInstance.RoomStatus&quot; status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
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
                status=status,
                unique_name=unique_name,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        status=values.unset,
        unique_name=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> RoomPage:
        """
        Retrieve a single page of RoomInstance records from the API.
        Request is executed immediately

        :param &quot;RoomInstance.RoomStatus&quot; status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoomInstance
        """
        data = values.of(
            {
                "Status": status,
                "UniqueName": unique_name,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return RoomPage(self._version, response)

    async def page_async(
        self,
        status=values.unset,
        unique_name=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> RoomPage:
        """
        Asynchronously retrieve a single page of RoomInstance records from the API.
        Request is executed immediately

        :param &quot;RoomInstance.RoomStatus&quot; status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoomInstance
        """
        data = values.of(
            {
                "Status": status,
                "UniqueName": unique_name,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return RoomPage(self._version, response)

    def get_page(self, target_url) -> RoomPage:
        """
        Retrieve a specific page of RoomInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoomInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RoomPage(self._version, response)

    async def get_page_async(self, target_url) -> RoomPage:
        """
        Asynchronously retrieve a specific page of RoomInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoomInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RoomPage(self._version, response)

    def get(self, sid) -> RoomContext:
        """
        Constructs a RoomContext

        :param sid: The SID of the Room resource to update.
        """
        return RoomContext(self._version, sid=sid)

    def __call__(self, sid) -> RoomContext:
        """
        Constructs a RoomContext

        :param sid: The SID of the Room resource to update.
        """
        return RoomContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.RoomList>"
