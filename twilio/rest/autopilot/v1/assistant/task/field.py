r"""
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


from datetime import datetime
from typing import List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class FieldInstance(InstanceResource):
    def __init__(
        self,
        version,
        payload,
        assistant_sid: str,
        task_sid: str,
        sid: Optional[str] = None,
    ):
        """
        Initialize the FieldInstance
        """
        super().__init__(version)

        self._account_sid: Optional[str] = payload.get("account_sid")
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self._field_type: Optional[str] = payload.get("field_type")
        self._task_sid: Optional[str] = payload.get("task_sid")
        self._assistant_sid: Optional[str] = payload.get("assistant_sid")
        self._sid: Optional[str] = payload.get("sid")
        self._unique_name: Optional[str] = payload.get("unique_name")
        self._url: Optional[str] = payload.get("url")

        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
            "sid": sid or self._sid,
        }
        self._context: Optional[FieldContext] = None

    @property
    def _proxy(self) -> "FieldContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FieldContext for this FieldInstance
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
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Field resource.
        """
        return self._account_sid

    @property
    def date_created(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._date_created

    @property
    def date_updated(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._date_updated

    @property
    def field_type(self) -> Optional[str]:
        """
        :returns: The Field Type of the field. Can be: a [Built-in Field Type](https://www.twilio.com/docs/autopilot/built-in-field-types), the unique_name, or the SID of a custom Field Type.
        """
        return self._field_type

    @property
    def task_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) resource associated with this Field.
        """
        return self._task_sid

    @property
    def assistant_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource.
        """
        return self._assistant_sid

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that we created to identify the Field resource.
        """
        return self._sid

    @property
    def unique_name(self) -> Optional[str]:
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        """
        return self._unique_name

    @property
    def url(self) -> Optional[str]:
        """
        :returns: The absolute URL of the Field resource.
        """
        return self._url

    def delete(self) -> bool:
        """
        Deletes the FieldInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FieldInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "FieldInstance":
        """
        Fetch the FieldInstance


        :returns: The fetched FieldInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "FieldInstance":
        """
        Asynchronous coroutine to fetch the FieldInstance


        :returns: The fetched FieldInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.FieldInstance {}>".format(context)


class FieldContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str, sid: str):
        """
        Initialize the FieldContext

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource to fetch.
        :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) resource associated with the Field resource to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the Field resource to fetch.
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

    def delete(self) -> bool:
        """
        Deletes the FieldInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FieldInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> FieldInstance:
        """
        Fetch the FieldInstance


        :returns: The fetched FieldInstance
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

    async def fetch_async(self) -> FieldInstance:
        """
        Asynchronous coroutine to fetch the FieldInstance


        :returns: The fetched FieldInstance
        """

        payload = await self._version.fetch_async(
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

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.FieldContext {}>".format(context)


class FieldPage(Page):
    def get_instance(self, payload) -> FieldInstance:
        """
        Build an instance of FieldInstance

        :param dict payload: Payload response from the API
        """
        return FieldInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.FieldPage>"


class FieldList(ListResource):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the FieldList

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resources to read.
        :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) resource associated with the Field resources to read.

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

    def create(self, field_type, unique_name) -> FieldInstance:
        """
        Create the FieldInstance

        :param str field_type: The Field Type of the new field. Can be: a [Built-in Field Type](https://www.twilio.com/docs/autopilot/built-in-field-types), the `unique_name`, or the `sid` of a custom Field Type.
        :param str unique_name: An application-defined string that uniquely identifies the new resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The created FieldInstance
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

    async def create_async(self, field_type, unique_name) -> FieldInstance:
        """
        Asynchronously create the FieldInstance

        :param str field_type: The Field Type of the new field. Can be: a [Built-in Field Type](https://www.twilio.com/docs/autopilot/built-in-field-types), the `unique_name`, or the `sid` of a custom Field Type.
        :param str unique_name: An application-defined string that uniquely identifies the new resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The created FieldInstance
        """
        data = values.of(
            {
                "FieldType": field_type,
                "UniqueName": unique_name,
            }
        )

        payload = await self._version.create_async(
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

    def stream(self, limit=None, page_size=None) -> List[FieldInstance]:
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
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None) -> List[FieldInstance]:
        """
        Asynchronously streams FieldInstance records from the API as a generator stream.
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
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None) -> List[FieldInstance]:
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
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None) -> List[FieldInstance]:
        """
        Asynchronously lists FieldInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> FieldPage:
        """
        Retrieve a single page of FieldInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FieldInstance
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

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> FieldPage:
        """
        Asynchronously retrieve a single page of FieldInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FieldInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return FieldPage(self._version, response, self._solution)

    def get_page(self, target_url) -> FieldPage:
        """
        Retrieve a specific page of FieldInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FieldInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FieldPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> FieldPage:
        """
        Asynchronously retrieve a specific page of FieldInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FieldInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FieldPage(self._version, response, self._solution)

    def get(self, sid) -> FieldContext:
        """
        Constructs a FieldContext

        :param sid: The Twilio-provided string that uniquely identifies the Field resource to fetch.
        """
        return FieldContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> FieldContext:
        """
        Constructs a FieldContext

        :param sid: The Twilio-provided string that uniquely identifies the Field resource to fetch.
        """
        return FieldContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.FieldList>"
