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




from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.pricing.v1.voice.country import CountryList
from twilio.rest.pricing.v1.voice.number import NumberList


class VoiceList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the VoiceList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.pricing.v1.voice.VoiceList
        :rtype: twilio.rest.pricing.v1.voice.VoiceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/Voice".format(**self._solution)

        self._countries = None
        self._numbers = None

    @property
    def countries(self):
        """
        Access the countries

        :returns: twilio.rest.pricing.v1.voice.CountryList
        :rtype: twilio.rest.pricing.v1.voice.CountryList
        """
        if self._countries is None:
            self._countries = CountryList(self._version)
        return self._countries

    @property
    def numbers(self):
        """
        Access the numbers

        :returns: twilio.rest.pricing.v1.voice.NumberList
        :rtype: twilio.rest.pricing.v1.voice.NumberList
        """
        if self._numbers is None:
            self._numbers = NumberList(self._version)
        return self._numbers

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Pricing.V1.VoiceList>"
