"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
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

# 


class WorkersStatisticsContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Workers/Statistics'
        
    
    def fetch(self, minutes, start_date, end_date, task_queue_sid, task_queue_name, friendly_name, task_channel):
        
        """
        Fetch the WorkersStatisticsInstance

        :returns: The fetched WorkersStatisticsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WorkersStatisticsInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WorkersStatisticsContext>'



class WorkersStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str):
        super().__init__(version)
        self._properties = { 
            'realtime' : payload.get('realtime'),
            'cumulative' : payload.get('cumulative'),
            'account_sid' : payload.get('account_sid'),
            'workspace_sid' : payload.get('workspace_sid'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WorkersStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.WorkersStatisticsInstance {}>'.format(context)



class WorkersStatisticsList(ListResource):
    def __init__(self, version: Version, workspace_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        self._uri = ''
        


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WorkersStatisticsList>'

