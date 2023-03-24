r"""
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


from typing import Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class BuildStatusInstance(InstanceResource):

    class Status(object):
        BUILDING = "building"
        COMPLETED = "completed"
        FAILED = "failed"

    def __init__(self, version, payload, service_sid: str, sid: str):
        """
        Initialize the BuildStatusInstance
        """
        super().__init__(version)

        
        self._sid: Optional[str] = payload.get('sid')
        self._account_sid: Optional[str] = payload.get('account_sid')
        self._service_sid: Optional[str] = payload.get('service_sid')
        self._status: Optional["BuildStatusInstance.Status"] = payload.get('status')
        self._url: Optional[str] = payload.get('url')

        self._solution = { 'service_sid': service_sid, 'sid': sid,  }
        self._context: Optional[BuildStatusContext] = None

    @property
    def _proxy(self) -> "BuildStatusContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BuildStatusContext for this BuildStatusInstance
        """
        if self._context is None:
            self._context = BuildStatusContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that we created to identify the Build resource.
        """
        return self._sid
    
    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Build resource.
        """
        return self._account_sid
    
    @property
    def service_sid(self) -> Optional[str]:
        """
        :returns: The SID of the Service that the Build resource is associated with.
        """
        return self._service_sid
    
    @property
    def status(self) -> Optional["BuildStatusInstance.Status"]:
        
        return self._status
    
    @property
    def url(self) -> Optional[str]:
        """
        :returns: The absolute URL of the Build Status resource.
        """
        return self._url
    
    
    def fetch(self) -> "BuildStatusInstance":
        """
        Fetch the BuildStatusInstance
        

        :returns: The fetched BuildStatusInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "BuildStatusInstance":
        """
        Asynchronous coroutine to fetch the BuildStatusInstance
        

        :returns: The fetched BuildStatusInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildStatusInstance {}>'.format(context)

class BuildStatusContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the BuildStatusContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Build resource from.
        :param sid: The SID of the Build resource to fetch.
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Builds/{sid}/Status'.format(**self._solution)
        
    
    
    def fetch(self) -> BuildStatusInstance:
        """
        Fetch the BuildStatusInstance
        

        :returns: The fetched BuildStatusInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BuildStatusInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> BuildStatusInstance:
        """
        Asynchronous coroutine to fetch the BuildStatusInstance
        

        :returns: The fetched BuildStatusInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return BuildStatusInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildStatusContext {}>'.format(context)



class BuildStatusList(ListResource):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the BuildStatusList

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Build resource from.
        :param sid: The SID of the Build resource to fetch.
        
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 'service_sid': service_sid, 'sid': sid,  }
        
        
        

    def get(self) -> BuildStatusContext:
        """
        Constructs a BuildStatusContext
        
        """
        return BuildStatusContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'])

    def __call__(self) -> BuildStatusContext:
        """
        Constructs a BuildStatusContext
        
        """
        return BuildStatusContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Serverless.V1.BuildStatusList>'

