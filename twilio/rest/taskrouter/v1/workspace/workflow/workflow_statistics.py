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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class WorkflowStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str, workflow_sid: str):
        """
        Initialize the WorkflowStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Workflow to fetch.
        :param workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.
        
        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'workflow_sid': workflow_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a WorkflowStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsContext
        """
        return WorkflowStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'], workflow_sid=self._solution['workflow_sid'])

    def __call__(self):
        """
        Constructs a WorkflowStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsContext
        """
        return WorkflowStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'], workflow_sid=self._solution['workflow_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowStatisticsList>'

class WorkflowStatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str, workflow_sid: str):
        """
        Initialize the WorkflowStatisticsInstance
        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'cumulative': payload.get('cumulative'),
            'realtime': payload.get('realtime'),
            'workflow_sid': payload.get('workflow_sid'),
            'workspace_sid': payload.get('workspace_sid'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'workspace_sid': workspace_sid, 'workflow_sid': workflow_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WorkflowStatisticsContext for this WorkflowStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsContext
        """
        if self._context is None:
            self._context = WorkflowStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'], workflow_sid=self._solution['workflow_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Workflow resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def cumulative(self):
        """
        :returns: An object that contains the cumulative statistics for the Workflow.
        :rtype: dict
        """
        return self._properties['cumulative']
    
    @property
    def realtime(self):
        """
        :returns: An object that contains the real-time statistics for the Workflow.
        :rtype: dict
        """
        return self._properties['realtime']
    
    @property
    def workflow_sid(self):
        """
        :returns: Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.
        :rtype: str
        """
        return self._properties['workflow_sid']
    
    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the Workflow.
        :rtype: str
        """
        return self._properties['workspace_sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Workflow statistics resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self, minutes=values.unset, start_date=values.unset, end_date=values.unset, task_channel=values.unset, split_by_wait_time=values.unset):
        """
        Fetch the WorkflowStatisticsInstance
        
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :params str task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :params str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.

        :returns: The fetched WorkflowStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsInstance
        """
        return self._proxy.fetch(minutes=minutes, start_date=start_date, end_date=end_date, task_channel=task_channel, split_by_wait_time=split_by_wait_time, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkflowStatisticsInstance {}>'.format(context)

class WorkflowStatisticsContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str, workflow_sid: str):
        """
        Initialize the WorkflowStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Workflow to fetch.:param workflow_sid: Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
            'workflow_sid': workflow_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/Statistics'.format(**self._solution)
        
    
    def fetch(self, minutes=values.unset, start_date=values.unset, end_date=values.unset, task_channel=values.unset, split_by_wait_time=values.unset):
        """
        Fetch the WorkflowStatisticsInstance
        
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :params str task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :params str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.

        :returns: The fetched WorkflowStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics.WorkflowStatisticsInstance
        """
        
        data = values.of({ 
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'EndDate': serialize.iso8601_datetime(end_date),
            'TaskChannel': task_channel,
            'SplitByWaitTime': split_by_wait_time,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return WorkflowStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            workflow_sid=self._solution['workflow_sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkflowStatisticsContext {}>'.format(context)


