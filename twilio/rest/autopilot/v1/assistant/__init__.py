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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.autopilot.v1.assistant.defaults import DefaultsList
from twilio.rest.autopilot.v1.assistant.dialogue import DialogueList
from twilio.rest.autopilot.v1.assistant.field_type import FieldTypeList
from twilio.rest.autopilot.v1.assistant.model_build import ModelBuildList
from twilio.rest.autopilot.v1.assistant.query import QueryList
from twilio.rest.autopilot.v1.assistant.style_sheet import StyleSheetList
from twilio.rest.autopilot.v1.assistant.task import TaskList
from twilio.rest.autopilot.v1.assistant.webhook import WebhookList


class AssistantList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the AssistantList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.autopilot.v1.assistant.AssistantList
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Assistants'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name=values.unset, log_queries=values.unset, unique_name=values.unset, callback_url=values.unset, callback_events=values.unset, style_sheet=values.unset, defaults=values.unset):
        """
        Create the AssistantInstance

        :param str friendly_name: A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
        :param bool log_queries: Whether queries should be logged and kept after training. Can be: `true` or `false` and defaults to `true`. If `true`, queries are stored for 30 days, and then deleted. If `false`, no queries are stored.
        :param str unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the `sid` in the URL path to address the resource. The first 64 characters must be unique.
        :param str callback_url: Reserved.
        :param str callback_events: Reserved.
        :param object style_sheet: The JSON string that defines the Assistant's [style sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet)
        :param object defaults: A JSON object that defines the Assistant's [default tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults) for various scenarios, including initiation actions and fallback tasks.
        
        :returns: The created AssistantInstance
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'LogQueries': log_queries,
            'UniqueName': unique_name,
            'CallbackUrl': callback_url,
            'CallbackEvents': callback_events,
            'StyleSheet': serialize.object(style_sheet),
            'Defaults': serialize.object(defaults),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return AssistantInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams AssistantInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.autopilot.v1.assistant.AssistantInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AssistantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.AssistantInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AssistantInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AssistantInstance
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AssistantPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AssistantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AssistantInstance
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AssistantPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a AssistantContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Assistant resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.AssistantContext
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantContext
        """
        return AssistantContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a AssistantContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Assistant resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.AssistantContext
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantContext
        """
        return AssistantContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.AssistantList>'










class AssistantPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AssistantPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.autopilot.v1.assistant.AssistantPage
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AssistantInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.AssistantInstance
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantInstance
        """
        return AssistantInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.AssistantPage>'




class AssistantContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the AssistantContext

        :param Version version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the Assistant resource to update.

        :returns: twilio.rest.autopilot.v1.assistant.AssistantContext
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Assistants/{sid}'.format(**self._solution)
        
        self._defaults = None
        self._dialogues = None
        self._field_types = None
        self._model_builds = None
        self._queries = None
        self._style_sheet = None
        self._tasks = None
        self._webhooks = None
    
    def delete(self):
        """
        Deletes the AssistantInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the AssistantInstance
        

        :returns: The fetched AssistantInstance
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AssistantInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, log_queries=values.unset, unique_name=values.unset, callback_url=values.unset, callback_events=values.unset, style_sheet=values.unset, defaults=values.unset, development_stage=values.unset):
        """
        Update the AssistantInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :params bool log_queries: Whether queries should be logged and kept after training. Can be: `true` or `false` and defaults to `true`. If `true`, queries are stored for 30 days, and then deleted. If `false`, no queries are stored.
        :params str unique_name: An application-defined string that uniquely identifies the resource. It can be used as an alternative to the `sid` in the URL path to address the resource. The first 64 characters must be unique.
        :params str callback_url: Reserved.
        :params str callback_events: Reserved.
        :params object style_sheet: The JSON string that defines the Assistant's [style sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet)
        :params object defaults: A JSON object that defines the Assistant's [default tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults) for various scenarios, including initiation actions and fallback tasks.
        :params str development_stage: A string describing the state of the assistant.

        :returns: The updated AssistantInstance
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'LogQueries': log_queries,
            'UniqueName': unique_name,
            'CallbackUrl': callback_url,
            'CallbackEvents': callback_events,
            'StyleSheet': serialize.object(style_sheet),
            'Defaults': serialize.object(defaults),
            'DevelopmentStage': development_stage,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return AssistantInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def defaults(self):
        """
        Access the defaults

        :returns: twilio.rest.autopilot.v1.assistant.DefaultsList
        :rtype: twilio.rest.autopilot.v1.assistant.DefaultsList
        """
        if self._defaults is None:
            self._defaults = DefaultsList(self._version, self._solution['sid'],
            )
        return self._defaults
    
    @property
    def dialogues(self):
        """
        Access the dialogues

        :returns: twilio.rest.autopilot.v1.assistant.DialogueList
        :rtype: twilio.rest.autopilot.v1.assistant.DialogueList
        """
        if self._dialogues is None:
            self._dialogues = DialogueList(self._version, self._solution['sid'],
            )
        return self._dialogues
    
    @property
    def field_types(self):
        """
        Access the field_types

        :returns: twilio.rest.autopilot.v1.assistant.FieldTypeList
        :rtype: twilio.rest.autopilot.v1.assistant.FieldTypeList
        """
        if self._field_types is None:
            self._field_types = FieldTypeList(self._version, self._solution['sid'],
            )
        return self._field_types
    
    @property
    def model_builds(self):
        """
        Access the model_builds

        :returns: twilio.rest.autopilot.v1.assistant.ModelBuildList
        :rtype: twilio.rest.autopilot.v1.assistant.ModelBuildList
        """
        if self._model_builds is None:
            self._model_builds = ModelBuildList(self._version, self._solution['sid'],
            )
        return self._model_builds
    
    @property
    def queries(self):
        """
        Access the queries

        :returns: twilio.rest.autopilot.v1.assistant.QueryList
        :rtype: twilio.rest.autopilot.v1.assistant.QueryList
        """
        if self._queries is None:
            self._queries = QueryList(self._version, self._solution['sid'],
            )
        return self._queries
    
    @property
    def style_sheet(self):
        """
        Access the style_sheet

        :returns: twilio.rest.autopilot.v1.assistant.StyleSheetList
        :rtype: twilio.rest.autopilot.v1.assistant.StyleSheetList
        """
        if self._style_sheet is None:
            self._style_sheet = StyleSheetList(self._version, self._solution['sid'],
            )
        return self._style_sheet
    
    @property
    def tasks(self):
        """
        Access the tasks

        :returns: twilio.rest.autopilot.v1.assistant.TaskList
        :rtype: twilio.rest.autopilot.v1.assistant.TaskList
        """
        if self._tasks is None:
            self._tasks = TaskList(self._version, self._solution['sid'],
            )
        return self._tasks
    
    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.autopilot.v1.assistant.WebhookList
        :rtype: twilio.rest.autopilot.v1.assistant.WebhookList
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(self._version, self._solution['sid'],
            )
        return self._webhooks
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.AssistantContext {}>'.format(context)

class AssistantInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the AssistantInstance
        :returns: twilio.rest.autopilot.v1.assistant.AssistantInstance
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'latest_model_build_sid': payload.get('latest_model_build_sid'),
            'links': payload.get('links'),
            'log_queries': payload.get('log_queries'),
            'development_stage': payload.get('development_stage'),
            'needs_model_build': payload.get('needs_model_build'),
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'url': payload.get('url'),
            'callback_url': payload.get('callback_url'),
            'callback_events': payload.get('callback_events'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssistantContext for this AssistantInstance
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantContext
        """
        if self._context is None:
            self._context = AssistantContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Assistant resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource. It is not unique and can be up to 255 characters long.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def latest_model_build_sid(self):
        """
        :returns: Reserved.
        :rtype: str
        """
        return self._properties['latest_model_build_sid']
    
    @property
    def links(self):
        """
        :returns: A list of the URLs of the Assistant's related resources.
        :rtype: dict
        """
        return self._properties['links']
    
    @property
    def log_queries(self):
        """
        :returns: Whether queries should be logged and kept after training. Can be: `true` or `false` and defaults to `true`. If `true`, queries are stored for 30 days, and then deleted. If `false`, no queries are stored.
        :rtype: bool
        """
        return self._properties['log_queries']
    
    @property
    def development_stage(self):
        """
        :returns: A string describing the state of the assistant.
        :rtype: str
        """
        return self._properties['development_stage']
    
    @property
    def needs_model_build(self):
        """
        :returns: Whether model needs to be rebuilt.
        :rtype: bool
        """
        return self._properties['needs_model_build']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Assistant resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource. It can be up to 64 characters long.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Assistant resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def callback_url(self):
        """
        :returns: Reserved.
        :rtype: str
        """
        return self._properties['callback_url']
    
    @property
    def callback_events(self):
        """
        :returns: Reserved.
        :rtype: str
        """
        return self._properties['callback_events']
    
    def delete(self):
        """
        Deletes the AssistantInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the AssistantInstance
        

        :returns: The fetched AssistantInstance
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, log_queries=values.unset, unique_name=values.unset, callback_url=values.unset, callback_events=values.unset, style_sheet=values.unset, defaults=values.unset, development_stage=values.unset):
        """
        Update the AssistantInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :params bool log_queries: Whether queries should be logged and kept after training. Can be: `true` or `false` and defaults to `true`. If `true`, queries are stored for 30 days, and then deleted. If `false`, no queries are stored.
        :params str unique_name: An application-defined string that uniquely identifies the resource. It can be used as an alternative to the `sid` in the URL path to address the resource. The first 64 characters must be unique.
        :params str callback_url: Reserved.
        :params str callback_events: Reserved.
        :params object style_sheet: The JSON string that defines the Assistant's [style sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet)
        :params object defaults: A JSON object that defines the Assistant's [default tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults) for various scenarios, including initiation actions and fallback tasks.
        :params str development_stage: A string describing the state of the assistant.

        :returns: The updated AssistantInstance
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantInstance
        """
        return self._proxy.update(friendly_name=friendly_name, log_queries=log_queries, unique_name=unique_name, callback_url=callback_url, callback_events=callback_events, style_sheet=style_sheet, defaults=defaults, development_stage=development_stage, )
    
    @property
    def defaults(self):
        """
        Access the defaults

        :returns: twilio.rest.autopilot.v1.assistant.DefaultsList
        :rtype: twilio.rest.autopilot.v1.assistant.DefaultsList
        """
        return self._proxy.defaults
    
    @property
    def dialogues(self):
        """
        Access the dialogues

        :returns: twilio.rest.autopilot.v1.assistant.DialogueList
        :rtype: twilio.rest.autopilot.v1.assistant.DialogueList
        """
        return self._proxy.dialogues
    
    @property
    def field_types(self):
        """
        Access the field_types

        :returns: twilio.rest.autopilot.v1.assistant.FieldTypeList
        :rtype: twilio.rest.autopilot.v1.assistant.FieldTypeList
        """
        return self._proxy.field_types
    
    @property
    def model_builds(self):
        """
        Access the model_builds

        :returns: twilio.rest.autopilot.v1.assistant.ModelBuildList
        :rtype: twilio.rest.autopilot.v1.assistant.ModelBuildList
        """
        return self._proxy.model_builds
    
    @property
    def queries(self):
        """
        Access the queries

        :returns: twilio.rest.autopilot.v1.assistant.QueryList
        :rtype: twilio.rest.autopilot.v1.assistant.QueryList
        """
        return self._proxy.queries
    
    @property
    def style_sheet(self):
        """
        Access the style_sheet

        :returns: twilio.rest.autopilot.v1.assistant.StyleSheetList
        :rtype: twilio.rest.autopilot.v1.assistant.StyleSheetList
        """
        return self._proxy.style_sheet
    
    @property
    def tasks(self):
        """
        Access the tasks

        :returns: twilio.rest.autopilot.v1.assistant.TaskList
        :rtype: twilio.rest.autopilot.v1.assistant.TaskList
        """
        return self._proxy.tasks
    
    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.autopilot.v1.assistant.WebhookList
        :rtype: twilio.rest.autopilot.v1.assistant.WebhookList
        """
        return self._proxy.webhooks
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.AssistantInstance {}>'.format(context)


