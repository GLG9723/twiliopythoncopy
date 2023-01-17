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

from twilio.base.page import Page






class TaskQueuesStatisticsListInstance(ListResource):
    def __init__(self, version: V1, workspace_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/TaskQueues/Statistics'
        
    
    def page(self, end_date, friendly_name, minutes, start_date, task_channel, split_by_wait_time, page_size):
        
        data = values.of({
            'end_date': end_date,'friendly_name': friendly_name,'minutes': minutes,'start_date': start_date,'task_channel': task_channel,'split_by_wait_time': split_by_wait_time,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return TaskQueuesStatisticsPage(self._version, payload, workspace_sid=self._solution['workspace_sid'], )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TaskQueuesStatisticsListInstance>'

