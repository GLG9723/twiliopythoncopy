"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
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


class BrandVettingList(ListResource):

    def __init__(self, version: Version, brand_sid: str):
        """
        Initialize the BrandVettingList

        :param Version version: Version that contains the resource
        :param brand_sid: The SID of the Brand Registration resource of the vettings to read .
        
        :returns: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingList
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'brand_sid': brand_sid,  }
        self._uri = '/a2p/BrandRegistrations/${brand_sid}/Vettings'.format(**self._solution)
        
        
    
    
    def create(self, vetting_provider, vetting_id=values.unset):
        """
        Create the BrandVettingInstance
        :param BrandVettingVettingProvider vetting_provider: 
        :param str vetting_id: The unique ID of the vetting
        
        :returns: The created BrandVettingInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingInstance
        """
        data = values.of({ 
            'VettingProvider': vetting_provider,
            'VettingId': vetting_id,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return BrandVettingInstance(self._version, payload, brand_sid=self._solution['brand_sid'])
    
    
    def stream(self, vetting_provider=values.unset, limit=None, page_size=None):
        """
        Streams BrandVettingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param BrandVettingVettingProvider vetting_provider: The third-party provider of the vettings to read
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            vetting_provider=vetting_provider,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, vetting_provider=values.unset, limit=None, page_size=None):
        """
        Lists BrandVettingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param BrandVettingVettingProvider vetting_provider: The third-party provider of the vettings to read
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingInstance]
        """
        return list(self.stream(
            vetting_provider=vetting_provider,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, vetting_provider=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of BrandVettingInstance records from the API.
        Request is executed immediately
        
        :param BrandVettingVettingProvider vetting_provider: The third-party provider of the vettings to read
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BrandVettingInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingPage
        """
        data = values.of({ 
            'VettingProvider': vetting_provider,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return BrandVettingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BrandVettingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BrandVettingInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return BrandVettingPage(self._version, response, self._solution)


    def get(self, brand_vetting_sid):
        """
        Constructs a BrandVettingContext
        
        :param brand_vetting_sid: The Twilio SID of the third-party vetting record.
        
        :returns: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingContext
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingContext
        """
        return BrandVettingContext(self._version, brand_sid=self._solution['brand_sid'], brand_vetting_sid=brand_vetting_sid)

    def __call__(self, brand_vetting_sid):
        """
        Constructs a BrandVettingContext
        
        :param brand_vetting_sid: The Twilio SID of the third-party vetting record.
        
        :returns: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingContext
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingContext
        """
        return BrandVettingContext(self._version, brand_sid=self._solution['brand_sid'], brand_vetting_sid=brand_vetting_sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.BrandVettingList>'






class BrandVettingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the BrandVettingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingPage
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BrandVettingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingInstance
        """
        return BrandVettingInstance(self._version, payload, brand_sid=self._solution['brand_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.BrandVettingPage>'




class BrandVettingContext(InstanceContext):

    def __init__(self, version: Version, brand_sid: str, brand_vetting_sid: str):
        """
        Initialize the BrandVettingContext

        :param Version version: Version that contains the resource
        :param brand_sid: The SID of the Brand Registration resource of the vettings to read .:param brand_vetting_sid: The Twilio SID of the third-party vetting record.

        :returns: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingContext
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'brand_sid': brand_sid,
            'brand_vetting_sid': brand_vetting_sid,
        }
        self._uri = '/a2p/BrandRegistrations/${brand_sid}/Vettings/${brand_vetting_sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the BrandVettingInstance

        :returns: The fetched BrandVettingInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri)

        return BrandVettingInstance(
            self._version,
            payload,
            brand_sid=self._solution['brand_sid'],
            brand_vetting_sid=self._solution['brand_vetting_sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.BrandVettingContext {}>'.format(context)

class BrandVettingInstance(InstanceResource):

    def __init__(self, version, payload, brand_sid: str, brand_vetting_sid: str=None):
        """
        Initialize the BrandVettingInstance
        :returns: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'brand_sid': payload.get('brand_sid'),
            'brand_vetting_sid': payload.get('brand_vetting_sid'),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'vetting_id': payload.get('vetting_id'),
            'vetting_class': payload.get('vetting_class'),
            'vetting_status': payload.get('vetting_status'),
            'vetting_provider': payload.get('vetting_provider'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'brand_sid': brand_sid, 'brand_vetting_sid': brand_vetting_sid or self._properties['brand_vetting_sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BrandVettingContext for this BrandVettingInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingContext
        """
        if self._context is None:
            self._context = BrandVettingContext(self._version, brand_sid=self._solution['brand_sid'], brand_vetting_sid=self._solution['brand_vetting_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the vetting record.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def brand_sid(self):
        """
        :returns: The unique string to identify Brand Registration.
        :rtype: str
        """
        return self._properties['brand_sid']
    
    @property
    def brand_vetting_sid(self):
        """
        :returns: The Twilio SID of the third-party vetting record.
        :rtype: str
        """
        return self._properties['brand_vetting_sid']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def vetting_id(self):
        """
        :returns: The unique identifier of the vetting from the third-party provider.
        :rtype: str
        """
        return self._properties['vetting_id']
    
    @property
    def vetting_class(self):
        """
        :returns: The type of vetting that has been conducted. One of “STANDARD” (Aegis) or “POLITICAL” (Campaign Verify).
        :rtype: str
        """
        return self._properties['vetting_class']
    
    @property
    def vetting_status(self):
        """
        :returns: The status of the import vetting attempt. One of “PENDING,” “SUCCESS,” or “FAILED”.
        :rtype: str
        """
        return self._properties['vetting_status']
    
    @property
    def vetting_provider(self):
        """
        :returns: 
        :rtype: BrandVettingVettingProvider
        """
        return self._properties['vetting_provider']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Brand Vetting resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the BrandVettingInstance

        :returns: The fetched BrandVettingInstance
        :rtype: twilio.rest.messaging.v1.brand_registration.brand_vetting.BrandVettingInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.BrandVettingInstance {}>'.format(context)


