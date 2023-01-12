"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
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




class VariableContext(InstanceContext):
    def __init__(self, version: V1, service_sid: str, environment_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super(VariableContextList, self).__init__(version)

        # Path Solution
        self._solution = { service_sid, environment_sid, sid,  }
        self._uri = '/Services/${service_sid}/Environments/${environment_sid}/Variables/${sid}'
        
        
        def delete(self):
            
            
            """
            Deletes the VariableInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the VariableInstance

            :returns: The fetched VariableInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return VariableInstance(
                self._version,
                payload,
                service_sidenvironment_sidsid=self._solution['service_sid''environment_sid''sid'],
            )
            
            
        
        def update(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return VariableInstance(self._version, payload, service_sid=self._solution['service_sid'], environment_sid=self._solution['environment_sid'], sid=self._solution['sid'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.VariableContext>'



class VariableInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, environment_sid: str, sid: str):
        super(VariableInstance, self).__init__(version)
        self._properties = { 
            'sid' = payload.get('sid'),
            'account_sid' = payload.get('account_sid'),
            'service_sid' = payload.get('service_sid'),
            'environment_sid' = payload.get('environment_sid'),
            'key' = payload.get('key'),
            'value' = payload.get('value'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'url' = payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid']'environment_sid': environment_sid or self._properties['environment_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = VariableContext(
                self._version,
                service_sid=self._solution['service_sid'],environment_sid=self._solution['environment_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.VariableInstance {}>'.format(context)



class VariableListInstance(ListResource):
    def __init__(self, version: V1, service_sid: str, environment_sid: str):
        # TODO: needs autogenerated docs
        super(VariableListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { service_sid, environment_sid,  }
        self._uri = '/Services/${service_sid}/Environments/${environment_sid}/Variables'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return VariableInstance(self._version, payload, service_sid=self._solution['service_sid']environment_sid=self._solution['environment_sid'])
            
        
        def page(self, page_size):
            
            data = values.of({
                'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return VariablePage(self._version, payload, service_sid=self._solution['service_sid']environment_sid=self._solution['environment_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.VariableListInstance>'

