r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Microvisor
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


class AccountConfigInstance(InstanceResource):
    def __init__(self, version, payload, key: Optional[str] = None):
        """
        Initialize the AccountConfigInstance
        """
        super().__init__(version)

        self._properties = {
            "key": payload.get("key"),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "value": payload.get("value"),
            "url": payload.get("url"),
        }

        self._solution = {
            "key": key or self._properties["key"],
        }
        self._context: Optional[AccountConfigContext] = None

    @property
    def _proxy(self) -> "AccountConfigContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AccountConfigContext for this AccountConfigInstance
        """
        if self._context is None:
            self._context = AccountConfigContext(
                self._version,
                key=self._solution["key"],
            )
        return self._context

    @property
    def key(self) -> str:
        """
        :returns: The config key; up to 100 characters.
        """
        return self._properties["key"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns:
        """
        return self._properties["date_updated"]

    @property
    def value(self) -> str:
        """
        :returns: The config value; up to 4096 characters.
        """
        return self._properties["value"]

    @property
    def url(self) -> str:
        """
        :returns: The absolute URL of the Config.
        """
        return self._properties["url"]

    def delete(self) -> bool:
        """
        Deletes the AccountConfigInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AccountConfigInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "AccountConfigInstance":
        """
        Fetch the AccountConfigInstance


        :returns: The fetched AccountConfigInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AccountConfigInstance":
        """
        Asynchronous coroutine to fetch the AccountConfigInstance


        :returns: The fetched AccountConfigInstance
        """
        return await self._proxy.fetch_async()

    def update(self, value) -> "AccountConfigInstance":
        """
        Update the AccountConfigInstance

        :param str value: The config value; up to 4096 characters.

        :returns: The updated AccountConfigInstance
        """
        return self._proxy.update(
            value=value,
        )

    async def update_async(self, value) -> "AccountConfigInstance":
        """
        Asynchronous coroutine to update the AccountConfigInstance

        :param str value: The config value; up to 4096 characters.

        :returns: The updated AccountConfigInstance
        """
        return await self._proxy.update_async(
            value=value,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Microvisor.V1.AccountConfigInstance {}>".format(context)


class AccountConfigContext(InstanceContext):
    def __init__(self, version: Version, key: str):
        """
        Initialize the AccountConfigContext

        :param version: Version that contains the resource
        :param key: The config key; up to 100 characters.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "key": key,
        }
        self._uri = "/Configs/{key}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the AccountConfigInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AccountConfigInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> AccountConfigInstance:
        """
        Fetch the AccountConfigInstance


        :returns: The fetched AccountConfigInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AccountConfigInstance(
            self._version,
            payload,
            key=self._solution["key"],
        )

    async def fetch_async(self) -> AccountConfigInstance:
        """
        Asynchronous coroutine to fetch the AccountConfigInstance


        :returns: The fetched AccountConfigInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AccountConfigInstance(
            self._version,
            payload,
            key=self._solution["key"],
        )

    def update(self, value) -> AccountConfigInstance:
        """
        Update the AccountConfigInstance

        :param str value: The config value; up to 4096 characters.

        :returns: The updated AccountConfigInstance
        """
        data = values.of(
            {
                "Value": value,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountConfigInstance(self._version, payload, key=self._solution["key"])

    async def update_async(self, value) -> AccountConfigInstance:
        """
        Asynchronous coroutine to update the AccountConfigInstance

        :param str value: The config value; up to 4096 characters.

        :returns: The updated AccountConfigInstance
        """
        data = values.of(
            {
                "Value": value,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountConfigInstance(self._version, payload, key=self._solution["key"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Microvisor.V1.AccountConfigContext {}>".format(context)


class AccountConfigPage(Page):
    def get_instance(self, payload) -> AccountConfigInstance:
        """
        Build an instance of AccountConfigInstance

        :param dict payload: Payload response from the API
        """
        return AccountConfigInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Microvisor.V1.AccountConfigPage>"


class AccountConfigList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AccountConfigList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Configs"

    def create(self, key, value) -> AccountConfigInstance:
        """
        Create the AccountConfigInstance

        :param str key: The config key; up to 100 characters.
        :param str value: The config value; up to 4096 characters.

        :returns: The created AccountConfigInstance
        """
        data = values.of(
            {
                "Key": key,
                "Value": value,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountConfigInstance(self._version, payload)

    async def create_async(self, key, value) -> AccountConfigInstance:
        """
        Asynchronously create the AccountConfigInstance

        :param str key: The config key; up to 100 characters.
        :param str value: The config value; up to 4096 characters.

        :returns: The created AccountConfigInstance
        """
        data = values.of(
            {
                "Key": key,
                "Value": value,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountConfigInstance(self._version, payload)

    def stream(self, limit=None, page_size=None) -> List[AccountConfigInstance]:
        """
        Streams AccountConfigInstance records from the API as a generator stream.
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
    ) -> List[AccountConfigInstance]:
        """
        Asynchronously streams AccountConfigInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[AccountConfigInstance]:
        """
        Lists AccountConfigInstance records from the API as a list.
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
    ) -> List[AccountConfigInstance]:
        """
        Asynchronously lists AccountConfigInstance records from the API as a list.
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
    ) -> AccountConfigPage:
        """
        Retrieve a single page of AccountConfigInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AccountConfigInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AccountConfigPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> AccountConfigPage:
        """
        Asynchronously retrieve a single page of AccountConfigInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AccountConfigInstance
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
        return AccountConfigPage(self._version, response)

    def get_page(self, target_url) -> AccountConfigPage:
        """
        Retrieve a specific page of AccountConfigInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AccountConfigInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AccountConfigPage(self._version, response)

    async def get_page_async(self, target_url) -> AccountConfigPage:
        """
        Asynchronously retrieve a specific page of AccountConfigInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AccountConfigInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AccountConfigPage(self._version, response)

    def get(self, key) -> AccountConfigContext:
        """
        Constructs a AccountConfigContext

        :param key: The config key; up to 100 characters.
        """
        return AccountConfigContext(self._version, key=key)

    def __call__(self, key) -> AccountConfigContext:
        """
        Constructs a AccountConfigContext

        :param key: The config key; up to 100 characters.
        """
        return AccountConfigContext(self._version, key=key)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Microvisor.V1.AccountConfigList>"
