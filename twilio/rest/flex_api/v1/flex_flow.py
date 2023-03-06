"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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


class FlexFlowList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the FlexFlowList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowList
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/FlexFlows'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, chat_service_sid, channel_type, contact_identity=values.unset, enabled=values.unset, integration_type=values.unset, integration_flow_sid=values.unset, integration_url=values.unset, integration_workspace_sid=values.unset, integration_workflow_sid=values.unset, integration_channel=values.unset, integration_timeout=values.unset, integration_priority=values.unset, integration_creation_on_message=values.unset, long_lived=values.unset, janitor_enabled=values.unset, integration_retry_count=values.unset):
        """
        Create the FlexFlowInstance

        :param str friendly_name: A descriptive string that you create to describe the Flex Flow resource.
        :param str chat_service_sid: The SID of the chat service.
        :param FlexFlowInstance.ChannelType channel_type: 
        :param str contact_identity: The channel contact's Identity.
        :param bool enabled: Whether the new Flex Flow is enabled.
        :param FlexFlowInstance.IntegrationType integration_type: 
        :param str integration_flow_sid: The SID of the Studio Flow. Required when `integrationType` is `studio`.
        :param str integration_url: The URL of the external webhook. Required when `integrationType` is `external`.
        :param str integration_workspace_sid: The Workspace SID for a new Task. Required when `integrationType` is `task`.
        :param str integration_workflow_sid: The Workflow SID for a new Task. Required when `integrationType` is `task`.
        :param str integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., `sms`) to use for the Task that will be created. Applicable and required when `integrationType` is `task`. The default value is `default`.
        :param int integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when `integrationType` is `task`, not applicable otherwise.
        :param int integration_priority: The Task priority of a new Task. The default priority is 0. Optional when `integrationType` is `task`, not applicable otherwise.
        :param bool integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging.
        :param bool long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to `false`.
        :param bool janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to `false`.
        :param int integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when `integrationType` is `studio` or `external`, not applicable otherwise.
        
        :returns: The created FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'ChatServiceSid': chat_service_sid,
            'ChannelType': channel_type,
            'ContactIdentity': contact_identity,
            'Enabled': enabled,
            'IntegrationType': integration_type,
            'Integration.FlowSid': integration_flow_sid,
            'Integration.Url': integration_url,
            'Integration.WorkspaceSid': integration_workspace_sid,
            'Integration.WorkflowSid': integration_workflow_sid,
            'Integration.Channel': integration_channel,
            'Integration.Timeout': integration_timeout,
            'Integration.Priority': integration_priority,
            'Integration.CreationOnMessage': integration_creation_on_message,
            'LongLived': long_lived,
            'JanitorEnabled': janitor_enabled,
            'Integration.RetryCount': integration_retry_count,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return FlexFlowInstance(self._version, payload)
    
    
    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams FlexFlowInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str friendly_name: The `friendly_name` of the Flex Flow resources to read.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            friendly_name=friendly_name,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists FlexFlowInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str friendly_name: The `friendly_name` of the Flex Flow resources to read.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of FlexFlowInstance records from the API.
        Request is executed immediately
        
        :param str friendly_name: The `friendly_name` of the Flex Flow resources to read.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowPage
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return FlexFlowPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FlexFlowInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return FlexFlowPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a FlexFlowContext
        
        :param sid: The SID of the Flex Flow resource to update.
        
        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        """
        return FlexFlowContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a FlexFlowContext
        
        :param sid: The SID of the Flex Flow resource to update.
        
        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        """
        return FlexFlowContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.FlexFlowList>'










class FlexFlowPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FlexFlowPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowPage
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FlexFlowInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        return FlexFlowInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.FlexFlowPage>'




class FlexFlowContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the FlexFlowContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Flex Flow resource to update.

        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/FlexFlows/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the FlexFlowInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the FlexFlowInstance
        

        :returns: The fetched FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FlexFlowInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, chat_service_sid=values.unset, channel_type=values.unset, contact_identity=values.unset, enabled=values.unset, integration_type=values.unset, integration_flow_sid=values.unset, integration_url=values.unset, integration_workspace_sid=values.unset, integration_workflow_sid=values.unset, integration_channel=values.unset, integration_timeout=values.unset, integration_priority=values.unset, integration_creation_on_message=values.unset, long_lived=values.unset, janitor_enabled=values.unset, integration_retry_count=values.unset):
        """
        Update the FlexFlowInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Flex Flow resource.
        :params str chat_service_sid: The SID of the chat service.
        :params FlexFlowInstance.ChannelType channel_type: 
        :params str contact_identity: The channel contact's Identity.
        :params bool enabled: Whether the new Flex Flow is enabled.
        :params FlexFlowInstance.IntegrationType integration_type: 
        :params str integration_flow_sid: The SID of the Studio Flow. Required when `integrationType` is `studio`.
        :params str integration_url: The URL of the external webhook. Required when `integrationType` is `external`.
        :params str integration_workspace_sid: The Workspace SID for a new Task. Required when `integrationType` is `task`.
        :params str integration_workflow_sid: The Workflow SID for a new Task. Required when `integrationType` is `task`.
        :params str integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., `sms`) to use for the Task that will be created. Applicable and required when `integrationType` is `task`. The default value is `default`.
        :params int integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when `integrationType` is `task`, not applicable otherwise.
        :params int integration_priority: The Task priority of a new Task. The default priority is 0. Optional when `integrationType` is `task`, not applicable otherwise.
        :params bool integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging.
        :params bool long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to `false`.
        :params bool janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to `false`.
        :params int integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when `integrationType` is `studio` or `external`, not applicable otherwise.

        :returns: The updated FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'ChatServiceSid': chat_service_sid,
            'ChannelType': channel_type,
            'ContactIdentity': contact_identity,
            'Enabled': enabled,
            'IntegrationType': integration_type,
            'Integration.FlowSid': integration_flow_sid,
            'Integration.Url': integration_url,
            'Integration.WorkspaceSid': integration_workspace_sid,
            'Integration.WorkflowSid': integration_workflow_sid,
            'Integration.Channel': integration_channel,
            'Integration.Timeout': integration_timeout,
            'Integration.Priority': integration_priority,
            'Integration.CreationOnMessage': integration_creation_on_message,
            'LongLived': long_lived,
            'JanitorEnabled': janitor_enabled,
            'Integration.RetryCount': integration_retry_count,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return FlexFlowInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.FlexFlowContext {}>'.format(context)

