"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Lookups
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

# 


class PhoneNumberContext(InstanceContext):
    def __init__(self, version: Version, phone_number: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'phone_number': phone_number,  }
        self._uri = '/PhoneNumbers/${phone_number}'
        
    
    def fetch(self, fields, country_code, first_name, last_name, address_line1, address_line2, city, state, postal_code, address_country_code, national_id, date_of_birth):
        
        """
        Fetch the PhoneNumberInstance

        :returns: The fetched PhoneNumberInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PhoneNumberInstance(self._version, payload, phone_number=self._solution['phone_number'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.PhoneNumberContext>'



class PhoneNumberInstance(InstanceResource):
    def __init__(self, version, payload, phone_number: str):
        super().__init__(version)
        self._properties = { 
            'calling_country_code' : payload.get('calling_country_code'),
            'country_code' : payload.get('country_code'),
            'phone_number' : payload.get('phone_number'),
            'national_format' : payload.get('national_format'),
            'valid' : payload.get('valid'),
            'validation_errors' : payload.get('validation_errors'),
            'caller_name' : payload.get('caller_name'),
            'sim_swap' : payload.get('sim_swap'),
            'call_forwarding' : payload.get('call_forwarding'),
            'live_activity' : payload.get('live_activity'),
            'line_type_intelligence' : payload.get('line_type_intelligence'),
            'identity_match' : payload.get('identity_match'),
            'sms_pumping_risk' : payload.get('sms_pumping_risk'),
            'disposable_phone_number_risk' : payload.get('disposable_phone_number_risk'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'phone_number': phone_number or self._properties['phone_number'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                phone_number=self._solution['phone_number'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.PhoneNumberInstance {}>'.format(context)



class PhoneNumberList(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = ''
        


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.PhoneNumberList>'

