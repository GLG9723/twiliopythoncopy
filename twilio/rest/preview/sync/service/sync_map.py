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

from twilio.base.page import Page

from twilio.rest.sync_map.sync_map_item import SyncMapItemListInstancefrom twilio.rest.sync_map.sync_map_permission import SyncMapPermissionListInstance


class SyncMapContext(InstanceContext):
    def __init__(self, version: Sync, service_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Maps/${sid}'
        
        self._sync_map_items = None
        self._sync_map_permissions = None
    
    def delete(self):
        
        
        """
        Deletes the SyncMapInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the SyncMapInstance

        :returns: The fetched SyncMapInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return SyncMapInstance(
            self._version,
            payload,
            service_sidsid=self._solution['service_sid''sid'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.Sync.SyncMapContext>'



class SyncMapInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'unique_name' : payload.get('unique_name'),
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
            'revision' : payload.get('revision'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'created_by' : payload.get('created_by'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid']'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SyncMapContext(
                self._version,
                service_sid=self._solution['service_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def sync_map_items(self):
        return self._proxy.sync_map_items
    @property
    def sync_map_permissions(self):
        return self._proxy.sync_map_permissions
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.Sync.SyncMapInstance {}>'.format(context)



class SyncMapListInstance(ListResource):
    def __init__(self, version: Sync, service_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/${service_sid}/Maps'
        
    
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return SyncMapInstance(self._version, payload, service_sid=self._solution['service_sid'])
        
    
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return SyncMapPage(self._version, payload, service_sid=self._solution['service_sid'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.Sync.SyncMapListInstance>'

