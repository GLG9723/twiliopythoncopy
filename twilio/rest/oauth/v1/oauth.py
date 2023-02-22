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



class OauthList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the OauthList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.oauth.v1.oauth.OauthList
        :rtype: twilio.rest.oauth.v1.oauth.OauthList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    

    def get(self):
        """
        Constructs a OauthContext
        
        :returns: twilio.rest.oauth.v1.oauth.OauthContext
        :rtype: twilio.rest.oauth.v1.oauth.OauthContext
        """
        return OauthContext(self._version)

    def __call__(self):
        """
        Constructs a OauthContext
        
        :returns: twilio.rest.oauth.v1.oauth.OauthContext
        :rtype: twilio.rest.oauth.v1.oauth.OauthContext
        """
        return OauthContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Oauth.V1.OauthList>'


class OauthContext(InstanceContext):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/certs'
        
    
    def fetch(self):
        
        """
        Fetch the OauthInstance

        :returns: The fetched OauthInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return OauthInstance(self._version, payload, )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Oauth.V1.OauthContext>'



class OauthInstance(InstanceResource):
    def __init__(self, version, payload):
        super().__init__(version)
        self._properties = { 
            'keys' : payload.get('keys'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = OauthContext(
                self._version,
                
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Oauth.V1.OauthInstance {}>'.format(context)



