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

from twilio.base.page import Page




class CustomerProfilesEntityAssignmentsContext(InstanceContext):
    def __init__(self, version: V1, customer_profile_sid: str, sid: str):
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
        return CustomerProfilesEntityAssignmentsInstance(
            self._version,
            payload,
            customer_profile_sidsid=self._solution['customer_profile_sid''sid'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.CustomerProfilesEntityAssignmentsContext>'



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
            'customer_profile_sid': customer_profile_sid or self._properties['customer_profile_sid']'sid': sid or self._properties['sid']
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
        return '<Twilio.Api.V1.CustomerProfilesEntityAssignmentsInstance {}>'.format(context)



class CustomerProfilesEntityAssignmentsListInstance(ListResource):
    def __init__(self, version: V1, customer_profile_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'customer_profile_sid': customer_profile_sid,  }
        self._uri = '/CustomerProfiles/${customer_profile_sid}/EntityAssignments'
        
    
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return CustomerProfilesEntityAssignmentsInstance(self._version, payload, customer_profile_sid=self._solution['customer_profile_sid'])
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return CustomerProfilesEntityAssignmentsPage(self._version, payload, customer_profile_sid=self._solution['customer_profile_sid'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.CustomerProfilesEntityAssignmentsListInstance>'

