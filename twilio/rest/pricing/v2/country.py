r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Pricing
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CountryList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the CountryList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.pricing.v2.country.CountryList
        :rtype: twilio.rest.pricing.v2.country.CountryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Trunking/Countries".format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams CountryInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.pricing.v2.country.CountryInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams CountryInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.pricing.v2.country.CountryInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists CountryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.pricing.v2.country.CountryInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists CountryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.pricing.v2.country.CountryInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of CountryInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CountryPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of CountryInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryPage
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
        return CountryPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CountryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CountryPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of CountryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CountryPage(self._version, response, self._solution)

    def get(self, iso_country):
        """
        Constructs a CountryContext

        :param iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the origin-based voice pricing information to fetch.

        :returns: twilio.rest.pricing.v2.country.CountryContext
        :rtype: twilio.rest.pricing.v2.country.CountryContext
        """
        return CountryContext(self._version, iso_country=iso_country)

    def __call__(self, iso_country):
        """
        Constructs a CountryContext

        :param iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the origin-based voice pricing information to fetch.

        :returns: twilio.rest.pricing.v2.country.CountryContext
        :rtype: twilio.rest.pricing.v2.country.CountryContext
        """
        return CountryContext(self._version, iso_country=iso_country)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Pricing.V2.CountryList>"


class CountryPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the CountryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.pricing.v2.country.CountryPage
        :rtype: twilio.rest.pricing.v2.country.CountryPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CountryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.pricing.v2.country.CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryInstance
        """
        return CountryInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Pricing.V2.CountryPage>"


class CountryInstance(InstanceResource):
    def __init__(self, version, payload, iso_country: str | None = None):
        """
        Initialize the CountryInstance

        :returns: twilio.rest.pricing.v2.country.CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryInstance
        """
        super().__init__(version)

        self._properties = {
            "country": payload.get("country"),
            "iso_country": payload.get("iso_country"),
            "terminating_prefix_prices": payload.get("terminating_prefix_prices"),
            "originating_call_prices": payload.get("originating_call_prices"),
            "price_unit": payload.get("price_unit"),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {
            "iso_country": iso_country or self._properties["iso_country"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CountryContext for this CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryContext
        """
        if self._context is None:
            self._context = CountryContext(
                self._version,
                iso_country=self._solution["iso_country"],
            )
        return self._context

    @property
    def country(self):
        """
        :returns: The name of the country.
        :rtype: str
        """
        return self._properties["country"]

    @property
    def iso_country(self):
        """
        :returns: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
        :rtype: str
        """
        return self._properties["iso_country"]

    @property
    def terminating_prefix_prices(self):
        """
        :returns: The list of [TerminatingPrefixPrice](https://www.twilio.com/docs/voice/pricing#outbound-prefix-price-with-origin) records.
        :rtype: list[PricingV2TrunkingCountryInstanceTerminatingPrefixPrices]
        """
        return self._properties["terminating_prefix_prices"]

    @property
    def originating_call_prices(self):
        """
        :returns: The list of [OriginatingCallPrice](https://www.twilio.com/docs/voice/pricing#inbound-call-price) records.
        :rtype: list[PricingV2TrunkingCountryInstanceOriginatingCallPrices]
        """
        return self._properties["originating_call_prices"]

    @property
    def price_unit(self):
        """
        :returns: The currency in which prices are measured, specified in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. `usd`, `eur`, `jpy`).
        :rtype: str
        """
        return self._properties["price_unit"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self):
        """
        Fetch the CountryInstance


        :returns: The fetched CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the CountryInstance


        :returns: The fetched CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Pricing.V2.CountryInstance {}>".format(context)


class CountryContext(InstanceContext):
    def __init__(self, version: Version, iso_country: str):
        """
        Initialize the CountryContext

        :param Version version: Version that contains the resource
        :param iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the origin-based voice pricing information to fetch.

        :returns: twilio.rest.pricing.v2.country.CountryContext
        :rtype: twilio.rest.pricing.v2.country.CountryContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "iso_country": iso_country,
        }
        self._uri = "/Trunking/Countries/{iso_country}".format(**self._solution)

    def fetch(self):
        """
        Fetch the CountryInstance


        :returns: The fetched CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CountryInstance(
            self._version,
            payload,
            iso_country=self._solution["iso_country"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the CountryInstance


        :returns: The fetched CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CountryInstance(
            self._version,
            payload,
            iso_country=self._solution["iso_country"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Pricing.V2.CountryContext {}>".format(context)
