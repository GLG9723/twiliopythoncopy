"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
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


class AssetVersionContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, asset_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'asset_sid': asset_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Assets/${asset_sid}/Versions/${sid}'
        
    
    def fetch(self):
        
        """
        Fetch the AssetVersionInstance

        :returns: The fetched AssetVersionInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AssetVersionInstance(self._version, payload, service_sid=self._solution['service_sid'], asset_sid=self._solution['asset_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.AssetVersionContext>'



class AssetVersionInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, asset_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'asset_sid' : payload.get('asset_sid'),
            'path' : payload.get('path'),
            'visibility' : payload.get('visibility'),
            'date_created' : payload.get('date_created'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'asset_sid': asset_sid or self._properties['asset_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AssetVersionContext(
                self._version,
                service_sid=self._solution['service_sid'],asset_sid=self._solution['asset_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.AssetVersionInstance {}>'.format(context)



class AssetVersionList(ListResource):
    def __init__(self, version: Version, service_sid: str, asset_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'asset_sid': asset_sid,  }
        self._uri = '/Services/${service_sid}/Assets/${asset_sid}/Versions'
        

    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return AssetVersionPage(self._version, payload, service_sid=self._solution['service_sid'], asset_sid=self._solution['asset_sid'], )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.AssetVersionList>'

