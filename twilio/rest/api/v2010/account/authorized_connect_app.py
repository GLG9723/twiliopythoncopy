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


class AuthorizedConnectAppInstance(InstanceResource):
    class Permission(object):
        GET_ALL = "get-all"
        POST_ALL = "post-all"

    def __init__(
        self, version, payload, account_sid: str, connect_app_sid: Optional[str] = None
    ):
        """
        Initialize the AuthorizedConnectAppInstance
        """
        super().__init__(version)

        self._account_sid: Optional[str] = payload.get("account_sid")
        self._connect_app_company_name: Optional[str] = payload.get(
            "connect_app_company_name"
        )
        self._connect_app_description: Optional[str] = payload.get(
            "connect_app_description"
        )
        self._connect_app_friendly_name: Optional[str] = payload.get(
            "connect_app_friendly_name"
        )
        self._connect_app_homepage_url: Optional[str] = payload.get(
            "connect_app_homepage_url"
        )
        self._connect_app_sid: Optional[str] = payload.get("connect_app_sid")
        self._date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self._date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self._permissions: Optional[
            List["AuthorizedConnectAppInstance.Permission"]
        ] = payload.get("permissions")
        self._uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "connect_app_sid": connect_app_sid or self._connect_app_sid,
        }
        self._context: Optional[AuthorizedConnectAppContext] = None

    @property
    def _proxy(self) -> "AuthorizedConnectAppContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AuthorizedConnectAppContext for this AuthorizedConnectAppInstance
        """
        if self._context is None:
            self._context = AuthorizedConnectAppContext(
                self._version,
                account_sid=self._solution["account_sid"],
                connect_app_sid=self._solution["connect_app_sid"],
            )
        return self._context

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AuthorizedConnectApp resource.
        """
        return self._account_sid

    @property
    def connect_app_company_name(self) -> Optional[str]:
        """
        :returns: The company name set for the Connect App.
        """
        return self._connect_app_company_name

    @property
    def connect_app_description(self) -> Optional[str]:
        """
        :returns: A detailed description of the Connect App.
        """
        return self._connect_app_description

    @property
    def connect_app_friendly_name(self) -> Optional[str]:
        """
        :returns: The name of the Connect App.
        """
        return self._connect_app_friendly_name

    @property
    def connect_app_homepage_url(self) -> Optional[str]:
        """
        :returns: The public URL for the Connect App.
        """
        return self._connect_app_homepage_url

    @property
    def connect_app_sid(self) -> Optional[str]:
        """
        :returns: The SID that we assigned to the Connect App.
        """
        return self._connect_app_sid

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
    def permissions(self) -> Optional[List["AuthorizedConnectAppInstance.Permission"]]:
        """
        :returns: The set of permissions that you authorized for the Connect App.  Can be: `get-all` or `post-all`.
        """
        return self._permissions

    @property
    def uri(self) -> Optional[str]:
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        """
        return self._uri

    def fetch(self) -> "AuthorizedConnectAppInstance":
        """
        Fetch the AuthorizedConnectAppInstance


        :returns: The fetched AuthorizedConnectAppInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AuthorizedConnectAppInstance":
        """
        Asynchronous coroutine to fetch the AuthorizedConnectAppInstance


        :returns: The fetched AuthorizedConnectAppInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AuthorizedConnectAppInstance {}>".format(context)


class AuthorizedConnectAppContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, connect_app_sid: str):
        """
        Initialize the AuthorizedConnectAppContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AuthorizedConnectApp resource to fetch.
        :param connect_app_sid: The SID of the Connect App to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "connect_app_sid": connect_app_sid,
        }
        self._uri = "/Accounts/{account_sid}/AuthorizedConnectApps/{connect_app_sid}.json".format(
            **self._solution
        )

    def fetch(self) -> AuthorizedConnectAppInstance:
        """
        Fetch the AuthorizedConnectAppInstance


        :returns: The fetched AuthorizedConnectAppInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AuthorizedConnectAppInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            connect_app_sid=self._solution["connect_app_sid"],
        )

    async def fetch_async(self) -> AuthorizedConnectAppInstance:
        """
        Asynchronous coroutine to fetch the AuthorizedConnectAppInstance


        :returns: The fetched AuthorizedConnectAppInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AuthorizedConnectAppInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            connect_app_sid=self._solution["connect_app_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AuthorizedConnectAppContext {}>".format(context)


class AuthorizedConnectAppPage(Page):
    def get_instance(self, payload) -> AuthorizedConnectAppInstance:
        """
        Build an instance of AuthorizedConnectAppInstance

        :param dict payload: Payload response from the API
        """
        return AuthorizedConnectAppInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AuthorizedConnectAppPage>"


class AuthorizedConnectAppList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the AuthorizedConnectAppList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AuthorizedConnectApp resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/AuthorizedConnectApps.json".format(
            **self._solution
        )

    def stream(self, limit=None, page_size=None) -> List[AuthorizedConnectAppInstance]:
        """
        Streams AuthorizedConnectAppInstance records from the API as a generator stream.
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
    ) -> List[AuthorizedConnectAppInstance]:
        """
        Asynchronously streams AuthorizedConnectAppInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[AuthorizedConnectAppInstance]:
        """
        Lists AuthorizedConnectAppInstance records from the API as a list.
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
    ) -> List[AuthorizedConnectAppInstance]:
        """
        Asynchronously lists AuthorizedConnectAppInstance records from the API as a list.
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
    ) -> AuthorizedConnectAppPage:
        """
        Retrieve a single page of AuthorizedConnectAppInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AuthorizedConnectAppInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AuthorizedConnectAppPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> AuthorizedConnectAppPage:
        """
        Asynchronously retrieve a single page of AuthorizedConnectAppInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AuthorizedConnectAppInstance
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
        return AuthorizedConnectAppPage(self._version, response, self._solution)

    def get_page(self, target_url) -> AuthorizedConnectAppPage:
        """
        Retrieve a specific page of AuthorizedConnectAppInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AuthorizedConnectAppInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AuthorizedConnectAppPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> AuthorizedConnectAppPage:
        """
        Asynchronously retrieve a specific page of AuthorizedConnectAppInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AuthorizedConnectAppInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AuthorizedConnectAppPage(self._version, response, self._solution)

    def get(self, connect_app_sid) -> AuthorizedConnectAppContext:
        """
        Constructs a AuthorizedConnectAppContext

        :param connect_app_sid: The SID of the Connect App to fetch.
        """
        return AuthorizedConnectAppContext(
            self._version,
            account_sid=self._solution["account_sid"],
            connect_app_sid=connect_app_sid,
        )

    def __call__(self, connect_app_sid) -> AuthorizedConnectAppContext:
        """
        Constructs a AuthorizedConnectAppContext

        :param connect_app_sid: The SID of the Connect App to fetch.
        """
        return AuthorizedConnectAppContext(
            self._version,
            account_sid=self._solution["account_sid"],
            connect_app_sid=connect_app_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AuthorizedConnectAppList>"
