"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
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


class SyncMapPermissionContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, map_sid: str, identity: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'map_sid': map_sid, 'identity': identity,  }
        self._uri = '/Services/${service_sid}/Maps/${map_sid}/Permissions/${identity}'
        
    
    def delete(self):
        
        

        """
        Deletes the SyncMapPermissionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the SyncMapPermissionInstance

        :returns: The fetched SyncMapPermissionInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SyncMapPermissionInstance(self._version, payload, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'], identity=self._solution['identity'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return SyncMapPermissionInstance(self._version, payload, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'], identity=self._solution['identity'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.SyncMapPermissionContext>'



class SyncMapPermissionInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, map_sid: str, identity: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'map_sid' : payload.get('map_sid'),
            'identity' : payload.get('identity'),
            'read' : payload.get('read'),
            'write' : payload.get('write'),
            'manage' : payload.get('manage'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'map_sid': map_sid or self._properties['map_sid'],'identity': identity or self._properties['identity'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SyncMapPermissionContext(
                self._version,
                service_sid=self._solution['service_sid'],map_sid=self._solution['map_sid'],identity=self._solution['identity'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.SyncMapPermissionInstance {}>'.format(context)



class SyncMapPermissionListInstance(ListResource):
    def __init__(self, version: Version, service_sid: str, map_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'map_sid': map_sid,  }
        self._uri = '/Services/${service_sid}/Maps/${map_sid}/Permissions'
        
    
    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return SyncMapPermissionPage(self._version, payload, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.SyncMapPermissionListInstance>'

