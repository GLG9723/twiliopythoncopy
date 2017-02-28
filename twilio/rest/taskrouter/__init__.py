# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.domain import Domain
from twilio.rest.taskrouter.v1 import V1


class Taskrouter(Domain):

    def __init__(self, twilio):
        """
        Initialize the Taskrouter Domain

        :returns: Domain for Taskrouter
        :rtype: Taskrouter
        """
        super(Taskrouter, self).__init__(twilio)

        self.base_url = 'https://taskrouter.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of taskrouter
        :rtype: V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def workspaces(self):
        """
        :rtype: WorkspaceList
        """
        return self.v1.workspaces

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter>'
