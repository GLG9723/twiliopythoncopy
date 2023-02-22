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
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class YearlyList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the YearlyList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resources to read.
        
        :returns: twilio.rest.api.v2010.account.usage.record.yearly.YearlyList
        :rtype: twilio.rest.api.v2010.account.usage.record.yearly.YearlyList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/Usage/Records/Yearly.json'.format(**self._solution)
        
        
    
    def stream(self, category=values.unset, start_date=values.unset, end_date=values.unset, include_subaccounts=values.unset, limit=None, page_size=None):
        """
        Streams YearlyInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param UsageRecordYearlyCategory category: The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
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
        :rtype: list[twilio.rest.api.v2010.account.usage.record.yearly.YearlyInstance]
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
        Lists YearlyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param UsageRecordYearlyCategory category: The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
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
        :rtype: list[twilio.rest.api.v2010.account.usage.record.yearly.YearlyInstance]
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
        Retrieve a single page of YearlyInstance records from the API.
        Request is executed immediately
        
        :param UsageRecordYearlyCategory category: The [usage category](https://www.twilio.com/docs/usage/api/usage-record#usage-categories) of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.
        :param date start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date.
        :param date end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.  You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date.
        :param bool include_subaccounts: Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of YearlyInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.yearly.YearlyPage
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
        return YearlyPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of YearlyInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of YearlyInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.yearly.YearlyPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return YearlyPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.YearlyList>'


class YearlyPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the YearlyPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.usage.record.yearly.YearlyPage
        :rtype: twilio.rest.api.v2010.account.usage.record.yearly.YearlyPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of YearlyInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.usage.record.yearly.YearlyInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.yearly.YearlyInstance
        """
        return YearlyInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.YearlyPage>'






class YearlyInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'api_version' : payload.get('api_version'),
            'as_of' : payload.get('as_of'),
            'category' : payload.get('category'),
            'count' : payload.get('count'),
            'count_unit' : payload.get('count_unit'),
            'description' : payload.get('description'),
            'end_date' : payload.get('end_date'),
            'price' : payload.get('price'),
            'price_unit' : payload.get('price_unit'),
            'start_date' : payload.get('start_date'),
            'subresource_uris' : payload.get('subresource_uris'),
            'uri' : payload.get('uri'),
            'usage' : payload.get('usage'),
            'usage_unit' : payload.get('usage_unit'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = YearlyContext(
                self._version,
                account_sid=self._solution['account_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.YearlyInstance {}>'.format(context)



