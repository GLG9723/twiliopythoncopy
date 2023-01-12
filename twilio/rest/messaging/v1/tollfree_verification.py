"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
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




class TollfreeVerificationContext(InstanceContext):
    def __init__(self, version: V1, sid: str):
        # TODO: needs autogenerated docs
        super(TollfreeVerificationContextList, self).__init__(version)

        # Path Solution
        self._solution = { sid,  }
        self._uri = '/Tollfree/Verifications/${sid}'
        
        
        def fetch(self):
            
            """
            Fetch the TollfreeVerificationInstance

            :returns: The fetched TollfreeVerificationInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return TollfreeVerificationInstance(
                self._version,
                payload,
                sid=self._solution['sid'],
            )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TollfreeVerificationContext>'



class TollfreeVerificationInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super(TollfreeVerificationInstance, self).__init__(version)
        self._properties = { 
            'sid' = payload.get('sid'),
            'account_sid' = payload.get('account_sid'),
            'customer_profile_sid' = payload.get('customer_profile_sid'),
            'trust_product_sid' = payload.get('trust_product_sid'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'regulated_item_sid' = payload.get('regulated_item_sid'),
            'business_name' = payload.get('business_name'),
            'business_street_address' = payload.get('business_street_address'),
            'business_street_address2' = payload.get('business_street_address2'),
            'business_city' = payload.get('business_city'),
            'business_state_province_region' = payload.get('business_state_province_region'),
            'business_postal_code' = payload.get('business_postal_code'),
            'business_country' = payload.get('business_country'),
            'business_website' = payload.get('business_website'),
            'business_contact_first_name' = payload.get('business_contact_first_name'),
            'business_contact_last_name' = payload.get('business_contact_last_name'),
            'business_contact_email' = payload.get('business_contact_email'),
            'business_contact_phone' = payload.get('business_contact_phone'),
            'notification_email' = payload.get('notification_email'),
            'use_case_categories' = payload.get('use_case_categories'),
            'use_case_summary' = payload.get('use_case_summary'),
            'production_message_sample' = payload.get('production_message_sample'),
            'opt_in_image_urls' = payload.get('opt_in_image_urls'),
            'opt_in_type' = payload.get('opt_in_type'),
            'message_volume' = payload.get('message_volume'),
            'additional_information' = payload.get('additional_information'),
            'tollfree_phone_number_sid' = payload.get('tollfree_phone_number_sid'),
            'status' = payload.get('status'),
            'url' = payload.get('url'),
            'resource_links' = payload.get('resource_links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TollfreeVerificationContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.TollfreeVerificationInstance {}>'.format(context)



class TollfreeVerificationListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super(TollfreeVerificationListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Tollfree/Verifications'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return TollfreeVerificationInstance(self._version, payload, )
            
        
        def page(self, tollfree_phone_number_sid, status, page_size):
            
            data = values.of({
                'tollfree_phone_number_sid': tollfree_phone_number_sid,'status': status,'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return TollfreeVerificationPage(self._version, payload, )
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TollfreeVerificationListInstance>'

