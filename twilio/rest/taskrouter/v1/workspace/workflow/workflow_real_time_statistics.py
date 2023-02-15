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



class WorkflowRealTimeStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str, workflow_sid: str):
        """
        Initialize the WorkflowRealTimeStatisticsList
        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Workflow to fetch.
        :param workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.
        
        :returns: twilio.taskrouter.v1.workflow_real_time_statistics..WorkflowRealTimeStatisticsList
        :rtype: twilio.taskrouter.v1.workflow_real_time_statistics..WorkflowRealTimeStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'workflow_sid': workflow_sid,  }
        self._uri = ''.format(**self._solution)


    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowRealTimeStatisticsList>'


class WorkflowRealTimeStatisticsContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str, workflow_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'workflow_sid': workflow_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Workflows/${workflow_sid}/RealTimeStatistics'
        
    
    def fetch(self, task_channel):
        
        """
        Fetch the WorkflowRealTimeStatisticsInstance

        :returns: The fetched WorkflowRealTimeStatisticsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WorkflowRealTimeStatisticsInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], workflow_sid=self._solution['workflow_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowRealTimeStatisticsContext>'



class WorkflowRealTimeStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str, workflow_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'longest_task_waiting_age' : payload.get('longest_task_waiting_age'),
            'longest_task_waiting_sid' : payload.get('longest_task_waiting_sid'),
            'tasks_by_priority' : payload.get('tasks_by_priority'),
            'tasks_by_status' : payload.get('tasks_by_status'),
            'total_tasks' : payload.get('total_tasks'),
            'workflow_sid' : payload.get('workflow_sid'),
            'workspace_sid' : payload.get('workspace_sid'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid'],'workflow_sid': workflow_sid or self._properties['workflow_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WorkflowRealTimeStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],workflow_sid=self._solution['workflow_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkflowRealTimeStatisticsInstance {}>'.format(context)



