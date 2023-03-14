"""
  This code was generated by
  ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
   |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
   |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

from twilio.base.domain import Domain
from twilio.rest.chat.v1 import V1
from twilio.rest.chat.v2 import V2
from twilio.rest.chat.v3 import V3


class ChatBase(Domain):
    def __init__(self, twilio):
        """
        Initialize the Chat Domain

        :returns: Domain for Chat
        :rtype: twilio.rest.chat.Chat
        """
        super().__init__(twilio)
        self.base_url = "https://chat.twilio.com"
        self._v1 = None
        self._v2 = None
        self._v3 = None

    @property
    def v1(self):
        """
        :returns: Versions v1 of Chat
        :rtype: twilio.rest.chat.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def v2(self):
        """
        :returns: Versions v2 of Chat
        :rtype: twilio.rest.chat.v2.V2
        """
        if self._v2 is None:
            self._v2 = V2(self)
        return self._v2

    @property
    def v3(self):
        """
        :returns: Versions v3 of Chat
        :rtype: twilio.rest.chat.v3.V3
        """
        if self._v3 is None:
            self._v3 = V3(self)
        return self._v3

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Chat>"
