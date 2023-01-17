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


class TaskQueueStatisticsContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str, task_queue_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/TaskQueues/${task_queue_sid}/Statistics'
        
    
    def fetch(self, end_date, minutes, start_date, task_channel, split_by_wait_time):
        
        """
        Fetch the TaskQueueStatisticsInstance

        :returns: The fetched TaskQueueStatisticsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TaskQueueStatisticsInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], task_queue_sid=self._solution['task_queue_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TaskQueueStatisticsContext>'



class TaskQueueStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str, task_queue_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'cumulative' : payload.get('cumulative'),
            'realtime' : payload.get('realtime'),
            'task_queue_sid' : payload.get('task_queue_sid'),
            'workspace_sid' : payload.get('workspace_sid'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid'],'task_queue_sid': task_queue_sid or self._properties['task_queue_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TaskQueueStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],task_queue_sid=self._solution['task_queue_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.TaskQueueStatisticsInstance {}>'.format(context)



class TaskQueueStatisticsListInstance(ListResource):
    def __init__(self, version: Version, workspace_sid: str, task_queue_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid,  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TaskQueueStatisticsListInstance>'

