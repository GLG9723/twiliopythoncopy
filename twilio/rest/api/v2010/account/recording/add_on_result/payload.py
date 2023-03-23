r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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


class PayloadInstance(InstanceResource):
    def __init__(
        self,
        version,
        payload,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        sid: Optional[str] = None,
    ):
        """
        Initialize the PayloadInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "add_on_result_sid": payload.get("add_on_result_sid"),
            "account_sid": payload.get("account_sid"),
            "label": payload.get("label"),
            "add_on_sid": payload.get("add_on_sid"),
            "add_on_configuration_sid": payload.get("add_on_configuration_sid"),
            "content_type": payload.get("content_type"),
            "date_created": deserialize.rfc2822_datetime(payload.get("date_created")),
            "date_updated": deserialize.rfc2822_datetime(payload.get("date_updated")),
            "reference_sid": payload.get("reference_sid"),
            "subresource_uris": payload.get("subresource_uris"),
        }

        self._solution = {
            "account_sid": account_sid,
            "reference_sid": reference_sid,
            "add_on_result_sid": add_on_result_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[PayloadContext] = None

    @property
    def _proxy(self) -> "PayloadContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PayloadContext for this PayloadInstance
        """
        if self._context is None:
            self._context = PayloadContext(
                self._version,
                account_sid=self._solution["account_sid"],
                reference_sid=self._solution["reference_sid"],
                add_on_result_sid=self._solution["add_on_result_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> str:
        """
        :returns: The unique string that that we created to identify the Recording AddOnResult Payload resource.
        """
        return self._properties["sid"]

    @property
    def add_on_result_sid(self) -> str:
        """
        :returns: The SID of the AddOnResult to which the payload belongs.
        """
        return self._properties["add_on_result_sid"]

    @property
    def account_sid(self) -> str:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resource.
        """
        return self._properties["account_sid"]

    @property
    def label(self) -> str:
        """
        :returns: The string provided by the vendor that describes the payload.
        """
        return self._properties["label"]

    @property
    def add_on_sid(self) -> str:
        """
        :returns: The SID of the Add-on to which the result belongs.
        """
        return self._properties["add_on_sid"]

    @property
    def add_on_configuration_sid(self) -> str:
        """
        :returns: The SID of the Add-on configuration.
        """
        return self._properties["add_on_configuration_sid"]

    @property
    def content_type(self) -> str:
        """
        :returns: The MIME type of the payload.
        """
        return self._properties["content_type"]

    @property
    def date_created(self) -> datetime:
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._properties["date_updated"]

    @property
    def reference_sid(self) -> str:
        """
        :returns: The SID of the recording to which the AddOnResult resource that contains the payload belongs.
        """
        return self._properties["reference_sid"]

    @property
    def subresource_uris(self) -> dict:
        """
        :returns: A list of related resources identified by their relative URIs.
        """
        return self._properties["subresource_uris"]

    def delete(self) -> bool:
        """
        Deletes the PayloadInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the PayloadInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "PayloadInstance":
        """
        Fetch the PayloadInstance


        :returns: The fetched PayloadInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "PayloadInstance":
        """
        Asynchronous coroutine to fetch the PayloadInstance


        :returns: The fetched PayloadInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.PayloadInstance {}>".format(context)


class PayloadContext(InstanceContext):
    def __init__(
        self,
        version: Version,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
        sid: str,
    ):
        """
        Initialize the PayloadContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resource to fetch.
        :param reference_sid: The SID of the recording to which the AddOnResult resource that contains the payload to fetch belongs.
        :param add_on_result_sid: The SID of the AddOnResult to which the payload to fetch belongs.
        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "reference_sid": reference_sid,
            "add_on_result_sid": add_on_result_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads/{sid}.json".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the PayloadInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the PayloadInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> PayloadInstance:
        """
        Fetch the PayloadInstance


        :returns: The fetched PayloadInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return PayloadInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            reference_sid=self._solution["reference_sid"],
            add_on_result_sid=self._solution["add_on_result_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> PayloadInstance:
        """
        Asynchronous coroutine to fetch the PayloadInstance


        :returns: The fetched PayloadInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return PayloadInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            reference_sid=self._solution["reference_sid"],
            add_on_result_sid=self._solution["add_on_result_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.PayloadContext {}>".format(context)


class PayloadPage(Page):
    def get_instance(self, payload) -> PayloadInstance:
        """
        Build an instance of PayloadInstance

        :param dict payload: Payload response from the API
        """
        return PayloadInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            reference_sid=self._solution["reference_sid"],
            add_on_result_sid=self._solution["add_on_result_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.PayloadPage>"


class PayloadList(ListResource):
    def __init__(
        self,
        version: Version,
        account_sid: str,
        reference_sid: str,
        add_on_result_sid: str,
    ):
        """
        Initialize the PayloadList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult Payload resources to read.
        :param reference_sid: The SID of the recording to which the AddOnResult resource that contains the payloads to read belongs.
        :param add_on_result_sid: The SID of the AddOnResult to which the payloads to read belongs.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "reference_sid": reference_sid,
            "add_on_result_sid": add_on_result_sid,
        }
        self._uri = "/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads.json".format(
            **self._solution
        )

    def stream(self, limit=None, page_size=None) -> List[PayloadInstance]:
        """
        Streams PayloadInstance records from the API as a generator stream.
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

    async def stream_async(self, limit=None, page_size=None) -> List[PayloadInstance]:
        """
        Asynchronously streams PayloadInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[PayloadInstance]:
        """
        Lists PayloadInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[PayloadInstance]:
        """
        Asynchronously lists PayloadInstance records from the API as a list.
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
    ) -> PayloadPage:
        """
        Retrieve a single page of PayloadInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PayloadInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return PayloadPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> PayloadPage:
        """
        Asynchronously retrieve a single page of PayloadInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PayloadInstance
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
        return PayloadPage(self._version, response, self._solution)

    def get_page(self, target_url) -> PayloadPage:
        """
        Retrieve a specific page of PayloadInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PayloadInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return PayloadPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> PayloadPage:
        """
        Asynchronously retrieve a specific page of PayloadInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PayloadInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return PayloadPage(self._version, response, self._solution)

    def get(self, sid) -> PayloadContext:
        """
        Constructs a PayloadContext

        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch.
        """
        return PayloadContext(
            self._version,
            account_sid=self._solution["account_sid"],
            reference_sid=self._solution["reference_sid"],
            add_on_result_sid=self._solution["add_on_result_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> PayloadContext:
        """
        Constructs a PayloadContext

        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult Payload resource to fetch.
        """
        return PayloadContext(
            self._version,
            account_sid=self._solution["account_sid"],
            reference_sid=self._solution["reference_sid"],
            add_on_result_sid=self._solution["add_on_result_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.PayloadList>"
