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


from typing import Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CompositionInstance(InstanceResource):
    class Format(object):
        MP4 = "mp4"
        WEBM = "webm"

    class Status(object):
        ENQUEUED = "enqueued"
        PROCESSING = "processing"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"

    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the CompositionInstance

        :returns: twilio.rest.video.v1.composition.CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "status": payload.get("status"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_completed": deserialize.iso8601_datetime(
                payload.get("date_completed")
            ),
            "date_deleted": deserialize.iso8601_datetime(payload.get("date_deleted")),
            "sid": payload.get("sid"),
            "room_sid": payload.get("room_sid"),
            "audio_sources": payload.get("audio_sources"),
            "audio_sources_excluded": payload.get("audio_sources_excluded"),
            "video_layout": payload.get("video_layout"),
            "resolution": payload.get("resolution"),
            "trim": payload.get("trim"),
            "format": payload.get("format"),
            "bitrate": deserialize.integer(payload.get("bitrate")),
            "size": payload.get("size"),
            "duration": deserialize.integer(payload.get("duration")),
            "media_external_location": payload.get("media_external_location"),
            "status_callback": payload.get("status_callback"),
            "status_callback_method": payload.get("status_callback_method"),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[CompositionContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CompositionContext for this CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionContext
        """
        if self._context is None:
            self._context = CompositionContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Composition resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def status(self):
        """
        :returns:
        :rtype: CompositionInstance.Status
        """
        return self._properties["status"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_completed(self):
        """
        :returns: The date and time in GMT when the composition's media processing task finished, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_completed"]

    @property
    def date_deleted(self):
        """
        :returns: The date and time in GMT when the composition generated media was deleted, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_deleted"]

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Composition resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def room_sid(self):
        """
        :returns: The SID of the Group Room that generated the audio and video tracks used in the composition. All media sources included in a composition must belong to the same Group Room.
        :rtype: str
        """
        return self._properties["room_sid"]

    @property
    def audio_sources(self):
        """
        :returns: The array of track names to include in the composition. The composition includes all audio sources specified in `audio_sources` except those specified in `audio_sources_excluded`. The track names in this property can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` includes tracks named `student` as well as `studentTeam`.
        :rtype: List[str]
        """
        return self._properties["audio_sources"]

    @property
    def audio_sources_excluded(self):
        """
        :returns: The array of track names to exclude from the composition. The composition includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this property can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
        :rtype: List[str]
        """
        return self._properties["audio_sources_excluded"]

    @property
    def video_layout(self):
        """
        :returns: An object that describes the video layout of the composition in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :rtype: dict
        """
        return self._properties["video_layout"]

    @property
    def resolution(self):
        """
        :returns: The dimensions of the video image in pixels expressed as columns (width) and rows (height). The string's format is `{width}x{height}`, such as `640x480`.
        :rtype: str
        """
        return self._properties["resolution"]

    @property
    def trim(self):
        """
        :returns: Whether to remove intervals with no media, as specified in the POST request that created the composition. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :rtype: bool
        """
        return self._properties["trim"]

    @property
    def format(self):
        """
        :returns:
        :rtype: CompositionInstance.Format
        """
        return self._properties["format"]

    @property
    def bitrate(self):
        """
        :returns: The average bit rate of the composition's media.
        :rtype: int
        """
        return self._properties["bitrate"]

    @property
    def size(self):
        """
        :returns: The size of the composed media file in bytes.
        :rtype: int
        """
        return self._properties["size"]

    @property
    def duration(self):
        """
        :returns: The duration of the composition's media file in seconds.
        :rtype: int
        """
        return self._properties["duration"]

    @property
    def media_external_location(self):
        """
        :returns: The URL of the media file associated with the composition when stored externally. See [External S3 Compositions](/docs/video/api/external-s3-compositions) for more details.
        :rtype: str
        """
        return self._properties["media_external_location"]

    @property
    def status_callback(self):
        """
        :returns: The URL called using the `status_callback_method` to send status information on every composition event.
        :rtype: str
        """
        return self._properties["status_callback"]

    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method used to call `status_callback`. Can be: `POST` or `GET`, defaults to `POST`.
        :rtype: str
        """
        return self._properties["status_callback_method"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns: The URL of the media file associated with the composition.
        :rtype: dict
        """
        return self._properties["links"]

    def delete(self):
        """
        Deletes the CompositionInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the CompositionInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the CompositionInstance


        :returns: The fetched CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the CompositionInstance


        :returns: The fetched CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.CompositionInstance {}>".format(context)


class CompositionContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the CompositionContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Composition resource to fetch.

        :returns: twilio.rest.video.v1.composition.CompositionContext
        :rtype: twilio.rest.video.v1.composition.CompositionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Compositions/{sid}".format(**self._solution)

    def delete(self):
        """
        Deletes the CompositionInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the CompositionInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the CompositionInstance


        :returns: The fetched CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CompositionInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the CompositionInstance


        :returns: The fetched CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CompositionInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.CompositionContext {}>".format(context)


class CompositionPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of CompositionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.composition.CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        return CompositionInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.CompositionPage>"


class CompositionList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the CompositionList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.video.v1.composition.CompositionList
        :rtype: twilio.rest.video.v1.composition.CompositionList
        """
        super().__init__(version)

        self._uri = "/Compositions"

    def create(
        self,
        room_sid,
        video_layout=values.unset,
        audio_sources=values.unset,
        audio_sources_excluded=values.unset,
        resolution=values.unset,
        format=values.unset,
        status_callback=values.unset,
        status_callback_method=values.unset,
        trim=values.unset,
    ):
        """
        Create the CompositionInstance

        :param str room_sid: The SID of the Group Room with the media tracks to be used as composition sources.
        :param object video_layout: An object that describes the video layout of the composition in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
        :param List[str] audio_sources: An array of track names from the same group room to merge into the new composition. Can include zero or more track names. The new composition includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which will match zero or more characters in a track name. For example, `student*` includes `student` as well as `studentTeam`. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
        :param List[str] audio_sources_excluded: An array of track names to exclude. The new composition includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which will match zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
        :param str resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to `640x480`.  The string's format is `{width}x{height}` where:   * 16 <= `{width}` <= 1280 * 16 <= `{height}` <= 1280 * `{width}` * `{height}` <= 921,600  Typical values are:   * HD = `1280x720` * PAL = `1024x576` * VGA = `640x480` * CIF = `320x240`  Note that the `resolution` imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :param CompositionInstance.Format format:
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.
        :param bool trim: Whether to clip the intervals where there is no active media in the composition. The default is `true`. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.

        :returns: The created CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        data = values.of(
            {
                "RoomSid": room_sid,
                "VideoLayout": serialize.object(video_layout),
                "AudioSources": serialize.map(audio_sources, lambda e: e),
                "AudioSourcesExcluded": serialize.map(
                    audio_sources_excluded, lambda e: e
                ),
                "Resolution": resolution,
                "Format": format,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "Trim": trim,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CompositionInstance(self._version, payload)

    async def create_async(
        self,
        room_sid,
        video_layout=values.unset,
        audio_sources=values.unset,
        audio_sources_excluded=values.unset,
        resolution=values.unset,
        format=values.unset,
        status_callback=values.unset,
        status_callback_method=values.unset,
        trim=values.unset,
    ):
        """
        Asynchronously create the CompositionInstance

        :param str room_sid: The SID of the Group Room with the media tracks to be used as composition sources.
        :param object video_layout: An object that describes the video layout of the composition in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
        :param List[str] audio_sources: An array of track names from the same group room to merge into the new composition. Can include zero or more track names. The new composition includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which will match zero or more characters in a track name. For example, `student*` includes `student` as well as `studentTeam`. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
        :param List[str] audio_sources_excluded: An array of track names to exclude. The new composition includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which will match zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
        :param str resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to `640x480`.  The string's format is `{width}x{height}` where:   * 16 <= `{width}` <= 1280 * 16 <= `{height}` <= 1280 * `{width}` * `{height}` <= 921,600  Typical values are:   * HD = `1280x720` * PAL = `1024x576` * VGA = `640x480` * CIF = `320x240`  Note that the `resolution` imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :param CompositionInstance.Format format:
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.
        :param bool trim: Whether to clip the intervals where there is no active media in the composition. The default is `true`. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.

        :returns: The created CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        data = values.of(
            {
                "RoomSid": room_sid,
                "VideoLayout": serialize.object(video_layout),
                "AudioSources": serialize.map(audio_sources, lambda e: e),
                "AudioSourcesExcluded": serialize.map(
                    audio_sources_excluded, lambda e: e
                ),
                "Resolution": resolution,
                "Format": format,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "Trim": trim,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CompositionInstance(self._version, payload)

    def stream(
        self,
        status=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        room_sid=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams CompositionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param CompositionInstance.Status status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param str room_sid: Read only Composition resources with this Room SID.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.composition.CompositionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            room_sid=room_sid,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        room_sid=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams CompositionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param CompositionInstance.Status status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param str room_sid: Read only Composition resources with this Room SID.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.composition.CompositionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            status=status,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            room_sid=room_sid,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        room_sid=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists CompositionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param CompositionInstance.Status status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param str room_sid: Read only Composition resources with this Room SID.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.composition.CompositionInstance]
        """
        return list(
            self.stream(
                status=status,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                room_sid=room_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        room_sid=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists CompositionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param CompositionInstance.Status status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param str room_sid: Read only Composition resources with this Room SID.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.composition.CompositionInstance]
        """
        return list(
            await self.stream_async(
                status=status,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                room_sid=room_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        status=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        room_sid=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of CompositionInstance records from the API.
        Request is executed immediately

        :param CompositionInstance.Status status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param str room_sid: Read only Composition resources with this Room SID.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionPage
        """
        data = values.of(
            {
                "Status": status,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "RoomSid": room_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CompositionPage(self._version, response)

    async def page_async(
        self,
        status=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        room_sid=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of CompositionInstance records from the API.
        Request is executed immediately

        :param CompositionInstance.Status status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param str room_sid: Read only Composition resources with this Room SID.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionPage
        """
        data = values.of(
            {
                "Status": status,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "RoomSid": room_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return CompositionPage(self._version, response)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CompositionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CompositionPage(self._version, response)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of CompositionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CompositionPage(self._version, response)

    def get(self, sid):
        """
        Constructs a CompositionContext

        :param sid: The SID of the Composition resource to fetch.

        :returns: twilio.rest.video.v1.composition.CompositionContext
        :rtype: twilio.rest.video.v1.composition.CompositionContext
        """
        return CompositionContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a CompositionContext

        :param sid: The SID of the Composition resource to fetch.

        :returns: twilio.rest.video.v1.composition.CompositionContext
        :rtype: twilio.rest.video.v1.composition.CompositionContext
        """
        return CompositionContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Video.V1.CompositionList>"
