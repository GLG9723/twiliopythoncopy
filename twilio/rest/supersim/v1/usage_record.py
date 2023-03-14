r"""
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
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UsageRecordList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the UsageRecordList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.supersim.v1.usage_record.UsageRecordList
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/UsageRecords'.format(**self._solution)
        
        
    
    def stream(self, sim=values.unset, fleet=values.unset, network=values.unset, iso_country=values.unset, group=values.unset, granularity=values.unset, start_time=values.unset, end_time=values.unset, limit=None, page_size=None):
        """
        Streams UsageRecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param str fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param str network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param str iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param UsageRecordInstance.Group group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param UsageRecordInstance.Granularity granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param datetime start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param datetime end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.usage_record.UsageRecordInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            sim=sim,
            fleet=fleet,
            network=network,
            iso_country=iso_country,
            group=group,
            granularity=granularity,
            start_time=start_time,
            end_time=end_time,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, sim=values.unset, fleet=values.unset, network=values.unset, iso_country=values.unset, group=values.unset, granularity=values.unset, start_time=values.unset, end_time=values.unset, limit=None, page_size=None):
        """
        Asynchronously streams UsageRecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param str fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param str network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param str iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param UsageRecordInstance.Group group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param UsageRecordInstance.Granularity granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param datetime start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param datetime end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.usage_record.UsageRecordInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            sim=sim,
            fleet=fleet,
            network=network,
            iso_country=iso_country,
            group=group,
            granularity=granularity,
            start_time=start_time,
            end_time=end_time,
            page_size=limits['page_size']
        )

        return await self._version.stream_async(page, limits['limit'])

    def list(self, sim=values.unset, fleet=values.unset, network=values.unset, iso_country=values.unset, group=values.unset, granularity=values.unset, start_time=values.unset, end_time=values.unset, limit=None, page_size=None):
        """
        Lists UsageRecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param str fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param str network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param str iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param UsageRecordInstance.Group group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param UsageRecordInstance.Granularity granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param datetime start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param datetime end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.usage_record.UsageRecordInstance]
        """
        return list(self.stream(
            sim=sim,
            fleet=fleet,
            network=network,
            iso_country=iso_country,
            group=group,
            granularity=granularity,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, sim=values.unset, fleet=values.unset, network=values.unset, iso_country=values.unset, group=values.unset, granularity=values.unset, start_time=values.unset, end_time=values.unset, limit=None, page_size=None):
        """
        Asynchronously lists UsageRecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param str fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param str network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param str iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param UsageRecordInstance.Group group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param UsageRecordInstance.Granularity granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param datetime start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param datetime end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.usage_record.UsageRecordInstance]
        """
        return list(await self.stream_async(
            sim=sim,
            fleet=fleet,
            network=network,
            iso_country=iso_country,
            group=group,
            granularity=granularity,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, sim=values.unset, fleet=values.unset, network=values.unset, iso_country=values.unset, group=values.unset, granularity=values.unset, start_time=values.unset, end_time=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of UsageRecordInstance records from the API.
        Request is executed immediately
        
        :param str sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param str fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param str network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param str iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param UsageRecordInstance.Group group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param UsageRecordInstance.Granularity granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param datetime start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param datetime end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordPage
        """
        data = values.of({ 
            'Sim': sim,
            'Fleet': fleet,
            'Network': network,
            'IsoCountry': iso_country,
            'Group': group,
            'Granularity': granularity,
            'StartTime': serialize.iso8601_datetime(start_time),
            'EndTime': serialize.iso8601_datetime(end_time),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return UsageRecordPage(self._version, response, self._solution)

    async def page_async(self, sim=values.unset, fleet=values.unset, network=values.unset, iso_country=values.unset, group=values.unset, granularity=values.unset, start_time=values.unset, end_time=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronously retrieve a single page of UsageRecordInstance records from the API.
        Request is executed immediately
        
        :param str sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param str fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param str network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param str iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param UsageRecordInstance.Group group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param UsageRecordInstance.Granularity granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param datetime start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param datetime end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordPage
        """
        data = values.of({ 
            'Sim': sim,
            'Fleet': fleet,
            'Network': network,
            'IsoCountry': iso_country,
            'Group': group,
            'Granularity': granularity,
            'StartTime': serialize.iso8601_datetime(start_time),
            'EndTime': serialize.iso8601_datetime(end_time),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return UsageRecordPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return UsageRecordPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UsageRecordInstance
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return UsageRecordPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.UsageRecordList>'


class UsageRecordPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UsageRecordPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.usage_record.UsageRecordPage
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UsageRecordInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.usage_record.UsageRecordInstance
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordInstance
        """
        return UsageRecordInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.UsageRecordPage>'




class UsageRecordInstance(InstanceResource):

    class Granularity(object):
        HOUR = "hour"
        DAY = "day"
        ALL = "all"

    class Group(object):
        SIM = "sim"
        FLEET = "fleet"
        NETWORK = "network"
        ISOCOUNTRY = "isoCountry"

    def __init__(self, version, payload):
        """
        Initialize the UsageRecordInstance
        :returns: twilio.rest.supersim.v1.usage_record.UsageRecordInstance
        :rtype: twilio.rest.supersim.v1.usage_record.UsageRecordInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'sim_sid': payload.get('sim_sid'),
            'network_sid': payload.get('network_sid'),
            'fleet_sid': payload.get('fleet_sid'),
            'iso_country': payload.get('iso_country'),
            'period': payload.get('period'),
            'data_upload': payload.get('data_upload'),
            'data_download': payload.get('data_download'),
            'data_total': payload.get('data_total'),
            'data_total_billed': deserialize.decimal(payload.get('data_total_billed')),
            'billed_unit': payload.get('billed_unit'),
        }

        self._context = None
        self._solution = {  }
    
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that incurred the usage.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def sim_sid(self):
        """
        :returns: SID of a Sim resource to which the UsageRecord belongs. Value will only be present when either a value for the `Sim` query parameter is provided or when UsageRecords are grouped by `sim`. Otherwise, the value will be `null`.
        :rtype: str
        """
        return self._properties['sim_sid']
    
    @property
    def network_sid(self):
        """
        :returns: SID of the Network resource the usage occurred on. Value will only be present when either a value for the `Network` query parameter is provided or when UsageRecords are grouped by `network`. Otherwise, the value will be `null`.
        :rtype: str
        """
        return self._properties['network_sid']
    
    @property
    def fleet_sid(self):
        """
        :returns: SID of the Fleet resource the usage occurred on. Value will only be present when either a value for the `Fleet` query parameter is provided or when UsageRecords are grouped by `fleet`. Otherwise, the value will be `null`.
        :rtype: str
        """
        return self._properties['fleet_sid']
    
    @property
    def iso_country(self):
        """
        :returns: Alpha-2 ISO Country Code that the usage occurred in. Value will only be present when either a value for the `IsoCountry` query parameter is provided or when UsageRecords are grouped by `isoCountry`. Otherwise, the value will be `null`.
        :rtype: str
        """
        return self._properties['iso_country']
    
    @property
    def period(self):
        """
        :returns: The time period for which the usage is reported. The period is represented as a pair of `start_time` and `end_time` timestamps specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: dict
        """
        return self._properties['period']
    
    @property
    def data_upload(self):
        """
        :returns: Total data uploaded in bytes, aggregated by the query parameters.
        :rtype: int
        """
        return self._properties['data_upload']
    
    @property
    def data_download(self):
        """
        :returns: Total data downloaded in bytes, aggregated by the query parameters.
        :rtype: int
        """
        return self._properties['data_download']
    
    @property
    def data_total(self):
        """
        :returns: Total of data_upload and data_download.
        :rtype: int
        """
        return self._properties['data_total']
    
    @property
    def data_total_billed(self):
        """
        :returns: Total amount in the `billed_unit` that was charged for the data uploaded or downloaded. Will return 0 for usage prior to February 1, 2022. Value may be 0 despite `data_total` being greater than 0 if the data usage is still being processed by Twilio's billing system. Refer to [Data Usage Processing](https://www.twilio.com/docs/iot/supersim/api/usage-record-resource#data-usage-processing) for more details.
        :rtype: float
        """
        return self._properties['data_total_billed']
    
    @property
    def billed_unit(self):
        """
        :returns: The currency in which the billed amounts are measured, specified in the 3 letter ISO 4127 format (e.g. `USD`, `EUR`, `JPY`). This can be null when data_toal_billed is 0 and we do not yet have billing information for the corresponding data usage. Refer to [Data Usage Processing](https://www.twilio.com/docs/iot/supersim/api/usage-record-resource#data-usage-processing) for more details.
        :rtype: str
        """
        return self._properties['billed_unit']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.UsageRecordInstance {}>'.format(context)



