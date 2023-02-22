"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
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


class CustomerProfilesEntityAssignmentsList(ListResource):

    def __init__(self, version: Version, customer_profile_sid: str):
        """
        Initialize the CustomerProfilesEntityAssignmentsList

        :param Version version: Version that contains the resource
        :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
        
        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsList
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'customer_profile_sid': customer_profile_sid,  }
        self._uri = '/CustomerProfiles/${customer_profile_sid}/EntityAssignments'.format(**self._solution)
        
        
    
    
    
    def create(self, object_sid):
        """
        Create the CustomerProfilesEntityAssignmentsInstance
        :param str object_sid: The SID of an object bag that holds information of the different items.
        
        :returns: The created CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance
        """
        data = values.of({ 
            'ObjectSid': object_sid,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return CustomerProfilesEntityAssignmentsInstance(self._version, payload, customer_profile_sid=self._solution['customer_profile_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams CustomerProfilesEntityAssignmentsInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists CustomerProfilesEntityAssignmentsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CustomerProfilesEntityAssignmentsInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CustomerProfilesEntityAssignmentsPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CustomerProfilesEntityAssignmentsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CustomerProfilesEntityAssignmentsPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a CustomerProfilesEntityAssignmentsContext
        
        :param sid: The unique string that we created to identify the Identity resource.
        
        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        """
        return CustomerProfilesEntityAssignmentsContext(self._version, customer_profile_sid=self._solution['customer_profile_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a CustomerProfilesEntityAssignmentsContext
        
        :param sid: The unique string that we created to identify the Identity resource.
        
        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        """
        return CustomerProfilesEntityAssignmentsContext(self._version, customer_profile_sid=self._solution['customer_profile_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.CustomerProfilesEntityAssignmentsList>'








class CustomerProfilesEntityAssignmentsPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CustomerProfilesEntityAssignmentsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsPage
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CustomerProfilesEntityAssignmentsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance
        """
        return CustomerProfilesEntityAssignmentsInstance(self._version, payload, customer_profile_sid=self._solution['customer_profile_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.CustomerProfilesEntityAssignmentsPage>'





class CustomerProfilesEntityAssignmentsContext(InstanceContext):
    def __init__(self, version: Version, customer_profile_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'customer_profile_sid': customer_profile_sid, 'sid': sid,  }
        self._uri = '/CustomerProfiles/${customer_profile_sid}/EntityAssignments/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the CustomerProfilesEntityAssignmentsInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the CustomerProfilesEntityAssignmentsInstance

        :returns: The fetched CustomerProfilesEntityAssignmentsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CustomerProfilesEntityAssignmentsInstance(self._version, payload, customer_profile_sid=self._solution['customer_profile_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.CustomerProfilesEntityAssignmentsContext>'



class CustomerProfilesEntityAssignmentsInstance(InstanceResource):
    def __init__(self, version, payload, customer_profile_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'customer_profile_sid' : payload.get('customer_profile_sid'),
            'account_sid' : payload.get('account_sid'),
            'object_sid' : payload.get('object_sid'),
            'date_created' : payload.get('date_created'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'customer_profile_sid': customer_profile_sid or self._properties['customer_profile_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = CustomerProfilesEntityAssignmentsContext(
                self._version,
                customer_profile_sid=self._solution['customer_profile_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.CustomerProfilesEntityAssignmentsInstance {}>'.format(context)



