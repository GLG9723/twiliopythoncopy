"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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



class AccessTokenList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the AccessTokenList

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        
        :returns: twilio.rest.verify.v2.service.access_token.AccessTokenList
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/AccessTokens'.format(**self._solution)
        
        
    
    
    def create(self, identity, factor_type, factor_friendly_name=values.unset, ttl=values.unset):
        """
        Create the AccessTokenInstance

        :param str identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, and generated by your external system, such as your user's UUID, GUID, or SID.
        :param AccessTokenInstance.FactorTypes factor_type: 
        :param str factor_friendly_name: The friendly name of the factor that is going to be created with this access token
        :param int ttl: How long, in seconds, the access token is valid. Can be an integer between 60 and 300. Default is 60.
        
        :returns: The created AccessTokenInstance
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenInstance
        """
        data = values.of({ 
            'Identity': identity,
            'FactorType': factor_type,
            'FactorFriendlyName': factor_friendly_name,
            'Ttl': ttl,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return AccessTokenInstance(self._version, payload, service_sid=self._solution['service_sid'])
    

    def get(self, sid):
        """
        Constructs a AccessTokenContext
        
        :param sid: A 34 character string that uniquely identifies this Access Token.
        
        :returns: twilio.rest.verify.v2.service.access_token.AccessTokenContext
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenContext
        """
        return AccessTokenContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a AccessTokenContext
        
        :param sid: A 34 character string that uniquely identifies this Access Token.
        
        :returns: twilio.rest.verify.v2.service.access_token.AccessTokenContext
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenContext
        """
        return AccessTokenContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.AccessTokenList>'

class AccessTokenContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the AccessTokenContext

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.:param sid: A 34 character string that uniquely identifies this Access Token.

        :returns: twilio.rest.verify.v2.service.access_token.AccessTokenContext
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/AccessTokens/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the AccessTokenInstance
        

        :returns: The fetched AccessTokenInstance
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AccessTokenInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.AccessTokenContext {}>'.format(context)

class AccessTokenInstance(InstanceResource):

    class FactorTypes(object):
        PUSH = "push"

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the AccessTokenInstance
        :returns: twilio.rest.verify.v2.service.access_token.AccessTokenInstance
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'entity_identity': payload.get('entity_identity'),
            'factor_type': payload.get('factor_type'),
            'factor_friendly_name': payload.get('factor_friendly_name'),
            'token': payload.get('token'),
            'url': payload.get('url'),
            'ttl': deserialize.integer(payload.get('ttl')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AccessTokenContext for this AccessTokenInstance
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenContext
        """
        if self._context is None:
            self._context = AccessTokenContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this Access Token.
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
    def service_sid(self):
        """
        :returns: The unique SID identifier of the Verify Service.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def entity_identity(self):
        """
        :returns: The unique external identifier for the Entity of the Service.
        :rtype: str
        """
        return self._properties['entity_identity']
    
    @property
    def factor_type(self):
        """
        :returns: 
        :rtype: AccessTokenInstance.FactorTypes
        """
        return self._properties['factor_type']
    
    @property
    def factor_friendly_name(self):
        """
        :returns: A human readable description of this factor, up to 64 characters. For a push factor, this can be the device's name.
        :rtype: str
        """
        return self._properties['factor_friendly_name']
    
    @property
    def token(self):
        """
        :returns: The access token generated for enrollment, this is an encrypted json web token.
        :rtype: str
        """
        return self._properties['token']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def ttl(self):
        """
        :returns: How long, in seconds, the access token is valid. Max: 5 minutes
        :rtype: int
        """
        return self._properties['ttl']
    
    @property
    def date_created(self):
        """
        :returns: The date that this access token was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    def fetch(self):
        """
        Fetch the AccessTokenInstance
        

        :returns: The fetched AccessTokenInstance
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.AccessTokenInstance {}>'.format(context)


