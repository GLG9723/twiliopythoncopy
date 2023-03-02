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


class AssetVersionList(ListResource):

    def __init__(self, version: Version, service_sid: str, asset_sid: str):
        """
        Initialize the AssetVersionList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Asset Version resource from.
        :param asset_sid: The SID of the Asset resource that is the parent of the Asset Version resources to read.
        
        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionList
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'asset_sid': asset_sid,  }
        self._uri = '/Services/{service_sid}/Assets/{asset_sid}/Versions'.format(**self._solution)
        
        
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams AssetVersionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AssetVersionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AssetVersionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AssetVersionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AssetVersionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AssetVersionPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a AssetVersionContext
        
        :param sid: The SID of the Asset Version resource to fetch.
        
        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        """
        return AssetVersionContext(self._version, service_sid=self._solution['service_sid'], asset_sid=self._solution['asset_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a AssetVersionContext
        
        :param sid: The SID of the Asset Version resource to fetch.
        
        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        """
        return AssetVersionContext(self._version, service_sid=self._solution['service_sid'], asset_sid=self._solution['asset_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.AssetVersionList>'




class AssetVersionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AssetVersionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionPage
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AssetVersionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        """
        return AssetVersionInstance(self._version, payload, service_sid=self._solution['service_sid'], asset_sid=self._solution['asset_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.AssetVersionPage>'




class AssetVersionContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, asset_sid: str, sid: str):
        """
        Initialize the AssetVersionContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Asset Version resource from.:param asset_sid: The SID of the Asset resource that is the parent of the Asset Version resource to fetch.:param sid: The SID of the Asset Version resource to fetch.

        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'asset_sid': asset_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Assets/{asset_sid}/Versions/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the AssetVersionInstance
        

        :returns: The fetched AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AssetVersionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            asset_sid=self._solution['asset_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.AssetVersionContext {}>'.format(context)

class AssetVersionInstance(InstanceResource):

    class AssetVersionVisibility(object):
        PUBLIC = "public"
        PRIVATE = "private"
        PROTECTED = "protected"

    def __init__(self, version, payload, service_sid: str, asset_sid: str, sid: str=None):
        """
        Initialize the AssetVersionInstance
        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'asset_sid': payload.get('asset_sid'),
            'path': payload.get('path'),
            'visibility': payload.get('visibility'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'asset_sid': asset_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssetVersionContext for this AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        """
        if self._context is None:
            self._context = AssetVersionContext(self._version, service_sid=self._solution['service_sid'], asset_sid=self._solution['asset_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Asset Version resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Asset Version resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the Asset Version resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def asset_sid(self):
        """
        :returns: The SID of the Asset resource that is the parent of the Asset Version.
        :rtype: str
        """
        return self._properties['asset_sid']
    
    @property
    def path(self):
        """
        :returns: The URL-friendly string by which the Asset Version can be referenced. It can be a maximum of 255 characters. All paths begin with a forward slash ('/'). If an Asset Version creation request is submitted with a path not containing a leading slash, the path will automatically be prepended with one.
        :rtype: str
        """
        return self._properties['path']
    
    @property
    def visibility(self):
        """
        :returns: 
        :rtype: AssetVersionVisibility
        """
        return self._properties['visibility']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the Asset Version resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Asset Version resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the AssetVersionInstance
        

        :returns: The fetched AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.AssetVersionInstance {}>'.format(context)


