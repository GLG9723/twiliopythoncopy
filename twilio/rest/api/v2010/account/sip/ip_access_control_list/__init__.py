"""
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


from datetime import date
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address import (
    IpAddressList,
)


class IpAccessControlListList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the IpAccessControlListList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListList
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/IpAccessControlLists.json".format(
            **self._solution
        )

    def create(self, friendly_name):
        """
        Create the IpAccessControlListInstance

        :param str friendly_name: A human readable descriptive text that describes the IpAccessControlList, up to 255 characters long.

        :returns: The created IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return IpAccessControlListInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams IpAccessControlListInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists IpAccessControlListInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return IpAccessControlListPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return IpAccessControlListPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a IpAccessControlListContext

        :param sid: A 34 character string that uniquely identifies the resource to udpate.

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        """
        return IpAccessControlListContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __call__(self, sid):
        """
        Constructs a IpAccessControlListContext

        :param sid: A 34 character string that uniquely identifies the resource to udpate.

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        """
        return IpAccessControlListContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api.V2010.IpAccessControlListList>"


class IpAccessControlListPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the IpAccessControlListPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListPage
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IpAccessControlListInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        return IpAccessControlListInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api.V2010.IpAccessControlListPage>"


class IpAccessControlListInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, sid: str = None):
        """
        Initialize the IpAccessControlListInstance

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "friendly_name": payload.get("friendly_name"),
            "date_created": deserialize.rfc2822_datetime(payload.get("date_created")),
            "date_updated": deserialize.rfc2822_datetime(payload.get("date_updated")),
            "subresource_uris": payload.get("subresource_uris"),
            "uri": payload.get("uri"),
        }

        self._context = None
        self._solution = {
            "account_sid": account_sid,
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: IpAccessControlListContext for this IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        """
        if self._context is None:
            self._context = IpAccessControlListContext(
                self._version,
                account_sid=self._solution["account_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) that owns this resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def friendly_name(self):
        """
        :returns: A human readable descriptive text, up to 255 characters long.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def subresource_uris(self):
        """
        :returns: A list of the IpAddress resources associated with this IP access control list resource.
        :rtype: dict
        """
        return self._properties["subresource_uris"]

    @property
    def uri(self):
        """
        :returns: The URI for this resource, relative to `https://api.twilio.com`
        :rtype: str
        """
        return self._properties["uri"]

    def delete(self):
        """
        Deletes the IpAccessControlListInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch the IpAccessControlListInstance


        :returns: The fetched IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name):
        """
        Update the IpAccessControlListInstance

        :param str friendly_name: A human readable descriptive text, up to 255 characters long.

        :returns: The updated IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
        )

    @property
    def ip_addresses(self):
        """
        Access the ip_addresses

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAddressList
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAddressList
        """
        return self._proxy.ip_addresses

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.IpAccessControlListInstance {}>".format(context)


class IpAccessControlListContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the IpAccessControlListContext

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param sid: A 34 character string that uniquely identifies the resource to udpate.

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "sid": sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json".format(
                **self._solution
            )
        )

        self._ip_addresses = None

    def delete(self):
        """
        Deletes the IpAccessControlListInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the IpAccessControlListInstance


        :returns: The fetched IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return IpAccessControlListInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def update(self, friendly_name):
        """
        Update the IpAccessControlListInstance

        :param str friendly_name: A human readable descriptive text, up to 255 characters long.

        :returns: The updated IpAccessControlListInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAccessControlListInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return IpAccessControlListInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    @property
    def ip_addresses(self):
        """
        Access the ip_addresses

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAddressList
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.IpAddressList
        """
        if self._ip_addresses is None:
            self._ip_addresses = IpAddressList(
                self._version,
                self._solution["account_sid"],
                self._solution["sid"],
            )
        return self._ip_addresses

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.IpAccessControlListContext {}>".format(context)
