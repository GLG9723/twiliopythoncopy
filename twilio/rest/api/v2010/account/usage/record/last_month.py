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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class LastMonthList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the LastMonthList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
        
        :returns: twilio.rest.api.v2010.account.usage.record.last_month.LastMonthList
        :rtype: twilio.rest.api.v2010.account.usage.record.last_month.LastMonthList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/Usage/Records/LastMonth.json'.format(**self._solution)
        
        
    
    def stream(self, category=values.unset, start_date=values.unset, end_date=values.unset, include_subaccounts=values.unset, limit=None, page_size=None):
        """
        Streams LastMonthInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param UsageRecordLastMonthCategory category: The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date.
        :param bool include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.usage.record.last_month.LastMonthInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            category=category,
            start_date=start_date,
            end_date=end_date,
            include_subaccounts=include_subaccounts,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, category=values.unset, start_date=values.unset, end_date=values.unset, include_subaccounts=values.unset, limit=None, page_size=None):
        """
        Lists LastMonthInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param UsageRecordLastMonthCategory category: The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date.
        :param bool include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.usage.record.last_month.LastMonthInstance]
        """
        return list(self.stream(
            category=category,
            start_date=start_date,
            end_date=end_date,
            include_subaccounts=include_subaccounts,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, category=values.unset, start_date=values.unset, end_date=values.unset, include_subaccounts=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of LastMonthInstance records from the API.
        Request is executed immediately
        
        :param UsageRecordLastMonthCategory category: The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date.
        :param bool include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of LastMonthInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.last_month.LastMonthPage
        """
        data = values.of({ 
            'Category': category,
            'StartDate': serialize.iso8601_date(start_date),
            'EndDate': serialize.iso8601_date(end_date),
            'IncludeSubaccounts': include_subaccounts,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return LastMonthPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of LastMonthInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of LastMonthInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.last_month.LastMonthPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return LastMonthPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.LastMonthList>'


class LastMonthPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the LastMonthPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.usage.record.last_month.LastMonthPage
        :rtype: twilio.rest.api.v2010.account.usage.record.last_month.LastMonthPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of LastMonthInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.usage.record.last_month.LastMonthInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.last_month.LastMonthInstance
        """
        return LastMonthInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.LastMonthPage>'





class LastMonthInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str):
        """
        Initialize the LastMonthInstance
        :returns: twilio.rest.api.v2010.account.usage.record.last_month.LastMonthInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.last_month.LastMonthInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'api_version': payload.get('api_version'),
            'as_of': payload.get('as_of'),
            'category': payload.get('category'),
            'count': payload.get('count'),
            'count_unit': payload.get('count_unit'),
            'description': payload.get('description'),
            'end_date': deserialize.iso8601_date(payload.get('end_date')),
            'price': deserialize.decimal(payload.get('price')),
            'price_unit': payload.get('price_unit'),
            'start_date': deserialize.iso8601_date(payload.get('start_date')),
            'subresource_uris': payload.get('subresource_uris'),
            'uri': payload.get('uri'),
            'usage': payload.get('usage'),
            'usage_unit': payload.get('usage_unit'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid,  }
    
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that accrued the usage.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def api_version(self):
        """
        :returns: The API version used to create the resource.
        :rtype: str
        """
        return self._properties['api_version']
    
    @property
    def as_of(self):
        """
        :returns: Usage records up to date as of this timestamp, formatted as YYYY-MM-DDTHH:MM:SS+00:00. All timestamps are in GMT
        :rtype: str
        """
        return self._properties['as_of']
    
    @property
    def category(self):
        """
        :returns: 
        :rtype: UsageRecordLastMonthCategory
        """
        return self._properties['category']
    
    @property
    def count(self):
        """
        :returns: The number of usage events, such as the number of calls.
        :rtype: str
        """
        return self._properties['count']
    
    @property
    def count_unit(self):
        """
        :returns: The units in which `count` is measured, such as `calls` for calls or `messages` for SMS.
        :rtype: str
        """
        return self._properties['count_unit']
    
    @property
    def description(self):
        """
        :returns: A plain-language description of the usage category.
        :rtype: str
        """
        return self._properties['description']
    
    @property
    def end_date(self):
        """
        :returns: The last date for which usage is included in the UsageRecord. The date is specified in GMT and formatted as `YYYY-MM-DD`.
        :rtype: date
        """
        return self._properties['end_date']
    
    @property
    def price(self):
        """
        :returns: The total price of the usage in the currency specified in `price_unit` and associated with the account.
        :rtype: float
        """
        return self._properties['price']
    
    @property
    def price_unit(self):
        """
        :returns: The currency in which `price` is measured, in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format, such as `usd`, `eur`, and `jpy`.
        :rtype: str
        """
        return self._properties['price_unit']
    
    @property
    def start_date(self):
        """
        :returns: The first date for which usage is included in this UsageRecord. The date is specified in GMT and formatted as `YYYY-MM-DD`.
        :rtype: date
        """
        return self._properties['start_date']
    
    @property
    def subresource_uris(self):
        """
        :returns: A list of related resources identified by their URIs. For more information, see [List Subresources](https://www.twilio.com/docs/usage/api/usage-record#list-subresources).
        :rtype: dict
        """
        return self._properties['subresource_uris']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    @property
    def usage(self):
        """
        :returns: The amount used to bill usage and measured in units described in `usage_unit`.
        :rtype: str
        """
        return self._properties['usage']
    
    @property
    def usage_unit(self):
        """
        :returns: The units in which `usage` is measured, such as `minutes` for calls or `messages` for SMS.
        :rtype: str
        """
        return self._properties['usage_unit']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.LastMonthInstance {}>'.format(context)


