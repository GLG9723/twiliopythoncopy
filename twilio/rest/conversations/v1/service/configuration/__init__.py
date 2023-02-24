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

from twilio.rest.conversations.v1.service.configuration.notification import NotificationList
from twilio.rest.conversations.v1.service.configuration.webhook import WebhookList


class ConfigurationList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the ConfigurationList

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the Service configuration resource to fetch.
        
        :returns: twilio.rest.conversations.v1.service.configuration.ConfigurationList
        :rtype: twilio.rest.conversations.v1.service.configuration.ConfigurationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        
        
        self._notifications = None
        self._webhooks = None
        
    
    

    @property
    def notifications(self):
        """
        Access the notifications

        :returns: twilio.rest.conversations.v1.service.configuration.NotificationList
        :rtype: twilio.rest.conversations.v1.service.configuration.NotificationList
        """
        if self._notifications is None:
            self._notifications = NotificationList(self._version, chat_service_sid=self._solution['chat_service_sid'])
        return self._notifications

    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.conversations.v1.service.configuration.WebhookList
        :rtype: twilio.rest.conversations.v1.service.configuration.WebhookList
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(self._version, chat_service_sid=self._solution['chat_service_sid'])
        return self._webhooks

    def get(self):
        """
        Constructs a ConfigurationContext
        
        :returns: twilio.rest.conversations.v1.service.configuration.ConfigurationContext
        :rtype: twilio.rest.conversations.v1.service.configuration.ConfigurationContext
        """
        return ConfigurationContext(self._version, chat_service_sid=self._solution['chat_service_sid'])

    def __call__(self):
        """
        Constructs a ConfigurationContext
        
        :returns: twilio.rest.conversations.v1.service.configuration.ConfigurationContext
        :rtype: twilio.rest.conversations.v1.service.configuration.ConfigurationContext
        """
        return ConfigurationContext(self._version, chat_service_sid=self._solution['chat_service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ConfigurationList>'

class ConfigurationContext(InstanceContext):

    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the ConfigurationContext

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the Service configuration resource to update.

        :returns: twilio.rest.conversations.v1.service.configuration.ConfigurationContext
        :rtype: twilio.rest.conversations.v1.service.configuration.ConfigurationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'chat_service_sid': chat_service_sid,
        }
        self._uri = '/Services/{chat_service_sid}/Configuration'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the ConfigurationInstance
        

        :returns: The fetched ConfigurationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.ConfigurationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ConfigurationInstance(
            self._version,
            payload,
            chat_service_sid=self._solution['chat_service_sid'],
            
        )
        
    def update(self, default_conversation_creator_role_sid=values.unset, default_conversation_role_sid=values.unset, default_chat_service_role_sid=values.unset, reachability_enabled=values.unset):
        """
        Update the ConfigurationInstance
        
        :params str default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when they join a new conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :params str default_conversation_role_sid: The conversation-level role assigned to users when they are added to a conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :params str default_chat_service_role_sid: The service-level role assigned to users when they are added to the service. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :params bool reachability_enabled: Whether the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) is enabled for this Conversations Service. The default is `false`.

        :returns: The updated ConfigurationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.ConfigurationInstance
        """
        data = values.of({ 
            'DefaultConversationCreatorRoleSid': default_conversation_creator_role_sid,
            'DefaultConversationRoleSid': default_conversation_role_sid,
            'DefaultChatServiceRoleSid': default_chat_service_role_sid,
            'ReachabilityEnabled': reachability_enabled,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ConfigurationInstance(
            self._version,
            payload,
            chat_service_sid=self._solution['chat_service_sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.ConfigurationContext {}>'.format(context)

class ConfigurationInstance(InstanceResource):

    def __init__(self, version, payload, chat_service_sid: str):
        """
        Initialize the ConfigurationInstance
        :returns: twilio.rest.conversations.v1.service.configuration.ConfigurationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.ConfigurationInstance
        """
        super().__init__(version)

        self._properties = { 
            'chat_service_sid': payload.get('chat_service_sid'),
            'default_conversation_creator_role_sid': payload.get('default_conversation_creator_role_sid'),
            'default_conversation_role_sid': payload.get('default_conversation_role_sid'),
            'default_chat_service_role_sid': payload.get('default_chat_service_role_sid'),
            'url': payload.get('url'),
            'links': payload.get('links'),
            'reachability_enabled': payload.get('reachability_enabled'),
        }

        self._context = None
        self._solution = { 'chat_service_sid': chat_service_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ConfigurationContext for this ConfigurationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.ConfigurationContext
        """
        if self._context is None:
            self._context = ConfigurationContext(self._version, chat_service_sid=self._solution['chat_service_sid'],)
        return self._context
    
    @property
    def chat_service_sid(self):
        """
        :returns: The unique string that we created to identify the Service configuration resource.
        :rtype: str
        """
        return self._properties['chat_service_sid']
    
    @property
    def default_conversation_creator_role_sid(self):
        """
        :returns: The conversation-level role assigned to a conversation creator user when they join a new conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :rtype: str
        """
        return self._properties['default_conversation_creator_role_sid']
    
    @property
    def default_conversation_role_sid(self):
        """
        :returns: The conversation-level role assigned to users when they are added to a conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :rtype: str
        """
        return self._properties['default_conversation_role_sid']
    
    @property
    def default_chat_service_role_sid(self):
        """
        :returns: The service-level role assigned to users when they are added to the service. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :rtype: str
        """
        return self._properties['default_chat_service_role_sid']
    
    @property
    def url(self):
        """
        :returns: An absolute API resource URL for this service configuration.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: Contains an absolute API resource URL to access the push notifications configuration of this service.
        :rtype: dict
        """
        return self._properties['links']
    
    @property
    def reachability_enabled(self):
        """
        :returns: Whether the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) is enabled for this Conversations Service. The default is `false`.
        :rtype: bool
        """
        return self._properties['reachability_enabled']
    
    def fetch(self):
        """
        Fetch the ConfigurationInstance
        

        :returns: The fetched ConfigurationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.ConfigurationInstance
        """
        return self._proxy.fetch()
    
    def update(self, default_conversation_creator_role_sid=values.unset, default_conversation_role_sid=values.unset, default_chat_service_role_sid=values.unset, reachability_enabled=values.unset):
        """
        Update the ConfigurationInstance
        
        :params str default_conversation_creator_role_sid: The conversation-level role assigned to a conversation creator when they join a new conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :params str default_conversation_role_sid: The conversation-level role assigned to users when they are added to a conversation. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :params str default_chat_service_role_sid: The service-level role assigned to users when they are added to the service. See the [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
        :params bool reachability_enabled: Whether the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) is enabled for this Conversations Service. The default is `false`.

        :returns: The updated ConfigurationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.ConfigurationInstance
        """
        return self._proxy.update(default_conversation_creator_role_sid=default_conversation_creator_role_sid, default_conversation_role_sid=default_conversation_role_sid, default_chat_service_role_sid=default_chat_service_role_sid, reachability_enabled=reachability_enabled, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.ConfigurationInstance {}>'.format(context)


