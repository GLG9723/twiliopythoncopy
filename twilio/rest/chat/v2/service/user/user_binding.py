"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
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


class UserBindingList(ListResource):

    def __init__(self, version: Version, service_sid: str, user_sid: str):
        """
        Initialize the UserBindingList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the User Binding resources from.
        :param user_sid: The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) with the User Binding resources to read.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        
        :returns: twilio.rest.chat.v2.service.user.user_binding.UserBindingList
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'user_sid': user_sid,  }
        self._uri = '/Services/{service_sid}/Users/{user_sid}/Bindings'.format(**self._solution)
        
        
    
    
    
    def stream(self, binding_type=values.unset, limit=None, page_size=None):
        """
        Streams UserBindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param list[UserBindingInstance.BindingType] binding_type: The push technology used by the User Binding resources to read. Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.user.user_binding.UserBindingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            binding_type=binding_type,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, binding_type=values.unset, limit=None, page_size=None):
        """
        Lists UserBindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param list[UserBindingInstance.BindingType] binding_type: The push technology used by the User Binding resources to read. Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.user.user_binding.UserBindingInstance]
        """
        return list(self.stream(
            binding_type=binding_type,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, binding_type=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of UserBindingInstance records from the API.
        Request is executed immediately
        
        :param list[UserBindingInstance.BindingType] binding_type: The push technology used by the User Binding resources to read. Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserBindingInstance
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingPage
        """
        data = values.of({ 
            'BindingType': serialize.map(binding_type, lambda e: e),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return UserBindingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserBindingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserBindingInstance
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return UserBindingPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a UserBindingContext
        
        :param sid: The SID of the User Binding resource to fetch.
        
        :returns: twilio.rest.chat.v2.service.user.user_binding.UserBindingContext
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingContext
        """
        return UserBindingContext(self._version, service_sid=self._solution['service_sid'], user_sid=self._solution['user_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a UserBindingContext
        
        :param sid: The SID of the User Binding resource to fetch.
        
        :returns: twilio.rest.chat.v2.service.user.user_binding.UserBindingContext
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingContext
        """
        return UserBindingContext(self._version, service_sid=self._solution['service_sid'], user_sid=self._solution['user_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.UserBindingList>'






class UserBindingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UserBindingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.chat.v2.service.user.user_binding.UserBindingPage
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserBindingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v2.service.user.user_binding.UserBindingInstance
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingInstance
        """
        return UserBindingInstance(self._version, payload, service_sid=self._solution['service_sid'], user_sid=self._solution['user_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.UserBindingPage>'




class UserBindingContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, user_sid: str, sid: str):
        """
        Initialize the UserBindingContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the User Binding resource from.
        :param user_sid: The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) with the User Binding resource to fetch.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param sid: The SID of the User Binding resource to fetch.

        :returns: twilio.rest.chat.v2.service.user.user_binding.UserBindingContext
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'user_sid': user_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Users/{user_sid}/Bindings/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the UserBindingInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the UserBindingInstance
        

        :returns: The fetched UserBindingInstance
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UserBindingInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            user_sid=self._solution['user_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.UserBindingContext {}>'.format(context)

class UserBindingInstance(InstanceResource):

    class BindingType(object):
        GCM = "gcm"
        APN = "apn"
        FCM = "fcm"

    def __init__(self, version, payload, service_sid: str, user_sid: str, sid: str=None):
        """
        Initialize the UserBindingInstance
        :returns: twilio.rest.chat.v2.service.user.user_binding.UserBindingInstance
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'endpoint': payload.get('endpoint'),
            'identity': payload.get('identity'),
            'user_sid': payload.get('user_sid'),
            'credential_sid': payload.get('credential_sid'),
            'binding_type': payload.get('binding_type'),
            'message_types': payload.get('message_types'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'user_sid': user_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserBindingContext for this UserBindingInstance
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingContext
        """
        if self._context is None:
            self._context = UserBindingContext(self._version, service_sid=self._solution['service_sid'], user_sid=self._solution['user_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the User Binding resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the User Binding resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the User Binding resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def endpoint(self):
        """
        :returns: The unique endpoint identifier for the User Binding. The format of the value depends on the `binding_type`.
        :rtype: str
        """
        return self._properties['endpoint']
    
    @property
    def identity(self):
        """
        :returns: The application-defined string that uniquely identifies the resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more info.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def user_sid(self):
        """
        :returns: The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) with the User Binding resource.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :rtype: str
        """
        return self._properties['user_sid']
    
    @property
    def credential_sid(self):
        """
        :returns: The SID of the [Credential](https://www.twilio.com/docs/chat/rest/credential-resource) for the binding. See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :rtype: str
        """
        return self._properties['credential_sid']
    
    @property
    def binding_type(self):
        """
        :returns: 
        :rtype: UserBindingInstance.BindingType
        """
        return self._properties['binding_type']
    
    @property
    def message_types(self):
        """
        :returns: The [Programmable Chat message types](https://www.twilio.com/docs/chat/push-notification-configuration#push-types) the binding is subscribed to.
        :rtype: list[str]
        """
        return self._properties['message_types']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the User Binding resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the UserBindingInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the UserBindingInstance
        

        :returns: The fetched UserBindingInstance
        :rtype: twilio.rest.chat.v2.service.user.user_binding.UserBindingInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.UserBindingInstance {}>'.format(context)


