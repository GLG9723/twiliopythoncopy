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
from twilio.rest.preview.deployed_devices.fleet.certificates import CertificateList
from twilio.rest.preview.deployed_devices.fleet.deployments import DeploymentList
from twilio.rest.preview.deployed_devices.fleet.devices import DeviceList
from twilio.rest.preview.deployed_devices.fleet.keys import KeyList


class FleetList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the FleetList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.preview.deployed_devices.fleet.FleetList
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Fleets'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name=values.unset):
        """
        Create the FleetInstance
        :param str friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
        
        :returns: The created FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return FleetInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams FleetInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.FleetInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FleetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.FleetInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of FleetInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return FleetPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FleetInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return FleetPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a FleetContext
        
        :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.
        
        :returns: twilio.rest.preview.deployed_devices.fleet.FleetContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetContext
        """
        return FleetContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a FleetContext
        
        :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.
        
        :returns: twilio.rest.preview.deployed_devices.fleet.FleetContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetContext
        """
        return FleetContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.FleetList>'










class FleetPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FleetPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetPage
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FleetInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        return FleetInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.FleetPage>'





class FleetContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Fleets/${sid}'
        
        self._certificates = None
        self._deployments = None
        self._devices = None
        self._keys = None
    
    def delete(self):
        
        

        """
        Deletes the FleetInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the FleetInstance

        :returns: The fetched FleetInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FleetInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, friendly_name, default_deployment_sid):
        data = values.of({
            'friendly_name': friendly_name,'default_deployment_sid': default_deployment_sid,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return FleetInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.FleetContext>'



class FleetInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'url' : payload.get('url'),
            'unique_name' : payload.get('unique_name'),
            'friendly_name' : payload.get('friendly_name'),
            'account_sid' : payload.get('account_sid'),
            'default_deployment_sid' : payload.get('default_deployment_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = FleetContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def certificates(self):
        return self._proxy.certificates
    @property
    def deployments(self):
        return self._proxy.deployments
    @property
    def devices(self):
        return self._proxy.devices
    @property
    def keys(self):
        return self._proxy.keys
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.FleetInstance {}>'.format(context)



