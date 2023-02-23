"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Oauth
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



class OpenidDiscoveryList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the OpenidDiscoveryList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryList
        :rtype: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    

    def get(self):
        """
        Constructs a OpenidDiscoveryContext
        
        :returns: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryContext
        :rtype: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryContext
        """
        return OpenidDiscoveryContext(self._version)

    def __call__(self):
        """
        Constructs a OpenidDiscoveryContext
        
        :returns: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryContext
        :rtype: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryContext
        """
        return OpenidDiscoveryContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Oauth.V1.OpenidDiscoveryList>'

class OpenidDiscoveryContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the OpenidDiscoveryContext

        :param Version version: Version that contains the resource
        

        :returns: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryContext
        :rtype: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
        }
        self._uri = '/.well-known/openid-configuration'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the OpenidDiscoveryInstance

        :returns: The fetched OpenidDiscoveryInstance
        :rtype: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri)

        return OpenidDiscoveryInstance(
            self._version,
            payload,
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Oauth.V1.OpenidDiscoveryContext {}>'.format(context)

class OpenidDiscoveryInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the OpenidDiscoveryInstance
        :returns: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryInstance
        :rtype: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryInstance
        """
        super().__init__(version)

        self._properties = { 
            'issuer': payload.get('issuer'),
            'authorization_endpoint': payload.get('authorization_endpoint'),
            'device_authorization_endpoint': payload.get('device_authorization_endpoint'),
            'token_endpoint': payload.get('token_endpoint'),
            'userinfo_endpoint': payload.get('userinfo_endpoint'),
            'revocation_endpoint': payload.get('revocation_endpoint'),
            'jwk_uri': payload.get('jwk_uri'),
            'response_type_supported': payload.get('response_type_supported'),
            'subject_type_supported': payload.get('subject_type_supported'),
            'id_token_signing_alg_values_supported': payload.get('id_token_signing_alg_values_supported'),
            'scopes_supported': payload.get('scopes_supported'),
            'claims_supported': payload.get('claims_supported'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: OpenidDiscoveryContext for this OpenidDiscoveryInstance
        :rtype: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryContext
        """
        if self._context is None:
            self._context = OpenidDiscoveryContext(self._version,)
        return self._context
    
    @property
    def issuer(self):
        """
        :returns: The URL of the party that will create the token and sign it with its private key.
        :rtype: str
        """
        return self._properties['issuer']
    
    @property
    def authorization_endpoint(self):
        """
        :returns: The endpoint that validates all authorization requests.
        :rtype: str
        """
        return self._properties['authorization_endpoint']
    
    @property
    def device_authorization_endpoint(self):
        """
        :returns: The endpoint that validates all device code related authorization requests.
        :rtype: str
        """
        return self._properties['device_authorization_endpoint']
    
    @property
    def token_endpoint(self):
        """
        :returns: The URL of the token endpoint. After a client has received an authorization code, that code is presented to the token endpoint and exchanged for an identity token, an access token, and a refresh token.
        :rtype: str
        """
        return self._properties['token_endpoint']
    
    @property
    def userinfo_endpoint(self):
        """
        :returns: The URL of the user info endpoint, which returns user profile information to a client. Keep in mind that the user info endpoint returns only the information that has been requested.
        :rtype: str
        """
        return self._properties['userinfo_endpoint']
    
    @property
    def revocation_endpoint(self):
        """
        :returns: The endpoint used to revoke access or refresh tokens issued by the authorization server.
        :rtype: str
        """
        return self._properties['revocation_endpoint']
    
    @property
    def jwk_uri(self):
        """
        :returns: The URL of your JSON Web Key Set. This set is a collection of JSON Web Keys, a standard method for representing cryptographic keys in a JSON structure.
        :rtype: str
        """
        return self._properties['jwk_uri']
    
    @property
    def response_type_supported(self):
        """
        :returns: A collection of response type supported by authorization server.
        :rtype: list[str]
        """
        return self._properties['response_type_supported']
    
    @property
    def subject_type_supported(self):
        """
        :returns: A collection of subject by authorization server.
        :rtype: list[str]
        """
        return self._properties['subject_type_supported']
    
    @property
    def id_token_signing_alg_values_supported(self):
        """
        :returns: A collection of JWS signing algorithms supported by authorization server to sign identity token.
        :rtype: list[str]
        """
        return self._properties['id_token_signing_alg_values_supported']
    
    @property
    def scopes_supported(self):
        """
        :returns: A collection of scopes supported by authorization server for identity token
        :rtype: list[str]
        """
        return self._properties['scopes_supported']
    
    @property
    def claims_supported(self):
        """
        :returns: A collection of claims supported by authorization server for identity token
        :rtype: list[str]
        """
        return self._properties['claims_supported']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the OpenidDiscoveryInstance

        :returns: The fetched OpenidDiscoveryInstance
        :rtype: twilio.rest.oauth.v1.openid_discovery.OpenidDiscoveryInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Oauth.V1.OpenidDiscoveryInstance {}>'.format(context)


