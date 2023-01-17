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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.base.page import Page

# 


class InstalledAddOnExtensionContext(InstanceContext):
    def __init__(self, version: Version, installed_add_on_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'installed_add_on_sid': installed_add_on_sid, 'sid': sid,  }
        self._uri = '/InstalledAddOns/${installed_add_on_sid}/Extensions/${sid}'
        
    
    def fetch(self):
        
        """
        Fetch the InstalledAddOnExtensionInstance

        :returns: The fetched InstalledAddOnExtensionInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return InstalledAddOnExtensionInstance(self._version, payload, installed_add_on_sid=self._solution['installed_add_on_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return InstalledAddOnExtensionInstance(self._version, payload, installed_add_on_sid=self._solution['installed_add_on_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.Marketplace.InstalledAddOnExtensionContext>'



class InstalledAddOnExtensionInstance(InstanceResource):
    def __init__(self, version, payload, installed_add_on_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'installed_add_on_sid' : payload.get('installed_add_on_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'product_name' : payload.get('product_name'),
            'unique_name' : payload.get('unique_name'),
            'enabled' : payload.get('enabled'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'installed_add_on_sid': installed_add_on_sid or self._properties['installed_add_on_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = InstalledAddOnExtensionContext(
                self._version,
                installed_add_on_sid=self._solution['installed_add_on_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.Marketplace.InstalledAddOnExtensionInstance {}>'.format(context)



class InstalledAddOnExtensionListInstance(ListResource):
    def __init__(self, version: Version, installed_add_on_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'installed_add_on_sid': installed_add_on_sid,  }
        self._uri = '/InstalledAddOns/${installed_add_on_sid}/Extensions'
        
    
    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return InstalledAddOnExtensionPage(self._version, payload, installed_add_on_sid=self._solution['installed_add_on_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.Marketplace.InstalledAddOnExtensionListInstance>'

