r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
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


class CredentialListInstance(InstanceResource):
    def __init__(self, version, payload, trunk_sid: str, sid: Optional[str] = None):
        """
        Initialize the CredentialListInstance
        """
        super().__init__(version)

        self._account_sid: Optional[str] = payload.get("account_sid")
        self._sid: Optional[str] = payload.get("sid")
        self._trunk_sid: Optional[str] = payload.get("trunk_sid")
        self._friendly_name: Optional[str] = payload.get("friendly_name")
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self._url: Optional[str] = payload.get("url")

        self._solution = {
            "trunk_sid": trunk_sid,
            "sid": sid or self._sid,
        }
        self._context: Optional[CredentialListContext] = None

    @property
    def _proxy(self) -> "CredentialListContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CredentialListContext for this CredentialListInstance
        """
        if self._context is None:
            self._context = CredentialListContext(
                self._version,
                trunk_sid=self._solution["trunk_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialList resource.
        """
        return self._account_sid

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that we created to identify the CredentialList resource.
        """
        return self._sid

    @property
    def trunk_sid(self) -> Optional[str]:
        """
        :returns: The SID of the Trunk the credential list in associated with.
        """
        return self._trunk_sid

    @property
    def friendly_name(self) -> Optional[str]:
        """
        :returns: The string that you assigned to describe the resource.
        """
        return self._friendly_name

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
    def url(self) -> Optional[str]:
        """
        :returns: The absolute URL of the resource.
        """
        return self._url

    def delete(self) -> bool:
        """
        Deletes the CredentialListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CredentialListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "CredentialListInstance":
        """
        Fetch the CredentialListInstance


        :returns: The fetched CredentialListInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CredentialListInstance":
        """
        Asynchronous coroutine to fetch the CredentialListInstance


        :returns: The fetched CredentialListInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.CredentialListInstance {}>".format(context)


class CredentialListContext(InstanceContext):
    def __init__(self, version: Version, trunk_sid: str, sid: str):
        """
        Initialize the CredentialListContext

        :param version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to fetch the credential list.
        :param sid: The unique string that we created to identify the CredentialList resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
            "sid": sid,
        }
        self._uri = "/Trunks/{trunk_sid}/CredentialLists/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the CredentialListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CredentialListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> CredentialListInstance:
        """
        Fetch the CredentialListInstance


        :returns: The fetched CredentialListInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CredentialListInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CredentialListInstance:
        """
        Asynchronous coroutine to fetch the CredentialListInstance


        :returns: The fetched CredentialListInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CredentialListInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.CredentialListContext {}>".format(context)


class CredentialListPage(Page):
    def get_instance(self, payload) -> CredentialListInstance:
        """
        Build an instance of CredentialListInstance

        :param dict payload: Payload response from the API
        """
        return CredentialListInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.CredentialListPage>"


class CredentialListList(ListResource):
    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the CredentialListList

        :param version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to read the credential lists.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
        }
        self._uri = "/Trunks/{trunk_sid}/CredentialLists".format(**self._solution)

    def create(self, credential_list_sid) -> CredentialListInstance:
        """
        Create the CredentialListInstance

        :param str credential_list_sid: The SID of the [Credential List](https://www.twilio.com/docs/voice/sip/api/sip-credentiallist-resource) that you want to associate with the trunk. Once associated, we will authenticate access to the trunk against this list.

        :returns: The created CredentialListInstance
        """
        data = values.of(
            {
                "CredentialListSid": credential_list_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialListInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    async def create_async(self, credential_list_sid) -> CredentialListInstance:
        """
        Asynchronously create the CredentialListInstance

        :param str credential_list_sid: The SID of the [Credential List](https://www.twilio.com/docs/voice/sip/api/sip-credentiallist-resource) that you want to associate with the trunk. Once associated, we will authenticate access to the trunk against this list.

        :returns: The created CredentialListInstance
        """
        data = values.of(
            {
                "CredentialListSid": credential_list_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialListInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def stream(self, limit=None, page_size=None) -> List[CredentialListInstance]:
        """
        Streams CredentialListInstance records from the API as a generator stream.
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
    ) -> List[CredentialListInstance]:
        """
        Asynchronously streams CredentialListInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[CredentialListInstance]:
        """
        Lists CredentialListInstance records from the API as a list.
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
    ) -> List[CredentialListInstance]:
        """
        Asynchronously lists CredentialListInstance records from the API as a list.
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
    ) -> CredentialListPage:
        """
        Retrieve a single page of CredentialListInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialListInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CredentialListPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> CredentialListPage:
        """
        Asynchronously retrieve a single page of CredentialListInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialListInstance
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
        return CredentialListPage(self._version, response, self._solution)

    def get_page(self, target_url) -> CredentialListPage:
        """
        Retrieve a specific page of CredentialListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialListInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CredentialListPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> CredentialListPage:
        """
        Asynchronously retrieve a specific page of CredentialListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialListInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CredentialListPage(self._version, response, self._solution)

    def get(self, sid) -> CredentialListContext:
        """
        Constructs a CredentialListContext

        :param sid: The unique string that we created to identify the CredentialList resource to fetch.
        """
        return CredentialListContext(
            self._version, trunk_sid=self._solution["trunk_sid"], sid=sid
        )

    def __call__(self, sid) -> CredentialListContext:
        """
        Constructs a CredentialListContext

        :param sid: The unique string that we created to identify the CredentialList resource to fetch.
        """
        return CredentialListContext(
            self._version, trunk_sid=self._solution["trunk_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.CredentialListList>"
