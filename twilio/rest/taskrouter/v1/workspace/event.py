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
from twilio.base.page import Page


class EventList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the EventList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Events to read. Returns only the Events that pertain to the specified Workspace.
        
        :returns: twilio.rest.taskrouter.v1.workspace.event.EventList
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        self._uri = '/Workspaces/{workspace_sid}/Events'.format(**self._solution)
        
        
    
    
    def stream(self, end_date=values.unset, event_type=values.unset, minutes=values.unset, reservation_sid=values.unset, start_date=values.unset, task_queue_sid=values.unset, task_sid=values.unset, worker_sid=values.unset, workflow_sid=values.unset, task_channel=values.unset, sid=values.unset, limit=None, page_size=None):
        """
        Streams EventInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param datetime end_date: Only include Events that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param str event_type: The type of Events to read. Returns only Events of the type specified.
        :param int minutes: The period of events to read in minutes. Returns only Events that occurred since this many minutes in the past. The default is `15` minutes. Task Attributes for Events occuring more 43,200 minutes ago will be redacted.
        :param str reservation_sid: The SID of the Reservation with the Events to read. Returns only Events that pertain to the specified Reservation.
        :param datetime start_date: Only include Events from on or after this date and time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Task Attributes for Events older than 30 days will be redacted.
        :param str task_queue_sid: The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to the specified TaskQueue.
        :param str task_sid: The SID of the Task with the Events to read. Returns only the Events that pertain to the specified Task.
        :param str worker_sid: The SID of the Worker with the Events to read. Returns only the Events that pertain to the specified Worker.
        :param str workflow_sid: The SID of the Workflow with the Events to read. Returns only the Events that pertain to the specified Workflow.
        :param str task_channel: The TaskChannel with the Events to read. Returns only the Events that pertain to the specified TaskChannel.
        :param str sid: The SID of the Event resource to read.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.event.EventInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            end_date=end_date,
            event_type=event_type,
            minutes=minutes,
            reservation_sid=reservation_sid,
            start_date=start_date,
            task_queue_sid=task_queue_sid,
            task_sid=task_sid,
            worker_sid=worker_sid,
            workflow_sid=workflow_sid,
            task_channel=task_channel,
            sid=sid,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, end_date=values.unset, event_type=values.unset, minutes=values.unset, reservation_sid=values.unset, start_date=values.unset, task_queue_sid=values.unset, task_sid=values.unset, worker_sid=values.unset, workflow_sid=values.unset, task_channel=values.unset, sid=values.unset, limit=None, page_size=None):
        """
        Lists EventInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param datetime end_date: Only include Events that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param str event_type: The type of Events to read. Returns only Events of the type specified.
        :param int minutes: The period of events to read in minutes. Returns only Events that occurred since this many minutes in the past. The default is `15` minutes. Task Attributes for Events occuring more 43,200 minutes ago will be redacted.
        :param str reservation_sid: The SID of the Reservation with the Events to read. Returns only Events that pertain to the specified Reservation.
        :param datetime start_date: Only include Events from on or after this date and time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Task Attributes for Events older than 30 days will be redacted.
        :param str task_queue_sid: The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to the specified TaskQueue.
        :param str task_sid: The SID of the Task with the Events to read. Returns only the Events that pertain to the specified Task.
        :param str worker_sid: The SID of the Worker with the Events to read. Returns only the Events that pertain to the specified Worker.
        :param str workflow_sid: The SID of the Workflow with the Events to read. Returns only the Events that pertain to the specified Workflow.
        :param str task_channel: The TaskChannel with the Events to read. Returns only the Events that pertain to the specified TaskChannel.
        :param str sid: The SID of the Event resource to read.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.event.EventInstance]
        """
        return list(self.stream(
            end_date=end_date,
            event_type=event_type,
            minutes=minutes,
            reservation_sid=reservation_sid,
            start_date=start_date,
            task_queue_sid=task_queue_sid,
            task_sid=task_sid,
            worker_sid=worker_sid,
            workflow_sid=workflow_sid,
            task_channel=task_channel,
            sid=sid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, end_date=values.unset, event_type=values.unset, minutes=values.unset, reservation_sid=values.unset, start_date=values.unset, task_queue_sid=values.unset, task_sid=values.unset, worker_sid=values.unset, workflow_sid=values.unset, task_channel=values.unset, sid=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of EventInstance records from the API.
        Request is executed immediately
        
        :param datetime end_date: Only include Events that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :param str event_type: The type of Events to read. Returns only Events of the type specified.
        :param int minutes: The period of events to read in minutes. Returns only Events that occurred since this many minutes in the past. The default is `15` minutes. Task Attributes for Events occuring more 43,200 minutes ago will be redacted.
        :param str reservation_sid: The SID of the Reservation with the Events to read. Returns only Events that pertain to the specified Reservation.
        :param datetime start_date: Only include Events from on or after this date and time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Task Attributes for Events older than 30 days will be redacted.
        :param str task_queue_sid: The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to the specified TaskQueue.
        :param str task_sid: The SID of the Task with the Events to read. Returns only the Events that pertain to the specified Task.
        :param str worker_sid: The SID of the Worker with the Events to read. Returns only the Events that pertain to the specified Worker.
        :param str workflow_sid: The SID of the Workflow with the Events to read. Returns only the Events that pertain to the specified Workflow.
        :param str task_channel: The TaskChannel with the Events to read. Returns only the Events that pertain to the specified TaskChannel.
        :param str sid: The SID of the Event resource to read.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EventInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventPage
        """
        data = values.of({ 
            'EndDate': serialize.iso8601_datetime(end_date),
            'EventType': event_type,
            'Minutes': minutes,
            'ReservationSid': reservation_sid,
            'StartDate': serialize.iso8601_datetime(start_date),
            'TaskQueueSid': task_queue_sid,
            'TaskSid': task_sid,
            'WorkerSid': worker_sid,
            'WorkflowSid': workflow_sid,
            'TaskChannel': task_channel,
            'Sid': sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return EventPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EventInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EventInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return EventPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a EventContext
        
        :param sid: The SID of the Event resource to fetch.
        
        :returns: twilio.rest.taskrouter.v1.workspace.event.EventContext
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventContext
        """
        return EventContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a EventContext
        
        :param sid: The SID of the Event resource to fetch.
        
        :returns: twilio.rest.taskrouter.v1.workspace.event.EventContext
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventContext
        """
        return EventContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.EventList>'




class EventPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the EventPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.event.EventPage
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EventInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.event.EventInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventInstance
        """
        return EventInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.EventPage>'




class EventInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str, sid: str=None):
        """
        Initialize the EventInstance
        :returns: twilio.rest.taskrouter.v1.workspace.event.EventInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'actor_sid': payload.get('actor_sid'),
            'actor_type': payload.get('actor_type'),
            'actor_url': payload.get('actor_url'),
            'description': payload.get('description'),
            'event_data': payload.get('event_data'),
            'event_date': deserialize.iso8601_datetime(payload.get('event_date')),
            'event_date_ms': payload.get('event_date_ms'),
            'event_type': payload.get('event_type'),
            'resource_sid': payload.get('resource_sid'),
            'resource_type': payload.get('resource_type'),
            'resource_url': payload.get('resource_url'),
            'sid': payload.get('sid'),
            'source': payload.get('source'),
            'source_ip_address': payload.get('source_ip_address'),
            'url': payload.get('url'),
            'workspace_sid': payload.get('workspace_sid'),
        }

        self._context = None
        self._solution = { 'workspace_sid': workspace_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EventContext for this EventInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventContext
        """
        if self._context is None:
            self._context = EventContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Event resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def actor_sid(self):
        """
        :returns: The SID of the resource that triggered the event.
        :rtype: str
        """
        return self._properties['actor_sid']
    
    @property
    def actor_type(self):
        """
        :returns: The type of resource that triggered the event.
        :rtype: str
        """
        return self._properties['actor_type']
    
    @property
    def actor_url(self):
        """
        :returns: The absolute URL of the resource that triggered the event.
        :rtype: str
        """
        return self._properties['actor_url']
    
    @property
    def description(self):
        """
        :returns: A description of the event.
        :rtype: str
        """
        return self._properties['description']
    
    @property
    def event_data(self):
        """
        :returns: Data about the event. For more information, see [Event types](https://www.twilio.com/docs/taskrouter/api/event#event-types).
        :rtype: dict
        """
        return self._properties['event_data']
    
    @property
    def event_date(self):
        """
        :returns: The time the event was sent, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['event_date']
    
    @property
    def event_date_ms(self):
        """
        :returns: The time the event was sent in milliseconds.
        :rtype: int
        """
        return self._properties['event_date_ms']
    
    @property
    def event_type(self):
        """
        :returns: The identifier for the event.
        :rtype: str
        """
        return self._properties['event_type']
    
    @property
    def resource_sid(self):
        """
        :returns: The SID of the object the event is most relevant to, such as a TaskSid, ReservationSid, or a  WorkerSid.
        :rtype: str
        """
        return self._properties['resource_sid']
    
    @property
    def resource_type(self):
        """
        :returns: The type of object the event is most relevant to, such as a Task, Reservation, or a Worker).
        :rtype: str
        """
        return self._properties['resource_type']
    
    @property
    def resource_url(self):
        """
        :returns: The URL of the resource the event is most relevant to.
        :rtype: str
        """
        return self._properties['resource_url']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Event resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def source(self):
        """
        :returns: Where the Event originated.
        :rtype: str
        """
        return self._properties['source']
    
    @property
    def source_ip_address(self):
        """
        :returns: The IP from which the Event originated.
        :rtype: str
        """
        return self._properties['source_ip_address']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Event resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the Event.
        :rtype: str
        """
        return self._properties['workspace_sid']
    
    def fetch(self):
        """
        Fetch the EventInstance
        

        :returns: The fetched EventInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.EventInstance {}>'.format(context)

class EventContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str, sid: str):
        """
        Initialize the EventContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Event to fetch.:param sid: The SID of the Event resource to fetch.

        :returns: twilio.rest.taskrouter.v1.workspace.event.EventContext
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Events/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the EventInstance
        

        :returns: The fetched EventInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return EventInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.EventContext {}>'.format(context)


