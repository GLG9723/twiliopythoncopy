"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
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
from twilio.rest.supersim.v1.sim.billing_period import BillingPeriodList
from twilio.rest.supersim.v1.sim.sim_ip_address import SimIpAddressList


class SimList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the SimList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.supersim.v1.sim.SimList
        :rtype: twilio.rest.supersim.v1.sim.SimList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Sims".format(**self._solution)

    def create(self, iccid, registration_code):
        """
        Create the SimInstance

        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) of the Super SIM to be added to your Account.
        :param str registration_code: The 10-digit code required to claim the Super SIM for your Account.

        :returns: The created SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        data = values.of(
            {
                "Iccid": iccid,
                "RegistrationCode": registration_code,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SimInstance(self._version, payload)

    def stream(
        self,
        status=values.unset,
        fleet=values.unset,
        iccid=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param SimInstance.Status status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param str fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sim.SimInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status, fleet=fleet, iccid=iccid, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    def list(
        self,
        status=values.unset,
        fleet=values.unset,
        iccid=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param SimInstance.Status status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param str fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sim.SimInstance]
        """
        return list(
            self.stream(
                status=status,
                fleet=fleet,
                iccid=iccid,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        status=values.unset,
        fleet=values.unset,
        iccid=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of SimInstance records from the API.
        Request is executed immediately

        :param SimInstance.Status status: The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
        :param str fleet: The SID or unique name of the Fleet to which a list of Sims are assigned.
        :param str iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimPage
        """
        data = values.of(
            {
                "Status": status,
                "Fleet": fleet,
                "Iccid": iccid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SimPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SimPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SimContext

        :param sid: The SID of the Sim resource to update.

        :returns: twilio.rest.supersim.v1.sim.SimContext
        :rtype: twilio.rest.supersim.v1.sim.SimContext
        """
        return SimContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a SimContext

        :param sid: The SID of the Sim resource to update.

        :returns: twilio.rest.supersim.v1.sim.SimContext
        :rtype: twilio.rest.supersim.v1.sim.SimContext
        """
        return SimContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Supersim.V1.SimList>"


class SimPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the SimPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.sim.SimPage
        :rtype: twilio.rest.supersim.v1.sim.SimPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SimInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.sim.SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        return SimInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Supersim.V1.SimPage>"


class SimInstance(InstanceResource):
    class Status(object):
        NEW = "new"
        READY = "ready"
        ACTIVE = "active"
        INACTIVE = "inactive"
        SCHEDULED = "scheduled"

    def __init__(self, version, payload, sid: str = None):
        """
        Initialize the SimInstance

        :returns: twilio.rest.supersim.v1.sim.SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "unique_name": payload.get("unique_name"),
            "account_sid": payload.get("account_sid"),
            "iccid": payload.get("iccid"),
            "status": payload.get("status"),
            "fleet_sid": payload.get("fleet_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._context = None
        self._solution = {
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SimContext for this SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimContext
        """
        if self._context is None:
            self._context = SimContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the Sim resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :rtype: str
        """
        return self._properties["unique_name"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Super SIM belongs to.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def iccid(self):
        """
        :returns: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with the SIM.
        :rtype: str
        """
        return self._properties["iccid"]

    @property
    def status(self):
        """
        :returns:
        :rtype: SimInstance.Status
        """
        return self._properties["status"]

    @property
    def fleet_sid(self):
        """
        :returns: The unique ID of the Fleet configured for this SIM.
        :rtype: str
        """
        return self._properties["fleet_sid"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Sim Resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["links"]

    def fetch(self):
        """
        Fetch the SimInstance


        :returns: The fetched SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        return self._proxy.fetch()

    def update(
        self,
        unique_name=values.unset,
        status=values.unset,
        fleet=values.unset,
        callback_url=values.unset,
        callback_method=values.unset,
        account_sid=values.unset,
    ):
        """
        Update the SimInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param SimInstance.StatusUpdate status:
        :param str fleet: The SID or unique name of the Fleet to which the SIM resource should be assigned.
        :param str callback_url: The URL we should call using the `callback_method` after an asynchronous update has finished.
        :param str callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param str account_sid: The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource's status is new.

        :returns: The updated SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
            status=status,
            fleet=fleet,
            callback_url=callback_url,
            callback_method=callback_method,
            account_sid=account_sid,
        )

    @property
    def billing_periods(self):
        """
        Access the billing_periods

        :returns: twilio.rest.supersim.v1.sim.BillingPeriodList
        :rtype: twilio.rest.supersim.v1.sim.BillingPeriodList
        """
        return self._proxy.billing_periods

    @property
    def sim_ip_addresses(self):
        """
        Access the sim_ip_addresses

        :returns: twilio.rest.supersim.v1.sim.SimIpAddressList
        :rtype: twilio.rest.supersim.v1.sim.SimIpAddressList
        """
        return self._proxy.sim_ip_addresses

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.SimInstance {}>".format(context)


class SimContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the SimContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Sim resource to update.

        :returns: twilio.rest.supersim.v1.sim.SimContext
        :rtype: twilio.rest.supersim.v1.sim.SimContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Sims/{sid}".format(**self._solution)

        self._billing_periods = None
        self._sim_ip_addresses = None

    def fetch(self):
        """
        Fetch the SimInstance


        :returns: The fetched SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SimInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        unique_name=values.unset,
        status=values.unset,
        fleet=values.unset,
        callback_url=values.unset,
        callback_method=values.unset,
        account_sid=values.unset,
    ):
        """
        Update the SimInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param SimInstance.StatusUpdate status:
        :param str fleet: The SID or unique name of the Fleet to which the SIM resource should be assigned.
        :param str callback_url: The URL we should call using the `callback_method` after an asynchronous update has finished.
        :param str callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param str account_sid: The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource's status is new.

        :returns: The updated SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "Status": status,
                "Fleet": fleet,
                "CallbackUrl": callback_url,
                "CallbackMethod": callback_method,
                "AccountSid": account_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SimInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def billing_periods(self):
        """
        Access the billing_periods

        :returns: twilio.rest.supersim.v1.sim.BillingPeriodList
        :rtype: twilio.rest.supersim.v1.sim.BillingPeriodList
        """
        if self._billing_periods is None:
            self._billing_periods = BillingPeriodList(
                self._version,
                self._solution["sid"],
            )
        return self._billing_periods

    @property
    def sim_ip_addresses(self):
        """
        Access the sim_ip_addresses

        :returns: twilio.rest.supersim.v1.sim.SimIpAddressList
        :rtype: twilio.rest.supersim.v1.sim.SimIpAddressList
        """
        if self._sim_ip_addresses is None:
            self._sim_ip_addresses = SimIpAddressList(
                self._version,
                self._solution["sid"],
            )
        return self._sim_ip_addresses

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.SimContext {}>".format(context)
