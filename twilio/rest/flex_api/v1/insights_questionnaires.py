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

from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InsightsQuestionnairesInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Insights resource and owns this resource.
    :ivar questionnaire_sid: The sid of this questionnaire
    :ivar name: The name of this category.
    :ivar description: The description of this questionnaire
    :ivar active: The flag to enable or disable questionnaire
    :ivar questions: The list of questions with category for a questionnaire
    :ivar url:
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        questionnaire_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.questionnaire_sid: Optional[str] = payload.get("questionnaire_sid")
        self.name: Optional[str] = payload.get("name")
        self.description: Optional[str] = payload.get("description")
        self.active: Optional[bool] = payload.get("active")
        self.questions: Optional[List[Dict[str, object]]] = payload.get("questions")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "questionnaire_sid": questionnaire_sid or self.questionnaire_sid,
        }
        self._context: Optional[InsightsQuestionnairesContext] = None

    @property
    def _proxy(self) -> "InsightsQuestionnairesContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InsightsQuestionnairesContext for this InsightsQuestionnairesInstance
        """
        if self._context is None:
            self._context = InsightsQuestionnairesContext(
                self._version,
                questionnaire_sid=self._solution["questionnaire_sid"],
            )
        return self._context

    def delete(self, authorization: Union[str, object] = values.unset) -> bool:
        """
        Deletes the InsightsQuestionnairesInstance

        :param authorization: The Authorization HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            authorization=authorization,
        )

    async def delete_async(
        self, authorization: Union[str, object] = values.unset
    ) -> bool:
        """
        Asynchronous coroutine that deletes the InsightsQuestionnairesInstance

        :param authorization: The Authorization HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            authorization=authorization,
        )

    def fetch(
        self, authorization: Union[str, object] = values.unset
    ) -> "InsightsQuestionnairesInstance":
        """
        Fetch the InsightsQuestionnairesInstance

        :param authorization: The Authorization HTTP request header

        :returns: The fetched InsightsQuestionnairesInstance
        """
        return self._proxy.fetch(
            authorization=authorization,
        )

    async def fetch_async(
        self, authorization: Union[str, object] = values.unset
    ) -> "InsightsQuestionnairesInstance":
        """
        Asynchronous coroutine to fetch the InsightsQuestionnairesInstance

        :param authorization: The Authorization HTTP request header

        :returns: The fetched InsightsQuestionnairesInstance
        """
        return await self._proxy.fetch_async(
            authorization=authorization,
        )

    def update(
        self,
        active: bool,
        authorization: Union[str, object] = values.unset,
        name: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
        question_sids: Union[List[str], object] = values.unset,
    ) -> "InsightsQuestionnairesInstance":
        """
        Update the InsightsQuestionnairesInstance

        :param active: The flag to enable or disable questionnaire
        :param authorization: The Authorization HTTP request header
        :param name: The name of this questionnaire
        :param description: The description of this questionnaire
        :param question_sids: The list of questions sids under a questionnaire

        :returns: The updated InsightsQuestionnairesInstance
        """
        return self._proxy.update(
            active=active,
            authorization=authorization,
            name=name,
            description=description,
            question_sids=question_sids,
        )

    async def update_async(
        self,
        active: bool,
        authorization: Union[str, object] = values.unset,
        name: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
        question_sids: Union[List[str], object] = values.unset,
    ) -> "InsightsQuestionnairesInstance":
        """
        Asynchronous coroutine to update the InsightsQuestionnairesInstance

        :param active: The flag to enable or disable questionnaire
        :param authorization: The Authorization HTTP request header
        :param name: The name of this questionnaire
        :param description: The description of this questionnaire
        :param question_sids: The list of questions sids under a questionnaire

        :returns: The updated InsightsQuestionnairesInstance
        """
        return await self._proxy.update_async(
            active=active,
            authorization=authorization,
            name=name,
            description=description,
            question_sids=question_sids,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.FlexApi.V1.InsightsQuestionnairesInstance {context}>"


class InsightsQuestionnairesContext(InstanceContext):

    def __init__(self, version: Version, questionnaire_sid: str):
        """
        Initialize the InsightsQuestionnairesContext

        :param version: Version that contains the resource
        :param questionnaire_sid: The SID of the questionnaire
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "questionnaire_sid": questionnaire_sid,
        }
        self._uri = (
            "/Insights/QualityManagement/Questionnaires/{questionnaire_sid}".format(
                **self._solution
            )
        )

    def delete(self, authorization: Union[str, object] = values.unset) -> bool:
        """
        Deletes the InsightsQuestionnairesInstance

        :param authorization: The Authorization HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "Authorization": authorization,
            }
        )

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(
        self, authorization: Union[str, object] = values.unset
    ) -> bool:
        """
        Asynchronous coroutine that deletes the InsightsQuestionnairesInstance

        :param authorization: The Authorization HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "Authorization": authorization,
            }
        )

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def fetch(
        self, authorization: Union[str, object] = values.unset
    ) -> InsightsQuestionnairesInstance:
        """
        Fetch the InsightsQuestionnairesInstance

        :param authorization: The Authorization HTTP request header

        :returns: The fetched InsightsQuestionnairesInstance
        """

        data = values.of(
            {
                "Authorization": authorization,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return InsightsQuestionnairesInstance(
            self._version,
            payload,
            questionnaire_sid=self._solution["questionnaire_sid"],
        )

    async def fetch_async(
        self, authorization: Union[str, object] = values.unset
    ) -> InsightsQuestionnairesInstance:
        """
        Asynchronous coroutine to fetch the InsightsQuestionnairesInstance

        :param authorization: The Authorization HTTP request header

        :returns: The fetched InsightsQuestionnairesInstance
        """

        data = values.of(
            {
                "Authorization": authorization,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return InsightsQuestionnairesInstance(
            self._version,
            payload,
            questionnaire_sid=self._solution["questionnaire_sid"],
        )

    def update(
        self,
        active: bool,
        authorization: Union[str, object] = values.unset,
        name: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
        question_sids: Union[List[str], object] = values.unset,
    ) -> InsightsQuestionnairesInstance:
        """
        Update the InsightsQuestionnairesInstance

        :param active: The flag to enable or disable questionnaire
        :param authorization: The Authorization HTTP request header
        :param name: The name of this questionnaire
        :param description: The description of this questionnaire
        :param question_sids: The list of questions sids under a questionnaire

        :returns: The updated InsightsQuestionnairesInstance
        """
        data = values.of(
            {
                "Active": serialize.boolean_to_string(active),
                "Name": name,
                "Description": description,
                "QuestionSids": serialize.map(question_sids, lambda e: e),
            }
        )
        headers = values.of(
            {
                "Authorization": authorization,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsQuestionnairesInstance(
            self._version,
            payload,
            questionnaire_sid=self._solution["questionnaire_sid"],
        )

    async def update_async(
        self,
        active: bool,
        authorization: Union[str, object] = values.unset,
        name: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
        question_sids: Union[List[str], object] = values.unset,
    ) -> InsightsQuestionnairesInstance:
        """
        Asynchronous coroutine to update the InsightsQuestionnairesInstance

        :param active: The flag to enable or disable questionnaire
        :param authorization: The Authorization HTTP request header
        :param name: The name of this questionnaire
        :param description: The description of this questionnaire
        :param question_sids: The list of questions sids under a questionnaire

        :returns: The updated InsightsQuestionnairesInstance
        """
        data = values.of(
            {
                "Active": serialize.boolean_to_string(active),
                "Name": name,
                "Description": description,
                "QuestionSids": serialize.map(question_sids, lambda e: e),
            }
        )
        headers = values.of(
            {
                "Authorization": authorization,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsQuestionnairesInstance(
            self._version,
            payload,
            questionnaire_sid=self._solution["questionnaire_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.FlexApi.V1.InsightsQuestionnairesContext {context}>"


class InsightsQuestionnairesPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> InsightsQuestionnairesInstance:
        """
        Build an instance of InsightsQuestionnairesInstance

        :param payload: Payload response from the API
        """
        return InsightsQuestionnairesInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsQuestionnairesPage>"


class InsightsQuestionnairesList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InsightsQuestionnairesList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Insights/QualityManagement/Questionnaires"

    def create(
        self,
        name: str,
        authorization: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
        active: Union[bool, object] = values.unset,
        question_sids: Union[List[str], object] = values.unset,
    ) -> InsightsQuestionnairesInstance:
        """
        Create the InsightsQuestionnairesInstance

        :param name: The name of this questionnaire
        :param authorization: The Authorization HTTP request header
        :param description: The description of this questionnaire
        :param active: The flag to enable or disable questionnaire
        :param question_sids: The list of questions sids under a questionnaire

        :returns: The created InsightsQuestionnairesInstance
        """

        data = values.of(
            {
                "Name": name,
                "Description": description,
                "Active": serialize.boolean_to_string(active),
                "QuestionSids": serialize.map(question_sids, lambda e: e),
            }
        )
        headers = values.of(
            {
                "Authorization": authorization,
                "Content-Type": "application/x-www-form-urlencoded",
            }
        )

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsQuestionnairesInstance(self._version, payload)

    async def create_async(
        self,
        name: str,
        authorization: Union[str, object] = values.unset,
        description: Union[str, object] = values.unset,
        active: Union[bool, object] = values.unset,
        question_sids: Union[List[str], object] = values.unset,
    ) -> InsightsQuestionnairesInstance:
        """
        Asynchronously create the InsightsQuestionnairesInstance

        :param name: The name of this questionnaire
        :param authorization: The Authorization HTTP request header
        :param description: The description of this questionnaire
        :param active: The flag to enable or disable questionnaire
        :param question_sids: The list of questions sids under a questionnaire

        :returns: The created InsightsQuestionnairesInstance
        """

        data = values.of(
            {
                "Name": name,
                "Description": description,
                "Active": serialize.boolean_to_string(active),
                "QuestionSids": serialize.map(question_sids, lambda e: e),
            }
        )
        headers = values.of(
            {
                "Authorization": authorization,
                "Content-Type": "application/x-www-form-urlencoded",
            }
        )

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsQuestionnairesInstance(self._version, payload)

    def stream(
        self,
        authorization: Union[str, object] = values.unset,
        include_inactive: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[InsightsQuestionnairesInstance]:
        """
        Streams InsightsQuestionnairesInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str authorization: The Authorization HTTP request header
        :param bool include_inactive: Flag indicating whether to include inactive questionnaires or not
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
            authorization=authorization,
            include_inactive=include_inactive,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        authorization: Union[str, object] = values.unset,
        include_inactive: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[InsightsQuestionnairesInstance]:
        """
        Asynchronously streams InsightsQuestionnairesInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str authorization: The Authorization HTTP request header
        :param bool include_inactive: Flag indicating whether to include inactive questionnaires or not
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
            authorization=authorization,
            include_inactive=include_inactive,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        authorization: Union[str, object] = values.unset,
        include_inactive: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsQuestionnairesInstance]:
        """
        Lists InsightsQuestionnairesInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str authorization: The Authorization HTTP request header
        :param bool include_inactive: Flag indicating whether to include inactive questionnaires or not
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
                authorization=authorization,
                include_inactive=include_inactive,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        authorization: Union[str, object] = values.unset,
        include_inactive: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsQuestionnairesInstance]:
        """
        Asynchronously lists InsightsQuestionnairesInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str authorization: The Authorization HTTP request header
        :param bool include_inactive: Flag indicating whether to include inactive questionnaires or not
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
                authorization=authorization,
                include_inactive=include_inactive,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        authorization: Union[str, object] = values.unset,
        include_inactive: Union[bool, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InsightsQuestionnairesPage:
        """
        Retrieve a single page of InsightsQuestionnairesInstance records from the API.
        Request is executed immediately

        :param authorization: The Authorization HTTP request header
        :param include_inactive: Flag indicating whether to include inactive questionnaires or not
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsQuestionnairesInstance
        """
        data = values.of(
            {
                "Authorization": authorization,
                "IncludeInactive": serialize.boolean_to_string(include_inactive),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InsightsQuestionnairesPage(self._version, response)

    async def page_async(
        self,
        authorization: Union[str, object] = values.unset,
        include_inactive: Union[bool, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InsightsQuestionnairesPage:
        """
        Asynchronously retrieve a single page of InsightsQuestionnairesInstance records from the API.
        Request is executed immediately

        :param authorization: The Authorization HTTP request header
        :param include_inactive: Flag indicating whether to include inactive questionnaires or not
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsQuestionnairesInstance
        """
        data = values.of(
            {
                "Authorization": authorization,
                "IncludeInactive": serialize.boolean_to_string(include_inactive),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return InsightsQuestionnairesPage(self._version, response)

    def get_page(self, target_url: str) -> InsightsQuestionnairesPage:
        """
        Retrieve a specific page of InsightsQuestionnairesInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InsightsQuestionnairesInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InsightsQuestionnairesPage(self._version, response)

    async def get_page_async(self, target_url: str) -> InsightsQuestionnairesPage:
        """
        Asynchronously retrieve a specific page of InsightsQuestionnairesInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InsightsQuestionnairesInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InsightsQuestionnairesPage(self._version, response)

    def get(self, questionnaire_sid: str) -> InsightsQuestionnairesContext:
        """
        Constructs a InsightsQuestionnairesContext

        :param questionnaire_sid: The SID of the questionnaire
        """
        return InsightsQuestionnairesContext(
            self._version, questionnaire_sid=questionnaire_sid
        )

    def __call__(self, questionnaire_sid: str) -> InsightsQuestionnairesContext:
        """
        Constructs a InsightsQuestionnairesContext

        :param questionnaire_sid: The SID of the questionnaire
        """
        return InsightsQuestionnairesContext(
            self._version, questionnaire_sid=questionnaire_sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsQuestionnairesList>"
