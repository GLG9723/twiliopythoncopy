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


class AuthRegistrationsCredentialListMappingInstance(InstanceResource):
    def __init__(
        self,
        version,
        payload,
        account_sid: str,
        domain_sid: str,
        sid: Optional[str] = None,
    ):
        """
        Initialize the AuthRegistrationsCredentialListMappingInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "date_created": deserialize.rfc2822_datetime(payload.get("date_created")),
            "date_updated": deserialize.rfc2822_datetime(payload.get("date_updated")),
            "friendly_name": payload.get("friendly_name"),
            "sid": payload.get("sid"),
        }

        self._solution = {
            "account_sid": account_sid,
            "domain_sid": domain_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[AuthRegistrationsCredentialListMappingContext] = None

    @property
    def _proxy(self) -> "AuthRegistrationsCredentialListMappingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AuthRegistrationsCredentialListMappingContext for this AuthRegistrationsCredentialListMappingInstance
        """
        if self._context is None:
            self._context = AuthRegistrationsCredentialListMappingContext(
                self._version,
                account_sid=self._solution["account_sid"],
                domain_sid=self._solution["domain_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self) -> str:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource.
        """
        return self._properties["account_sid"]

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
    def friendly_name(self) -> str:
        """
        :returns: The string that you assigned to describe the resource.
        """
        return self._properties["friendly_name"]

    @property
    def sid(self) -> str:
        """
        :returns: The unique string that that we created to identify the CredentialListMapping resource.
        """
        return self._properties["sid"]

    def delete(self) -> bool:
        """
        Deletes the AuthRegistrationsCredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AuthRegistrationsCredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "AuthRegistrationsCredentialListMappingInstance":
        """
        Fetch the AuthRegistrationsCredentialListMappingInstance


        :returns: The fetched AuthRegistrationsCredentialListMappingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AuthRegistrationsCredentialListMappingInstance":
        """
        Asynchronous coroutine to fetch the AuthRegistrationsCredentialListMappingInstance


        :returns: The fetched AuthRegistrationsCredentialListMappingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AuthRegistrationsCredentialListMappingInstance {}>".format(
            context
        )


class AuthRegistrationsCredentialListMappingContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, domain_sid: str, sid: str):
        """
        Initialize the AuthRegistrationsCredentialListMappingContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch.
        :param domain_sid: The SID of the SIP domain that contains the resource to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "domain_sid": domain_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings/{sid}.json".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the AuthRegistrationsCredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AuthRegistrationsCredentialListMappingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> AuthRegistrationsCredentialListMappingInstance:
        """
        Fetch the AuthRegistrationsCredentialListMappingInstance


        :returns: The fetched AuthRegistrationsCredentialListMappingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AuthRegistrationsCredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AuthRegistrationsCredentialListMappingInstance:
        """
        Asynchronous coroutine to fetch the AuthRegistrationsCredentialListMappingInstance


        :returns: The fetched AuthRegistrationsCredentialListMappingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AuthRegistrationsCredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AuthRegistrationsCredentialListMappingContext {}>".format(
            context
        )


class AuthRegistrationsCredentialListMappingPage(Page):
    def get_instance(self, payload) -> AuthRegistrationsCredentialListMappingInstance:
        """
        Build an instance of AuthRegistrationsCredentialListMappingInstance

        :param dict payload: Payload response from the API
        """
        return AuthRegistrationsCredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AuthRegistrationsCredentialListMappingPage>"


class AuthRegistrationsCredentialListMappingList(ListResource):
    def __init__(self, version: Version, account_sid: str, domain_sid: str):
        """
        Initialize the AuthRegistrationsCredentialListMappingList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read.
        :param domain_sid: The SID of the SIP domain that contains the resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "domain_sid": domain_sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/Domains/{domain_sid}/Auth/Registrations/CredentialListMappings.json".format(
            **self._solution
        )

    def create(
        self, credential_list_sid
    ) -> AuthRegistrationsCredentialListMappingInstance:
        """
        Create the AuthRegistrationsCredentialListMappingInstance

        :param str credential_list_sid: The SID of the CredentialList resource to map to the SIP domain.

        :returns: The created AuthRegistrationsCredentialListMappingInstance
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

        return AuthRegistrationsCredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
        )

    async def create_async(
        self, credential_list_sid
    ) -> AuthRegistrationsCredentialListMappingInstance:
        """
        Asynchronously create the AuthRegistrationsCredentialListMappingInstance

        :param str credential_list_sid: The SID of the CredentialList resource to map to the SIP domain.

        :returns: The created AuthRegistrationsCredentialListMappingInstance
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

        return AuthRegistrationsCredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
        )

    def stream(
        self, limit=None, page_size=None
    ) -> List[AuthRegistrationsCredentialListMappingInstance]:
        """
        Streams AuthRegistrationsCredentialListMappingInstance records from the API as a generator stream.
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
    ) -> List[AuthRegistrationsCredentialListMappingInstance]:
        """
        Asynchronously streams AuthRegistrationsCredentialListMappingInstance records from the API as a generator stream.
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

    def list(
        self, limit=None, page_size=None
    ) -> List[AuthRegistrationsCredentialListMappingInstance]:
        """
        Lists AuthRegistrationsCredentialListMappingInstance records from the API as a list.
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
    ) -> List[AuthRegistrationsCredentialListMappingInstance]:
        """
        Asynchronously lists AuthRegistrationsCredentialListMappingInstance records from the API as a list.
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
    ) -> AuthRegistrationsCredentialListMappingPage:
        """
        Retrieve a single page of AuthRegistrationsCredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AuthRegistrationsCredentialListMappingInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AuthRegistrationsCredentialListMappingPage(
            self._version, response, self._solution
        )

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> AuthRegistrationsCredentialListMappingPage:
        """
        Asynchronously retrieve a single page of AuthRegistrationsCredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AuthRegistrationsCredentialListMappingInstance
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
        return AuthRegistrationsCredentialListMappingPage(
            self._version, response, self._solution
        )

    def get_page(self, target_url) -> AuthRegistrationsCredentialListMappingPage:
        """
        Retrieve a specific page of AuthRegistrationsCredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AuthRegistrationsCredentialListMappingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AuthRegistrationsCredentialListMappingPage(
            self._version, response, self._solution
        )

    async def get_page_async(
        self, target_url
    ) -> AuthRegistrationsCredentialListMappingPage:
        """
        Asynchronously retrieve a specific page of AuthRegistrationsCredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AuthRegistrationsCredentialListMappingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AuthRegistrationsCredentialListMappingPage(
            self._version, response, self._solution
        )

    def get(self, sid) -> AuthRegistrationsCredentialListMappingContext:
        """
        Constructs a AuthRegistrationsCredentialListMappingContext

        :param sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
        """
        return AuthRegistrationsCredentialListMappingContext(
            self._version,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> AuthRegistrationsCredentialListMappingContext:
        """
        Constructs a AuthRegistrationsCredentialListMappingContext

        :param sid: The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
        """
        return AuthRegistrationsCredentialListMappingContext(
            self._version,
            account_sid=self._solution["account_sid"],
            domain_sid=self._solution["domain_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AuthRegistrationsCredentialListMappingList>"
