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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class BuildStatusList(ListResource):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the BuildStatusList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Build resource from.
        :param sid: The SID of the Build resource to fetch.
        
        :returns: twilio.rest.serverless.v1.service.build.build_status.BuildStatusList
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'sid': sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a BuildStatusContext
        
        :returns: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        """
        return BuildStatusContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'])

    def __call__(self):
        """
        Constructs a BuildStatusContext
        
        :returns: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        """
        return BuildStatusContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.BuildStatusList>'

class BuildStatusContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the BuildStatusContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Build resource from.
        :param sid: The SID of the Build resource to fetch.

        :returns: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Builds/{sid}/Status'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the BuildStatusInstance
        

        :returns: The fetched BuildStatusInstance
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BuildStatusInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildStatusContext {}>'.format(context)

class BuildStatusInstance(InstanceResource):

    class Status(object):
        BUILDING = "building"
        COMPLETED = "completed"
        FAILED = "failed"

    def __init__(self, version, payload, service_sid: str, sid: str):
        """
        Initialize the BuildStatusInstance
        :returns: twilio.rest.serverless.v1.service.build.build_status.BuildStatusInstance
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'status': payload.get('status'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BuildStatusContext for this BuildStatusInstance
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusContext
        """
        if self._context is None:
            self._context = BuildStatusContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Build resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Build resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the Build resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: BuildStatusInstance.Status
        """
        return self._properties['status']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Build Status resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the BuildStatusInstance
        

        :returns: The fetched BuildStatusInstance
        :rtype: twilio.rest.serverless.v1.service.build.build_status.BuildStatusInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildStatusInstance {}>'.format(context)


