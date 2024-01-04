r"""
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


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ConfigurationInstance(InstanceResource):
    class Status(object):
        OK = "ok"
        INPROGRESS = "inprogress"
        NOTSTARTED = "notstarted"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Configuration resource.
    :ivar date_created: The date and time in GMT when the Configuration resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the Configuration resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar attributes: An object that contains application-specific data.
    :ivar status: 
    :ivar taskrouter_workspace_sid: The SID of the TaskRouter Workspace.
    :ivar taskrouter_target_workflow_sid: The SID of the TaskRouter target Workflow.
    :ivar taskrouter_target_taskqueue_sid: The SID of the TaskRouter Target TaskQueue.
    :ivar taskrouter_taskqueues: The list of TaskRouter TaskQueues.
    :ivar taskrouter_skills: The Skill description for TaskRouter workers.
    :ivar taskrouter_worker_channels: The TaskRouter default channel capacities and availability for workers.
    :ivar taskrouter_worker_attributes: The TaskRouter Worker attributes.
    :ivar taskrouter_offline_activity_sid: The TaskRouter SID of the offline activity.
    :ivar runtime_domain: The URL where the Flex instance is hosted.
    :ivar messaging_service_instance_sid: The SID of the Messaging service instance.
    :ivar chat_service_instance_sid: The SID of the chat service this user belongs to.
    :ivar flex_service_instance_sid: The SID of the Flex service instance.
    :ivar ui_language: The primary language of the Flex UI.
    :ivar ui_attributes: The object that describes Flex UI characteristics and settings.
    :ivar ui_dependencies: The object that defines the NPM packages and versions to be used in Hosted Flex.
    :ivar ui_version: The Pinned UI version.
    :ivar service_version: The Flex Service version.
    :ivar call_recording_enabled: Whether call recording is enabled.
    :ivar call_recording_webhook_url: The call recording webhook URL.
    :ivar crm_enabled: Whether CRM is present for Flex.
    :ivar crm_type: The CRM type.
    :ivar crm_callback_url: The CRM Callback URL.
    :ivar crm_fallback_url: The CRM Fallback URL.
    :ivar crm_attributes: An object that contains the CRM attributes.
    :ivar public_attributes: The list of public attributes, which are visible to unauthenticated clients.
    :ivar plugin_service_enabled: Whether the plugin service enabled.
    :ivar plugin_service_attributes: The plugin service attributes.
    :ivar integrations: A list of objects that contain the configurations for the Integrations supported in this configuration.
    :ivar outbound_call_flows: The list of outbound call flows.
    :ivar serverless_service_sids: The list of serverless service SIDs.
    :ivar queue_stats_configuration: Configurable parameters for Queues Statistics.
    :ivar notifications: Configurable parameters for Notifications.
    :ivar markdown: Configurable parameters for Markdown.
    :ivar url: The absolute URL of the Configuration resource.
    :ivar flex_insights_hr: Object with enabled/disabled flag with list of workspaces.
    :ivar flex_insights_drilldown: Setting this to true will redirect Flex UI to the URL set in flex_url
    :ivar flex_url: URL to redirect to in case drilldown is enabled.
    :ivar channel_configs: Settings for different limits for Flex Conversations channels attachments.
    :ivar debugger_integration: Configurable parameters for Debugger Integration.
    :ivar flex_ui_status_report: Configurable parameters for Flex UI Status report.
    :ivar agent_conv_end_methods: Agent conversation end methods.
    :ivar citrix_voice_vdi: Citrix voice vdi configuration and settings.
    :ivar offline_config: Presence and presence ttl configuration
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.attributes: Optional[Dict[str, object]] = payload.get("attributes")
        self.status: Optional["ConfigurationInstance.Status"] = payload.get("status")
        self.taskrouter_workspace_sid: Optional[str] = payload.get(
            "taskrouter_workspace_sid"
        )
        self.taskrouter_target_workflow_sid: Optional[str] = payload.get(
            "taskrouter_target_workflow_sid"
        )
        self.taskrouter_target_taskqueue_sid: Optional[str] = payload.get(
            "taskrouter_target_taskqueue_sid"
        )
        self.taskrouter_taskqueues: Optional[List[Dict[str, object]]] = payload.get(
            "taskrouter_taskqueues"
        )
        self.taskrouter_skills: Optional[List[Dict[str, object]]] = payload.get(
            "taskrouter_skills"
        )
        self.taskrouter_worker_channels: Optional[Dict[str, object]] = payload.get(
            "taskrouter_worker_channels"
        )
        self.taskrouter_worker_attributes: Optional[Dict[str, object]] = payload.get(
            "taskrouter_worker_attributes"
        )
        self.taskrouter_offline_activity_sid: Optional[str] = payload.get(
            "taskrouter_offline_activity_sid"
        )
        self.runtime_domain: Optional[str] = payload.get("runtime_domain")
        self.messaging_service_instance_sid: Optional[str] = payload.get(
            "messaging_service_instance_sid"
        )
        self.chat_service_instance_sid: Optional[str] = payload.get(
            "chat_service_instance_sid"
        )
        self.flex_service_instance_sid: Optional[str] = payload.get(
            "flex_service_instance_sid"
        )
        self.ui_language: Optional[str] = payload.get("ui_language")
        self.ui_attributes: Optional[Dict[str, object]] = payload.get("ui_attributes")
        self.ui_dependencies: Optional[Dict[str, object]] = payload.get(
            "ui_dependencies"
        )
        self.ui_version: Optional[str] = payload.get("ui_version")
        self.service_version: Optional[str] = payload.get("service_version")
        self.call_recording_enabled: Optional[bool] = payload.get(
            "call_recording_enabled"
        )
        self.call_recording_webhook_url: Optional[str] = payload.get(
            "call_recording_webhook_url"
        )
        self.crm_enabled: Optional[bool] = payload.get("crm_enabled")
        self.crm_type: Optional[str] = payload.get("crm_type")
        self.crm_callback_url: Optional[str] = payload.get("crm_callback_url")
        self.crm_fallback_url: Optional[str] = payload.get("crm_fallback_url")
        self.crm_attributes: Optional[Dict[str, object]] = payload.get("crm_attributes")
        self.public_attributes: Optional[Dict[str, object]] = payload.get(
            "public_attributes"
        )
        self.plugin_service_enabled: Optional[bool] = payload.get(
            "plugin_service_enabled"
        )
        self.plugin_service_attributes: Optional[Dict[str, object]] = payload.get(
            "plugin_service_attributes"
        )
        self.integrations: Optional[List[Dict[str, object]]] = payload.get(
            "integrations"
        )
        self.outbound_call_flows: Optional[Dict[str, object]] = payload.get(
            "outbound_call_flows"
        )
        self.serverless_service_sids: Optional[List[str]] = payload.get(
            "serverless_service_sids"
        )
        self.queue_stats_configuration: Optional[Dict[str, object]] = payload.get(
            "queue_stats_configuration"
        )
        self.notifications: Optional[Dict[str, object]] = payload.get("notifications")
        self.markdown: Optional[Dict[str, object]] = payload.get("markdown")
        self.url: Optional[str] = payload.get("url")
        self.flex_insights_hr: Optional[Dict[str, object]] = payload.get(
            "flex_insights_hr"
        )
        self.flex_insights_drilldown: Optional[bool] = payload.get(
            "flex_insights_drilldown"
        )
        self.flex_url: Optional[str] = payload.get("flex_url")
        self.channel_configs: Optional[List[Dict[str, object]]] = payload.get(
            "channel_configs"
        )
        self.debugger_integration: Optional[Dict[str, object]] = payload.get(
            "debugger_integration"
        )
        self.flex_ui_status_report: Optional[Dict[str, object]] = payload.get(
            "flex_ui_status_report"
        )
        self.agent_conv_end_methods: Optional[Dict[str, object]] = payload.get(
            "agent_conv_end_methods"
        )
        self.citrix_voice_vdi: Optional[Dict[str, object]] = payload.get(
            "citrix_voice_vdi"
        )
        self.offline_config: Optional[Dict[str, object]] = payload.get("offline_config")

        self._context: Optional[ConfigurationContext] = None

    @property
    def _proxy(self) -> "ConfigurationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ConfigurationContext for this ConfigurationInstance
        """
        if self._context is None:
            self._context = ConfigurationContext(
                self._version,
            )
        return self._context

    def fetch(
        self, ui_version: Union[str, object] = values.unset
    ) -> "ConfigurationInstance":
        """
        Fetch the ConfigurationInstance

        :param ui_version: The Pinned UI version of the Configuration resource to fetch.

        :returns: The fetched ConfigurationInstance
        """
        return self._proxy.fetch(
            ui_version=ui_version,
        )

    async def fetch_async(
        self, ui_version: Union[str, object] = values.unset
    ) -> "ConfigurationInstance":
        """
        Asynchronous coroutine to fetch the ConfigurationInstance

        :param ui_version: The Pinned UI version of the Configuration resource to fetch.

        :returns: The fetched ConfigurationInstance
        """
        return await self._proxy.fetch_async(
            ui_version=ui_version,
        )

    def update(self) -> "ConfigurationInstance":
        """
        Update the ConfigurationInstance


        :returns: The updated ConfigurationInstance
        """
        return self._proxy.update()

    async def update_async(self) -> "ConfigurationInstance":
        """
        Asynchronous coroutine to update the ConfigurationInstance


        :returns: The updated ConfigurationInstance
        """
        return await self._proxy.update_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.FlexApi.V1.ConfigurationInstance>"


class ConfigurationContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the ConfigurationContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/Configuration"

    def fetch(
        self, ui_version: Union[str, object] = values.unset
    ) -> ConfigurationInstance:
        """
        Fetch the ConfigurationInstance

        :param ui_version: The Pinned UI version of the Configuration resource to fetch.

        :returns: The fetched ConfigurationInstance
        """

        data = values.of(
            {
                "UiVersion": ui_version,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return ConfigurationInstance(
            self._version,
            payload,
        )

    async def fetch_async(
        self, ui_version: Union[str, object] = values.unset
    ) -> ConfigurationInstance:
        """
        Asynchronous coroutine to fetch the ConfigurationInstance

        :param ui_version: The Pinned UI version of the Configuration resource to fetch.

        :returns: The fetched ConfigurationInstance
        """

        data = values.of(
            {
                "UiVersion": ui_version,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return ConfigurationInstance(
            self._version,
            payload,
        )

    def update(self) -> ConfigurationInstance:
        """
        Update the ConfigurationInstance


        :returns: The updated ConfigurationInstance
        """
        data = values.of({})

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ConfigurationInstance(self._version, payload)

    async def update_async(self) -> ConfigurationInstance:
        """
        Asynchronous coroutine to update the ConfigurationInstance


        :returns: The updated ConfigurationInstance
        """
        data = values.of({})

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ConfigurationInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.FlexApi.V1.ConfigurationContext>"


class ConfigurationList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ConfigurationList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> ConfigurationContext:
        """
        Constructs a ConfigurationContext

        """
        return ConfigurationContext(self._version)

    def __call__(self) -> ConfigurationContext:
        """
        Constructs a ConfigurationContext

        """
        return ConfigurationContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.ConfigurationList>"
