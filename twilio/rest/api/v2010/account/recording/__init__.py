# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.api.v2010.account.recording.add_on_result import AddOnResultList
from twilio.rest.api.v2010.account.recording.transcription import TranscriptionList


class RecordingList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the RecordingList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.recording.RecordingList
        :rtype: twilio.rest.api.v2010.account.recording.RecordingList
        """
        super(RecordingList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/Recordings.json'.format(**self._solution)

    def stream(self, date_created_before=values.unset, date_created=values.unset,
               date_created_after=values.unset, call_sid=values.unset,
               conference_sid=values.unset, limit=None, page_size=None):
        """
        Streams RecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime date_created_before: Only include recordings that were created on this date
        :param datetime date_created: Only include recordings that were created on this date
        :param datetime date_created_after: Only include recordings that were created on this date
        :param unicode call_sid: The Call SID of the resources to read
        :param unicode conference_sid: Read by unique Conference SID for the recording
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.recording.RecordingInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            date_created_before=date_created_before,
            date_created=date_created,
            date_created_after=date_created_after,
            call_sid=call_sid,
            conference_sid=conference_sid,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, date_created_before=values.unset, date_created=values.unset,
             date_created_after=values.unset, call_sid=values.unset,
             conference_sid=values.unset, limit=None, page_size=None):
        """
        Lists RecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime date_created_before: Only include recordings that were created on this date
        :param datetime date_created: Only include recordings that were created on this date
        :param datetime date_created_after: Only include recordings that were created on this date
        :param unicode call_sid: The Call SID of the resources to read
        :param unicode conference_sid: Read by unique Conference SID for the recording
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.recording.RecordingInstance]
        """
        return list(self.stream(
            date_created_before=date_created_before,
            date_created=date_created,
            date_created_after=date_created_after,
            call_sid=call_sid,
            conference_sid=conference_sid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, date_created_before=values.unset, date_created=values.unset,
             date_created_after=values.unset, call_sid=values.unset,
             conference_sid=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RecordingInstance records from the API.
        Request is executed immediately

        :param datetime date_created_before: Only include recordings that were created on this date
        :param datetime date_created: Only include recordings that were created on this date
        :param datetime date_created_after: Only include recordings that were created on this date
        :param unicode call_sid: The Call SID of the resources to read
        :param unicode conference_sid: Read by unique Conference SID for the recording
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingPage
        """
        params = values.of({
            'DateCreated<': serialize.iso8601_datetime(date_created_before),
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateCreated>': serialize.iso8601_datetime(date_created_after),
            'CallSid': call_sid,
            'ConferenceSid': conference_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return RecordingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RecordingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return RecordingPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a RecordingContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.recording.RecordingContext
        :rtype: twilio.rest.api.v2010.account.recording.RecordingContext
        """
        return RecordingContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a RecordingContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.recording.RecordingContext
        :rtype: twilio.rest.api.v2010.account.recording.RecordingContext
        """
        return RecordingContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.RecordingList>'


class RecordingPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the RecordingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.recording.RecordingPage
        :rtype: twilio.rest.api.v2010.account.recording.RecordingPage
        """
        super(RecordingPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RecordingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.recording.RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingInstance
        """
        return RecordingInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.RecordingPage>'


class RecordingContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, sid):
        """
        Initialize the RecordingContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource to fetch
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.recording.RecordingContext
        :rtype: twilio.rest.api.v2010.account.recording.RecordingContext
        """
        super(RecordingContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/Recordings/{sid}.json'.format(**self._solution)

        # Dependents
        self._transcriptions = None
        self._add_on_results = None

    def fetch(self):
        """
        Fetch a RecordingInstance

        :returns: Fetched RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return RecordingInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the RecordingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def transcriptions(self):
        """
        Access the transcriptions

        :returns: twilio.rest.api.v2010.account.recording.transcription.TranscriptionList
        :rtype: twilio.rest.api.v2010.account.recording.transcription.TranscriptionList
        """
        if self._transcriptions is None:
            self._transcriptions = TranscriptionList(
                self._version,
                account_sid=self._solution['account_sid'],
                recording_sid=self._solution['sid'],
            )
        return self._transcriptions

    @property
    def add_on_results(self):
        """
        Access the add_on_results

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultList
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultList
        """
        if self._add_on_results is None:
            self._add_on_results = AddOnResultList(
                self._version,
                account_sid=self._solution['account_sid'],
                reference_sid=self._solution['sid'],
            )
        return self._add_on_results

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.RecordingContext {}>'.format(context)


class RecordingInstance(InstanceResource):
    """  """

    class Status(object):
        IN_PROGRESS = "in-progress"
        PAUSED = "paused"
        STOPPED = "stopped"
        PROCESSING = "processing"
        COMPLETED = "completed"
        ABSENT = "absent"

    class Source(object):
        DIALVERB = "DialVerb"
        CONFERENCE = "Conference"
        OUTBOUNDAPI = "OutboundAPI"
        TRUNKING = "Trunking"
        RECORDVERB = "RecordVerb"
        STARTCALLRECORDINGAPI = "StartCallRecordingAPI"
        STARTCONFERENCERECORDINGAPI = "StartConferenceRecordingAPI"

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the RecordingInstance

        :returns: twilio.rest.api.v2010.account.recording.RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingInstance
        """
        super(RecordingInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'api_version': payload.get('api_version'),
            'call_sid': payload.get('call_sid'),
            'conference_sid': payload.get('conference_sid'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'start_time': deserialize.rfc2822_datetime(payload.get('start_time')),
            'duration': payload.get('duration'),
            'sid': payload.get('sid'),
            'price': payload.get('price'),
            'price_unit': payload.get('price_unit'),
            'status': payload.get('status'),
            'channels': deserialize.integer(payload.get('channels')),
            'source': payload.get('source'),
            'error_code': deserialize.integer(payload.get('error_code')),
            'uri': payload.get('uri'),
            'encryption_details': payload.get('encryption_details'),
            'subresource_uris': payload.get('subresource_uris'),
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: RecordingContext for this RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingContext
        """
        if self._context is None:
            self._context = RecordingContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """
        :returns: The API version used during the recording.
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def call_sid(self):
        """
        :returns: The SID of the Call the resource is associated with
        :rtype: unicode
        """
        return self._properties['call_sid']

    @property
    def conference_sid(self):
        """
        :returns: The unique ID for the conference associated with the recording.
        :rtype: unicode
        """
        return self._properties['conference_sid']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def start_time(self):
        """
        :returns: The start time of the recording, given in RFC 2822 format
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def duration(self):
        """
        :returns: The length of the recording in seconds.
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def price(self):
        """
        :returns: The one-time cost of creating the recording.
        :rtype: unicode
        """
        return self._properties['price']

    @property
    def price_unit(self):
        """
        :returns: The currency used in the price property.
        :rtype: unicode
        """
        return self._properties['price_unit']

    @property
    def status(self):
        """
        :returns: The status of the recording.
        :rtype: RecordingInstance.Status
        """
        return self._properties['status']

    @property
    def channels(self):
        """
        :returns: The number of channels in the final recording file as an integer.
        :rtype: unicode
        """
        return self._properties['channels']

    @property
    def source(self):
        """
        :returns: How the recording was created
        :rtype: RecordingInstance.Source
        """
        return self._properties['source']

    @property
    def error_code(self):
        """
        :returns: More information about why the recording is missing, if status is `absent`.
        :rtype: unicode
        """
        return self._properties['error_code']

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def encryption_details(self):
        """
        :returns: How to decrypt the recording.
        :rtype: dict
        """
        return self._properties['encryption_details']

    @property
    def subresource_uris(self):
        """
        :returns: A list of related resources identified by their relative URIs
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    def fetch(self):
        """
        Fetch a RecordingInstance

        :returns: Fetched RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the RecordingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def transcriptions(self):
        """
        Access the transcriptions

        :returns: twilio.rest.api.v2010.account.recording.transcription.TranscriptionList
        :rtype: twilio.rest.api.v2010.account.recording.transcription.TranscriptionList
        """
        return self._proxy.transcriptions

    @property
    def add_on_results(self):
        """
        Access the add_on_results

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultList
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultList
        """
        return self._proxy.add_on_results

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.RecordingInstance {}>'.format(context)
