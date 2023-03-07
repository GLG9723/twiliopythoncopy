"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
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
from twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension import InstalledAddOnExtensionList


class InstalledAddOnList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InstalledAddOnList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnList
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/InstalledAddOns'.format(**self._solution)
        
        
    
    
    
    
    def create(self, available_add_on_sid, accept_terms_of_service, configuration=values.unset, unique_name=values.unset):
        """
        Create the InstalledAddOnInstance

        :param str available_add_on_sid: The SID of the AvaliableAddOn to install.
        :param bool accept_terms_of_service: Whether the Terms of Service were accepted.
        :param object configuration: The JSON object that represents the configuration of the new Add-on being installed.
        :param str unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.
        
        :returns: The created InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        """
        data = values.of({ 
            'AvailableAddOnSid': available_add_on_sid,
            'AcceptTermsOfService': accept_terms_of_service,
            'Configuration': serialize.object(configuration),
            'UniqueName': unique_name,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return InstalledAddOnInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams InstalledAddOnInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists InstalledAddOnInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of InstalledAddOnInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return InstalledAddOnPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InstalledAddOnInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return InstalledAddOnPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a InstalledAddOnContext
        
        :param sid: The SID of the InstalledAddOn resource to update.
        
        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        """
        return InstalledAddOnContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a InstalledAddOnContext
        
        :param sid: The SID of the InstalledAddOn resource to update.
        
        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        """
        return InstalledAddOnContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace.InstalledAddOnList>'










class InstalledAddOnPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the InstalledAddOnPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnPage
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InstalledAddOnInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        """
        return InstalledAddOnInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace.InstalledAddOnPage>'




class InstalledAddOnContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the InstalledAddOnContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the InstalledAddOn resource to update.

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/InstalledAddOns/{sid}'.format(**self._solution)
        
        self._extensions = None
    
    def delete(self):
        """
        Deletes the InstalledAddOnInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the InstalledAddOnInstance
        

        :returns: The fetched InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return InstalledAddOnInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, configuration=values.unset, unique_name=values.unset):
        """
        Update the InstalledAddOnInstance
        
        :params object configuration: Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured
        :params str unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.

        :returns: The updated InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        """
        data = values.of({ 
            'Configuration': serialize.object(configuration),
            'UniqueName': unique_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return InstalledAddOnInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def extensions(self):
        """
        Access the extensions

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnExtensionList
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnExtensionList
        """
        if self._extensions is None:
            self._extensions = InstalledAddOnExtensionList(
                self._version, 
                self._solution['sid'],
            )
        return self._extensions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Marketplace.InstalledAddOnContext {}>'.format(context)

class InstalledAddOnInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the InstalledAddOnInstance
        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'description': payload.get('description'),
            'configuration': payload.get('configuration'),
            'unique_name': payload.get('unique_name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InstalledAddOnContext for this InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        """
        if self._context is None:
            self._context = InstalledAddOnContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the InstalledAddOn resource. This Sid can also be found in the Console on that specific Add-ons page as the 'Available Add-on Sid'.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the InstalledAddOn resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def description(self):
        """
        :returns: A short description of the Add-on's functionality.
        :rtype: str
        """
        return self._properties['description']
    
    @property
    def configuration(self):
        """
        :returns: The JSON object that represents the current configuration of installed Add-on.
        :rtype: dict
        """
        return self._properties['configuration']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource.
        :rtype: str
        """
        return self._properties['unique_name']
    
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
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the InstalledAddOnInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the InstalledAddOnInstance
        

        :returns: The fetched InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        """
        return self._proxy.fetch()
    
    def update(self, configuration=values.unset, unique_name=values.unset):
        """
        Update the InstalledAddOnInstance
        
        :params object configuration: Valid JSON object that conform to the configuration schema exposed by the associated AvailableAddOn resource. This is only required by Add-ons that need to be configured
        :params str unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within the Account.

        :returns: The updated InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        """
        return self._proxy.update(configuration=configuration, unique_name=unique_name, )
    
    @property
    def extensions(self):
        """
        Access the extensions

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnExtensionList
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnExtensionList
        """
        return self._proxy.extensions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Marketplace.InstalledAddOnInstance {}>'.format(context)


