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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource

from twilio.base.page import Page






class MachineToMachineListInstance(ListResource):
    def __init__(self, version: V2010, account_sid: str, country_code: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'country_code': country_code,  }
        self._uri = '/Accounts/${account_sid}/AvailablePhoneNumbers/${country_code}/MachineToMachine.json'
        
    
    def page(self, area_code, contains, sms_enabled, mms_enabled, voice_enabled, exclude_all_address_required, exclude_local_address_required, exclude_foreign_address_required, beta, near_number, near_lat_long, distance, in_postal_code, in_region, in_rate_center, in_lata, in_locality, fax_enabled, page_size):
        
        data = values.of({
            'area_code': area_code,'contains': contains,'sms_enabled': sms_enabled,'mms_enabled': mms_enabled,'voice_enabled': voice_enabled,'exclude_all_address_required': exclude_all_address_required,'exclude_local_address_required': exclude_local_address_required,'exclude_foreign_address_required': exclude_foreign_address_required,'beta': beta,'near_number': near_number,'near_lat_long': near_lat_long,'distance': distance,'in_postal_code': in_postal_code,'in_region': in_region,'in_rate_center': in_rate_center,'in_lata': in_lata,'in_locality': in_locality,'fax_enabled': fax_enabled,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return MachineToMachinePage(self._version, payload, account_sid=self._solution['account_sid'], country_code=self._solution['country_code'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MachineToMachineListInstance>'

