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


class UserBindingList(ListResource):

    def __init__(self, version: Version, service_sid: str, user_sid: str):
        """
        Initialize the UserBindingList
        :param Version version: Version that contains the resource
        :param service_sid: 
        :param user_sid: 
        
        :returns: twilio.ip_messaging.v2.user_binding..UserBindingList
        :rtype: twilio.ip_messaging.v2.user_binding..UserBindingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'user_sid': user_sid,  }
        self._uri = '/Services/${service_sid}/Users/${user_sid}/Bindings'.format(**self._solution)


    
    
    
    def stream(self, binding_type=values.unset, limit=None, page_size=None):
        """
        Streams UserBindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param [UserBindingBindingType] binding_type: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.user_binding.UserBindingInstance]
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
        
        :param [UserBindingBindingType] binding_type: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.user_binding.UserBindingInstance]
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
        
        :param [UserBindingBindingType] binding_type: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserBindingInstance
        :rtype: twilio.rest.ip_messaging.v2.user_binding.UserBindingPage
        """
        data = values.of({ 
            'BindingType': binding_type,
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
        :rtype: twilio.rest.ip_messaging.v2.user_binding.UserBindingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return UserBindingPage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.UserBindingList>'






class UserBindingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UserBindingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.ip_messaging.v2.user_binding.UserBindingPage
        :rtype: twilio.rest.ip_messaging.v2.user_binding.UserBindingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserBindingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.ip_messaging.v2.user_binding.UserBindingInstance
        :rtype: twilio.rest.ip_messaging.v2.user_binding.UserBindingInstance
        """
        return UserBindingInstance(self._version, payload, service_sid=self._solution['service_sid'], user_sid=self._solution['user_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.UserBindingPage>'





class UserBindingContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, user_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'user_sid': user_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Users/${user_sid}/Bindings/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the UserBindingInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the UserBindingInstance

        :returns: The fetched UserBindingInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UserBindingInstance(self._version, payload, service_sid=self._solution['service_sid'], user_sid=self._solution['user_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.UserBindingContext>'



class UserBindingInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, user_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'endpoint' : payload.get('endpoint'),
            'identity' : payload.get('identity'),
            'user_sid' : payload.get('user_sid'),
            'credential_sid' : payload.get('credential_sid'),
            'binding_type' : payload.get('binding_type'),
            'message_types' : payload.get('message_types'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'user_sid': user_sid or self._properties['user_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = UserBindingContext(
                self._version,
                service_sid=self._solution['service_sid'],user_sid=self._solution['user_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.UserBindingInstance {}>'.format(context)



