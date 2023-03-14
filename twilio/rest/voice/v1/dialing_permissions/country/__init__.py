"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
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
from twilio.rest.voice.v1.dialing_permissions.country.highrisk_special_prefix import (
    HighriskSpecialPrefixList,
)


class CountryList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the CountryList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.voice.v1.dialing_permissions.country.CountryList
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/DialingPermissions/Countries".format(**self._solution)

    def stream(
        self,
        iso_code=values.unset,
        continent=values.unset,
        country_code=values.unset,
        low_risk_numbers_enabled=values.unset,
        high_risk_special_numbers_enabled=values.unset,
        high_risk_tollfraud_numbers_enabled=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams CountryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str iso_code: Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        :param str continent: Filter to retrieve the country permissions by specifying the continent
        :param str country_code: Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
        :param bool low_risk_numbers_enabled: Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: `true` or `false`.
        :param bool high_risk_special_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: `true` or `false`
        :param bool high_risk_tollfraud_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/learn/voice-and-video/toll-fraud) numbers enabled. Can be: `true` or `false`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.voice.v1.dialing_permissions.country.CountryInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            iso_code=iso_code,
            continent=continent,
            country_code=country_code,
            low_risk_numbers_enabled=low_risk_numbers_enabled,
            high_risk_special_numbers_enabled=high_risk_special_numbers_enabled,
            high_risk_tollfraud_numbers_enabled=high_risk_tollfraud_numbers_enabled,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    def list(
        self,
        iso_code=values.unset,
        continent=values.unset,
        country_code=values.unset,
        low_risk_numbers_enabled=values.unset,
        high_risk_special_numbers_enabled=values.unset,
        high_risk_tollfraud_numbers_enabled=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists CountryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str iso_code: Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        :param str continent: Filter to retrieve the country permissions by specifying the continent
        :param str country_code: Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
        :param bool low_risk_numbers_enabled: Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: `true` or `false`.
        :param bool high_risk_special_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: `true` or `false`
        :param bool high_risk_tollfraud_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/learn/voice-and-video/toll-fraud) numbers enabled. Can be: `true` or `false`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.voice.v1.dialing_permissions.country.CountryInstance]
        """
        return list(
            self.stream(
                iso_code=iso_code,
                continent=continent,
                country_code=country_code,
                low_risk_numbers_enabled=low_risk_numbers_enabled,
                high_risk_special_numbers_enabled=high_risk_special_numbers_enabled,
                high_risk_tollfraud_numbers_enabled=high_risk_tollfraud_numbers_enabled,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        iso_code=values.unset,
        continent=values.unset,
        country_code=values.unset,
        low_risk_numbers_enabled=values.unset,
        high_risk_special_numbers_enabled=values.unset,
        high_risk_tollfraud_numbers_enabled=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of CountryInstance records from the API.
        Request is executed immediately

        :param str iso_code: Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        :param str continent: Filter to retrieve the country permissions by specifying the continent
        :param str country_code: Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
        :param bool low_risk_numbers_enabled: Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: `true` or `false`.
        :param bool high_risk_special_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: `true` or `false`
        :param bool high_risk_tollfraud_numbers_enabled: Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/learn/voice-and-video/toll-fraud) numbers enabled. Can be: `true` or `false`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CountryInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryPage
        """
        data = values.of(
            {
                "IsoCode": iso_code,
                "Continent": continent,
                "CountryCode": country_code,
                "LowRiskNumbersEnabled": low_risk_numbers_enabled,
                "HighRiskSpecialNumbersEnabled": high_risk_special_numbers_enabled,
                "HighRiskTollfraudNumbersEnabled": high_risk_tollfraud_numbers_enabled,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CountryPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CountryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CountryInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CountryPage(self._version, response, self._solution)

    def get(self, iso_code):
        """
        Constructs a CountryContext

        :param iso_code: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch

        :returns: twilio.rest.voice.v1.dialing_permissions.country.CountryContext
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryContext
        """
        return CountryContext(self._version, iso_code=iso_code)

    def __call__(self, iso_code):
        """
        Constructs a CountryContext

        :param iso_code: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch

        :returns: twilio.rest.voice.v1.dialing_permissions.country.CountryContext
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryContext
        """
        return CountryContext(self._version, iso_code=iso_code)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Voice.V1.CountryList>"


class CountryPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the CountryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.voice.v1.dialing_permissions.country.CountryPage
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CountryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.voice.v1.dialing_permissions.country.CountryInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryInstance
        """
        return CountryInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Voice.V1.CountryPage>"


class CountryInstance(InstanceResource):
    def __init__(self, version, payload, iso_code: str = None):
        """
        Initialize the CountryInstance

        :returns: twilio.rest.voice.v1.dialing_permissions.country.CountryInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryInstance
        """
        super().__init__(version)

        self._properties = {
            "iso_code": payload.get("iso_code"),
            "name": payload.get("name"),
            "continent": payload.get("continent"),
            "country_codes": payload.get("country_codes"),
            "low_risk_numbers_enabled": payload.get("low_risk_numbers_enabled"),
            "high_risk_special_numbers_enabled": payload.get(
                "high_risk_special_numbers_enabled"
            ),
            "high_risk_tollfraud_numbers_enabled": payload.get(
                "high_risk_tollfraud_numbers_enabled"
            ),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._context = None
        self._solution = {
            "iso_code": iso_code or self._properties["iso_code"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CountryContext for this CountryInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryContext
        """
        if self._context is None:
            self._context = CountryContext(
                self._version,
                iso_code=self._solution["iso_code"],
            )
        return self._context

    @property
    def iso_code(self):
        """
        :returns: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
        :rtype: str
        """
        return self._properties["iso_code"]

    @property
    def name(self):
        """
        :returns: The name of the country.
        :rtype: str
        """
        return self._properties["name"]

    @property
    def continent(self):
        """
        :returns: The name of the continent in which the country is located.
        :rtype: str
        """
        return self._properties["continent"]

    @property
    def country_codes(self):
        """
        :returns: The E.164 assigned [country codes(s)](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
        :rtype: list[str]
        """
        return self._properties["country_codes"]

    @property
    def low_risk_numbers_enabled(self):
        """
        :returns: Whether dialing to low-risk numbers is enabled.
        :rtype: bool
        """
        return self._properties["low_risk_numbers_enabled"]

    @property
    def high_risk_special_numbers_enabled(self):
        """
        :returns: Whether dialing to high-risk special services numbers is enabled. These prefixes include number ranges allocated by the country and include premium numbers, special services, shared cost, and others
        :rtype: bool
        """
        return self._properties["high_risk_special_numbers_enabled"]

    @property
    def high_risk_tollfraud_numbers_enabled(self):
        """
        :returns: Whether dialing to high-risk [toll fraud](https://www.twilio.com/learn/voice-and-video/toll-fraud) numbers is enabled. These prefixes include narrow number ranges that have a high-risk of international revenue sharing fraud (IRSF) attacks, also known as [toll fraud](https://www.twilio.com/learn/voice-and-video/toll-fraud). These prefixes are collected from anti-fraud databases and verified by analyzing calls on our network. These prefixes are not available for download and are updated frequently
        :rtype: bool
        """
        return self._properties["high_risk_tollfraud_numbers_enabled"]

    @property
    def url(self):
        """
        :returns: The absolute URL of this resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns: A list of URLs related to this resource.
        :rtype: dict
        """
        return self._properties["links"]

    def fetch(self):
        """
        Fetch the CountryInstance


        :returns: The fetched CountryInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryInstance
        """
        return self._proxy.fetch()

    @property
    def highrisk_special_prefixes(self):
        """
        Access the highrisk_special_prefixes

        :returns: twilio.rest.voice.v1.dialing_permissions.country.HighriskSpecialPrefixList
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.HighriskSpecialPrefixList
        """
        return self._proxy.highrisk_special_prefixes

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Voice.V1.CountryInstance {}>".format(context)


class CountryContext(InstanceContext):
    def __init__(self, version: Version, iso_code: str):
        """
        Initialize the CountryContext

        :param Version version: Version that contains the resource
        :param iso_code: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch

        :returns: twilio.rest.voice.v1.dialing_permissions.country.CountryContext
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "iso_code": iso_code,
        }
        self._uri = "/DialingPermissions/Countries/{iso_code}".format(**self._solution)

        self._highrisk_special_prefixes = None

    def fetch(self):
        """
        Fetch the CountryInstance


        :returns: The fetched CountryInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.CountryInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CountryInstance(
            self._version,
            payload,
            iso_code=self._solution["iso_code"],
        )

    @property
    def highrisk_special_prefixes(self):
        """
        Access the highrisk_special_prefixes

        :returns: twilio.rest.voice.v1.dialing_permissions.country.HighriskSpecialPrefixList
        :rtype: twilio.rest.voice.v1.dialing_permissions.country.HighriskSpecialPrefixList
        """
        if self._highrisk_special_prefixes is None:
            self._highrisk_special_prefixes = HighriskSpecialPrefixList(
                self._version,
                self._solution["iso_code"],
            )
        return self._highrisk_special_prefixes

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Voice.V1.CountryContext {}>".format(context)
