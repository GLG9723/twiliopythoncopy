"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
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


class WebhookContext(InstanceContext):
    def __init__(self, version: Version, conversation_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'conversation_sid': conversation_sid, 'sid': sid,  }
        self._uri = '/Conversations/${conversation_sid}/Webhooks/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the WebhookInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the WebhookInstance

        :returns: The fetched WebhookInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WebhookInstance(self._version, payload, conversation_sid=self._solution['conversation_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return WebhookInstance(self._version, payload, conversation_sid=self._solution['conversation_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WebhookContext>'



class WebhookInstance(InstanceResource):
    def __init__(self, version, payload, conversation_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'conversation_sid' : payload.get('conversation_sid'),
            'target' : payload.get('target'),
            'url' : payload.get('url'),
            'configuration' : payload.get('configuration'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
        }

        self._context = None
        self._solution = {
            'conversation_sid': conversation_sid or self._properties['conversation_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WebhookContext(
                self._version,
                conversation_sid=self._solution['conversation_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.WebhookInstance {}>'.format(context)



class WebhookListInstance(ListResource):
    def __init__(self, version: Version, conversation_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'conversation_sid': conversation_sid,  }
        self._uri = '/Conversations/${conversation_sid}/Webhooks'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return WebhookInstance(self._version, payload, conversation_sid=self._solution['conversation_sid'])
        
    """
    
    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return WebhookPage(self._version, payload, conversation_sid=self._solution['conversation_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WebhookListInstance>'

