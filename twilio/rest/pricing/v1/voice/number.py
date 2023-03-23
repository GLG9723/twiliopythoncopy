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


from typing import Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class NumberInstance(InstanceResource):
    def __init__(self, version, payload, number: Optional[str] = None):
        """
        Initialize the NumberInstance

        :returns: twilio.rest.pricing.v1.voice.number.NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberInstance
        """
        super().__init__(version)

        self._properties = {
            "number": payload.get("number"),
            "country": payload.get("country"),
            "iso_country": payload.get("iso_country"),
            "outbound_call_price": payload.get("outbound_call_price"),
            "inbound_call_price": payload.get("inbound_call_price"),
            "price_unit": payload.get("price_unit"),
            "url": payload.get("url"),
        }

        self._solution = {
            "number": number or self._properties["number"],
        }
        self._context: Optional[NumberContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: NumberContext for this NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberContext
        """
        if self._context is None:
            self._context = NumberContext(
                self._version,
                number=self._solution["number"],
            )
        return self._context

    @property
    def number(self):
        """
        :returns: The phone number.
        :rtype: str
        """
        return self._properties["number"]

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
        :returns: The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
        :rtype: str
        """
        return self._properties["iso_country"]

    @property
    def outbound_call_price(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["outbound_call_price"]

    @property
    def inbound_call_price(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["inbound_call_price"]

    @property
    def price_unit(self):
        """
        :returns: The currency in which prices are measured, specified in [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. `usd`, `eur`, `jpy`).
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
        Fetch the NumberInstance


        :returns: The fetched NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the NumberInstance


        :returns: The fetched NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Pricing.V1.NumberInstance {}>".format(context)


class NumberContext(InstanceContext):
    def __init__(self, version: Version, number: str):
        """
        Initialize the NumberContext

        :param Version version: Version that contains the resource
        :param number: The phone number to fetch.

        :returns: twilio.rest.pricing.v1.voice.number.NumberContext
        :rtype: twilio.rest.pricing.v1.voice.number.NumberContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "number": number,
        }
        self._uri = "/Voice/Numbers/{number}".format(**self._solution)

    def fetch(self):
        """
        Fetch the NumberInstance


        :returns: The fetched NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return NumberInstance(
            self._version,
            payload,
            number=self._solution["number"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the NumberInstance


        :returns: The fetched NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return NumberInstance(
            self._version,
            payload,
            number=self._solution["number"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Pricing.V1.NumberContext {}>".format(context)


class NumberList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the NumberList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.pricing.v1.voice.number.NumberList
        :rtype: twilio.rest.pricing.v1.voice.number.NumberList
        """
        super().__init__(version)

    def get(self, number):
        """
        Constructs a NumberContext

        :param number: The phone number to fetch.

        :returns: twilio.rest.pricing.v1.voice.number.NumberContext
        :rtype: twilio.rest.pricing.v1.voice.number.NumberContext
        """
        return NumberContext(self._version, number=number)

    def __call__(self, number):
        """
        Constructs a NumberContext

        :param number: The phone number to fetch.

        :returns: twilio.rest.pricing.v1.voice.number.NumberContext
        :rtype: twilio.rest.pricing.v1.voice.number.NumberContext
        """
        return NumberContext(self._version, number=number)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Pricing.V1.NumberList>"
