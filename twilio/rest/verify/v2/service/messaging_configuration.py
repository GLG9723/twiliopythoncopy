"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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


class MessagingConfigurationList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the MessagingConfigurationList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.
        
        :returns: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationList
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/MessagingConfigurations'.format(**self._solution)
        
        
    
    
    
    
    def create(self, country, messaging_service_sid):
        """
        Create the MessagingConfigurationInstance

        :param str country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.
        :param str messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) to be used to send SMS to the country of this configuration.
        
        :returns: The created MessagingConfigurationInstance
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance
        """
        data = values.of({ 
            'Country': country,
            'MessagingServiceSid': messaging_service_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return MessagingConfigurationInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams MessagingConfigurationInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists MessagingConfigurationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MessagingConfigurationInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessagingConfigurationInstance
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return MessagingConfigurationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MessagingConfigurationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessagingConfigurationInstance
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return MessagingConfigurationPage(self._version, response, self._solution)


    def get(self, country):
        """
        Constructs a MessagingConfigurationContext
        
        :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.
        
        :returns: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationContext
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationContext
        """
        return MessagingConfigurationContext(self._version, service_sid=self._solution['service_sid'], country=country)

    def __call__(self, country):
        """
        Constructs a MessagingConfigurationContext
        
        :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.
        
        :returns: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationContext
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationContext
        """
        return MessagingConfigurationContext(self._version, service_sid=self._solution['service_sid'], country=country)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.MessagingConfigurationList>'










class MessagingConfigurationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MessagingConfigurationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationPage
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessagingConfigurationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance
        """
        return MessagingConfigurationInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.MessagingConfigurationPage>'




class MessagingConfigurationContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, country: str):
        """
        Initialize the MessagingConfigurationContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.
        :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.

        :returns: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationContext
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'country': country,
        }
        self._uri = '/Services/{service_sid}/MessagingConfigurations/{country}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the MessagingConfigurationInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the MessagingConfigurationInstance
        

        :returns: The fetched MessagingConfigurationInstance
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MessagingConfigurationInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            country=self._solution['country'],
            
        )
        
    def update(self, messaging_service_sid):
        """
        Update the MessagingConfigurationInstance
        
        :params str messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) to be used to send SMS to the country of this configuration.

        :returns: The updated MessagingConfigurationInstance
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance
        """
        data = values.of({ 
            'MessagingServiceSid': messaging_service_sid,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return MessagingConfigurationInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            country=self._solution['country']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.MessagingConfigurationContext {}>'.format(context)

class MessagingConfigurationInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, country: str=None):
        """
        Initialize the MessagingConfigurationInstance
        :returns: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'country': payload.get('country'),
            'messaging_service_sid': payload.get('messaging_service_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'country': country or self._properties['country'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MessagingConfigurationContext for this MessagingConfigurationInstance
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationContext
        """
        if self._context is None:
            self._context = MessagingConfigurationContext(self._version, service_sid=self._solution['service_sid'], country=self._solution['country'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def country(self):
        """
        :returns: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value `all`.
        :rtype: str
        """
        return self._properties['country']
    
    @property
    def messaging_service_sid(self):
        """
        :returns: The SID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) to be used to send SMS to the country of this configuration.
        :rtype: str
        """
        return self._properties['messaging_service_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the MessagingConfigurationInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the MessagingConfigurationInstance
        

        :returns: The fetched MessagingConfigurationInstance
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance
        """
        return self._proxy.fetch()
    
    def update(self, messaging_service_sid):
        """
        Update the MessagingConfigurationInstance
        
        :params str messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) to be used to send SMS to the country of this configuration.

        :returns: The updated MessagingConfigurationInstance
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationInstance
        """
        return self._proxy.update(messaging_service_sid=messaging_service_sid, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.MessagingConfigurationInstance {}>'.format(context)


