"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Accounts
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



class SecondaryAuthTokenList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SecondaryAuthTokenList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenList
        :rtype: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    

    def get(self):
        """
        Constructs a SecondaryAuthTokenContext
        
        :returns: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenContext
        :rtype: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenContext
        """
        return SecondaryAuthTokenContext(self._version)

    def __call__(self):
        """
        Constructs a SecondaryAuthTokenContext
        
        :returns: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenContext
        :rtype: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenContext
        """
        return SecondaryAuthTokenContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.SecondaryAuthTokenList>'

class SecondaryAuthTokenInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the SecondaryAuthTokenInstance
        :returns: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenInstance
        :rtype: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'secondary_auth_token': payload.get('secondary_auth_token'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SecondaryAuthTokenContext for this SecondaryAuthTokenInstance
        :rtype: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenContext
        """
        if self._context is None:
            self._context = SecondaryAuthTokenContext(self._version,)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the secondary Auth Token was created for.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in UTC when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in UTC when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def secondary_auth_token(self):
        """
        :returns: The generated secondary Auth Token that can be used to authenticate future API requests.
        :rtype: str
        """
        return self._properties['secondary_auth_token']
    
    @property
    def url(self):
        """
        :returns: The URI for this resource, relative to `https://accounts.twilio.com`
        :rtype: str
        """
        return self._properties['url']
    
    def create(self):
        """
        Create the SecondaryAuthTokenInstance
        

        :returns: The created SecondaryAuthTokenInstance
        :rtype: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenInstance
        """
        return self._proxy.create()
    
    def delete(self):
        """
        Deletes the SecondaryAuthTokenInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Accounts.V1.SecondaryAuthTokenInstance {}>'.format(context)

class SecondaryAuthTokenContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the SecondaryAuthTokenContext

        :param Version version: Version that contains the resource
        

        :returns: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenContext
        :rtype: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
        }
        self._uri = '/AuthTokens/Secondary'.format(**self._solution)
        
    
    def create(self):
        """
        Create the SecondaryAuthTokenInstance
        

        :returns: The created SecondaryAuthTokenInstance
        :rtype: twilio.rest.accounts.v1.secondary_auth_token.SecondaryAuthTokenInstance
        """
        data = values.of({ 
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)

        return SecondaryAuthTokenInstance(
            self._version,
            payload
        )
    
    def delete(self):
        """
        Deletes the SecondaryAuthTokenInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Accounts.V1.SecondaryAuthTokenContext {}>'.format(context)