class FlexFlowInstance(InstanceResource):

    class ChannelType(object):
        WEB = "web"
        SMS = "sms"
        FACEBOOK = "facebook"
        WHATSAPP = "whatsapp"
        LINE = "line"
        CUSTOM = "custom"

    class IntegrationType(object):
        STUDIO = "studio"
        EXTERNAL = "external"
        TASK = "task"

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the FlexFlowInstance
        :returns: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'chat_service_sid': payload.get('chat_service_sid'),
            'channel_type': payload.get('channel_type'),
            'contact_identity': payload.get('contact_identity'),
            'enabled': payload.get('enabled'),
            'integration_type': payload.get('integration_type'),
            'integration': payload.get('integration'),
            'long_lived': payload.get('long_lived'),
            'janitor_enabled': payload.get('janitor_enabled'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FlexFlowContext for this FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowContext
        """
        if self._context is None:
            self._context = FlexFlowContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Flow resource and owns this Workflow.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Flex Flow resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def chat_service_sid(self):
        """
        :returns: The SID of the chat service.
        :rtype: str
        """
        return self._properties['chat_service_sid']
    
    @property
    def channel_type(self):
        """
        :returns: 
        :rtype: FlexFlowInstance.ChannelType
        """
        return self._properties['channel_type']
    
    @property
    def contact_identity(self):
        """
        :returns: The channel contact's Identity.
        :rtype: str
        """
        return self._properties['contact_identity']
    
    @property
    def enabled(self):
        """
        :returns: Whether the Flex Flow is enabled.
        :rtype: bool
        """
        return self._properties['enabled']
    
    @property
    def integration_type(self):
        """
        :returns: 
        :rtype: FlexFlowInstance.IntegrationType
        """
        return self._properties['integration_type']
    
    @property
    def integration(self):
        """
        :returns: An object that contains specific parameters for the integration.
        :rtype: dict
        """
        return self._properties['integration']
    
    @property
    def long_lived(self):
        """
        :returns: When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to `false`.
        :rtype: bool
        """
        return self._properties['long_lived']
    
    @property
    def janitor_enabled(self):
        """
        :returns: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to `false`.
        :rtype: bool
        """
        return self._properties['janitor_enabled']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Flex Flow resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the FlexFlowInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the FlexFlowInstance
        

        :returns: The fetched FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, chat_service_sid=values.unset, channel_type=values.unset, contact_identity=values.unset, enabled=values.unset, integration_type=values.unset, integration_flow_sid=values.unset, integration_url=values.unset, integration_workspace_sid=values.unset, integration_workflow_sid=values.unset, integration_channel=values.unset, integration_timeout=values.unset, integration_priority=values.unset, integration_creation_on_message=values.unset, long_lived=values.unset, janitor_enabled=values.unset, integration_retry_count=values.unset):
        """
        Update the FlexFlowInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Flex Flow resource.
        :params str chat_service_sid: The SID of the chat service.
        :params FlexFlowInstance.ChannelType channel_type: 
        :params str contact_identity: The channel contact's Identity.
        :params bool enabled: Whether the new Flex Flow is enabled.
        :params FlexFlowInstance.IntegrationType integration_type: 
        :params str integration_flow_sid: The SID of the Studio Flow. Required when `integrationType` is `studio`.
        :params str integration_url: The URL of the external webhook. Required when `integrationType` is `external`.
        :params str integration_workspace_sid: The Workspace SID for a new Task. Required when `integrationType` is `task`.
        :params str integration_workflow_sid: The Workflow SID for a new Task. Required when `integrationType` is `task`.
        :params str integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., `sms`) to use for the Task that will be created. Applicable and required when `integrationType` is `task`. The default value is `default`.
        :params int integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when `integrationType` is `task`, not applicable otherwise.
        :params int integration_priority: The Task priority of a new Task. The default priority is 0. Optional when `integrationType` is `task`, not applicable otherwise.
        :params bool integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging.
        :params bool long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to `false`.
        :params bool janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to `false`.
        :params int integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when `integrationType` is `studio` or `external`, not applicable otherwise.

        :returns: The updated FlexFlowInstance
        :rtype: twilio.rest.flex_api.v1.flex_flow.FlexFlowInstance
        """
        return self._proxy.update(friendly_name=friendly_name, chat_service_sid=chat_service_sid, channel_type=channel_type, contact_identity=contact_identity, enabled=enabled, integration_type=integration_type, integration_flow_sid=integration_flow_sid, integration_url=integration_url, integration_workspace_sid=integration_workspace_sid, integration_workflow_sid=integration_workflow_sid, integration_channel=integration_channel, integration_timeout=integration_timeout, integration_priority=integration_priority, integration_creation_on_message=integration_creation_on_message, long_lived=long_lived, janitor_enabled=janitor_enabled, integration_retry_count=integration_retry_count, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.FlexFlowInstance {}>'.format(context)


