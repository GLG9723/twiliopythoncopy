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
from twilio.rest.conversations.v1.service.user.user_conversation import UserConversationList


class UserList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the UserList

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to read the User resources from.
        
        :returns: twilio.rest.conversations.v1.service.user.UserList
        :rtype: twilio.rest.conversations.v1.service.user.UserList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        self._uri = '/Services/${chat_service_sid}/Users'.format(**self._solution)
        
        
    
    
    
    
    def create(self, identity, x_twilio_webhook_enabled=values.unset, friendly_name=values.unset, attributes=values.unset, role_sid=values.unset):
        """
        Create the UserInstance
        :param str identity: The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
        :param ServiceUserWebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param str role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
        
        :returns: The created UserInstance
        :rtype: twilio.rest.conversations.v1.service.user.UserInstance
        """
        data = values.of({ 
            'Identity': identity,
            'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled,
            'FriendlyName': friendly_name,
            'Attributes': attributes,
            'RoleSid': role_sid,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return UserInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams UserInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.user.UserInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists UserInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.user.UserInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of UserInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
        :rtype: twilio.rest.conversations.v1.service.user.UserPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return UserPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        :rtype: twilio.rest.conversations.v1.service.user.UserPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return UserPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a UserContext
        
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        
        :returns: twilio.rest.conversations.v1.service.user.UserContext
        :rtype: twilio.rest.conversations.v1.service.user.UserContext
        """
        return UserContext(self._version, chat_service_sid=self._solution['chat_service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a UserContext
        
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        
        :returns: twilio.rest.conversations.v1.service.user.UserContext
        :rtype: twilio.rest.conversations.v1.service.user.UserContext
        """
        return UserContext(self._version, chat_service_sid=self._solution['chat_service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.UserList>'










class UserPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UserPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.service.user.UserPage
        :rtype: twilio.rest.conversations.v1.service.user.UserPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.service.user.UserInstance
        :rtype: twilio.rest.conversations.v1.service.user.UserInstance
        """
        return UserInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.UserPage>'





class UserContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid, 'sid': sid,  }
        self._uri = '/Services/${chat_service_sid}/Users/${sid}'
        
        self._user_conversations = None
    
    def delete(self, x_twilio_webhook_enabled):
        
        

        """
        Deletes the UserInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the UserInstance

        :returns: The fetched UserInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UserInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, x_twilio_webhook_enabled, friendly_name, attributes, role_sid):
        data = values.of({
            'x_twilio_webhook_enabled': x_twilio_webhook_enabled,'friendly_name': friendly_name,'attributes': attributes,'role_sid': role_sid,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return UserInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.UserContext>'



class UserInstance(InstanceResource):
    def __init__(self, version, payload, chat_service_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'chat_service_sid' : payload.get('chat_service_sid'),
            'role_sid' : payload.get('role_sid'),
            'identity' : payload.get('identity'),
            'friendly_name' : payload.get('friendly_name'),
            'attributes' : payload.get('attributes'),
            'is_online' : payload.get('is_online'),
            'is_notifiable' : payload.get('is_notifiable'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'chat_service_sid': chat_service_sid or self._properties['chat_service_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = UserContext(
                self._version,
                chat_service_sid=self._solution['chat_service_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def user_conversations(self):
        return self._proxy.user_conversations
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.UserInstance {}>'.format(context)



