"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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



class TokenList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the TokenList
        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
        
        :returns: twilio.api.v2010.token..TokenList
        :rtype: twilio.api.v2010.token..TokenList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/Tokens.json'.format(**self._solution)


    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.TokenList>'



class TokenInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'ice_servers' : payload.get('ice_servers'),
            'password' : payload.get('password'),
            'ttl' : payload.get('ttl'),
            'username' : payload.get('username'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TokenContext(
                self._version,
                account_sid=self._solution['account_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.TokenInstance {}>'.format(context)



