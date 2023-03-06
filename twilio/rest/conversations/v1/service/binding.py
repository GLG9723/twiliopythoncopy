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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class BindingList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the BindingList

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Binding resource is associated with.
        
        :returns: twilio.rest.conversations.v1.service.binding.BindingList
        :rtype: twilio.rest.conversations.v1.service.binding.BindingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        self._uri = '/Services/{chat_service_sid}/Bindings'.format(**self._solution)
        
        
    
    
    
    def stream(self, binding_type=values.unset, identity=values.unset, limit=None, page_size=None):
        """
        Streams BindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param list[BindingType] binding_type: The push technology used by the Binding resources to read.  Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param list[str] identity: The identity of a [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) this binding belongs to. See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more details.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.binding.BindingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            binding_type=binding_type,
            identity=identity,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, binding_type=values.unset, identity=values.unset, limit=None, page_size=None):
        """
        Lists BindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param list[BindingType] binding_type: The push technology used by the Binding resources to read.  Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param list[str] identity: The identity of a [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) this binding belongs to. See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more details.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.binding.BindingInstance]
        """
        return list(self.stream(
            binding_type=binding_type,
            identity=identity,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, binding_type=values.unset, identity=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of BindingInstance records from the API.
        Request is executed immediately
        
        :param list[BindingType] binding_type: The push technology used by the Binding resources to read.  Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param list[str] identity: The identity of a [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) this binding belongs to. See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more details.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BindingInstance
        :rtype: twilio.rest.conversations.v1.service.binding.BindingPage
        """
        data = values.of({ 
            'BindingType': serialize.map(binding_type),
            'Identity': serialize.map(identity),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return BindingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BindingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BindingInstance
        :rtype: twilio.rest.conversations.v1.service.binding.BindingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return BindingPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a BindingContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.service.binding.BindingContext
        :rtype: twilio.rest.conversations.v1.service.binding.BindingContext
        """
        return BindingContext(self._version, chat_service_sid=self._solution['chat_service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a BindingContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.service.binding.BindingContext
        :rtype: twilio.rest.conversations.v1.service.binding.BindingContext
        """
        return BindingContext(self._version, chat_service_sid=self._solution['chat_service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.BindingList>'






class BindingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the BindingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.service.binding.BindingPage
        :rtype: twilio.rest.conversations.v1.service.binding.BindingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BindingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.service.binding.BindingInstance
        :rtype: twilio.rest.conversations.v1.service.binding.BindingInstance
        """
        return BindingInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.BindingPage>'




class BindingInstance(InstanceResource):

    class BindingType(object):
        APN = "apn"
        GCM = "gcm"
        FCM = "fcm"

    def __init__(self, version, payload, chat_service_sid: str, sid: str=None):
        """
        Initialize the BindingInstance
        :returns: twilio.rest.conversations.v1.service.binding.BindingInstance
        :rtype: twilio.rest.conversations.v1.service.binding.BindingInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'chat_service_sid': payload.get('chat_service_sid'),
            'credential_sid': payload.get('credential_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'endpoint': payload.get('endpoint'),
            'identity': payload.get('identity'),
            'binding_type': payload.get('binding_type'),
            'message_types': payload.get('message_types'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'chat_service_sid': chat_service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BindingContext for this BindingInstance
        :rtype: twilio.rest.conversations.v1.service.binding.BindingContext
        """
        if self._context is None:
            self._context = BindingContext(self._version, chat_service_sid=self._solution['chat_service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this binding.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def chat_service_sid(self):
        """
        :returns: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Binding resource is associated with.
        :rtype: str
        """
        return self._properties['chat_service_sid']
    
    @property
    def credential_sid(self):
        """
        :returns: The SID of the [Credential](https://www.twilio.com/docs/conversations/api/credential-resource) for the binding. See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :rtype: str
        """
        return self._properties['credential_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date that this resource was created.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def endpoint(self):
        """
        :returns: The unique endpoint identifier for the Binding. The format of this value depends on the `binding_type`.
        :rtype: str
        """
        return self._properties['endpoint']
    
    @property
    def identity(self):
        """
        :returns: The application-defined string that uniquely identifies the [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more info.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def binding_type(self):
        """
        :returns: 
        :rtype: BindingType
        """
        return self._properties['binding_type']
    
    @property
    def message_types(self):
        """
        :returns: The [Conversation message types](https://www.twilio.com/docs/chat/push-notification-configuration#push-types) the binding is subscribed to.
        :rtype: list[str]
        """
        return self._properties['message_types']
    
    @property
    def url(self):
        """
        :returns: An absolute API resource URL for this binding.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the BindingInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the BindingInstance
        

        :returns: The fetched BindingInstance
        :rtype: twilio.rest.conversations.v1.service.binding.BindingInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.BindingInstance {}>'.format(context)

class BindingContext(InstanceContext):

    def __init__(self, version: Version, chat_service_sid: str, sid: str):
        """
        Initialize the BindingContext

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Binding resource is associated with.:param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.service.binding.BindingContext
        :rtype: twilio.rest.conversations.v1.service.binding.BindingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'chat_service_sid': chat_service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{chat_service_sid}/Bindings/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the BindingInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the BindingInstance
        

        :returns: The fetched BindingInstance
        :rtype: twilio.rest.conversations.v1.service.binding.BindingInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BindingInstance(
            self._version,
            payload,
            chat_service_sid=self._solution['chat_service_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.BindingContext {}>'.format(context)


