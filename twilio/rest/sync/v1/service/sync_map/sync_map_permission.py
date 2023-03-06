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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SyncMapPermissionList(ListResource):

    def __init__(self, version: Version, service_sid: str, map_sid: str):
        """
        Initialize the SyncMapPermissionList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resources to read. Can be the Service's `sid` value or `default`.
        :param map_sid: The SID of the Sync Map with the Permission resources to read. Can be the Sync Map resource's `sid` or its `unique_name`.
        
        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionList
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'map_sid': map_sid,  }
        self._uri = '/Services/{service_sid}/Maps/{map_sid}/Permissions'.format(**self._solution)
        
        
    
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams SyncMapPermissionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SyncMapPermissionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SyncMapPermissionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapPermissionInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SyncMapPermissionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncMapPermissionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapPermissionInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SyncMapPermissionPage(self._version, response, self._solution)


    def get(self, identity):
        """
        Constructs a SyncMapPermissionContext
        
        :param identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to update.
        
        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionContext
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionContext
        """
        return SyncMapPermissionContext(self._version, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'], identity=identity)

    def __call__(self, identity):
        """
        Constructs a SyncMapPermissionContext
        
        :param identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to update.
        
        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionContext
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionContext
        """
        return SyncMapPermissionContext(self._version, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'], identity=identity)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncMapPermissionList>'








class SyncMapPermissionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SyncMapPermissionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionPage
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncMapPermissionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        return SyncMapPermissionInstance(self._version, payload, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncMapPermissionPage>'




class SyncMapPermissionInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, map_sid: str, identity: str=None):
        """
        Initialize the SyncMapPermissionInstance
        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'map_sid': payload.get('map_sid'),
            'identity': payload.get('identity'),
            'read': payload.get('read'),
            'write': payload.get('write'),
            'manage': payload.get('manage'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'map_sid': map_sid, 'identity': identity or self._properties['identity'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncMapPermissionContext for this SyncMapPermissionInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionContext
        """
        if self._context is None:
            self._context = SyncMapPermissionContext(self._version, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'], identity=self._solution['identity'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Sync Map Permission resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def map_sid(self):
        """
        :returns: The SID of the Sync Map to which the Permission applies.
        :rtype: str
        """
        return self._properties['map_sid']
    
    @property
    def identity(self):
        """
        :returns: The application-defined string that uniquely identifies the resource's User within the Service to an FPA token.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def read(self):
        """
        :returns: Whether the identity can read the Sync Map and its Items.
        :rtype: bool
        """
        return self._properties['read']
    
    @property
    def write(self):
        """
        :returns: Whether the identity can create, update, and delete Items in the Sync Map.
        :rtype: bool
        """
        return self._properties['write']
    
    @property
    def manage(self):
        """
        :returns: Whether the identity can delete the Sync Map.
        :rtype: bool
        """
        return self._properties['manage']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Sync Map Permission resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the SyncMapPermissionInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the SyncMapPermissionInstance
        

        :returns: The fetched SyncMapPermissionInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        return self._proxy.fetch()
    
    def update(self, read, write, manage):
        """
        Update the SyncMapPermissionInstance
        
        :params bool read: Whether the identity can read the Sync Map and its Items. Default value is `false`.
        :params bool write: Whether the identity can create, update, and delete Items in the Sync Map. Default value is `false`.
        :params bool manage: Whether the identity can delete the Sync Map. Default value is `false`.

        :returns: The updated SyncMapPermissionInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        return self._proxy.update(read=read, write=write, manage=manage, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncMapPermissionInstance {}>'.format(context)

class SyncMapPermissionContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, map_sid: str, identity: str):
        """
        Initialize the SyncMapPermissionContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to update. Can be the Service's `sid` value or `default`.:param map_sid: The SID of the Sync Map with the Sync Map Permission resource to update. Can be the Sync Map resource's `sid` or its `unique_name`.:param identity: The application-defined string that uniquely identifies the User's Sync Map Permission resource to update.

        :returns: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionContext
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'map_sid': map_sid,
            'identity': identity,
        }
        self._uri = '/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the SyncMapPermissionInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the SyncMapPermissionInstance
        

        :returns: The fetched SyncMapPermissionInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SyncMapPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            map_sid=self._solution['map_sid'],
            identity=self._solution['identity'],
            
        )
        
    def update(self, read, write, manage):
        """
        Update the SyncMapPermissionInstance
        
        :params bool read: Whether the identity can read the Sync Map and its Items. Default value is `false`.
        :params bool write: Whether the identity can create, update, and delete Items in the Sync Map. Default value is `false`.
        :params bool manage: Whether the identity can delete the Sync Map. Default value is `false`.

        :returns: The updated SyncMapPermissionInstance
        :rtype: twilio.rest.sync.v1.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        data = values.of({ 
            'Read': read,
            'Write': write,
            'Manage': manage,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SyncMapPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            map_sid=self._solution['map_sid'],
            identity=self._solution['identity']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncMapPermissionContext {}>'.format(context)


