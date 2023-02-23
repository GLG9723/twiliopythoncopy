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


class DeploymentList(ListResource):

    def __init__(self, version: Version, fleet_sid: str):
        """
        Initialize the DeploymentList

        :param Version version: Version that contains the resource
        :param fleet_sid: 
        
        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentList
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'fleet_sid': fleet_sid,  }
        self._uri = '/Fleets/${fleet_sid}/Deployments'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name=values.unset, sync_service_sid=values.unset):
        """
        Create the DeploymentInstance
        :param str friendly_name: Provides a human readable descriptive text for this Deployment, up to 256 characters long.
        :param str sync_service_sid: Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment.
        
        :returns: The created DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'SyncServiceSid': sync_service_sid,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return DeploymentInstance(self._version, payload, fleet_sid=self._solution['fleet_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams DeploymentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DeploymentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of DeploymentInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return DeploymentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DeploymentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return DeploymentPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a DeploymentContext
        
        :param sid: Provides a 34 character string that uniquely identifies the requested Deployment resource.
        
        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        """
        return DeploymentContext(self._version, fleet_sid=self._solution['fleet_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a DeploymentContext
        
        :param sid: Provides a 34 character string that uniquely identifies the requested Deployment resource.
        
        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        """
        return DeploymentContext(self._version, fleet_sid=self._solution['fleet_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.DeploymentList>'










class DeploymentPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the DeploymentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentPage
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeploymentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        return DeploymentInstance(self._version, payload, fleet_sid=self._solution['fleet_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.DeploymentPage>'




class DeploymentContext(InstanceContext):

    def __init__(self, version: Version, fleet_sid: str, sid: str):
        """
        Initialize the DeploymentContext

        :param Version version: Version that contains the resource
        :param fleet_sid: :param sid: Provides a 34 character string that uniquely identifies the requested Deployment resource.

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'fleet_sid': fleet_sid,
            'sid': sid,
        }
        self._uri = '/Fleets/${fleet_sid}/Deployments/${sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the DeploymentInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri)
        
    def fetch(self):
        """
        Fetch the DeploymentInstance

        :returns: The fetched DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri)

        return DeploymentInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, sync_service_sid=values.unset):
        """
        Update the DeploymentInstance
        
        :params str friendly_name: Provides a human readable descriptive text for this Deployment, up to 64 characters long
        :params str sync_service_sid: Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment.

        :returns: The updated DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'SyncServiceSid': sync_service_sid,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data)

        return DeploymentInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.DeploymentContext {}>'.format(context)

class DeploymentInstance(InstanceResource):

    def __init__(self, version, payload, fleet_sid: str, sid: str=None):
        """
        Initialize the DeploymentInstance
        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'url': payload.get('url'),
            'friendly_name': payload.get('friendly_name'),
            'fleet_sid': payload.get('fleet_sid'),
            'account_sid': payload.get('account_sid'),
            'sync_service_sid': payload.get('sync_service_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
        }

        self._context = None
        self._solution = { 'fleet_sid': fleet_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DeploymentContext for this DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        """
        if self._context is None:
            self._context = DeploymentContext(self._version, fleet_sid=self._solution['fleet_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: Contains a 34 character string that uniquely identifies this Deployment resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def url(self):
        """
        :returns: Contains an absolute URL for this Deployment resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def friendly_name(self):
        """
        :returns: Contains a human readable descriptive text for this Deployment, up to 64 characters long
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def fleet_sid(self):
        """
        :returns: Specifies the unique string identifier of the Fleet that the given Deployment belongs to.
        :rtype: str
        """
        return self._properties['fleet_sid']
    
    @property
    def account_sid(self):
        """
        :returns: Specifies the unique string identifier of the Account responsible for this Deployment.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def sync_service_sid(self):
        """
        :returns: Specifies the unique string identifier of the Twilio Sync service instance linked to and accessible by this Deployment.
        :rtype: str
        """
        return self._properties['sync_service_sid']
    
    @property
    def date_created(self):
        """
        :returns: Specifies the date this Deployment was created, given in UTC ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: Specifies the date this Deployment was last updated, given in UTC ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    def delete(self):
        """
        Deletes the DeploymentInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the DeploymentInstance

        :returns: The fetched DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, sync_service_sid=values.unset):
        """
        Update the DeploymentInstance
        
        :params str friendly_name: Provides a human readable descriptive text for this Deployment, up to 64 characters long
        :params str sync_service_sid: Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment.

        :returns: The updated DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        return self._proxy.update(friendly_name=friendly_name, sync_service_sid=sync_service_sid, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.DeploymentInstance {}>'.format(context)


