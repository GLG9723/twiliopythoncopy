"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
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

from twilio.base.page import Page




class ConnectionPolicyTargetContext(InstanceContext):
    def __init__(self, version: V1, connection_policy_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'connection_policy_sid': connection_policy_sid, 'sid': sid,  }
        self._uri = '/ConnectionPolicies/${connection_policy_sid}/Targets/${sid}'
        
    
    def delete(self):
        
        
        """
        Deletes the ConnectionPolicyTargetInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the ConnectionPolicyTargetInstance

        :returns: The fetched ConnectionPolicyTargetInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return ConnectionPolicyTargetInstance(
            self._version,
            payload,
            connection_policy_sidsid=self._solution['connection_policy_sid''sid'],
        )
        
        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ConnectionPolicyTargetInstance(self._version, payload, connection_policy_sid=self._solution['connection_policy_sid'], sid=self._solution['sid'], )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConnectionPolicyTargetContext>'



class ConnectionPolicyTargetInstance(InstanceResource):
    def __init__(self, version, payload, connection_policy_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'connection_policy_sid' : payload.get('connection_policy_sid'),
            'sid' : payload.get('sid'),
            'friendly_name' : payload.get('friendly_name'),
            'target' : payload.get('target'),
            'priority' : payload.get('priority'),
            'weight' : payload.get('weight'),
            'enabled' : payload.get('enabled'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'connection_policy_sid': connection_policy_sid or self._properties['connection_policy_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ConnectionPolicyTargetContext(
                self._version,
                connection_policy_sid=self._solution['connection_policy_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ConnectionPolicyTargetInstance {}>'.format(context)



class ConnectionPolicyTargetListInstance(ListResource):
    def __init__(self, version: V1, connection_policy_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'connection_policy_sid': connection_policy_sid,  }
        self._uri = '/ConnectionPolicies/${connection_policy_sid}/Targets'
        
    
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return ConnectionPolicyTargetInstance(self._version, payload, connection_policy_sid=self._solution['connection_policy_sid'])
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return ConnectionPolicyTargetPage(self._version, payload, connection_policy_sid=self._solution['connection_policy_sid'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConnectionPolicyTargetListInstance>'

