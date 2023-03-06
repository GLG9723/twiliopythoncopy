"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
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
from twilio.rest.events.v1.subscription.subscribed_event import SubscribedEventList


class SubscriptionList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SubscriptionList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.events.v1.subscription.SubscriptionList
        :rtype: twilio.rest.events.v1.subscription.SubscriptionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Subscriptions'.format(**self._solution)
        
        
    
    
    
    
    def create(self, description, sink_sid, types):
        """
        Create the SubscriptionInstance

        :param str description: A human readable description for the Subscription **This value should not contain PII.**
        :param str sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
        :param list[object] types: An array of objects containing the subscribed Event Types
        
        :returns: The created SubscriptionInstance
        :rtype: twilio.rest.events.v1.subscription.SubscriptionInstance
        """
        data = values.of({ 
            'Description': description,
            'SinkSid': sink_sid,
            'Types': serialize.map(types, lambda e: serialize.object(e)),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return SubscriptionInstance(self._version, payload)
    
    
    def stream(self, sink_sid=values.unset, limit=None, page_size=None):
        """
        Streams SubscriptionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str sink_sid: The SID of the sink that the list of Subscriptions should be filtered by.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.subscription.SubscriptionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            sink_sid=sink_sid,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, sink_sid=values.unset, limit=None, page_size=None):
        """
        Lists SubscriptionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str sink_sid: The SID of the sink that the list of Subscriptions should be filtered by.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.subscription.SubscriptionInstance]
        """
        return list(self.stream(
            sink_sid=sink_sid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, sink_sid=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SubscriptionInstance records from the API.
        Request is executed immediately
        
        :param str sink_sid: The SID of the sink that the list of Subscriptions should be filtered by.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SubscriptionInstance
        :rtype: twilio.rest.events.v1.subscription.SubscriptionPage
        """
        data = values.of({ 
            'SinkSid': sink_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SubscriptionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SubscriptionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SubscriptionInstance
        :rtype: twilio.rest.events.v1.subscription.SubscriptionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SubscriptionPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a SubscriptionContext
        
        :param sid: A 34 character string that uniquely identifies this Subscription.
        
        :returns: twilio.rest.events.v1.subscription.SubscriptionContext
        :rtype: twilio.rest.events.v1.subscription.SubscriptionContext
        """
        return SubscriptionContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a SubscriptionContext
        
        :param sid: A 34 character string that uniquely identifies this Subscription.
        
        :returns: twilio.rest.events.v1.subscription.SubscriptionContext
        :rtype: twilio.rest.events.v1.subscription.SubscriptionContext
        """
        return SubscriptionContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.SubscriptionList>'










class SubscriptionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SubscriptionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.events.v1.subscription.SubscriptionPage
        :rtype: twilio.rest.events.v1.subscription.SubscriptionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SubscriptionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.events.v1.subscription.SubscriptionInstance
        :rtype: twilio.rest.events.v1.subscription.SubscriptionInstance
        """
        return SubscriptionInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.SubscriptionPage>'




class SubscriptionContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the SubscriptionContext

        :param Version version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this Subscription.

        :returns: twilio.rest.events.v1.subscription.SubscriptionContext
        :rtype: twilio.rest.events.v1.subscription.SubscriptionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Subscriptions/{sid}'.format(**self._solution)
        
        self._subscribed_events = None
    
    def delete(self):
        """
        Deletes the SubscriptionInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the SubscriptionInstance
        

        :returns: The fetched SubscriptionInstance
        :rtype: twilio.rest.events.v1.subscription.SubscriptionInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SubscriptionInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, description=values.unset, sink_sid=values.unset):
        """
        Update the SubscriptionInstance
        
        :params str description: A human readable description for the Subscription.
        :params str sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.

        :returns: The updated SubscriptionInstance
        :rtype: twilio.rest.events.v1.subscription.SubscriptionInstance
        """
        data = values.of({ 
            'Description': description,
            'SinkSid': sink_sid,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SubscriptionInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def subscribed_events(self):
        """
        Access the subscribed_events

        :returns: twilio.rest.events.v1.subscription.SubscribedEventList
        :rtype: twilio.rest.events.v1.subscription.SubscribedEventList
        """
        if self._subscribed_events is None:
            self._subscribed_events = SubscribedEventList(self._version, self._solution['sid'],
            )
        return self._subscribed_events
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SubscriptionContext {}>'.format(context)

class SubscriptionInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the SubscriptionInstance
        :returns: twilio.rest.events.v1.subscription.SubscriptionInstance
        :rtype: twilio.rest.events.v1.subscription.SubscriptionInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'sid': payload.get('sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'description': payload.get('description'),
            'sink_sid': payload.get('sink_sid'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SubscriptionContext for this SubscriptionInstance
        :rtype: twilio.rest.events.v1.subscription.SubscriptionContext
        """
        if self._context is None:
            self._context = SubscriptionContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this Subscription.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def date_created(self):
        """
        :returns: The date that this Subscription was created, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this Subscription was updated, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def description(self):
        """
        :returns: A human readable description for the Subscription
        :rtype: str
        """
        return self._properties['description']
    
    @property
    def sink_sid(self):
        """
        :returns: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
        :rtype: str
        """
        return self._properties['sink_sid']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: Contains a dictionary of URL links to nested resources of this Subscription.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the SubscriptionInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the SubscriptionInstance
        

        :returns: The fetched SubscriptionInstance
        :rtype: twilio.rest.events.v1.subscription.SubscriptionInstance
        """
        return self._proxy.fetch()
    
    def update(self, description=values.unset, sink_sid=values.unset):
        """
        Update the SubscriptionInstance
        
        :params str description: A human readable description for the Subscription.
        :params str sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.

        :returns: The updated SubscriptionInstance
        :rtype: twilio.rest.events.v1.subscription.SubscriptionInstance
        """
        return self._proxy.update(description=description, sink_sid=sink_sid, )
    
    @property
    def subscribed_events(self):
        """
        Access the subscribed_events

        :returns: twilio.rest.events.v1.subscription.SubscribedEventList
        :rtype: twilio.rest.events.v1.subscription.SubscribedEventList
        """
        return self._proxy.subscribed_events
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SubscriptionInstance {}>'.format(context)


