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





class NewKeyInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'friendly_name' : payload.get('friendly_name'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'secret' : payload.get('secret'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = NewKeyContext(
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
        return '<Twilio.Api.V2010.NewKeyInstance {}>'.format(context)



class NewKeyListInstance(ListResource):
    def __init__(self, version: V2010, account_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/Keys.json'
        
    
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return NewKeyInstance(self._version, payload, account_sid=self._solution['account_sid'])
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NewKeyListInstance>'

