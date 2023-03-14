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
from twilio.rest.taskrouter.v1.workspace.task.reservation import ReservationList


class TaskList(ListResource):
    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the TaskList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Tasks to read.

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskList
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Tasks".format(**self._solution)

    def create(
        self,
        timeout=values.unset,
        priority=values.unset,
        task_channel=values.unset,
        workflow_sid=values.unset,
        attributes=values.unset,
    ):
        """
        Create the TaskInstance

        :param int timeout: The amount of time in seconds the new task can live before being assigned. Can be up to a maximum of 2 weeks (1,209,600 seconds). The default value is 24 hours (86,400 seconds). On timeout, the `task.canceled` event will fire with description `Task TTL Exceeded`.
        :param int priority: The priority to assign the new task and override the default. When supplied, the new Task will have this priority unless it matches a Workflow Target with a Priority set. When not supplied, the new Task will have the priority of the matching Workflow Target. Value can be 0 to 2^31^ (2,147,483,647).
        :param str task_channel: When MultiTasking is enabled, specify the TaskChannel by passing either its `unique_name` or `sid`. Default value is `default`.
        :param str workflow_sid: The SID of the Workflow that you would like to handle routing for the new Task. If there is only one Workflow defined for the Workspace that you are posting the new task to, this parameter is optional.
        :param str attributes: A URL-encoded JSON string with the attributes of the new task. This value is passed to the Workflow's `assignment_callback_url` when the Task is assigned to a Worker. For example: `{ \\\"task_type\\\": \\\"call\\\", \\\"twilio_call_sid\\\": \\\"CAxxx\\\", \\\"customer_ticket_number\\\": \\\"12345\\\" }`.

        :returns: The created TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        data = values.of(
            {
                "Timeout": timeout,
                "Priority": priority,
                "TaskChannel": task_channel,
                "WorkflowSid": workflow_sid,
                "Attributes": attributes,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskInstance(
            self._version, payload, workspace_sid=self._solution["workspace_sid"]
        )

    def stream(
        self,
        priority=values.unset,
        assignment_status=values.unset,
        workflow_sid=values.unset,
        workflow_name=values.unset,
        task_queue_sid=values.unset,
        task_queue_name=values.unset,
        evaluate_task_attributes=values.unset,
        ordering=values.unset,
        has_addons=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams TaskInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int priority: The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the specified priority.
        :param list[str] assignment_status: The `assignment_status` of the Tasks you want to read. Can be: `pending`, `reserved`, `assigned`, `canceled`, `wrapping`, or `completed`. Returns all Tasks in the Workspace with the specified `assignment_status`.
        :param str workflow_sid: The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this SID.
        :param str workflow_name: The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this friendly name.
        :param str task_queue_sid: The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this SID.
        :param str task_queue_name: The `friendly_name` of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this friendly name.
        :param str evaluate_task_attributes: The attributes of the Tasks to read. Returns the Tasks that match the attributes specified in this parameter.
        :param str ordering: How to order the returned Task resources. y default, Tasks are sorted by ascending DateCreated. This value is specified as: `Attribute:Order`, where `Attribute` can be either `Priority` or `DateCreated` and `Order` can be either `asc` or `desc`. For example, `Priority:desc` returns Tasks ordered in descending order of their Priority. Multiple sort orders can be specified in a comma-separated list such as `Priority:desc,DateCreated:asc`, which returns the Tasks in descending Priority order and ascending DateCreated Order.
        :param bool has_addons: Whether to read Tasks with addons. If `true`, returns only Tasks with addons. If `false`, returns only Tasks without addons.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.task.TaskInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            priority=priority,
            assignment_status=assignment_status,
            workflow_sid=workflow_sid,
            workflow_name=workflow_name,
            task_queue_sid=task_queue_sid,
            task_queue_name=task_queue_name,
            evaluate_task_attributes=evaluate_task_attributes,
            ordering=ordering,
            has_addons=has_addons,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    def list(
        self,
        priority=values.unset,
        assignment_status=values.unset,
        workflow_sid=values.unset,
        workflow_name=values.unset,
        task_queue_sid=values.unset,
        task_queue_name=values.unset,
        evaluate_task_attributes=values.unset,
        ordering=values.unset,
        has_addons=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists TaskInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int priority: The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the specified priority.
        :param list[str] assignment_status: The `assignment_status` of the Tasks you want to read. Can be: `pending`, `reserved`, `assigned`, `canceled`, `wrapping`, or `completed`. Returns all Tasks in the Workspace with the specified `assignment_status`.
        :param str workflow_sid: The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this SID.
        :param str workflow_name: The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this friendly name.
        :param str task_queue_sid: The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this SID.
        :param str task_queue_name: The `friendly_name` of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this friendly name.
        :param str evaluate_task_attributes: The attributes of the Tasks to read. Returns the Tasks that match the attributes specified in this parameter.
        :param str ordering: How to order the returned Task resources. y default, Tasks are sorted by ascending DateCreated. This value is specified as: `Attribute:Order`, where `Attribute` can be either `Priority` or `DateCreated` and `Order` can be either `asc` or `desc`. For example, `Priority:desc` returns Tasks ordered in descending order of their Priority. Multiple sort orders can be specified in a comma-separated list such as `Priority:desc,DateCreated:asc`, which returns the Tasks in descending Priority order and ascending DateCreated Order.
        :param bool has_addons: Whether to read Tasks with addons. If `true`, returns only Tasks with addons. If `false`, returns only Tasks without addons.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.task.TaskInstance]
        """
        return list(
            self.stream(
                priority=priority,
                assignment_status=assignment_status,
                workflow_sid=workflow_sid,
                workflow_name=workflow_name,
                task_queue_sid=task_queue_sid,
                task_queue_name=task_queue_name,
                evaluate_task_attributes=evaluate_task_attributes,
                ordering=ordering,
                has_addons=has_addons,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        priority=values.unset,
        assignment_status=values.unset,
        workflow_sid=values.unset,
        workflow_name=values.unset,
        task_queue_sid=values.unset,
        task_queue_name=values.unset,
        evaluate_task_attributes=values.unset,
        ordering=values.unset,
        has_addons=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of TaskInstance records from the API.
        Request is executed immediately

        :param int priority: The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the specified priority.
        :param list[str] assignment_status: The `assignment_status` of the Tasks you want to read. Can be: `pending`, `reserved`, `assigned`, `canceled`, `wrapping`, or `completed`. Returns all Tasks in the Workspace with the specified `assignment_status`.
        :param str workflow_sid: The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this SID.
        :param str workflow_name: The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this friendly name.
        :param str task_queue_sid: The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this SID.
        :param str task_queue_name: The `friendly_name` of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this friendly name.
        :param str evaluate_task_attributes: The attributes of the Tasks to read. Returns the Tasks that match the attributes specified in this parameter.
        :param str ordering: How to order the returned Task resources. y default, Tasks are sorted by ascending DateCreated. This value is specified as: `Attribute:Order`, where `Attribute` can be either `Priority` or `DateCreated` and `Order` can be either `asc` or `desc`. For example, `Priority:desc` returns Tasks ordered in descending order of their Priority. Multiple sort orders can be specified in a comma-separated list such as `Priority:desc,DateCreated:asc`, which returns the Tasks in descending Priority order and ascending DateCreated Order.
        :param bool has_addons: Whether to read Tasks with addons. If `true`, returns only Tasks with addons. If `false`, returns only Tasks without addons.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskPage
        """
        data = values.of(
            {
                "Priority": priority,
                "AssignmentStatus": serialize.map(assignment_status, lambda e: e),
                "WorkflowSid": workflow_sid,
                "WorkflowName": workflow_name,
                "TaskQueueSid": task_queue_sid,
                "TaskQueueName": task_queue_name,
                "EvaluateTaskAttributes": evaluate_task_attributes,
                "Ordering": ordering,
                "HasAddons": has_addons,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return TaskPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TaskInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return TaskPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a TaskContext

        :param sid: The SID of the Task resource to update.

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        """
        return TaskContext(
            self._version, workspace_sid=self._solution["workspace_sid"], sid=sid
        )

    def __call__(self, sid):
        """
        Constructs a TaskContext

        :param sid: The SID of the Task resource to update.

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        """
        return TaskContext(
            self._version, workspace_sid=self._solution["workspace_sid"], sid=sid
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Taskrouter.V1.TaskList>"


class TaskPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the TaskPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskPage
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TaskInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        return TaskInstance(
            self._version, payload, workspace_sid=self._solution["workspace_sid"]
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Taskrouter.V1.TaskPage>"


class TaskInstance(InstanceResource):
    class Status(object):
        PENDING = "pending"
        RESERVED = "reserved"
        ASSIGNED = "assigned"
        CANCELED = "canceled"
        COMPLETED = "completed"
        WRAPPING = "wrapping"

    def __init__(self, version, payload, workspace_sid: str, sid: str = None):
        """
        Initialize the TaskInstance

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "age": deserialize.integer(payload.get("age")),
            "assignment_status": payload.get("assignment_status"),
            "attributes": payload.get("attributes"),
            "addons": payload.get("addons"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "task_queue_entered_date": deserialize.iso8601_datetime(
                payload.get("task_queue_entered_date")
            ),
            "priority": deserialize.integer(payload.get("priority")),
            "reason": payload.get("reason"),
            "sid": payload.get("sid"),
            "task_queue_sid": payload.get("task_queue_sid"),
            "task_queue_friendly_name": payload.get("task_queue_friendly_name"),
            "task_channel_sid": payload.get("task_channel_sid"),
            "task_channel_unique_name": payload.get("task_channel_unique_name"),
            "timeout": deserialize.integer(payload.get("timeout")),
            "workflow_sid": payload.get("workflow_sid"),
            "workflow_friendly_name": payload.get("workflow_friendly_name"),
            "workspace_sid": payload.get("workspace_sid"),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._context = None
        self._solution = {
            "workspace_sid": workspace_sid,
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskContext for this TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        """
        if self._context is None:
            self._context = TaskContext(
                self._version,
                workspace_sid=self._solution["workspace_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Task resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def age(self):
        """
        :returns: The number of seconds since the Task was created.
        :rtype: int
        """
        return self._properties["age"]

    @property
    def assignment_status(self):
        """
        :returns:
        :rtype: TaskInstance.Status
        """
        return self._properties["assignment_status"]

    @property
    def attributes(self):
        """
        :returns: The JSON string with custom attributes of the work. **Note** If this property has been assigned a value, it will only be displayed in FETCH action that returns a single resource. Otherwise, it will be null.
        :rtype: str
        """
        return self._properties["attributes"]

    @property
    def addons(self):
        """
        :returns: An object that contains the [addon](https://www.twilio.com/docs/taskrouter/marketplace) data for all installed addons.
        :rtype: str
        """
        return self._properties["addons"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def task_queue_entered_date(self):
        """
        :returns: The date and time in GMT when the Task entered the TaskQueue, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["task_queue_entered_date"]

    @property
    def priority(self):
        """
        :returns: The current priority score of the Task as assigned to a Worker by the workflow. Tasks with higher priority values will be assigned before Tasks with lower values.
        :rtype: int
        """
        return self._properties["priority"]

    @property
    def reason(self):
        """
        :returns: The reason the Task was canceled or completed, if applicable.
        :rtype: str
        """
        return self._properties["reason"]

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Task resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def task_queue_sid(self):
        """
        :returns: The SID of the TaskQueue.
        :rtype: str
        """
        return self._properties["task_queue_sid"]

    @property
    def task_queue_friendly_name(self):
        """
        :returns: The friendly name of the TaskQueue.
        :rtype: str
        """
        return self._properties["task_queue_friendly_name"]

    @property
    def task_channel_sid(self):
        """
        :returns: The SID of the TaskChannel.
        :rtype: str
        """
        return self._properties["task_channel_sid"]

    @property
    def task_channel_unique_name(self):
        """
        :returns: The unique name of the TaskChannel.
        :rtype: str
        """
        return self._properties["task_channel_unique_name"]

    @property
    def timeout(self):
        """
        :returns: The amount of time in seconds that the Task can live before being assigned.
        :rtype: int
        """
        return self._properties["timeout"]

    @property
    def workflow_sid(self):
        """
        :returns: The SID of the Workflow that is controlling the Task.
        :rtype: str
        """
        return self._properties["workflow_sid"]

    @property
    def workflow_friendly_name(self):
        """
        :returns: The friendly name of the Workflow that is controlling the Task.
        :rtype: str
        """
        return self._properties["workflow_friendly_name"]

    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the Task.
        :rtype: str
        """
        return self._properties["workspace_sid"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Task resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties["links"]

    def delete(self, if_match=values.unset):
        """
        Deletes the TaskInstance

        :param str if_match: If provided, deletes this Task if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(
            if_match=if_match,
        )

    def fetch(self):
        """
        Fetch the TaskInstance


        :returns: The fetched TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        return self._proxy.fetch()

    def update(
        self,
        if_match=values.unset,
        attributes=values.unset,
        assignment_status=values.unset,
        reason=values.unset,
        priority=values.unset,
        task_channel=values.unset,
    ):
        """
        Update the TaskInstance

        :param str if_match: If provided, applies this mutation if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
        :param str attributes: The JSON string that describes the custom attributes of the task.
        :param TaskInstance.Status assignment_status:
        :param str reason: The reason that the Task was canceled or completed. This parameter is required only if the Task is canceled or completed. Setting this value queues the task for deletion and logs the reason.
        :param int priority: The Task's new priority value. When supplied, the Task takes on the specified priority unless it matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647).
        :param str task_channel: When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The updated TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        return self._proxy.update(
            if_match=if_match,
            attributes=attributes,
            assignment_status=assignment_status,
            reason=reason,
            priority=priority,
            task_channel=task_channel,
        )

    @property
    def reservations(self):
        """
        Access the reservations

        :returns: twilio.rest.taskrouter.v1.workspace.task.ReservationList
        :rtype: twilio.rest.taskrouter.v1.workspace.task.ReservationList
        """
        return self._proxy.reservations

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.TaskInstance {}>".format(context)


class TaskContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str, sid: str):
        """
        Initialize the TaskContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Task to update.
        :param sid: The SID of the Task resource to update.

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
            "sid": sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Tasks/{sid}".format(**self._solution)

        self._reservations = None

    def delete(self, if_match=values.unset):
        """
        Deletes the TaskInstance

        :param str if_match: If provided, deletes this Task if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    def fetch(self):
        """
        Fetch the TaskInstance


        :returns: The fetched TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TaskInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        if_match=values.unset,
        attributes=values.unset,
        assignment_status=values.unset,
        reason=values.unset,
        priority=values.unset,
        task_channel=values.unset,
    ):
        """
        Update the TaskInstance

        :param str if_match: If provided, applies this mutation if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
        :param str attributes: The JSON string that describes the custom attributes of the task.
        :param TaskInstance.Status assignment_status:
        :param str reason: The reason that the Task was canceled or completed. This parameter is required only if the Task is canceled or completed. Setting this value queues the task for deletion and logs the reason.
        :param int priority: The Task's new priority value. When supplied, the Task takes on the specified priority unless it matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647).
        :param str task_channel: When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The updated TaskInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskInstance
        """
        data = values.of(
            {
                "Attributes": attributes,
                "AssignmentStatus": assignment_status,
                "Reason": reason,
                "Priority": priority,
                "TaskChannel": task_channel,
            }
        )
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return TaskInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            sid=self._solution["sid"],
        )

    @property
    def reservations(self):
        """
        Access the reservations

        :returns: twilio.rest.taskrouter.v1.workspace.task.ReservationList
        :rtype: twilio.rest.taskrouter.v1.workspace.task.ReservationList
        """
        if self._reservations is None:
            self._reservations = ReservationList(
                self._version,
                self._solution["workspace_sid"],
                self._solution["sid"],
            )
        return self._reservations

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.TaskContext {}>".format(context)
