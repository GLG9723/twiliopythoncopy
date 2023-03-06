"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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


class AssignedAddOnExtensionList(ListResource):

    def __init__(self, version: Version, account_sid: str, resource_sid: str, assigned_add_on_sid: str):
        """
        Initialize the AssignedAddOnExtensionList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
        :param resource_sid: The SID of the Phone Number to which the Add-on is assigned.
        :param assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
        
        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'resource_sid': resource_sid, 'assigned_add_on_sid': assigned_add_on_sid,  }
        self._uri = '/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions.json'.format(**self._solution)
        
        
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams AssignedAddOnExtensionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AssignedAddOnExtensionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AssignedAddOnExtensionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AssignedAddOnExtensionInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AssignedAddOnExtensionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AssignedAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AssignedAddOnExtensionInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AssignedAddOnExtensionPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a AssignedAddOnExtensionContext
        
        :param sid: The Twilio-provided string that uniquely identifies the resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionContext
        """
        return AssignedAddOnExtensionContext(self._version, account_sid=self._solution['account_sid'], resource_sid=self._solution['resource_sid'], assigned_add_on_sid=self._solution['assigned_add_on_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a AssignedAddOnExtensionContext
        
        :param sid: The Twilio-provided string that uniquely identifies the resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionContext
        """
        return AssignedAddOnExtensionContext(self._version, account_sid=self._solution['account_sid'], resource_sid=self._solution['resource_sid'], assigned_add_on_sid=self._solution['assigned_add_on_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AssignedAddOnExtensionList>'




class AssignedAddOnExtensionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AssignedAddOnExtensionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionPage
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AssignedAddOnExtensionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionInstance
        """
        return AssignedAddOnExtensionInstance(self._version, payload, account_sid=self._solution['account_sid'], resource_sid=self._solution['resource_sid'], assigned_add_on_sid=self._solution['assigned_add_on_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AssignedAddOnExtensionPage>'




class AssignedAddOnExtensionInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, resource_sid: str, assigned_add_on_sid: str, sid: str=None):
        """
        Initialize the AssignedAddOnExtensionInstance
        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'resource_sid': payload.get('resource_sid'),
            'assigned_add_on_sid': payload.get('assigned_add_on_sid'),
            'friendly_name': payload.get('friendly_name'),
            'product_name': payload.get('product_name'),
            'unique_name': payload.get('unique_name'),
            'uri': payload.get('uri'),
            'enabled': payload.get('enabled'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'resource_sid': resource_sid, 'assigned_add_on_sid': assigned_add_on_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssignedAddOnExtensionContext for this AssignedAddOnExtensionInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionContext
        """
        if self._context is None:
            self._context = AssignedAddOnExtensionContext(self._version, account_sid=self._solution['account_sid'], resource_sid=self._solution['resource_sid'], assigned_add_on_sid=self._solution['assigned_add_on_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def resource_sid(self):
        """
        :returns: The SID of the Phone Number to which the Add-on is assigned.
        :rtype: str
        """
        return self._properties['resource_sid']
    
    @property
    def assigned_add_on_sid(self):
        """
        :returns: The SID that uniquely identifies the assigned Add-on installation.
        :rtype: str
        """
        return self._properties['assigned_add_on_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def product_name(self):
        """
        :returns: A string that you assigned to describe the Product this Extension is used within.
        :rtype: str
        """
        return self._properties['product_name']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    @property
    def enabled(self):
        """
        :returns: Whether the Extension will be invoked.
        :rtype: bool
        """
        return self._properties['enabled']
    
    def fetch(self):
        """
        Fetch the AssignedAddOnExtensionInstance
        

        :returns: The fetched AssignedAddOnExtensionInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AssignedAddOnExtensionInstance {}>'.format(context)

class AssignedAddOnExtensionContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, resource_sid: str, assigned_add_on_sid: str, sid: str):
        """
        Initialize the AssignedAddOnExtensionContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.:param resource_sid: The SID of the Phone Number to which the Add-on is assigned.:param assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.:param sid: The Twilio-provided string that uniquely identifies the resource to fetch.

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionContext
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'resource_sid': resource_sid,
            'assigned_add_on_sid': assigned_add_on_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions/{sid}.json'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the AssignedAddOnExtensionInstance
        

        :returns: The fetched AssignedAddOnExtensionInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.assigned_add_on.assigned_add_on_extension.AssignedAddOnExtensionInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AssignedAddOnExtensionInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            resource_sid=self._solution['resource_sid'],
            assigned_add_on_sid=self._solution['assigned_add_on_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AssignedAddOnExtensionContext {}>'.format(context)


