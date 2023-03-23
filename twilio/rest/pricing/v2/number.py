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


from typing import List, Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class NumberInstance(InstanceResource):
    def __init__(self, version, payload, destination_number: Optional[str] = None):
        """
        Initialize the NumberInstance
        """
        super().__init__(version)

        self._properties = {
            "destination_number": payload.get("destination_number"),
            "origination_number": payload.get("origination_number"),
            "country": payload.get("country"),
            "iso_country": payload.get("iso_country"),
            "terminating_prefix_prices": payload.get("terminating_prefix_prices"),
            "originating_call_price": payload.get("originating_call_price"),
            "price_unit": payload.get("price_unit"),
            "url": payload.get("url"),
        }

        self._solution = {
            "destination_number": destination_number
            or self._properties["destination_number"],
        }
        self._context: Optional[NumberContext] = None

    @property
    def _proxy(self) -> "NumberContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: NumberContext for this NumberInstance
        """
        if self._context is None:
            self._context = NumberContext(
                self._version,
                destination_number=self._solution["destination_number"],
            )
        return self._context

    @property
    def destination_number(self) -> str:
        """
        :returns: The destination phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        """
        return self._properties["destination_number"]

    @property
    def origination_number(self) -> str:
        """
        :returns: The origination phone number in [[E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        """
        return self._properties["origination_number"]

    @property
    def country(self) -> str:
        """
        :returns: The name of the country.
        """
        return self._properties["country"]

    @property
    def iso_country(self) -> str:
        """
        :returns: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
        """
        return self._properties["iso_country"]

    @property
    def terminating_prefix_prices(self) -> List[str]:
        """
        :returns:
        """
        return self._properties["terminating_prefix_prices"]

    @property
    def originating_call_price(self) -> str:
        """
        :returns:
        """
        return self._properties["originating_call_price"]

    @property
    def price_unit(self) -> str:
        """
        :returns: The currency in which prices are measured, specified in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. `usd`, `eur`, `jpy`).
        """
        return self._properties["price_unit"]

    @property
    def url(self) -> str:
        """
        :returns: The absolute URL of the resource.
        """
        return self._properties["url"]

    def fetch(self, origination_number=values.unset) -> "NumberInstance":
        """
        Fetch the NumberInstance

        :param str origination_number: The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.

        :returns: The fetched NumberInstance
        """
        return self._proxy.fetch(
            origination_number=origination_number,
        )

    async def fetch_async(self, origination_number=values.unset) -> "NumberInstance":
        """
        Asynchronous coroutine to fetch the NumberInstance

        :param str origination_number: The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.

        :returns: The fetched NumberInstance
        """
        return await self._proxy.fetch_async(
            origination_number=origination_number,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Pricing.V2.NumberInstance {}>".format(context)


class NumberContext(InstanceContext):
    def __init__(self, version: Version, destination_number: str):
        """
        Initialize the NumberContext

        :param version: Version that contains the resource
        :param destination_number: The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "destination_number": destination_number,
        }
        self._uri = "/Trunking/Numbers/{destination_number}".format(**self._solution)

    def fetch(self, origination_number=values.unset) -> NumberInstance:
        """
        Fetch the NumberInstance

        :param str origination_number: The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.

        :returns: The fetched NumberInstance
        """

        data = values.of(
            {
                "OriginationNumber": origination_number,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return NumberInstance(
            self._version,
            payload,
            destination_number=self._solution["destination_number"],
        )

    async def fetch_async(self, origination_number=values.unset) -> NumberInstance:
        """
        Asynchronous coroutine to fetch the NumberInstance

        :param str origination_number: The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.

        :returns: The fetched NumberInstance
        """

        data = values.of(
            {
                "OriginationNumber": origination_number,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return NumberInstance(
            self._version,
            payload,
            destination_number=self._solution["destination_number"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Pricing.V2.NumberContext {}>".format(context)


class NumberList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the NumberList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, destination_number) -> NumberContext:
        """
        Constructs a NumberContext

        :param destination_number: The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
        """
        return NumberContext(self._version, destination_number=destination_number)

    def __call__(self, destination_number) -> NumberContext:
        """
        Constructs a NumberContext

        :param destination_number: The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
        """
        return NumberContext(self._version, destination_number=destination_number)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Pricing.V2.NumberList>"
