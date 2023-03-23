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
from typing import List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SubscribedTrackInstance(InstanceResource):
    class Kind(object):
        AUDIO = "audio"
        VIDEO = "video"
        DATA = "data"

    def __init__(
        self,
        version,
        payload,
        room_sid: str,
        participant_sid: str,
        sid: Optional[str] = None,
    ):
        """
        Initialize the SubscribedTrackInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "participant_sid": payload.get("participant_sid"),
            "publisher_sid": payload.get("publisher_sid"),
            "room_sid": payload.get("room_sid"),
            "name": payload.get("name"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "enabled": payload.get("enabled"),
            "kind": payload.get("kind"),
            "url": payload.get("url"),
        }

        self._solution = {
            "room_sid": room_sid,
            "participant_sid": participant_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[SubscribedTrackContext] = None

    @property
    def _proxy(self) -> "SubscribedTrackContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SubscribedTrackContext for this SubscribedTrackInstance
        """
        if self._context is None:
            self._context = SubscribedTrackContext(
                self._version,
                room_sid=self._solution["room_sid"],
                participant_sid=self._solution["participant_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> str:
        """
        :returns: The unique string that we created to identify the RoomParticipantSubscribedTrack resource.
        """
        return self._properties["sid"]

    @property
    def participant_sid(self) -> str:
        """
        :returns: The SID of the participant that subscribes to the track.
        """
        return self._properties["participant_sid"]

    @property
    def publisher_sid(self) -> str:
        """
        :returns: The SID of the participant that publishes the track.
        """
        return self._properties["publisher_sid"]

    @property
    def room_sid(self) -> str:
        """
        :returns: The SID of the room where the track is published.
        """
        return self._properties["room_sid"]

    @property
    def name(self) -> str:
        """
        :returns: The track name. Must have no more than 128 characters and be unique among the participant's published tracks.
        """
        return self._properties["name"]

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
    def enabled(self) -> bool:
        """
        :returns: Whether the track is enabled.
        """
        return self._properties["enabled"]

    @property
    def kind(self) -> "SubscribedTrackInstance.Kind":
        """
        :returns:
        """
        return self._properties["kind"]

    @property
    def url(self) -> str:
        """
        :returns: The absolute URL of the resource.
        """
        return self._properties["url"]

    def fetch(self) -> "SubscribedTrackInstance":
        """
        Fetch the SubscribedTrackInstance


        :returns: The fetched SubscribedTrackInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SubscribedTrackInstance":
        """
        Asynchronous coroutine to fetch the SubscribedTrackInstance


        :returns: The fetched SubscribedTrackInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.SubscribedTrackInstance {}>".format(context)


class SubscribedTrackContext(InstanceContext):
    def __init__(self, version: Version, room_sid: str, participant_sid: str, sid: str):
        """
        Initialize the SubscribedTrackContext

        :param version: Version that contains the resource
        :param room_sid: The SID of the Room where the Track resource to fetch is subscribed.
        :param participant_sid: The SID of the participant that subscribes to the Track resource to fetch.
        :param sid: The SID of the RoomParticipantSubscribedTrack resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
            "participant_sid": participant_sid,
            "sid": sid,
        }
        self._uri = "/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks/{sid}".format(
            **self._solution
        )

    def fetch(self) -> SubscribedTrackInstance:
        """
        Fetch the SubscribedTrackInstance


        :returns: The fetched SubscribedTrackInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SubscribedTrackInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SubscribedTrackInstance:
        """
        Asynchronous coroutine to fetch the SubscribedTrackInstance


        :returns: The fetched SubscribedTrackInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SubscribedTrackInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.SubscribedTrackContext {}>".format(context)


class SubscribedTrackPage(Page):
    def get_instance(self, payload) -> SubscribedTrackInstance:
        """
        Build an instance of SubscribedTrackInstance

        :param dict payload: Payload response from the API
        """
        return SubscribedTrackInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.SubscribedTrackPage>"


class SubscribedTrackList(ListResource):
    def __init__(self, version: Version, room_sid: str, participant_sid: str):
        """
        Initialize the SubscribedTrackList

        :param version: Version that contains the resource
        :param room_sid: The SID of the Room resource with the Track resources to read.
        :param participant_sid: The SID of the participant that subscribes to the Track resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
            "participant_sid": participant_sid,
        }
        self._uri = (
            "/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks".format(
                **self._solution
            )
        )

    def stream(self, limit=None, page_size=None) -> List[SubscribedTrackInstance]:
        """
        Streams SubscribedTrackInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, limit=None, page_size=None
    ) -> List[SubscribedTrackInstance]:
        """
        Asynchronously streams SubscribedTrackInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None) -> List[SubscribedTrackInstance]:
        """
        Lists SubscribedTrackInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self, limit=None, page_size=None
    ) -> List[SubscribedTrackInstance]:
        """
        Asynchronously lists SubscribedTrackInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> SubscribedTrackPage:
        """
        Retrieve a single page of SubscribedTrackInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SubscribedTrackInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SubscribedTrackPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> SubscribedTrackPage:
        """
        Asynchronously retrieve a single page of SubscribedTrackInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SubscribedTrackInstance
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
        return SubscribedTrackPage(self._version, response, self._solution)

    def get_page(self, target_url) -> SubscribedTrackPage:
        """
        Retrieve a specific page of SubscribedTrackInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SubscribedTrackInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SubscribedTrackPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> SubscribedTrackPage:
        """
        Asynchronously retrieve a specific page of SubscribedTrackInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SubscribedTrackInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SubscribedTrackPage(self._version, response, self._solution)

    def get(self, sid) -> SubscribedTrackContext:
        """
        Constructs a SubscribedTrackContext

        :param sid: The SID of the RoomParticipantSubscribedTrack resource to fetch.
        """
        return SubscribedTrackContext(
            self._version,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> SubscribedTrackContext:
        """
        Constructs a SubscribedTrackContext

        :param sid: The SID of the RoomParticipantSubscribedTrack resource to fetch.
        """
        return SubscribedTrackContext(
            self._version,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.SubscribedTrackList>"
