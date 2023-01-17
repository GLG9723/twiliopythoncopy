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




class WorkspaceRealTimeStatisticsContext(InstanceContext):
    def __init__(self, version: V1, workspace_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/RealTimeStatistics'
        
    
    def fetch(self, task_channel):
        
        """
        Fetch the WorkspaceRealTimeStatisticsInstance

        :returns: The fetched WorkspaceRealTimeStatisticsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return WorkspaceRealTimeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.WorkspaceRealTimeStatisticsContext>'



class WorkspaceRealTimeStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'activity_statistics' : payload.get('activity_statistics'),
            'longest_task_waiting_age' : payload.get('longest_task_waiting_age'),
            'longest_task_waiting_sid' : payload.get('longest_task_waiting_sid'),
            'tasks_by_priority' : payload.get('tasks_by_priority'),
            'tasks_by_status' : payload.get('tasks_by_status'),
            'total_tasks' : payload.get('total_tasks'),
            'total_workers' : payload.get('total_workers'),
            'workspace_sid' : payload.get('workspace_sid'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WorkspaceRealTimeStatisticsContext(
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
        return '<Twilio.Api.V1.WorkspaceRealTimeStatisticsInstance {}>'.format(context)



class WorkspaceRealTimeStatisticsListInstance(ListResource):
    def __init__(self, version: V1, workspace_sid: str):
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
        return '<Twilio.Api.V1.WorkspaceRealTimeStatisticsListInstance>'

