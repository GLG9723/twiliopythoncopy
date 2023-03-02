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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class BillingPeriodList(ListResource):

    def __init__(self, version: Version, sim_sid: str):
        """
        Initialize the BillingPeriodList

        :param Version version: Version that contains the resource
        :param sim_sid: The SID of the Super SIM to list Billing Periods for.
        
        :returns: twilio.rest.supersim.v1.sim.billing_period.BillingPeriodList
        :rtype: twilio.rest.supersim.v1.sim.billing_period.BillingPeriodList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'sim_sid': sim_sid,  }
        self._uri = '/Sims/{sim_sid}/BillingPeriods'.format(**self._solution)
        
        
    
    def stream(self, limit=None, page_size=None):
        """
        Streams BillingPeriodInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.supersim.v1.sim.billing_period.BillingPeriodInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists BillingPeriodInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sim.billing_period.BillingPeriodInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of BillingPeriodInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BillingPeriodInstance
        :rtype: twilio.rest.supersim.v1.sim.billing_period.BillingPeriodPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return BillingPeriodPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BillingPeriodInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BillingPeriodInstance
        :rtype: twilio.rest.supersim.v1.sim.billing_period.BillingPeriodPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return BillingPeriodPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.BillingPeriodList>'


class BillingPeriodPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the BillingPeriodPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.sim.billing_period.BillingPeriodPage
        :rtype: twilio.rest.supersim.v1.sim.billing_period.BillingPeriodPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BillingPeriodInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.sim.billing_period.BillingPeriodInstance
        :rtype: twilio.rest.supersim.v1.sim.billing_period.BillingPeriodInstance
        """
        return BillingPeriodInstance(self._version, payload, sim_sid=self._solution['sim_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.BillingPeriodPage>'





class BillingPeriodInstance(InstanceResource):

    class BillingPeriodBpType(object):
        READY = "ready"
        ACTIVE = "active"

    def __init__(self, version, payload, sim_sid: str):
        """
        Initialize the BillingPeriodInstance
        :returns: twilio.rest.supersim.v1.sim.billing_period.BillingPeriodInstance
        :rtype: twilio.rest.supersim.v1.sim.billing_period.BillingPeriodInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'sim_sid': payload.get('sim_sid'),
            'start_time': deserialize.iso8601_datetime(payload.get('start_time')),
            'end_time': deserialize.iso8601_datetime(payload.get('end_time')),
            'period_type': payload.get('period_type'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
        }

        self._context = None
        self._solution = { 'sim_sid': sim_sid,  }
    
    
    @property
    def sid(self):
        """
        :returns: The SID of the Billing Period.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) the Super SIM belongs to.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def sim_sid(self):
        """
        :returns: The SID of the Super SIM the Billing Period belongs to.
        :rtype: str
        """
        return self._properties['sim_sid']
    
    @property
    def start_time(self):
        """
        :returns: The start time of the Billing Period specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['start_time']
    
    @property
    def end_time(self):
        """
        :returns: The end time of the Billing Period specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['end_time']
    
    @property
    def period_type(self):
        """
        :returns: 
        :rtype: BillingPeriodBpType
        """
        return self._properties['period_type']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.BillingPeriodInstance {}>'.format(context)


