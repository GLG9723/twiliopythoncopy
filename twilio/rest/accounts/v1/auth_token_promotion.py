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



class AuthTokenPromotionList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the AuthTokenPromotionList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionList
        :rtype: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    

    def get(self):
        """
        Constructs a AuthTokenPromotionContext
        
        :returns: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionContext
        :rtype: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionContext
        """
        return AuthTokenPromotionContext(self._version)

    def __call__(self):
        """
        Constructs a AuthTokenPromotionContext
        
        :returns: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionContext
        :rtype: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionContext
        """
        return AuthTokenPromotionContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.AuthTokenPromotionList>'

class AuthTokenPromotionContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the AuthTokenPromotionContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionContext
        :rtype: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
        }
        self._uri = '/AuthTokens/Promote'.format(**self._solution)
        
    
    def update(self):
        """
        Update the AuthTokenPromotionInstance
        

        :returns: The updated AuthTokenPromotionInstance
        :rtype: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionInstance
        """
        data = values.of({ 
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return AuthTokenPromotionInstance(
            self._version,
            payload
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Accounts.V1.AuthTokenPromotionContext {}>'.format(context)

class AuthTokenPromotionInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the AuthTokenPromotionInstance
        :returns: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionInstance
        :rtype: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'auth_token': payload.get('auth_token'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AuthTokenPromotionContext for this AuthTokenPromotionInstance
        :rtype: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionContext
        """
        if self._context is None:
            self._context = AuthTokenPromotionContext(self._version,)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the secondary Auth Token was created for.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def auth_token(self):
        """
        :returns: The promoted Auth Token that must be used to authenticate future API requests.
        :rtype: str
        """
        return self._properties['auth_token']
    
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
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The URI for this resource, relative to `https://accounts.twilio.com`
        :rtype: str
        """
        return self._properties['url']
    
    def update(self):
        """
        Update the AuthTokenPromotionInstance
        

        :returns: The updated AuthTokenPromotionInstance
        :rtype: twilio.rest.accounts.v1.auth_token_promotion.AuthTokenPromotionInstance
        """
        return self._proxy.update()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Accounts.V1.AuthTokenPromotionInstance {}>'.format(context)


