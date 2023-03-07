"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Proxy
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
from twilio.rest.proxy.v1.service.phone_number import PhoneNumberList
from twilio.rest.proxy.v1.service.session import SessionList
from twilio.rest.proxy.v1.service.short_code import ShortCodeList


class ServiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.proxy.v1.service.ServiceList
        :rtype: twilio.rest.proxy.v1.service.ServiceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Services'.format(**self._solution)
        
        
    
    
    
    
    def create(self, unique_name, default_ttl=values.unset, callback_url=values.unset, geo_match_level=values.unset, number_selection_behavior=values.unset, intercept_callback_url=values.unset, out_of_session_callback_url=values.unset, chat_instance_sid=values.unset):
        """
        Create the ServiceInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :param int default_ttl: The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
        :param str callback_url: The URL we should call when the interaction status changes.
        :param ServiceInstance.GeoMatchLevel geo_match_level: 
        :param ServiceInstance.NumberSelectionBehavior number_selection_behavior: 
        :param str intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
        :param str out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
        :param str chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
        
        :returns: The created ServiceInstance
        :rtype: twilio.rest.proxy.v1.service.ServiceInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'DefaultTtl': default_ttl,
            'CallbackUrl': callback_url,
            'GeoMatchLevel': geo_match_level,
            'NumberSelectionBehavior': number_selection_behavior,
            'InterceptCallbackUrl': intercept_callback_url,
            'OutOfSessionCallbackUrl': out_of_session_callback_url,
            'ChatInstanceSid': chat_instance_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ServiceInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.proxy.v1.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.service.ServiceInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.proxy.v1.service.ServicePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.proxy.v1.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ServicePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
        
        :returns: twilio.rest.proxy.v1.service.ServiceContext
        :rtype: twilio.rest.proxy.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
        
        :returns: twilio.rest.proxy.v1.service.ServiceContext
        :rtype: twilio.rest.proxy.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.ServiceList>'










class ServicePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.proxy.v1.service.ServicePage
        :rtype: twilio.rest.proxy.v1.service.ServicePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.proxy.v1.service.ServiceInstance
        :rtype: twilio.rest.proxy.v1.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.ServicePage>'




class ServiceContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param Version version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.

        :returns: twilio.rest.proxy.v1.service.ServiceContext
        :rtype: twilio.rest.proxy.v1.service.ServiceContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Services/{sid}'.format(**self._solution)
        
        self._phone_numbers = None
        self._sessions = None
        self._short_codes = None
    
    def delete(self):
        """
        Deletes the ServiceInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the ServiceInstance
        

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.proxy.v1.service.ServiceInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, unique_name=values.unset, default_ttl=values.unset, callback_url=values.unset, geo_match_level=values.unset, number_selection_behavior=values.unset, intercept_callback_url=values.unset, out_of_session_callback_url=values.unset, chat_instance_sid=values.unset):
        """
        Update the ServiceInstance
        
        :params str unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :params int default_ttl: The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
        :params str callback_url: The URL we should call when the interaction status changes.
        :params ServiceInstance.GeoMatchLevel geo_match_level: 
        :params ServiceInstance.NumberSelectionBehavior number_selection_behavior: 
        :params str intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
        :params str out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
        :params str chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.proxy.v1.service.ServiceInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'DefaultTtl': default_ttl,
            'CallbackUrl': callback_url,
            'GeoMatchLevel': geo_match_level,
            'NumberSelectionBehavior': number_selection_behavior,
            'InterceptCallbackUrl': intercept_callback_url,
            'OutOfSessionCallbackUrl': out_of_session_callback_url,
            'ChatInstanceSid': chat_instance_sid,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def phone_numbers(self):
        """
        Access the phone_numbers

        :returns: twilio.rest.proxy.v1.service.PhoneNumberList
        :rtype: twilio.rest.proxy.v1.service.PhoneNumberList
        """
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(
                self._version, 
                self._solution['sid'],
            )
        return self._phone_numbers
    
    @property
    def sessions(self):
        """
        Access the sessions

        :returns: twilio.rest.proxy.v1.service.SessionList
        :rtype: twilio.rest.proxy.v1.service.SessionList
        """
        if self._sessions is None:
            self._sessions = SessionList(
                self._version, 
                self._solution['sid'],
            )
        return self._sessions
    
    @property
    def short_codes(self):
        """
        Access the short_codes

        :returns: twilio.rest.proxy.v1.service.ShortCodeList
        :rtype: twilio.rest.proxy.v1.service.ShortCodeList
        """
        if self._short_codes is None:
            self._short_codes = ShortCodeList(
                self._version, 
                self._solution['sid'],
            )
        return self._short_codes
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Proxy.V1.ServiceContext {}>'.format(context)

class ServiceInstance(InstanceResource):

    class GeoMatchLevel(object):
        AREA_CODE = "area-code"
        OVERLAY = "overlay"
        RADIUS = "radius"
        COUNTRY = "country"

    class NumberSelectionBehavior(object):
        AVOID_STICKY = "avoid-sticky"
        PREFER_STICKY = "prefer-sticky"

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the ServiceInstance
        :returns: twilio.rest.proxy.v1.service.ServiceInstance
        :rtype: twilio.rest.proxy.v1.service.ServiceInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'account_sid': payload.get('account_sid'),
            'chat_instance_sid': payload.get('chat_instance_sid'),
            'callback_url': payload.get('callback_url'),
            'default_ttl': deserialize.integer(payload.get('default_ttl')),
            'number_selection_behavior': payload.get('number_selection_behavior'),
            'geo_match_level': payload.get('geo_match_level'),
            'intercept_callback_url': payload.get('intercept_callback_url'),
            'out_of_session_callback_url': payload.get('out_of_session_callback_url'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
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

        :returns: ServiceContext for this ServiceInstance
        :rtype: twilio.rest.proxy.v1.service.ServiceContext
        """
        if self._context is None:
            self._context = ServiceContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Service resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. Supports UTF-8 characters. **This value should not have PII.**
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def chat_instance_sid(self):
        """
        :returns: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
        :rtype: str
        """
        return self._properties['chat_instance_sid']
    
    @property
    def callback_url(self):
        """
        :returns: The URL we call when the interaction status changes.
        :rtype: str
        """
        return self._properties['callback_url']
    
    @property
    def default_ttl(self):
        """
        :returns: The default `ttl` value for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
        :rtype: int
        """
        return self._properties['default_ttl']
    
    @property
    def number_selection_behavior(self):
        """
        :returns: 
        :rtype: ServiceInstance.NumberSelectionBehavior
        """
        return self._properties['number_selection_behavior']
    
    @property
    def geo_match_level(self):
        """
        :returns: 
        :rtype: ServiceInstance.GeoMatchLevel
        """
        return self._properties['geo_match_level']
    
    @property
    def intercept_callback_url(self):
        """
        :returns: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
        :rtype: str
        """
        return self._properties['intercept_callback_url']
    
    @property
    def out_of_session_callback_url(self):
        """
        :returns: The URL we call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
        :rtype: str
        """
        return self._properties['out_of_session_callback_url']
    
    @property
    def date_created(self):
        """
        :returns: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Service resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of resources related to the Service.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the ServiceInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the ServiceInstance
        

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.proxy.v1.service.ServiceInstance
        """
        return self._proxy.fetch()
    
    def update(self, unique_name=values.unset, default_ttl=values.unset, callback_url=values.unset, geo_match_level=values.unset, number_selection_behavior=values.unset, intercept_callback_url=values.unset, out_of_session_callback_url=values.unset, chat_instance_sid=values.unset):
        """
        Update the ServiceInstance
        
        :params str unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :params int default_ttl: The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
        :params str callback_url: The URL we should call when the interaction status changes.
        :params ServiceInstance.GeoMatchLevel geo_match_level: 
        :params ServiceInstance.NumberSelectionBehavior number_selection_behavior: 
        :params str intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
        :params str out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
        :params str chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.proxy.v1.service.ServiceInstance
        """
        return self._proxy.update(unique_name=unique_name, default_ttl=default_ttl, callback_url=callback_url, geo_match_level=geo_match_level, number_selection_behavior=number_selection_behavior, intercept_callback_url=intercept_callback_url, out_of_session_callback_url=out_of_session_callback_url, chat_instance_sid=chat_instance_sid, )
    
    @property
    def phone_numbers(self):
        """
        Access the phone_numbers

        :returns: twilio.rest.proxy.v1.service.PhoneNumberList
        :rtype: twilio.rest.proxy.v1.service.PhoneNumberList
        """
        return self._proxy.phone_numbers
    
    @property
    def sessions(self):
        """
        Access the sessions

        :returns: twilio.rest.proxy.v1.service.SessionList
        :rtype: twilio.rest.proxy.v1.service.SessionList
        """
        return self._proxy.sessions
    
    @property
    def short_codes(self):
        """
        Access the short_codes

        :returns: twilio.rest.proxy.v1.service.ShortCodeList
        :rtype: twilio.rest.proxy.v1.service.ShortCodeList
        """
        return self._proxy.short_codes
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Proxy.V1.ServiceInstance {}>'.format(context)


