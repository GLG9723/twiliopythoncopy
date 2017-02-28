# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.domain import Domain
from twilio.rest.monitor.v1 import V1


class Monitor(Domain):

    def __init__(self, twilio):
        """
        Initialize the Monitor Domain

        :returns: Domain for Monitor
        :rtype: Monitor
        """
        super(Monitor, self).__init__(twilio)

        self.base_url = 'https://monitor.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of monitor
        :rtype: V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def alerts(self):
        """
        :rtype: AlertList
        """
        return self.v1.alerts

    @property
    def events(self):
        """
        :rtype: EventList
        """
        return self.v1.events

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Monitor>'
