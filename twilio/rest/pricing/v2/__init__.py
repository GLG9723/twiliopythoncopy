"""
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

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.pricing.v2.country import CountryList
from twilio.rest.pricing.v2.number import NumberList
from twilio.rest.pricing.v2.voice import VoiceList


class V2(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V2 version of pricing

        :param domain: The Twilio.pricing domain
        """
        super().__init__(domain)
        self.version = 'v2'
        self._countries = None
        self._numbers = None
        self._voice = None
        
    @property
    def countries(self) -> CountryList:
        if self._countries is None:
            self._countries = CountryList(self)
        return self._countries

    @property
    def numbers(self) -> NumberList:
        if self._numbers is None:
            self._numbers = NumberList(self)
        return self._numbers

    @property
    def voice(self) -> VoiceList:
        if self._voice is None:
            self._voice = VoiceList(self)
        return self._voice

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V2>'
