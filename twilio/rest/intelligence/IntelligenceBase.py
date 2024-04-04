r"""
  This code was generated by
  ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
   |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
   |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

from typing import Optional

from twilio.base.domain import Domain
from twilio.rest import Client
from twilio.rest.intelligence.v2 import V2


class IntelligenceBase(Domain):

    def __init__(self, twilio: Client):
        """
        Initialize the Intelligence Domain

        :returns: Domain for Intelligence
        """
        super().__init__(twilio, "https://intelligence.twilio.com")
        self._v2: Optional[V2] = None

    @property
    def v2(self) -> V2:
        """
        :returns: Versions v2 of Intelligence
        """
        if self._v2 is None:
            self._v2 = V2(self)
        return self._v2

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence>"
