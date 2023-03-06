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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CertificateList(ListResource):

    def __init__(self, version: Version, fleet_sid: str):
        """
        Initialize the CertificateList

        :param Version version: Version that contains the resource
        :param fleet_sid: 
        
        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateList
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'fleet_sid': fleet_sid,  }
        self._uri = '/Fleets/{fleet_sid}/Certificates'.format(**self._solution)
        
        
    
    
    
    
    def create(self, certificate_data, friendly_name=values.unset, device_sid=values.unset):
        """
        Create the CertificateInstance

        :param str certificate_data: Provides a URL encoded representation of the public certificate in PEM format.
        :param str friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
        :param str device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.
        
        :returns: The created CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        data = values.of({ 
            'CertificateData': certificate_data,
            'FriendlyName': friendly_name,
            'DeviceSid': device_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return CertificateInstance(self._version, payload, fleet_sid=self._solution['fleet_sid'])
    
    
    def stream(self, device_sid=values.unset, limit=None, page_size=None):
        """
        Streams CertificateInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str device_sid: Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            device_sid=device_sid,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, device_sid=values.unset, limit=None, page_size=None):
        """
        Lists CertificateInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str device_sid: Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance]
        """
        return list(self.stream(
            device_sid=device_sid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, device_sid=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CertificateInstance records from the API.
        Request is executed immediately
        
        :param str device_sid: Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificatePage
        """
        data = values.of({ 
            'DeviceSid': device_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CertificatePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CertificateInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificatePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CertificatePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a CertificateContext
        
        :param sid: Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
        
        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        """
        return CertificateContext(self._version, fleet_sid=self._solution['fleet_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a CertificateContext
        
        :param sid: Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
        
        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        """
        return CertificateContext(self._version, fleet_sid=self._solution['fleet_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.CertificateList>'










class CertificatePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CertificatePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificatePage
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificatePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CertificateInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        return CertificateInstance(self._version, payload, fleet_sid=self._solution['fleet_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.CertificatePage>'




class CertificateContext(InstanceContext):

    def __init__(self, version: Version, fleet_sid: str, sid: str):
        """
        Initialize the CertificateContext

        :param Version version: Version that contains the resource
        :param fleet_sid: :param sid: Provides a 34 character string that uniquely identifies the requested Certificate credential resource.

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'fleet_sid': fleet_sid,
            'sid': sid,
        }
        self._uri = '/Fleets/{fleet_sid}/Certificates/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the CertificateInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the CertificateInstance
        

        :returns: The fetched CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CertificateInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, device_sid=values.unset):
        """
        Update the CertificateInstance
        
        :params str friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
        :params str device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.

        :returns: The updated CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'DeviceSid': device_sid,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return CertificateInstance(
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
        return '<Twilio.Preview.DeployedDevices.CertificateContext {}>'.format(context)

class CertificateInstance(InstanceResource):

    def __init__(self, version, payload, fleet_sid: str, sid: str=None):
        """
        Initialize the CertificateInstance
        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'url': payload.get('url'),
            'friendly_name': payload.get('friendly_name'),
            'fleet_sid': payload.get('fleet_sid'),
            'account_sid': payload.get('account_sid'),
            'device_sid': payload.get('device_sid'),
            'thumbprint': payload.get('thumbprint'),
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

        :returns: CertificateContext for this CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        """
        if self._context is None:
            self._context = CertificateContext(self._version, fleet_sid=self._solution['fleet_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: Contains a 34 character string that uniquely identifies this Certificate credential resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def url(self):
        """
        :returns: Contains an absolute URL for this Certificate credential resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def friendly_name(self):
        """
        :returns: Contains a human readable descriptive text for this Certificate credential, up to 256 characters long.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def fleet_sid(self):
        """
        :returns: Specifies the unique string identifier of the Fleet that the given Certificate credential belongs to.
        :rtype: str
        """
        return self._properties['fleet_sid']
    
    @property
    def account_sid(self):
        """
        :returns: Specifies the unique string identifier of the Account responsible for this Certificate credential.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def device_sid(self):
        """
        :returns: Specifies the unique string identifier of a Device authenticated with this Certificate credential.
        :rtype: str
        """
        return self._properties['device_sid']
    
    @property
    def thumbprint(self):
        """
        :returns: Contains a unique hash of the payload of this Certificate credential, used to authenticate the Device.
        :rtype: str
        """
        return self._properties['thumbprint']
    
    @property
    def date_created(self):
        """
        :returns: Specifies the date this Certificate credential was created, given in UTC ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: Specifies the date this Certificate credential was last updated, given in UTC ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    def delete(self):
        """
        Deletes the CertificateInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the CertificateInstance
        

        :returns: The fetched CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, device_sid=values.unset):
        """
        Update the CertificateInstance
        
        :params str friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
        :params str device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.

        :returns: The updated CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        return self._proxy.update(friendly_name=friendly_name, device_sid=device_sid, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.CertificateInstance {}>'.format(context)


