r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Routes
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



class SipDomainList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SipDomainList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.routes.v2.sip_domain.SipDomainList
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    

    def get(self, sip_domain):
        """
        Constructs a SipDomainContext
        
        :param sip_domain: 
        
        :returns: twilio.rest.routes.v2.sip_domain.SipDomainContext
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainContext
        """
        return SipDomainContext(self._version, sip_domain=sip_domain)

    def __call__(self, sip_domain):
        """
        Constructs a SipDomainContext
        
        :param sip_domain: 
        
        :returns: twilio.rest.routes.v2.sip_domain.SipDomainContext
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainContext
        """
        return SipDomainContext(self._version, sip_domain=sip_domain)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Routes.V2.SipDomainList>'

class SipDomainInstance(InstanceResource):

    def __init__(self, version, payload, sip_domain: str=None):
        """
        Initialize the SipDomainInstance
        :returns: twilio.rest.routes.v2.sip_domain.SipDomainInstance
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainInstance
        """
        super().__init__(version)

        self._properties = { 
            'sip_domain': payload.get('sip_domain'),
            'url': payload.get('url'),
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'voice_region': payload.get('voice_region'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
        }

        self._context = None
        self._solution = { 'sip_domain': sip_domain or self._properties['sip_domain'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SipDomainContext for this SipDomainInstance
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainContext
        """
        if self._context is None:
            self._context = SipDomainContext(self._version, sip_domain=self._solution['sip_domain'],)
        return self._context
    
    @property
    def sip_domain(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sip_domain']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def voice_region(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['voice_region']
    
    @property
    def date_created(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    
    def fetch(self):
        """
        Fetch the SipDomainInstance
        

        :returns: The fetched SipDomainInstance
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SipDomainInstance
        

        :returns: The fetched SipDomainInstance
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, voice_region=values.unset, friendly_name=values.unset):
        """
        Update the SipDomainInstance
        
        :params str voice_region: 
        :params str friendly_name: 

        :returns: The updated SipDomainInstance
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainInstance
        """
        return self._proxy.update(voice_region=voice_region, friendly_name=friendly_name, )

    async def update_async(self, voice_region=values.unset, friendly_name=values.unset):
        """
        Asynchronous coroutine to update the SipDomainInstance
        
        :params str voice_region: 
        :params str friendly_name: 

        :returns: The updated SipDomainInstance
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainInstance
        """
        return await self._proxy.update_async(voice_region=voice_region, friendly_name=friendly_name, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Routes.V2.SipDomainInstance {}>'.format(context)

class SipDomainContext(InstanceContext):

    def __init__(self, version: Version, sip_domain: str):
        """
        Initialize the SipDomainContext

        :param Version version: Version that contains the resource
        :param sip_domain: 

        :returns: twilio.rest.routes.v2.sip_domain.SipDomainContext
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sip_domain': sip_domain,
        }
        self._uri = '/SipDomains/{sip_domain}'.format(**self._solution)
        
    
    
    def fetch(self):
        """
        Fetch the SipDomainInstance
        

        :returns: The fetched SipDomainInstance
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SipDomainInstance(
            self._version,
            payload,
            sip_domain=self._solution['sip_domain'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SipDomainInstance
        

        :returns: The fetched SipDomainInstance
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return SipDomainInstance(
            self._version,
            payload,
            sip_domain=self._solution['sip_domain'],
            
        )
    
    
    def update(self, voice_region=values.unset, friendly_name=values.unset):
        """
        Update the SipDomainInstance
        
        :params str voice_region: 
        :params str friendly_name: 

        :returns: The updated SipDomainInstance
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainInstance
        """
        data = values.of({ 
            'VoiceRegion': voice_region,
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SipDomainInstance(
            self._version,
            payload,
            sip_domain=self._solution['sip_domain']
        )

    async def update_async(self, voice_region=values.unset, friendly_name=values.unset):
        """
        Asynchronous coroutine to update the SipDomainInstance
        
        :params str voice_region: 
        :params str friendly_name: 

        :returns: The updated SipDomainInstance
        :rtype: twilio.rest.routes.v2.sip_domain.SipDomainInstance
        """
        data = values.of({ 
            'VoiceRegion': voice_region,
            'FriendlyName': friendly_name,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return SipDomainInstance(
            self._version,
            payload,
            sip_domain=self._solution['sip_domain']
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Routes.V2.SipDomainContext {}>'.format(context)


