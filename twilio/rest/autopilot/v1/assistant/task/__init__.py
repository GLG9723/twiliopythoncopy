"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
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
from twilio.rest.autopilot.v1.assistant.task.field import FieldList
from twilio.rest.autopilot.v1.assistant.task.sample import SampleList
from twilio.rest.autopilot.v1.assistant.task.task_actions import TaskActionsList
from twilio.rest.autopilot.v1.assistant.task.task_statistics import TaskStatisticsList


class TaskList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the TaskList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
        
        :returns: twilio.rest.autopilot.v1.assistant.task.TaskList
        :rtype: twilio.rest.autopilot.v1.assistant.task.TaskList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid,  }
        self._uri = '/Assistants/${assistant_sid}/Tasks'.format(**self._solution)
        
        
    
    
    
    
    def create(self, unique_name, friendly_name=values.unset, actions=values.unset, actions_url=values.unset):
        """
        Create the TaskInstance
        :param str unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the `sid` in the URL path to address the resource. This value must be unique and 64 characters or less in length.
        :param str friendly_name: A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
        :param object actions: The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task. It is optional and not unique.
        :param str actions_url: The URL from which the Assistant can fetch actions.
        
        :returns: The created TaskInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.TaskInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
            'Actions': serialize.object(actions),
            'ActionsUrl': actions_url,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return TaskInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams TaskInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.task.TaskInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists TaskInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.task.TaskInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of TaskInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TaskInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.TaskPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return TaskPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TaskInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TaskInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.TaskPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return TaskPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a TaskContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Task resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.task.TaskContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.TaskContext
        """
        return TaskContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a TaskContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Task resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.task.TaskContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.TaskContext
        """
        return TaskContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.TaskList>'










class TaskPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the TaskPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.autopilot.v1.assistant.task.TaskPage
        :rtype: twilio.rest.autopilot.v1.assistant.task.TaskPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TaskInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.task.TaskInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.TaskInstance
        """
        return TaskInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.TaskPage>'





class TaskContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'sid': sid,  }
        self._uri = '/Assistants/${assistant_sid}/Tasks/${sid}'
        
        self._fields = None
        self._samples = None
        self._task_actions = None
        self._statistics = None
    
    def delete(self):
        
        

        """
        Deletes the TaskInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the TaskInstance

        :returns: The fetched TaskInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TaskInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, friendly_name, unique_name, actions, actions_url):
        data = values.of({
            'friendly_name': friendly_name,'unique_name': unique_name,'actions': actions,'actions_url': actions_url,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return TaskInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.TaskContext>'



class TaskInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'friendly_name' : payload.get('friendly_name'),
            'links' : payload.get('links'),
            'assistant_sid' : payload.get('assistant_sid'),
            'sid' : payload.get('sid'),
            'unique_name' : payload.get('unique_name'),
            'actions_url' : payload.get('actions_url'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'assistant_sid': assistant_sid or self._properties['assistant_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TaskContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def fields(self):
        return self._proxy.fields
    @property
    def samples(self):
        return self._proxy.samples
    @property
    def task_actions(self):
        return self._proxy.task_actions
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
        return '<Twilio.Autopilot.V1.TaskInstance {}>'.format(context)



