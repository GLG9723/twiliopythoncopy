# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class SimList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version):
        """
        Initialize the SimList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.supersim.v1.sim.SimList
        :rtype: twilio.rest.supersim.v1.sim.SimList
        """
        super(SimList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Sims'.format(**self._solution)

    def create(self, iccid, registration_code):
        """
        Create the SimInstance

        :param unicode iccid: The `ICCID <https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID>`_ of the Super SIM to be added to your Account
        :param unicode registration_code: The 10 digit code required to claim the Super SIM for your Account

        :returns: The created SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        data = values.of({'Iccid': iccid, 'RegistrationCode': registration_code, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return SimInstance(self._version, payload, )

    def stream(self, status=values.unset, fleet=values.unset, iccid=values.unset,
               limit=None, page_size=None):
        """
        Streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param SimInstance.Status status: The status of the Sim resources to read
        :param unicode fleet: The SID or unique name of the Fleet to which a list of Sims are assigned
        :param unicode iccid: The ICCID associated with a Super SIM to filter the list by
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

        page = self.page(status=status, fleet=fleet, iccid=iccid, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, fleet=values.unset, iccid=values.unset,
             limit=None, page_size=None):
        """
        Lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param SimInstance.Status status: The status of the Sim resources to read
        :param unicode fleet: The SID or unique name of the Fleet to which a list of Sims are assigned
        :param unicode iccid: The ICCID associated with a Super SIM to filter the list by
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sim.SimInstance]
        """
        return list(self.stream(status=status, fleet=fleet, iccid=iccid, limit=limit, page_size=page_size, ))

    def page(self, status=values.unset, fleet=values.unset, iccid=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SimInstance records from the API.
        Request is executed immediately

        :param SimInstance.Status status: The status of the Sim resources to read
        :param unicode fleet: The SID or unique name of the Fleet to which a list of Sims are assigned
        :param unicode iccid: The ICCID associated with a Super SIM to filter the list by
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimPage
        """
        data = values.of({
            'Status': status,
            'Fleet': fleet,
            'Iccid': iccid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return SimPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SimPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SimContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.supersim.v1.sim.SimContext
        :rtype: twilio.rest.supersim.v1.sim.SimContext
        """
        return SimContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a SimContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.supersim.v1.sim.SimContext
        :rtype: twilio.rest.supersim.v1.sim.SimContext
        """
        return SimContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SimList>'


class SimPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the SimPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.sim.SimPage
        :rtype: twilio.rest.supersim.v1.sim.SimPage
        """
        super(SimPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SimInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.sim.SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        return SimInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SimPage>'


class SimContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, sid):
        """
        Initialize the SimContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.supersim.v1.sim.SimContext
        :rtype: twilio.rest.supersim.v1.sim.SimContext
        """
        super(SimContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Sims/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the SimInstance

        :returns: The fetched SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SimInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, unique_name=values.unset, status=values.unset,
               fleet=values.unset, callback_url=values.unset,
               callback_method=values.unset, account_sid=values.unset):
        """
        Update the SimInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param SimInstance.StatusUpdate status: The new status of the Super SIM
        :param unicode fleet: The SID or unique name of the Fleet to which the SIM resource should be assigned
        :param unicode callback_url: The URL we should call after the update has finished
        :param unicode callback_method: The HTTP method we should use to call callback_url
        :param unicode account_sid: The SID of the Account to which the Sim resource should belong

        :returns: The updated SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'Status': status,
            'Fleet': fleet,
            'CallbackUrl': callback_url,
            'CallbackMethod': callback_method,
            'AccountSid': account_sid,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return SimInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.SimContext {}>'.format(context)


class SimInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class Status(object):
        NEW = "new"
        READY = "ready"
        ACTIVE = "active"
        INACTIVE = "inactive"
        SCHEDULED = "scheduled"

    class StatusUpdate(object):
        READY = "ready"
        ACTIVE = "active"
        INACTIVE = "inactive"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the SimInstance

        :returns: twilio.rest.supersim.v1.sim.SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        super(SimInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'account_sid': payload.get('account_sid'),
            'iccid': payload.get('iccid'),
            'status': payload.get('status'),
            'fleet_sid': payload.get('fleet_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SimContext for this SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimContext
        """
        if self._context is None:
            self._context = SimContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that the Super SIM belongs to
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def iccid(self):
        """
        :returns: The ICCID associated with the SIM
        :rtype: unicode
        """
        return self._properties['iccid']

    @property
    def status(self):
        """
        :returns: The status of the Super SIM
        :rtype: SimInstance.Status
        """
        return self._properties['status']

    @property
    def fleet_sid(self):
        """
        :returns: The unique ID of the Fleet configured for this SIM
        :rtype: unicode
        """
        return self._properties['fleet_sid']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Sim Resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the SimInstance

        :returns: The fetched SimInstance
        :rtype: twilio.rest.supersim.v1.sim.SimInstance
        """
        return self._proxy.fetch()

    def update(self, unique_name=values.unset, status=values.unset,
               fleet=values.unset, callback_url=values.unset,
               callback_method=values.unset, account_sid=values.unset):
        """
        Update the SimInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param SimInstance.StatusUpdate status: The new status of the Super SIM
        :param unicode fleet: The SID or unique name of the Fleet to which the SIM resource should be assigned
        :param unicode callback_url: The URL we should call after the update has finished
        :param unicode callback_method: The HTTP method we should use to call callback_url
        :param unicode account_sid: The SID of the Account to which the Sim resource should belong

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

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.SimInstance {}>'.format(context)
