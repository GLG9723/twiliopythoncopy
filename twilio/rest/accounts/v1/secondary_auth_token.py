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
        
        :returns: twilio.accounts.v1.secondary_auth_token..SecondaryAuthTokenList
        :rtype: twilio.accounts.v1.secondary_auth_token..SecondaryAuthTokenList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = ''.format(**self._solution)


    
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.SecondaryAuthTokenList>'


class SecondaryAuthTokenContext(InstanceContext):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/AuthTokens/Secondary'
        
    
    def create(self):
        
        

        
    
    def delete(self):
        
        

        """
        Deletes the SecondaryAuthTokenInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.SecondaryAuthTokenContext>'



class SecondaryAuthTokenInstance(InstanceResource):
    def __init__(self, version, payload):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'secondary_auth_token' : payload.get('secondary_auth_token'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SecondaryAuthTokenContext(
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
        return '<Twilio.Accounts.V1.SecondaryAuthTokenInstance {}>'.format(context)



