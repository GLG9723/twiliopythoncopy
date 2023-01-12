"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
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

from twilio.rest.service.binding import BindingListInstancefrom twilio.rest.service.channel import ChannelListInstancefrom twilio.rest.service.role import RoleListInstancefrom twilio.rest.service.user import UserListInstance


class ServiceContext(InstanceContext):
    def __init__(self, version: V2, sid: str):
        # TODO: needs autogenerated docs
        super(ServiceContextList, self).__init__(version)

        # Path Solution
        self._solution = { sid,  }
        self._uri = '/Services/${sid}'
        
        self._bindings = None
        self._channels = None
        self._roles = None
        self._users = None
        
        def delete(self):
            
            
            """
            Deletes the ServiceInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the ServiceInstance

            :returns: The fetched ServiceInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return ServiceInstance(
                self._version,
                payload,
                sid=self._solution['sid'],
            )
            
            
        
        def update(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return ServiceInstance(self._version, payload, sid=self._solution['sid'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.ServiceContext>'



class ServiceInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super(ServiceInstance, self).__init__(version)
        self._properties = { 
            'sid' = payload.get('sid'),
            'account_sid' = payload.get('account_sid'),
            'friendly_name' = payload.get('friendly_name'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'default_service_role_sid' = payload.get('default_service_role_sid'),
            'default_channel_role_sid' = payload.get('default_channel_role_sid'),
            'default_channel_creator_role_sid' = payload.get('default_channel_creator_role_sid'),
            'read_status_enabled' = payload.get('read_status_enabled'),
            'reachability_enabled' = payload.get('reachability_enabled'),
            'typing_indicator_timeout' = payload.get('typing_indicator_timeout'),
            'consumption_report_interval' = payload.get('consumption_report_interval'),
            'limits' = payload.get('limits'),
            'pre_webhook_url' = payload.get('pre_webhook_url'),
            'post_webhook_url' = payload.get('post_webhook_url'),
            'webhook_method' = payload.get('webhook_method'),
            'webhook_filters' = payload.get('webhook_filters'),
            'pre_webhook_retry_count' = payload.get('pre_webhook_retry_count'),
            'post_webhook_retry_count' = payload.get('post_webhook_retry_count'),
            'notifications' = payload.get('notifications'),
            'media' = payload.get('media'),
            'url' = payload.get('url'),
            'links' = payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ServiceContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def bindings(self):
        return self._proxy.bindings
    @property
    def channels(self):
        return self._proxy.channels
    @property
    def roles(self):
        return self._proxy.roles
    @property
    def users(self):
        return self._proxy.users
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.ServiceInstance {}>'.format(context)



class ServiceListInstance(ListResource):
    def __init__(self, version: V2):
        # TODO: needs autogenerated docs
        super(ServiceListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Services'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return ServiceInstance(self._version, payload, )
            
        
        def page(self, page_size):
            
            data = values.of({
                'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return ServicePage(self._version, payload, )
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.ServiceListInstance>'

