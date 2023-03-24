r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
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


class QueryInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, sid: Optional[str] = None):
        """
        Initialize the QueryInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "results": payload.get("results"),
            "language": payload.get("language"),
            "model_build_sid": payload.get("model_build_sid"),
            "query": payload.get("query"),
            "sample_sid": payload.get("sample_sid"),
            "assistant_sid": payload.get("assistant_sid"),
            "sid": payload.get("sid"),
            "status": payload.get("status"),
            "url": payload.get("url"),
            "source_channel": payload.get("source_channel"),
        }

        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[QueryContext] = None

    @property
    def _proxy(self) -> "QueryContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: QueryContext for this QueryInstance
        """
        if self._context is None:
            self._context = QueryContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self) -> str:
        """
        :returns: The unique ID of the Account that created this Query.
        """
        return self._properties["account_sid"]

    @property
    def date_created(self) -> datetime:
        """
        :returns: The date that this resource was created
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns: The date that this resource was last updated
        """
        return self._properties["date_updated"]

    @property
    def results(self) -> dict:
        """
        :returns: The natural language analysis results which include the Task recognized, the confidence score and a list of identified Fields.
        """
        return self._properties["results"]

    @property
    def language(self) -> str:
        """
        :returns: An ISO language-country string of the sample.
        """
        return self._properties["language"]

    @property
    def model_build_sid(self) -> str:
        """
        :returns: The unique ID of the Model Build queried.
        """
        return self._properties["model_build_sid"]

    @property
    def query(self) -> str:
        """
        :returns: The end-user's natural language input.
        """
        return self._properties["query"]

    @property
    def sample_sid(self) -> str:
        """
        :returns: An optional reference to the Sample created from this query.
        """
        return self._properties["sample_sid"]

    @property
    def assistant_sid(self) -> str:
        """
        :returns: The unique ID of the parent Assistant.
        """
        return self._properties["assistant_sid"]

    @property
    def sid(self) -> str:
        """
        :returns: A 34 character string that uniquely identifies this resource.
        """
        return self._properties["sid"]

    @property
    def status(self) -> str:
        """
        :returns: A string that described the query status. The values can be: pending_review, reviewed, discarded
        """
        return self._properties["status"]

    @property
    def url(self) -> str:
        """
        :returns:
        """
        return self._properties["url"]

    @property
    def source_channel(self) -> str:
        """
        :returns: The communication channel where this end-user input came from
        """
        return self._properties["source_channel"]

    def delete(self) -> bool:
        """
        Deletes the QueryInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the QueryInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "QueryInstance":
        """
        Fetch the QueryInstance


        :returns: The fetched QueryInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "QueryInstance":
        """
        Asynchronous coroutine to fetch the QueryInstance


        :returns: The fetched QueryInstance
        """
        return await self._proxy.fetch_async()

    def update(self, sample_sid=values.unset, status=values.unset) -> "QueryInstance":
        """
        Update the QueryInstance

        :param str sample_sid: An optional reference to the Sample created from this query.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded

        :returns: The updated QueryInstance
        """
        return self._proxy.update(
            sample_sid=sample_sid,
            status=status,
        )

    async def update_async(
        self, sample_sid=values.unset, status=values.unset
    ) -> "QueryInstance":
        """
        Asynchronous coroutine to update the QueryInstance

        :param str sample_sid: An optional reference to the Sample created from this query.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded

        :returns: The updated QueryInstance
        """
        return await self._proxy.update_async(
            sample_sid=sample_sid,
            status=status,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.QueryInstance {}>".format(context)


class QueryContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, sid: str):
        """
        Initialize the QueryContext

        :param version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.
        :param sid: A 34 character string that uniquely identifies this resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Queries/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the QueryInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the QueryInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> QueryInstance:
        """
        Fetch the QueryInstance


        :returns: The fetched QueryInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return QueryInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> QueryInstance:
        """
        Asynchronous coroutine to fetch the QueryInstance


        :returns: The fetched QueryInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return QueryInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    def update(self, sample_sid=values.unset, status=values.unset) -> QueryInstance:
        """
        Update the QueryInstance

        :param str sample_sid: An optional reference to the Sample created from this query.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded

        :returns: The updated QueryInstance
        """
        data = values.of(
            {
                "SampleSid": sample_sid,
                "Status": status,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return QueryInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, sample_sid=values.unset, status=values.unset
    ) -> QueryInstance:
        """
        Asynchronous coroutine to update the QueryInstance

        :param str sample_sid: An optional reference to the Sample created from this query.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded

        :returns: The updated QueryInstance
        """
        data = values.of(
            {
                "SampleSid": sample_sid,
                "Status": status,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return QueryInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.QueryContext {}>".format(context)


class QueryPage(Page):
    def get_instance(self, payload) -> QueryInstance:
        """
        Build an instance of QueryInstance

        :param dict payload: Payload response from the API
        """
        return QueryInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Understand.QueryPage>"


class QueryList(ListResource):
    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the QueryList

        :param version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Queries".format(**self._solution)

    def create(
        self,
        language,
        query,
        tasks=values.unset,
        model_build=values.unset,
        field=values.unset,
    ) -> QueryInstance:
        """
        Create the QueryInstance

        :param str language: An ISO language-country string of the sample.
        :param str query: A user-provided string that uniquely identifies this resource as an alternative to the sid. It can be up to 2048 characters long.
        :param str tasks: Constraints the query to a set of tasks. Useful when you need to constrain the paths the user can take. Tasks should be comma separated *task-unique-name-1*, *task-unique-name-2*
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str field: Constraints the query to a given Field with an task. Useful when you know the Field you are expecting. It accepts one field in the format *task-unique-name-1*:*field-unique-name*

        :returns: The created QueryInstance
        """
        data = values.of(
            {
                "Language": language,
                "Query": query,
                "Tasks": tasks,
                "ModelBuild": model_build,
                "Field": field,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return QueryInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    async def create_async(
        self,
        language,
        query,
        tasks=values.unset,
        model_build=values.unset,
        field=values.unset,
    ) -> QueryInstance:
        """
        Asynchronously create the QueryInstance

        :param str language: An ISO language-country string of the sample.
        :param str query: A user-provided string that uniquely identifies this resource as an alternative to the sid. It can be up to 2048 characters long.
        :param str tasks: Constraints the query to a set of tasks. Useful when you need to constrain the paths the user can take. Tasks should be comma separated *task-unique-name-1*, *task-unique-name-2*
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str field: Constraints the query to a given Field with an task. Useful when you know the Field you are expecting. It accepts one field in the format *task-unique-name-1*:*field-unique-name*

        :returns: The created QueryInstance
        """
        data = values.of(
            {
                "Language": language,
                "Query": query,
                "Tasks": tasks,
                "ModelBuild": model_build,
                "Field": field,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return QueryInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    def stream(
        self,
        language=values.unset,
        model_build=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ) -> List[QueryInstance]:
        """
        Streams QueryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str language: An ISO language-country string of the sample.
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            language=language,
            model_build=model_build,
            status=status,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        language=values.unset,
        model_build=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ) -> List[QueryInstance]:
        """
        Asynchronously streams QueryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str language: An ISO language-country string of the sample.
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            language=language,
            model_build=model_build,
            status=status,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        language=values.unset,
        model_build=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ) -> List[QueryInstance]:
        """
        Lists QueryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str language: An ISO language-country string of the sample.
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded
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
                language=language,
                model_build=model_build,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        language=values.unset,
        model_build=values.unset,
        status=values.unset,
        limit=None,
        page_size=None,
    ) -> List[QueryInstance]:
        """
        Asynchronously lists QueryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str language: An ISO language-country string of the sample.
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded
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
                language=language,
                model_build=model_build,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        language=values.unset,
        model_build=values.unset,
        status=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> QueryPage:
        """
        Retrieve a single page of QueryInstance records from the API.
        Request is executed immediately

        :param str language: An ISO language-country string of the sample.
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of QueryInstance
        """
        data = values.of(
            {
                "Language": language,
                "ModelBuild": model_build,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return QueryPage(self._version, response, self._solution)

    async def page_async(
        self,
        language=values.unset,
        model_build=values.unset,
        status=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> QueryPage:
        """
        Asynchronously retrieve a single page of QueryInstance records from the API.
        Request is executed immediately

        :param str language: An ISO language-country string of the sample.
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of QueryInstance
        """
        data = values.of(
            {
                "Language": language,
                "ModelBuild": model_build,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return QueryPage(self._version, response, self._solution)

    def get_page(self, target_url) -> QueryPage:
        """
        Retrieve a specific page of QueryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of QueryInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return QueryPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> QueryPage:
        """
        Asynchronously retrieve a specific page of QueryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of QueryInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return QueryPage(self._version, response, self._solution)

    def get(self, sid) -> QueryContext:
        """
        Constructs a QueryContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return QueryContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __call__(self, sid) -> QueryContext:
        """
        Constructs a QueryContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return QueryContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Understand.QueryList>"
