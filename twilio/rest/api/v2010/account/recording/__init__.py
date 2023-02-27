"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.api.v2010.account.recording.add_on_result import AddOnResultList
from twilio.rest.api.v2010.account.recording.transcription import TranscriptionList


class RecordingList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the RecordingList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to read.
        
        :returns: twilio.rest.api.v2010.account.recording.RecordingList
        :rtype: twilio.rest.api.v2010.account.recording.RecordingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/Recordings.json'.format(**self._solution)
        
        
    
    
    
    def stream(self, date_created=values.unset, date_created_before=values.unset, date_created_after=values.unset, call_sid=values.unset, conference_sid=values.unset, include_soft_deleted=values.unset, limit=None, page_size=None):
        """
        Streams RecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param datetime date_created: Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
        :param datetime date_created_before: Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
        :param datetime date_created_after: Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
        :param str call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read.
        :param str conference_sid: The Conference SID that identifies the conference associated with the recording to read.
        :param bool include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days.
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
            date_created=date_created,
            date_created_before=date_created_before,
            date_created_after=date_created_after,
            call_sid=call_sid,
            conference_sid=conference_sid,
            include_soft_deleted=include_soft_deleted,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, date_created=values.unset, date_created_before=values.unset, date_created_after=values.unset, call_sid=values.unset, conference_sid=values.unset, include_soft_deleted=values.unset, limit=None, page_size=None):
        """
        Lists RecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param datetime date_created: Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
        :param datetime date_created_before: Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
        :param datetime date_created_after: Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
        :param str call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read.
        :param str conference_sid: The Conference SID that identifies the conference associated with the recording to read.
        :param bool include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days.
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
            date_created=date_created,
            date_created_before=date_created_before,
            date_created_after=date_created_after,
            call_sid=call_sid,
            conference_sid=conference_sid,
            include_soft_deleted=include_soft_deleted,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, date_created=values.unset, date_created_before=values.unset, date_created_after=values.unset, call_sid=values.unset, conference_sid=values.unset, include_soft_deleted=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RecordingInstance records from the API.
        Request is executed immediately
        
        :param datetime date_created: Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
        :param datetime date_created_before: Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
        :param datetime date_created_after: Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
        :param str call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read.
        :param str conference_sid: The Conference SID that identifies the conference associated with the recording to read.
        :param bool include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingPage
        """
        data = values.of({ 
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateCreated<': serialize.iso8601_datetime(date_created_before),
            'DateCreated>': serialize.iso8601_datetime(date_created_after),
            'CallSid': call_sid,
            'ConferenceSid': conference_sid,
            'IncludeSoftDeleted': include_soft_deleted,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
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
            target_url
        )
        return RecordingPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a RecordingContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Recording resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.recording.RecordingContext
        :rtype: twilio.rest.api.v2010.account.recording.RecordingContext
        """
        return RecordingContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a RecordingContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Recording resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.recording.RecordingContext
        :rtype: twilio.rest.api.v2010.account.recording.RecordingContext
        """
        return RecordingContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.RecordingList>'






class RecordingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RecordingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.recording.RecordingPage
        :rtype: twilio.rest.api.v2010.account.recording.RecordingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RecordingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.recording.RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingInstance
        """
        return RecordingInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.RecordingPage>'




class RecordingContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the RecordingContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to fetch.:param sid: The Twilio-provided string that uniquely identifies the Recording resource to fetch.

        :returns: twilio.rest.api.v2010.account.recording.RecordingContext
        :rtype: twilio.rest.api.v2010.account.recording.RecordingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Recordings/{sid}.json'.format(**self._solution)
        
        self._add_on_results = None
        self._transcriptions = None
    
    def delete(self):
        """
        Deletes the RecordingInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self, include_soft_deleted=values.unset):
        """
        Fetch the RecordingInstance
        
        :params bool include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days.

        :returns: The fetched RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingInstance
        """
        
        data = values.of({ 
            'IncludeSoftDeleted': include_soft_deleted,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return RecordingInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    @property
    def add_on_results(self):
        """
        Access the add_on_results

        :returns: twilio.rest.api.v2010.account.recording.AddOnResultList
        :rtype: twilio.rest.api.v2010.account.recording.AddOnResultList
        """
        if self._add_on_results is None:
            self._add_on_results = AddOnResultList(self._version, self._solution['account_sid'], self._solution['sid'],
            )
        return self._add_on_results
    
    @property
    def transcriptions(self):
        """
        Access the transcriptions

        :returns: twilio.rest.api.v2010.account.recording.TranscriptionList
        :rtype: twilio.rest.api.v2010.account.recording.TranscriptionList
        """
        if self._transcriptions is None:
            self._transcriptions = TranscriptionList(self._version, self._solution['account_sid'], self._solution['sid'],
            )
        return self._transcriptions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.RecordingContext {}>'.format(context)

class RecordingInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, sid: str=None):
        """
        Initialize the RecordingInstance
        :returns: twilio.rest.api.v2010.account.recording.RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingInstance
        """
        super().__init__(version)

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
            'media_url': payload.get('media_url'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RecordingContext for this RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingContext
        """
        if self._context is None:
            self._context = RecordingContext(self._version, account_sid=self._solution['account_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def api_version(self):
        """
        :returns: The API version used during the recording.
        :rtype: str
        """
        return self._properties['api_version']
    
    @property
    def call_sid(self):
        """
        :returns: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Recording resource is associated with. This will always refer to the parent leg of a two-leg call.
        :rtype: str
        """
        return self._properties['call_sid']
    
    @property
    def conference_sid(self):
        """
        :returns: The Conference SID that identifies the conference associated with the recording, if a conference recording.
        :rtype: str
        """
        return self._properties['conference_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def start_time(self):
        """
        :returns: The start time of the recording in GMT and in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        :rtype: datetime
        """
        return self._properties['start_time']
    
    @property
    def duration(self):
        """
        :returns: The length of the recording in seconds.
        :rtype: str
        """
        return self._properties['duration']
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the Recording resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def price(self):
        """
        :returns: The one-time cost of creating the recording in the `price_unit` currency.
        :rtype: str
        """
        return self._properties['price']
    
    @property
    def price_unit(self):
        """
        :returns: The currency used in the `price` property. Example: `USD`.
        :rtype: str
        """
        return self._properties['price_unit']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: RecordingStatus
        """
        return self._properties['status']
    
    @property
    def channels(self):
        """
        :returns: The number of channels in the final recording file. Can be: `1` or `2`. You can split a call with two legs into two separate recording channels if you record using [TwiML Dial](https://www.twilio.com/docs/voice/twiml/dial#record) or the [Outbound Rest API](https://www.twilio.com/docs/voice/make-calls#manage-your-outbound-call).
        :rtype: int
        """
        return self._properties['channels']
    
    @property
    def source(self):
        """
        :returns: 
        :rtype: RecordingSource
        """
        return self._properties['source']
    
    @property
    def error_code(self):
        """
        :returns: The error code that describes why the recording is `absent`. The error code is described in our [Error Dictionary](https://www.twilio.com/docs/api/errors). This value is null if the recording `status` is not `absent`.
        :rtype: int
        """
        return self._properties['error_code']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    @property
    def encryption_details(self):
        """
        :returns: How to decrypt the recording if it was encrypted using [Call Recording Encryption](https://www.twilio.com/docs/voice/tutorials/voice-recording-encryption) feature.
        :rtype: dict
        """
        return self._properties['encryption_details']
    
    @property
    def subresource_uris(self):
        """
        :returns: A list of related resources identified by their relative URIs.
        :rtype: dict
        """
        return self._properties['subresource_uris']
    
    @property
    def media_url(self):
        """
        :returns: The URL of the media file associated with this recording resource. When stored externally, this is the full URL location of the media file.
        :rtype: str
        """
        return self._properties['media_url']
    
    def delete(self):
        """
        Deletes the RecordingInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self, include_soft_deleted=values.unset):
        """
        Fetch the RecordingInstance
        
        :params bool include_soft_deleted: A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days.

        :returns: The fetched RecordingInstance
        :rtype: twilio.rest.api.v2010.account.recording.RecordingInstance
        """
        return self._proxy.fetch(include_soft_deleted=include_soft_deleted, )
    
    @property
    def add_on_results(self):
        """
        Access the add_on_results

        :returns: twilio.rest.api.v2010.account.recording.AddOnResultList
        :rtype: twilio.rest.api.v2010.account.recording.AddOnResultList
        """
        return self._proxy.add_on_results
    
    @property
    def transcriptions(self):
        """
        Access the transcriptions

        :returns: twilio.rest.api.v2010.account.recording.TranscriptionList
        :rtype: twilio.rest.api.v2010.account.recording.TranscriptionList
        """
        return self._proxy.transcriptions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.RecordingInstance {}>'.format(context)


