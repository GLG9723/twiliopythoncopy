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
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class QueryInstance(InstanceResource):
    """
    :ivar account_sid: The unique ID of the Account that created this Query.
    :ivar date_created: The date that this resource was created
    :ivar date_updated: The date that this resource was last updated
    :ivar results: The natural language analysis results which include the Task recognized, the confidence score and a list of identified Fields.
    :ivar language: An ISO language-country string of the sample.
    :ivar model_build_sid: The unique ID of the Model Build queried.
    :ivar query: The end-user's natural language input.
    :ivar sample_sid: An optional reference to the Sample created from this query.
    :ivar assistant_sid: The unique ID of the parent Assistant.
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar status: A string that described the query status. The values can be: pending_review, reviewed, discarded
    :ivar url:
    :ivar source_channel: The communication channel where this end-user input came from
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        assistant_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.results: Optional[Dict[str, object]] = payload.get("results")
        self.language: Optional[str] = payload.get("language")
        self.model_build_sid: Optional[str] = payload.get("model_build_sid")
        self.query: Optional[str] = payload.get("query")
        self.sample_sid: Optional[str] = payload.get("sample_sid")
        self.assistant_sid: Optional[str] = payload.get("assistant_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.status: Optional[str] = payload.get("status")
        self.url: Optional[str] = payload.get("url")
        self.source_channel: Optional[str] = payload.get("source_channel")

        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid or self.sid,
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

    def update(
        self,
        sample_sid: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
    ) -> "QueryInstance":
        """
        Update the QueryInstance

        :param sample_sid: An optional reference to the Sample created from this query.
        :param status: A string that described the query status. The values can be: pending_review, reviewed, discarded

        :returns: The updated QueryInstance
        """
        return self._proxy.update(
            sample_sid=sample_sid,
            status=status,
        )

    async def update_async(
        self,
        sample_sid: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
    ) -> "QueryInstance":
        """
        Asynchronous coroutine to update the QueryInstance

        :param sample_sid: An optional reference to the Sample created from this query.
        :param status: A string that described the query status. The values can be: pending_review, reviewed, discarded

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

    def update(
        self,
        sample_sid: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
    ) -> QueryInstance:
        """
        Update the QueryInstance

        :param sample_sid: An optional reference to the Sample created from this query.
        :param status: A string that described the query status. The values can be: pending_review, reviewed, discarded

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
        self,
        sample_sid: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
    ) -> QueryInstance:
        """
        Asynchronous coroutine to update the QueryInstance

        :param sample_sid: An optional reference to the Sample created from this query.
        :param status: A string that described the query status. The values can be: pending_review, reviewed, discarded

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
    def get_instance(self, payload: Dict[str, Any]) -> QueryInstance:
        """
        Build an instance of QueryInstance

        :param payload: Payload response from the API
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
        language: str,
        query: str,
        tasks: Union[str, object] = values.unset,
        model_build: Union[str, object] = values.unset,
        field: Union[str, object] = values.unset,
    ) -> QueryInstance:
        """
        Create the QueryInstance

        :param language: An ISO language-country string of the sample.
        :param query: A user-provided string that uniquely identifies this resource as an alternative to the sid. It can be up to 2048 characters long.
        :param tasks: Constraints the query to a set of tasks. Useful when you need to constrain the paths the user can take. Tasks should be comma separated *task-unique-name-1*, *task-unique-name-2*
        :param model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param field: Constraints the query to a given Field with an task. Useful when you know the Field you are expecting. It accepts one field in the format *task-unique-name-1*:*field-unique-name*

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
        language: str,
        query: str,
        tasks: Union[str, object] = values.unset,
        model_build: Union[str, object] = values.unset,
        field: Union[str, object] = values.unset,
    ) -> QueryInstance:
        """
        Asynchronously create the QueryInstance

        :param language: An ISO language-country string of the sample.
        :param query: A user-provided string that uniquely identifies this resource as an alternative to the sid. It can be up to 2048 characters long.
        :param tasks: Constraints the query to a set of tasks. Useful when you need to constrain the paths the user can take. Tasks should be comma separated *task-unique-name-1*, *task-unique-name-2*
        :param model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param field: Constraints the query to a given Field with an task. Useful when you know the Field you are expecting. It accepts one field in the format *task-unique-name-1*:*field-unique-name*

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
        language: Union[str, object] = values.unset,
        model_build: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[QueryInstance]:
        """
        Streams QueryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str language: An ISO language-country string of the sample.
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
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
        language: Union[str, object] = values.unset,
        model_build: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[QueryInstance]:
        """
        Asynchronously streams QueryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str language: An ISO language-country string of the sample.
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
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

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        language: Union[str, object] = values.unset,
        model_build: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[QueryInstance]:
        """
        Lists QueryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str language: An ISO language-country string of the sample.
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
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
        language: Union[str, object] = values.unset,
        model_build: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[QueryInstance]:
        """
        Asynchronously lists QueryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str language: An ISO language-country string of the sample.
        :param str model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param str status: A string that described the query status. The values can be: pending_review, reviewed, discarded
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                language=language,
                model_build=model_build,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        language: Union[str, object] = values.unset,
        model_build: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> QueryPage:
        """
        Retrieve a single page of QueryInstance records from the API.
        Request is executed immediately

        :param language: An ISO language-country string of the sample.
        :param model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param status: A string that described the query status. The values can be: pending_review, reviewed, discarded
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

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
        language: Union[str, object] = values.unset,
        model_build: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> QueryPage:
        """
        Asynchronously retrieve a single page of QueryInstance records from the API.
        Request is executed immediately

        :param language: An ISO language-country string of the sample.
        :param model_build: The Model Build Sid or unique name of the Model Build to be queried.
        :param status: A string that described the query status. The values can be: pending_review, reviewed, discarded
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

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

    def get_page(self, target_url: str) -> QueryPage:
        """
        Retrieve a specific page of QueryInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of QueryInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return QueryPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> QueryPage:
        """
        Asynchronously retrieve a specific page of QueryInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of QueryInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return QueryPage(self._version, response, self._solution)

    def get(self, sid: str) -> QueryContext:
        """
        Constructs a QueryContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return QueryContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __call__(self, sid: str) -> QueryContext:
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
