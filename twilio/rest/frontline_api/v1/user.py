"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Frontline
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



class UserList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the UserList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.frontline_api.v1.user.UserList
        :rtype: twilio.rest.frontline_api.v1.user.UserList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    

    def get(self, sid):
        """
        Constructs a UserContext
        
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        
        :returns: twilio.rest.frontline_api.v1.user.UserContext
        :rtype: twilio.rest.frontline_api.v1.user.UserContext
        """
        return UserContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a UserContext
        
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        
        :returns: twilio.rest.frontline_api.v1.user.UserContext
        :rtype: twilio.rest.frontline_api.v1.user.UserContext
        """
        return UserContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FrontlineApi.V1.UserList>'

class UserContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the UserContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.

        :returns: twilio.rest.frontline_api.v1.user.UserContext
        :rtype: twilio.rest.frontline_api.v1.user.UserContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Users/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the UserInstance
        

        :returns: The fetched UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UserInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, avatar=values.unset, state=values.unset, is_available=values.unset):
        """
        Update the UserInstance
        
        :params str friendly_name: The string that you assigned to describe the User.
        :params str avatar: The avatar URL which will be shown in Frontline application.
        :params StateType state: 
        :params bool is_available: Whether the User is available for new conversations. Set to `false` to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing).

        :returns: The updated UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Avatar': avatar,
            'State': state,
            'IsAvailable': is_available,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return UserInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FrontlineApi.V1.UserContext {}>'.format(context)

class UserInstance(InstanceResource):

    class StateType(object):
        ACTIVE = "active"
        DEACTIVATED = "deactivated"

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the UserInstance
        :returns: twilio.rest.frontline_api.v1.user.UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'identity': payload.get('identity'),
            'friendly_name': payload.get('friendly_name'),
            'avatar': payload.get('avatar'),
            'state': payload.get('state'),
            'is_available': payload.get('is_available'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserContext for this UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserContext
        """
        if self._context is None:
            self._context = UserContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the User resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def identity(self):
        """
        :returns: The application-defined string that uniquely identifies the resource's User. This value is often a username or an email address, and is case-sensitive.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the User.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def avatar(self):
        """
        :returns: The avatar URL which will be shown in Frontline application.
        :rtype: str
        """
        return self._properties['avatar']
    
    @property
    def state(self):
        """
        :returns: 
        :rtype: StateType
        """
        return self._properties['state']
    
    @property
    def is_available(self):
        """
        :returns: Whether the User is available for new conversations. Defaults to `false` for new users.
        :rtype: bool
        """
        return self._properties['is_available']
    
    @property
    def url(self):
        """
        :returns: An absolute API resource URL for this user.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the UserInstance
        

        :returns: The fetched UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, avatar=values.unset, state=values.unset, is_available=values.unset):
        """
        Update the UserInstance
        
        :params str friendly_name: The string that you assigned to describe the User.
        :params str avatar: The avatar URL which will be shown in Frontline application.
        :params StateType state: 
        :params bool is_available: Whether the User is available for new conversations. Set to `false` to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing).

        :returns: The updated UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        return self._proxy.update(friendly_name=friendly_name, avatar=avatar, state=state, is_available=is_available, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FrontlineApi.V1.UserInstance {}>'.format(context)


