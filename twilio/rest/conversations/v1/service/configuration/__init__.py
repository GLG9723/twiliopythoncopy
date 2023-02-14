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

# from twilio.rest.configuration.notification import NotificationListInstancefrom twilio.rest.configuration.webhook import WebhookListInstance


class ConfigurationContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        self._uri = '/Services/${chat_service_sid}/Configuration'
        
    
    def fetch(self):
        
        """
        Fetch the ConfigurationInstance

        :returns: The fetched ConfigurationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ConfigurationInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ConfigurationInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConfigurationContext>'



class ConfigurationInstance(InstanceResource):
    def __init__(self, version, payload, chat_service_sid: str):
        super().__init__(version)
        self._properties = { 
            'chat_service_sid' : payload.get('chat_service_sid'),
            'default_conversation_creator_role_sid' : payload.get('default_conversation_creator_role_sid'),
            'default_conversation_role_sid' : payload.get('default_conversation_role_sid'),
            'default_chat_service_role_sid' : payload.get('default_chat_service_role_sid'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
            'reachability_enabled' : payload.get('reachability_enabled'),
        }

        self._context = None
        self._solution = {
            'chat_service_sid': chat_service_sid or self._properties['chat_service_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ConfigurationContext(
                self._version,
                chat_service_sid=self._solution['chat_service_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ConfigurationInstance {}>'.format(context)



class ConfigurationListInstance(ListResource):
    def __init__(self, version: Version, chat_service_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        self._uri = ''
        
        self._notifications = None
        self._webhooks = None
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ConfigurationListInstance>'

