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
from twilio.base.page import Page
from twilio.rest.taskrouter.v1.workspace.activities import ActivityList
from twilio.rest.taskrouter.v1.workspace.events import EventList
from twilio.rest.taskrouter.v1.workspace.tasks import TaskList
from twilio.rest.taskrouter.v1.workspace.task_channels import TaskChannelList
from twilio.rest.taskrouter.v1.workspace.task_queues import TaskQueueList
from twilio.rest.taskrouter.v1.workspace.workers import WorkerList
from twilio.rest.taskrouter.v1.workspace.workflows import WorkflowList
from twilio.rest.taskrouter.v1.workspace.cumulative_statistics import WorkspaceCumulativeStatisticsList
from twilio.rest.taskrouter.v1.workspace.real_time_statistics import WorkspaceRealTimeStatisticsList
from twilio.rest.taskrouter.v1.workspace.statistics import WorkspaceStatisticsList


class WorkspaceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the WorkspaceList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.taskrouter.v1.workspace.WorkspaceList
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Workspaces'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, event_callback_url=values.unset, events_filter=values.unset, multi_task_enabled=values.unset, template=values.unset, prioritize_queue_order=values.unset):
        """
        Create the WorkspaceInstance
        :param str friendly_name: A descriptive string that you create to describe the Workspace resource. It can be up to 64 characters long. For example: `Customer Support` or `2014 Election Campaign`.
        :param str event_callback_url: The URL we should call when an event occurs. If provided, the Workspace will publish events to this URL, for example, to collect data for reporting. See [Workspace Events](https://www.twilio.com/docs/taskrouter/api/event) for more information. This parameter supports Twilio's [Webhooks (HTTP callbacks) Connection Overrides](https://www.twilio.com/docs/usage/webhooks/webhooks-connection-overrides).
        :param str events_filter: The list of Workspace events for which to call event_callback_url. For example, if `EventsFilter=task.created, task.canceled, worker.activity.update`, then TaskRouter will call event_callback_url only when a task is created, canceled, or a Worker activity is updated.
        :param bool multi_task_enabled: Whether to enable multi-tasking. Can be: `true` to enable multi-tasking, or `false` to disable it. However, all workspaces should be created as multi-tasking. The default is `true`. Multi-tasking allows Workers to handle multiple Tasks simultaneously. When enabled (`true`), each Worker can receive parallel reservations up to the per-channel maximums defined in the Workers section. In single-tasking mode (legacy mode), each Worker will only receive a new reservation when the previous task is completed. Learn more at [Multitasking](https://www.twilio.com/docs/taskrouter/multitasking).
        :param str template: An available template name. Can be: `NONE` or `FIFO` and the default is `NONE`. Pre-configures the Workspace with the Workflow and Activities specified in the template. `NONE` will create a Workspace with only a set of default activities. `FIFO` will configure TaskRouter with a set of default activities and a single TaskQueue for first-in, first-out distribution, which can be useful when you are getting started with TaskRouter.
        :param WorkspaceQueueOrder prioritize_queue_order: 
        
        :returns: The created WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'EventCallbackUrl': event_callback_url,
            'EventsFilter': events_filter,
            'MultiTaskEnabled': multi_task_enabled,
            'Template': template,
            'PrioritizeQueueOrder': prioritize_queue_order,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return WorkspaceInstance(self._version, payload)
    
    
    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams WorkspaceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str friendly_name: The `friendly_name` of the Workspace resources to read. For example `Customer Support` or `2014 Election Campaign`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.WorkspaceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            friendly_name=friendly_name,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists WorkspaceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str friendly_name: The `friendly_name` of the Workspace resources to read. For example `Customer Support` or `2014 Election Campaign`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.WorkspaceInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of WorkspaceInstance records from the API.
        Request is executed immediately
        
        :param str friendly_name: The `friendly_name` of the Workspace resources to read. For example `Customer Support` or `2014 Election Campaign`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspacePage
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return WorkspacePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WorkspaceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspacePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return WorkspacePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a WorkspaceContext
        
        :param sid: The SID of the Workspace resource to update.
        
        :returns: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        """
        return WorkspaceContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a WorkspaceContext
        
        :param sid: The SID of the Workspace resource to update.
        
        :returns: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        """
        return WorkspaceContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspaceList>'










class WorkspacePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the WorkspacePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.WorkspacePage
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspacePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkspaceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        """
        return WorkspaceInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspacePage>'





class WorkspaceContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Workspaces/${sid}'
        
        self._activities = None
        self._events = None
        self._tasks = None
        self._task_channels = None
        self._task_queues = None
        self._workers = None
        self._workflows = None
        self._cumulative_statistics = None
        self._real_time_statistics = None
        self._statistics = None
    
    def delete(self):
        
        

        """
        Deletes the WorkspaceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the WorkspaceInstance

        :returns: The fetched WorkspaceInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WorkspaceInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, default_activity_sid, event_callback_url, events_filter, friendly_name, multi_task_enabled, timeout_activity_sid, prioritize_queue_order):
        data = values.of({
            'default_activity_sid': default_activity_sid,'event_callback_url': event_callback_url,'events_filter': events_filter,'friendly_name': friendly_name,'multi_task_enabled': multi_task_enabled,'timeout_activity_sid': timeout_activity_sid,'prioritize_queue_order': prioritize_queue_order,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return WorkspaceInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspaceContext>'



class WorkspaceInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'default_activity_name' : payload.get('default_activity_name'),
            'default_activity_sid' : payload.get('default_activity_sid'),
            'event_callback_url' : payload.get('event_callback_url'),
            'events_filter' : payload.get('events_filter'),
            'friendly_name' : payload.get('friendly_name'),
            'multi_task_enabled' : payload.get('multi_task_enabled'),
            'sid' : payload.get('sid'),
            'timeout_activity_name' : payload.get('timeout_activity_name'),
            'timeout_activity_sid' : payload.get('timeout_activity_sid'),
            'prioritize_queue_order' : payload.get('prioritize_queue_order'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = WorkspaceContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def activities(self):
        return self._proxy.activities
    @property
    def events(self):
        return self._proxy.events
    @property
    def tasks(self):
        return self._proxy.tasks
    @property
    def task_channels(self):
        return self._proxy.task_channels
    @property
    def task_queues(self):
        return self._proxy.task_queues
    @property
    def workers(self):
        return self._proxy.workers
    @property
    def workflows(self):
        return self._proxy.workflows
    @property
    def cumulative_statistics(self):
        return self._proxy.cumulative_statistics
    @property
    def real_time_statistics(self):
        return self._proxy.real_time_statistics
    @property
    def statistics(self):
        return self._proxy.statistics
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceInstance {}>'.format(context)



