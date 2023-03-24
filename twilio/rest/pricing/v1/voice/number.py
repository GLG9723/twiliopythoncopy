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


from typing import Any, Dict, Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class NumberInstance(InstanceResource):

    """
    :ivar number: The phone number.
    :ivar country: The name of the country.
    :ivar iso_country: The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    :ivar outbound_call_price:
    :ivar inbound_call_price:
    :ivar price_unit: The currency in which prices are measured, specified in [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. `usd`, `eur`, `jpy`).
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], number: Optional[str] = None
    ):
        super().__init__(version)

        self.number: Optional[str] = payload.get("number")
        self.country: Optional[str] = payload.get("country")
        self.iso_country: Optional[str] = payload.get("iso_country")
        self.outbound_call_price: Optional[str] = payload.get("outbound_call_price")
        self.inbound_call_price: Optional[str] = payload.get("inbound_call_price")
        self.price_unit: Optional[str] = payload.get("price_unit")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "number": number or self.number,
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
                number=self._solution["number"],
            )
        return self._context

    def fetch(self) -> "NumberInstance":
        """
        Fetch the NumberInstance


        :returns: The fetched NumberInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "NumberInstance":
        """
        Asynchronous coroutine to fetch the NumberInstance


        :returns: The fetched NumberInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Pricing.V1.NumberInstance {}>".format(context)


class NumberContext(InstanceContext):
    def __init__(self, version: Version, number: str):
        """
        Initialize the NumberContext

        :param version: Version that contains the resource
        :param number: The phone number to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "number": number,
        }
        self._uri = "/Voice/Numbers/{number}".format(**self._solution)

    def fetch(self) -> NumberInstance:
        """
        Fetch the NumberInstance


        :returns: The fetched NumberInstance
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

    async def fetch_async(self) -> NumberInstance:
        """
        Asynchronous coroutine to fetch the NumberInstance


        :returns: The fetched NumberInstance
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

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Pricing.V1.NumberContext {}>".format(context)


class NumberList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the NumberList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, number) -> NumberContext:
        """
        Constructs a NumberContext

        :param number: The phone number to fetch.
        """
        return NumberContext(self._version, number=number)

    def __call__(self, number) -> NumberContext:
        """
        Constructs a NumberContext

        :param number: The phone number to fetch.
        """
        return NumberContext(self._version, number=number)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Pricing.V1.NumberList>"
