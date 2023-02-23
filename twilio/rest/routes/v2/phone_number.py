"""
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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class PhoneNumberList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberList
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    

    def get(self, phone_number):
        """
        Constructs a PhoneNumberContext
        
        :param phone_number: The phone number in E.164 format
        
        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __call__(self, phone_number):
        """
        Constructs a PhoneNumberContext
        
        :param phone_number: The phone number in E.164 format
        
        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Routes.V2.PhoneNumberList>'

class PhoneNumberContext(InstanceContext):

    def __init__(self, version: Version, phone_number: str):
        """
        Initialize the PhoneNumberContext

        :param Version version: Version that contains the resource
        :param phone_number: The phone number in E.164 format

        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'phone_number': phone_number,
        }
        self._uri = '/PhoneNumbers/${phone_number}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the PhoneNumberInstance

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri)

        return PhoneNumberInstance(
            self._version,
            payload,
            phone_number=self._solution['phone_number'],
            
        )
        
    def update(self, voice_region=values.unset, friendly_name=values.unset):
        """
        Update the PhoneNumberInstance
        
        :params str voice_region: The Inbound Processing Region used for this phone number for voice
        :params str friendly_name: A human readable description of this resource, up to 64 characters.

        :returns: The updated PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        data = values.of({ 
            'VoiceRegion': voice_region,
            'FriendlyName': friendly_name,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data)

        return PhoneNumberInstance(
            self._version,
            payload,
            phone_number=self._solution['phone_number']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Routes.V2.PhoneNumberContext {}>'.format(context)

class PhoneNumberInstance(InstanceResource):

    def __init__(self, version, payload, phone_number: str=None):
        """
        Initialize the PhoneNumberInstance
        :returns: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        super().__init__(version)

        self._properties = { 
            'phone_number': payload.get('phone_number'),
            'url': payload.get('url'),
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'voice_region': payload.get('voice_region'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
        }

        self._context = None
        self._solution = { 'phone_number': phone_number or self._properties['phone_number'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(self._version, phone_number=self._solution['phone_number'],)
        return self._context
    
    @property
    def phone_number(self):
        """
        :returns: The phone number in E.164 format
        :rtype: str
        """
        return self._properties['phone_number']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies the Inbound Processing Region assignments for this phone number.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: A human readable description of the Inbound Processing Region assignments for this phone number, up to 64 characters.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def voice_region(self):
        """
        :returns: The Inbound Processing Region used for this phone number for voice.
        :rtype: str
        """
        return self._properties['voice_region']
    
    @property
    def date_created(self):
        """
        :returns: The date that this phone number was assigned an Inbound Processing Region, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that the Inbound Processing Region was updated for this phone number, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    def fetch(self):
        """
        Fetch the PhoneNumberInstance

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        return self._proxy.fetch()
    
    def update(self, voice_region=values.unset, friendly_name=values.unset):
        """
        Update the PhoneNumberInstance
        
        :params str voice_region: The Inbound Processing Region used for this phone number for voice
        :params str friendly_name: A human readable description of this resource, up to 64 characters.

        :returns: The updated PhoneNumberInstance
        :rtype: twilio.rest.routes.v2.phone_number.PhoneNumberInstance
        """
        return self._proxy.update(voice_region=voice_region, friendly_name=friendly_name, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Routes.V2.PhoneNumberInstance {}>'.format(context)


