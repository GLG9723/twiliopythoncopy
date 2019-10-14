# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class SubscribedTrackList(ListResource):
    """  """

    def __init__(self, version, room_sid, participant_sid):
        """
        Initialize the SubscribedTrackList

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the room where the track is published
        :param participant_sid: The SID of the participant that subscribes to the track

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackList
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackList
        """
        super(SubscribedTrackList, self).__init__(version)

        # Path Solution
        self._solution = {'room_sid': room_sid, 'participant_sid': participant_sid, }
        self._uri = '/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
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
        :rtype: list[twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
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
        :rtype: list[twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SubscribedTrackInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SubscribedTrackPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SubscribedTrackInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SubscribedTrackPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SubscribedTrackContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackContext
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackContext
        """
        return SubscribedTrackContext(
            self._version,
            room_sid=self._solution['room_sid'],
            participant_sid=self._solution['participant_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a SubscribedTrackContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackContext
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackContext
        """
        return SubscribedTrackContext(
            self._version,
            room_sid=self._solution['room_sid'],
            participant_sid=self._solution['participant_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.SubscribedTrackList>'


class SubscribedTrackPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the SubscribedTrackPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param room_sid: The SID of the room where the track is published
        :param participant_sid: The SID of the participant that subscribes to the track

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackPage
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackPage
        """
        super(SubscribedTrackPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SubscribedTrackInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        """
        return SubscribedTrackInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            participant_sid=self._solution['participant_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.SubscribedTrackPage>'


class SubscribedTrackContext(InstanceContext):
    """  """

    def __init__(self, version, room_sid, participant_sid, sid):
        """
        Initialize the SubscribedTrackContext

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the Room where the Track resource to fetch is subscribed
        :param participant_sid: The SID of the participant that subscribes to the Track resource to fetch
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackContext
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackContext
        """
        super(SubscribedTrackContext, self).__init__(version)

        # Path Solution
        self._solution = {'room_sid': room_sid, 'participant_sid': participant_sid, 'sid': sid, }
        self._uri = '/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a SubscribedTrackInstance

        :returns: Fetched SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SubscribedTrackInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            participant_sid=self._solution['participant_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.SubscribedTrackContext {}>'.format(context)


class SubscribedTrackInstance(InstanceResource):
    """  """

    class Kind(object):
        AUDIO = "audio"
        VIDEO = "video"
        DATA = "data"

    def __init__(self, version, payload, room_sid, participant_sid, sid=None):
        """
        Initialize the SubscribedTrackInstance

        :returns: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        """
        super(SubscribedTrackInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'participant_sid': payload.get('participant_sid'),
            'publisher_sid': payload.get('publisher_sid'),
            'room_sid': payload.get('room_sid'),
            'name': payload.get('name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'enabled': payload.get('enabled'),
            'kind': payload.get('kind'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'room_sid': room_sid,
            'participant_sid': participant_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SubscribedTrackContext for this SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackContext
        """
        if self._context is None:
            self._context = SubscribedTrackContext(
                self._version,
                room_sid=self._solution['room_sid'],
                participant_sid=self._solution['participant_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def participant_sid(self):
        """
        :returns: The SID of the participant that subscribes to the track
        :rtype: unicode
        """
        return self._properties['participant_sid']

    @property
    def publisher_sid(self):
        """
        :returns: The SID of the participant that publishes the track
        :rtype: unicode
        """
        return self._properties['publisher_sid']

    @property
    def room_sid(self):
        """
        :returns: The SID of the room where the track is published
        :rtype: unicode
        """
        return self._properties['room_sid']

    @property
    def name(self):
        """
        :returns: The track name
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def enabled(self):
        """
        :returns: Whether the track is enabled
        :rtype: bool
        """
        return self._properties['enabled']

    @property
    def kind(self):
        """
        :returns: The track type
        :rtype: SubscribedTrackInstance.Kind
        """
        return self._properties['kind']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a SubscribedTrackInstance

        :returns: Fetched SubscribedTrackInstance
        :rtype: twilio.rest.video.v1.room.room_participant.room_participant_subscribed_track.SubscribedTrackInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.SubscribedTrackInstance {}>'.format(context)
