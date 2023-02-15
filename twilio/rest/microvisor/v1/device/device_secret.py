"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Microvisor
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


class DeviceSecretList(ListResource):

    def __init__(self, version: Version, device_sid: str):
        """
        Initialize the DeviceSecretList
        :param Version version: Version that contains the resource
        :param device_sid: A 34-character string that uniquely identifies the Device.
        
        :returns: twilio.microvisor.v1.device_secret..DeviceSecretList
        :rtype: twilio.microvisor.v1.device_secret..DeviceSecretList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'device_sid': device_sid,  }
        self._uri = '/Devices/${device_sid}/Secrets'.format(**self._solution)


    
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams DeviceSecretInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.microvisor.v1.device_secret.DeviceSecretInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DeviceSecretInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.microvisor.v1.device_secret.DeviceSecretInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of DeviceSecretInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DeviceSecretInstance
        :rtype: twilio.rest.microvisor.v1.device_secret.DeviceSecretPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return DeviceSecretPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DeviceSecretInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeviceSecretInstance
        :rtype: twilio.rest.microvisor.v1.device_secret.DeviceSecretPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return DeviceSecretPage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.DeviceSecretList>'








class DeviceSecretPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the DeviceSecretPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.microvisor.v1.device_secret.DeviceSecretPage
        :rtype: twilio.rest.microvisor.v1.device_secret.DeviceSecretPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeviceSecretInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.microvisor.v1.device_secret.DeviceSecretInstance
        :rtype: twilio.rest.microvisor.v1.device_secret.DeviceSecretInstance
        """
        return DeviceSecretInstance(self._version, payload, device_sid=self._solution['device_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.DeviceSecretPage>'





class DeviceSecretContext(InstanceContext):
    def __init__(self, version: Version, device_sid: str, key: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'device_sid': device_sid, 'key': key,  }
        self._uri = '/Devices/${device_sid}/Secrets/${key}'
        
    
    def delete(self):
        
        

        """
        Deletes the DeviceSecretInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the DeviceSecretInstance

        :returns: The fetched DeviceSecretInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DeviceSecretInstance(self._version, payload, device_sid=self._solution['device_sid'], key=self._solution['key'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.DeviceSecretContext>'



class DeviceSecretInstance(InstanceResource):
    def __init__(self, version, payload, device_sid: str, key: str):
        super().__init__(version)
        self._properties = { 
            'device_sid' : payload.get('device_sid'),
            'key' : payload.get('key'),
            'date_rotated' : payload.get('date_rotated'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'device_sid': device_sid or self._properties['device_sid'],'key': key or self._properties['key'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = DeviceSecretContext(
                self._version,
                device_sid=self._solution['device_sid'],key=self._solution['key'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Microvisor.V1.DeviceSecretInstance {}>'.format(context)



