"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Notify
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

from twilio.rest.service.binding import BindingListInstancefrom twilio.rest.service.notification import NotificationListInstance


class ServiceContext(InstanceContext):
    def __init__(self, version: V1, sid: str):
        # TODO: needs autogenerated docs
        super(ServiceContextList, self).__init__(version)

        # Path Solution
        self._solution = { sid,  }
        self._uri = '/Services/${sid}'
        
        self._bindings = None
        self._notifications = None
        
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
        return '<Twilio.Api.V1.ServiceContext>'



class ServiceInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super(ServiceInstance, self).__init__(version)
        self._properties = { 
            'sid' = payload.get('sid'),
            'account_sid' = payload.get('account_sid'),
            'friendly_name' = payload.get('friendly_name'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'apn_credential_sid' = payload.get('apn_credential_sid'),
            'gcm_credential_sid' = payload.get('gcm_credential_sid'),
            'fcm_credential_sid' = payload.get('fcm_credential_sid'),
            'messaging_service_sid' = payload.get('messaging_service_sid'),
            'facebook_messenger_page_id' = payload.get('facebook_messenger_page_id'),
            'default_apn_notification_protocol_version' = payload.get('default_apn_notification_protocol_version'),
            'default_gcm_notification_protocol_version' = payload.get('default_gcm_notification_protocol_version'),
            'default_fcm_notification_protocol_version' = payload.get('default_fcm_notification_protocol_version'),
            'log_enabled' = payload.get('log_enabled'),
            'url' = payload.get('url'),
            'links' = payload.get('links'),
            'alexa_skill_id' = payload.get('alexa_skill_id'),
            'default_alexa_notification_protocol_version' = payload.get('default_alexa_notification_protocol_version'),
            'delivery_callback_url' = payload.get('delivery_callback_url'),
            'delivery_callback_enabled' = payload.get('delivery_callback_enabled'),
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
    def notifications(self):
        return self._proxy.notifications
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.ServiceInstance {}>'.format(context)



class ServiceListInstance(ListResource):
    def __init__(self, version: V1):
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
            
        
        def page(self, friendly_name, page_size):
            
            data = values.of({
                'friendly_name': friendly_name,'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return ServicePage(self._version, payload, )
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ServiceListInstance>'

