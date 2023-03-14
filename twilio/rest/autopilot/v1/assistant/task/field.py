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
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class FieldList(ListResource):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the FieldList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resources to read.
        :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) resource associated with the Field resources to read.

        :returns: twilio.rest.autopilot.v1.assistant.task.field.FieldList
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields".format(
            **self._solution
        )

    def create(self, field_type, unique_name):
        """
        Create the FieldInstance

        :param str field_type: The Field Type of the new field. Can be: a [Built-in Field Type](https://www.twilio.com/docs/autopilot/built-in-field-types), the `unique_name`, or the `sid` of a custom Field Type.
        :param str unique_name: An application-defined string that uniquely identifies the new resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The created FieldInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldInstance
        """
        data = values.of(
            {
                "FieldType": field_type,
                "UniqueName": unique_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FieldInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams FieldInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.autopilot.v1.assistant.task.field.FieldInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists FieldInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.task.field.FieldInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of FieldInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FieldInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return FieldPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FieldInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FieldInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FieldPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a FieldContext

        :param sid: The Twilio-provided string that uniquely identifies the Field resource to fetch.

        :returns: twilio.rest.autopilot.v1.assistant.task.field.FieldContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldContext
        """
        return FieldContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a FieldContext

        :param sid: The Twilio-provided string that uniquely identifies the Field resource to fetch.

        :returns: twilio.rest.autopilot.v1.assistant.task.field.FieldContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldContext
        """
        return FieldContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Autopilot.V1.FieldList>"


class FieldPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the FieldPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.autopilot.v1.assistant.task.field.FieldPage
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FieldInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.task.field.FieldInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldInstance
        """
        return FieldInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Autopilot.V1.FieldPage>"


class FieldInstance(InstanceResource):
    def __init__(
        self, version, payload, assistant_sid: str, task_sid: str, sid: str = None
    ):
        """
        Initialize the FieldInstance

        :returns: twilio.rest.autopilot.v1.assistant.task.field.FieldInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "field_type": payload.get("field_type"),
            "task_sid": payload.get("task_sid"),
            "assistant_sid": payload.get("assistant_sid"),
            "sid": payload.get("sid"),
            "unique_name": payload.get("unique_name"),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FieldContext for this FieldInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldContext
        """
        if self._context is None:
            self._context = FieldContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                task_sid=self._solution["task_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Field resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def field_type(self):
        """
        :returns: The Field Type of the field. Can be: a [Built-in Field Type](https://www.twilio.com/docs/autopilot/built-in-field-types), the unique_name, or the SID of a custom Field Type.
        :rtype: str
        """
        return self._properties["field_type"]

    @property
    def task_sid(self):
        """
        :returns: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) resource associated with this Field.
        :rtype: str
        """
        return self._properties["task_sid"]

    @property
    def assistant_sid(self):
        """
        :returns: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource.
        :rtype: str
        """
        return self._properties["assistant_sid"]

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Field resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :rtype: str
        """
        return self._properties["unique_name"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Field resource.
        :rtype: str
        """
        return self._properties["url"]

    def delete(self):
        """
        Deletes the FieldInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch the FieldInstance


        :returns: The fetched FieldInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.FieldInstance {}>".format(context)


class FieldContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str, sid: str):
        """
        Initialize the FieldContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource to fetch.
        :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) resource associated with the Field resource to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the Field resource to fetch.

        :returns: twilio.rest.autopilot.v1.assistant.task.field.FieldContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
            "sid": sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks/{task_sid}/Fields/{sid}".format(
            **self._solution
        )

    def delete(self):
        """
        Deletes the FieldInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the FieldInstance


        :returns: The fetched FieldInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.field.FieldInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FieldInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.FieldContext {}>".format(context)
