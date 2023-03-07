"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.sync.v1.service.sync_stream.stream_message import StreamMessageList


class SyncStreamList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the SyncStreamList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Stream resources to read.
        
        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamList
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Streams'.format(**self._solution)
        
        
    
    
    
    
    def create(self, unique_name=values.unset, ttl=values.unset):
        """
        Create the SyncStreamInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within its Service and it can be up to 320 characters long. The `unique_name` value can be used as an alternative to the `sid` in the URL path to address the resource.
        :param int ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).
        
        :returns: The created SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'Ttl': ttl,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return SyncStreamInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams SyncStreamInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SyncStreamInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SyncStreamInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SyncStreamPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncStreamInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SyncStreamPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a SyncStreamContext
        
        :param sid: The SID of the Stream resource to update.
        
        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        """
        return SyncStreamContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a SyncStreamContext
        
        :param sid: The SID of the Stream resource to update.
        
        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        """
        return SyncStreamContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncStreamList>'










class SyncStreamPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SyncStreamPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamPage
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncStreamInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        return SyncStreamInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncStreamPage>'




class SyncStreamContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the SyncStreamContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to update.
        :param sid: The SID of the Stream resource to update.

        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Streams/{sid}'.format(**self._solution)
        
        self._stream_messages = None
    
    def delete(self):
        """
        Deletes the SyncStreamInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the SyncStreamInstance
        

        :returns: The fetched SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SyncStreamInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, ttl=values.unset):
        """
        Update the SyncStreamInstance
        
        :params int ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).

        :returns: The updated SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        data = values.of({ 
            'Ttl': ttl,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SyncStreamInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def stream_messages(self):
        """
        Access the stream_messages

        :returns: twilio.rest.sync.v1.service.sync_stream.StreamMessageList
        :rtype: twilio.rest.sync.v1.service.sync_stream.StreamMessageList
        """
        if self._stream_messages is None:
            self._stream_messages = StreamMessageList(
                self._version, 
                self._solution['service_sid'],
                self._solution['sid'],
            )
        return self._stream_messages
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncStreamContext {}>'.format(context)

class SyncStreamInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the SyncStreamInstance
        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'url': payload.get('url'),
            'links': payload.get('links'),
            'date_expires': deserialize.iso8601_datetime(payload.get('date_expires')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'created_by': payload.get('created_by'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncStreamContext for this SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        """
        if self._context is None:
            self._context = SyncStreamContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Sync Stream resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Sync Stream resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Message Stream resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of the Stream's nested resources.
        :rtype: dict
        """
        return self._properties['links']
    
    @property
    def date_expires(self):
        """
        :returns: The date and time in GMT when the Message Stream expires and will be deleted, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. If the Message Stream does not expire, this value is `null`. The Stream might not be deleted immediately after it expires.
        :rtype: datetime
        """
        return self._properties['date_expires']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def created_by(self):
        """
        :returns: The identity of the Stream's creator. If the Stream is created from the client SDK, the value matches the Access Token's `identity` field. If the Stream was created from the REST API, the value is 'system'.
        :rtype: str
        """
        return self._properties['created_by']
    
    def delete(self):
        """
        Deletes the SyncStreamInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the SyncStreamInstance
        

        :returns: The fetched SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        return self._proxy.fetch()
    
    def update(self, ttl=values.unset):
        """
        Update the SyncStreamInstance
        
        :params int ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).

        :returns: The updated SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        return self._proxy.update(ttl=ttl, )
    
    @property
    def stream_messages(self):
        """
        Access the stream_messages

        :returns: twilio.rest.sync.v1.service.sync_stream.StreamMessageList
        :rtype: twilio.rest.sync.v1.service.sync_stream.StreamMessageList
        """
        return self._proxy.stream_messages
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncStreamInstance {}>'.format(context)


