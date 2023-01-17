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

from twilio.base.page import Page

# 


class MessagingConfigurationContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, country: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'country': country,  }
        self._uri = '/Services/${service_sid}/MessagingConfigurations/${country}'
        
    
    def delete(self):
        
        

        """
        Deletes the MessagingConfigurationInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the MessagingConfigurationInstance

        :returns: The fetched MessagingConfigurationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MessagingConfigurationInstance(self._version, payload, service_sid=self._solution['service_sid'], country=self._solution['country'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return MessagingConfigurationInstance(self._version, payload, service_sid=self._solution['service_sid'], country=self._solution['country'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.MessagingConfigurationContext>'



class MessagingConfigurationInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, country: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'country' : payload.get('country'),
            'messaging_service_sid' : payload.get('messaging_service_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'country': country or self._properties['country'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = MessagingConfigurationContext(
                self._version,
                service_sid=self._solution['service_sid'],country=self._solution['country'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.MessagingConfigurationInstance {}>'.format(context)



class MessagingConfigurationListInstance(ListResource):
    def __init__(self, version: Version, service_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/${service_sid}/MessagingConfigurations'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return MessagingConfigurationInstance(self._version, payload, service_sid=self._solution['service_sid'])
        
    """
    
    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return MessagingConfigurationPage(self._version, payload, service_sid=self._solution['service_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.MessagingConfigurationListInstance>'

