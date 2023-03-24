r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Content
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Dict, List, Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ContentAndApprovalsInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the ContentAndApprovalsInstance
        """
        super().__init__(version)

        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self._sid: Optional[str] = payload.get("sid")
        self._account_sid: Optional[str] = payload.get("account_sid")
        self._friendly_name: Optional[str] = payload.get("friendly_name")
        self._language: Optional[str] = payload.get("language")
        self._variables: Optional[Dict[str, object]] = payload.get("variables")
        self._types: Optional[Dict[str, object]] = payload.get("types")
        self._approval_requests: Optional[Dict[str, object]] = payload.get(
            "approval_requests"
        )

        self._solution = {}

    @property
    def date_created(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._date_created

    @property
    def date_updated(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._date_updated

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that that we created to identify the Content resource.
        """
        return self._sid

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource.
        """
        return self._account_sid

    @property
    def friendly_name(self) -> Optional[str]:
        """
        :returns: A string name used to describe the Content resource. Not visible to the end recipient.
        """
        return self._friendly_name

    @property
    def language(self) -> Optional[str]:
        """
        :returns: Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in.
        """
        return self._language

    @property
    def variables(self) -> Optional[Dict[str, object]]:
        """
        :returns: Defines the default placeholder values for variables included in the Content resource. e.g. {\"1\": \"Customer_Name\"}.
        """
        return self._variables

    @property
    def types(self) -> Optional[Dict[str, object]]:
        """
        :returns: The [Content types](https://www.twilio.com/docs/content-api/content-types-overview) (e.g. twilio/text) for this Content resource.
        """
        return self._types

    @property
    def approval_requests(self) -> Optional[Dict[str, object]]:
        """
        :returns: The submitted information and approval request status of the Content resource.
        """
        return self._approval_requests

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Content.V1.ContentAndApprovalsInstance {}>".format(context)


class ContentAndApprovalsPage(Page):
    def get_instance(self, payload) -> ContentAndApprovalsInstance:
        """
        Build an instance of ContentAndApprovalsInstance

        :param dict payload: Payload response from the API
        """
        return ContentAndApprovalsInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Content.V1.ContentAndApprovalsPage>"


class ContentAndApprovalsList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ContentAndApprovalsList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/ContentAndApprovals"

    def stream(self, limit=None, page_size=None) -> List[ContentAndApprovalsInstance]:
        """
        Streams ContentAndApprovalsInstance records from the API as a generator stream.
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

    async def stream_async(
        self, limit=None, page_size=None
    ) -> List[ContentAndApprovalsInstance]:
        """
        Asynchronously streams ContentAndApprovalsInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[ContentAndApprovalsInstance]:
        """
        Lists ContentAndApprovalsInstance records from the API as a list.
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

    async def list_async(
        self, limit=None, page_size=None
    ) -> List[ContentAndApprovalsInstance]:
        """
        Asynchronously lists ContentAndApprovalsInstance records from the API as a list.
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
    ) -> ContentAndApprovalsPage:
        """
        Retrieve a single page of ContentAndApprovalsInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ContentAndApprovalsInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ContentAndApprovalsPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> ContentAndApprovalsPage:
        """
        Asynchronously retrieve a single page of ContentAndApprovalsInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ContentAndApprovalsInstance
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
        return ContentAndApprovalsPage(self._version, response)

    def get_page(self, target_url) -> ContentAndApprovalsPage:
        """
        Retrieve a specific page of ContentAndApprovalsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ContentAndApprovalsInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ContentAndApprovalsPage(self._version, response)

    async def get_page_async(self, target_url) -> ContentAndApprovalsPage:
        """
        Asynchronously retrieve a specific page of ContentAndApprovalsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ContentAndApprovalsInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ContentAndApprovalsPage(self._version, response)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Content.V1.ContentAndApprovalsList>"
