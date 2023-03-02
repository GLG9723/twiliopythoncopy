"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class ReplaceItemsList(ListResource):

    def __init__(self, version: Version, bundle_sid: str):
        """
        Initialize the ReplaceItemsList

        :param Version version: Version that contains the resource
        :param bundle_sid: The unique string that identifies the Bundle where the item assignments are going to be replaced.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.replace_items.ReplaceItemsList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.replace_items.ReplaceItemsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'bundle_sid': bundle_sid,  }
        self._uri = '/RegulatoryCompliance/Bundles/{bundle_sid}/ReplaceItems'.format(**self._solution)
        
        
    
    def create(self, from_bundle_sid):
        """
        Create the ReplaceItemsInstance

        :param str from_bundle_sid: The source bundle sid to copy the item assignments from.
        
        :returns: The created ReplaceItemsInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.replace_items.ReplaceItemsInstance
        """
        data = values.of({ 
            'FromBundleSid': from_bundle_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ReplaceItemsInstance(self._version, payload, bundle_sid=self._solution['bundle_sid'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.ReplaceItemsList>'


class ReplaceItemsInstance(InstanceResource):

    class ReplaceItemsStatus(object):
        DRAFT = "draft"
        PENDING_REVIEW = "pending-review"
        IN_REVIEW = "in-review"
        TWILIO_REJECTED = "twilio-rejected"
        TWILIO_APPROVED = "twilio-approved"
        PROVISIONALLY_APPROVED = "provisionally-approved"

    def __init__(self, version, payload, bundle_sid: str):
        """
        Initialize the ReplaceItemsInstance
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.replace_items.ReplaceItemsInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.replace_items.ReplaceItemsInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'regulation_sid': payload.get('regulation_sid'),
            'friendly_name': payload.get('friendly_name'),
            'status': payload.get('status'),
            'valid_until': deserialize.iso8601_datetime(payload.get('valid_until')),
            'email': payload.get('email'),
            'status_callback': payload.get('status_callback'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
        }

        self._context = None
        self._solution = { 'bundle_sid': bundle_sid,  }
    
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Bundle resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Bundle resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def regulation_sid(self):
        """
        :returns: The unique string of a regulation that is associated to the Bundle resource.
        :rtype: str
        """
        return self._properties['regulation_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: ReplaceItemsStatus
        """
        return self._properties['status']
    
    @property
    def valid_until(self):
        """
        :returns: The date and time in GMT in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format when the resource will be valid until.
        :rtype: datetime
        """
        return self._properties['valid_until']
    
    @property
    def email(self):
        """
        :returns: The email address that will receive updates when the Bundle resource changes status.
        :rtype: str
        """
        return self._properties['email']
    
    @property
    def status_callback(self):
        """
        :returns: The URL we call to inform your application of status changes.
        :rtype: str
        """
        return self._properties['status_callback']
    
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
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Numbers.V2.ReplaceItemsInstance {}>'.format(context)


