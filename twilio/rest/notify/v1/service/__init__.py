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
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.notify.v1.service.binding import BindingList
from twilio.rest.notify.v1.service.notification import NotificationList


class ServiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.notify.v1.service.ServiceList
        :rtype: twilio.rest.notify.v1.service.ServiceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Services'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name=values.unset, apn_credential_sid=values.unset, gcm_credential_sid=values.unset, messaging_service_sid=values.unset, facebook_messenger_page_id=values.unset, default_apn_notification_protocol_version=values.unset, default_gcm_notification_protocol_version=values.unset, fcm_credential_sid=values.unset, default_fcm_notification_protocol_version=values.unset, log_enabled=values.unset, alexa_skill_id=values.unset, default_alexa_notification_protocol_version=values.unset, delivery_callback_url=values.unset, delivery_callback_enabled=values.unset):
        """
        Create the ServiceInstance
        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str apn_credential_sid: The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for APN Bindings.
        :param str gcm_credential_sid: The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for GCM Bindings.
        :param str messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/sms/send-messages#messaging-services) to use for SMS Bindings. This parameter must be set in order to send SMS notifications.
        :param str facebook_messenger_page_id: Deprecated.
        :param str default_apn_notification_protocol_version: The protocol version to use for sending APNS notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
        :param str default_gcm_notification_protocol_version: The protocol version to use for sending GCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
        :param str fcm_credential_sid: The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for FCM Bindings.
        :param str default_fcm_notification_protocol_version: The protocol version to use for sending FCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
        :param bool log_enabled: Whether to log notifications. Can be: `true` or `false` and the default is `true`.
        :param str alexa_skill_id: Deprecated.
        :param str default_alexa_notification_protocol_version: Deprecated.
        :param str delivery_callback_url: URL to send delivery status callback.
        :param bool delivery_callback_enabled: Callback configuration that enables delivery callbacks, default false
        
        :returns: The created ServiceInstance
        :rtype: twilio.rest.notify.v1.service.ServiceInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'ApnCredentialSid': apn_credential_sid,
            'GcmCredentialSid': gcm_credential_sid,
            'MessagingServiceSid': messaging_service_sid,
            'FacebookMessengerPageId': facebook_messenger_page_id,
            'DefaultApnNotificationProtocolVersion': default_apn_notification_protocol_version,
            'DefaultGcmNotificationProtocolVersion': default_gcm_notification_protocol_version,
            'FcmCredentialSid': fcm_credential_sid,
            'DefaultFcmNotificationProtocolVersion': default_fcm_notification_protocol_version,
            'LogEnabled': log_enabled,
            'AlexaSkillId': alexa_skill_id,
            'DefaultAlexaNotificationProtocolVersion': default_alexa_notification_protocol_version,
            'DeliveryCallbackUrl': delivery_callback_url,
            'DeliveryCallbackEnabled': delivery_callback_enabled,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return ServiceInstance(self._version, payload)
    
    
    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str friendly_name: The string that identifies the Service resources to read.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            friendly_name=friendly_name,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str friendly_name: The string that identifies the Service resources to read.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.notify.v1.service.ServiceInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately
        
        :param str friendly_name: The string that identifies the Service resources to read.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.notify.v1.service.ServicePage
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.notify.v1.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ServicePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
        
        :returns: twilio.rest.notify.v1.service.ServiceContext
        :rtype: twilio.rest.notify.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
        
        :returns: twilio.rest.notify.v1.service.ServiceContext
        :rtype: twilio.rest.notify.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.ServiceList>'










class ServicePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.notify.v1.service.ServicePage
        :rtype: twilio.rest.notify.v1.service.ServicePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.notify.v1.service.ServiceInstance
        :rtype: twilio.rest.notify.v1.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.ServicePage>'





class ServiceContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
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

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, friendly_name, apn_credential_sid, gcm_credential_sid, messaging_service_sid, facebook_messenger_page_id, default_apn_notification_protocol_version, default_gcm_notification_protocol_version, fcm_credential_sid, default_fcm_notification_protocol_version, log_enabled, alexa_skill_id, default_alexa_notification_protocol_version, delivery_callback_url, delivery_callback_enabled):
        data = values.of({
            'friendly_name': friendly_name,'apn_credential_sid': apn_credential_sid,'gcm_credential_sid': gcm_credential_sid,'messaging_service_sid': messaging_service_sid,'facebook_messenger_page_id': facebook_messenger_page_id,'default_apn_notification_protocol_version': default_apn_notification_protocol_version,'default_gcm_notification_protocol_version': default_gcm_notification_protocol_version,'fcm_credential_sid': fcm_credential_sid,'default_fcm_notification_protocol_version': default_fcm_notification_protocol_version,'log_enabled': log_enabled,'alexa_skill_id': alexa_skill_id,'default_alexa_notification_protocol_version': default_alexa_notification_protocol_version,'delivery_callback_url': delivery_callback_url,'delivery_callback_enabled': delivery_callback_enabled,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1.ServiceContext>'



class ServiceInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'apn_credential_sid' : payload.get('apn_credential_sid'),
            'gcm_credential_sid' : payload.get('gcm_credential_sid'),
            'fcm_credential_sid' : payload.get('fcm_credential_sid'),
            'messaging_service_sid' : payload.get('messaging_service_sid'),
            'facebook_messenger_page_id' : payload.get('facebook_messenger_page_id'),
            'default_apn_notification_protocol_version' : payload.get('default_apn_notification_protocol_version'),
            'default_gcm_notification_protocol_version' : payload.get('default_gcm_notification_protocol_version'),
            'default_fcm_notification_protocol_version' : payload.get('default_fcm_notification_protocol_version'),
            'log_enabled' : payload.get('log_enabled'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
            'alexa_skill_id' : payload.get('alexa_skill_id'),
            'default_alexa_notification_protocol_version' : payload.get('default_alexa_notification_protocol_version'),
            'delivery_callback_url' : payload.get('delivery_callback_url'),
            'delivery_callback_enabled' : payload.get('delivery_callback_enabled'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
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
        return '<Twilio.Notify.V1.ServiceInstance {}>'.format(context)



