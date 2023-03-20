r"""
  This code was generated by
  ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
   |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
   |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

from twilio.base.domain import Domain
from twilio.rest.studio.v1 import V1
from twilio.rest.studio.v2 import V2


class StudioBase(Domain):
    def __init__(self, twilio):
        """
        Initialize the Studio Domain

        :returns: Domain for Studio
        """
        super().__init__(twilio, "https://studio.twilio.com")
        self._v1 = None
        self._v2 = None

    @property
    def v1(self) -> V1:
        """
        :returns: Versions v1 of Studio
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def v2(self) -> V2:
        """
        :returns: Versions v2 of Studio
        """
        if self._v2 is None:
            self._v2 = V2(self)
        return self._v2

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Studio>"
