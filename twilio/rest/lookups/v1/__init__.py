r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Lookups
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.lookups.v1.phone_number import PhoneNumberList


class V1(Version):
    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Lookups

        :param domain: The Twilio.lookups domain
        """
        super().__init__(domain)
        self.version = "v1"
        self._phone_numbers = None

    @property
    def phone_numbers(self) -> PhoneNumberList:
        """
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberList
        """
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(self)
        return self._phone_numbers

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Lookups.V1>"
