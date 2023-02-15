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
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.ip_messaging.v1.service.channels import ChannelList
from twilio.rest.ip_messaging.v1.service.roles import RoleList
from twilio.rest.ip_messaging.v1.service.users import UserList


class ServiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ServiceList
        :param Version version: Version that contains the resource
        
        :returns: twilio.ip_messaging.v1.service..ServiceList
        :rtype: twilio.ip_messaging.v1.service..ServiceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Services'.format(**self._solution)


    
    
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.ip_messaging.v1.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v1.service.ServiceInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.ip_messaging.v1.service.ServicePage
        """
        data = values.of({ 
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
        :rtype: twilio.rest.ip_messaging.v1.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ServicePage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.ServiceList>'










class ServicePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.ip_messaging.v1.service.ServicePage
        :rtype: twilio.rest.ip_messaging.v1.service.ServicePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.ip_messaging.v1.service.ServiceInstance
        :rtype: twilio.rest.ip_messaging.v1.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.ServicePage>'





class ServiceContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Services/${sid}'
        
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

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
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
        return '<Twilio.IpMessaging.V1.ServiceContext>'



class ServiceInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'default_service_role_sid' : payload.get('default_service_role_sid'),
            'default_channel_role_sid' : payload.get('default_channel_role_sid'),
            'default_channel_creator_role_sid' : payload.get('default_channel_creator_role_sid'),
            'read_status_enabled' : payload.get('read_status_enabled'),
            'reachability_enabled' : payload.get('reachability_enabled'),
            'typing_indicator_timeout' : payload.get('typing_indicator_timeout'),
            'consumption_report_interval' : payload.get('consumption_report_interval'),
            'limits' : payload.get('limits'),
            'webhooks' : payload.get('webhooks'),
            'pre_webhook_url' : payload.get('pre_webhook_url'),
            'post_webhook_url' : payload.get('post_webhook_url'),
            'webhook_method' : payload.get('webhook_method'),
            'webhook_filters' : payload.get('webhook_filters'),
            'notifications' : payload.get('notifications'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
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
        return '<Twilio.IpMessaging.V1.ServiceInstance {}>'.format(context)



