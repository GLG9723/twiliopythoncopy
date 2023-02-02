"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.taskrouter.v1.workspace import WorkspaceList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of taskrouter

        :param domain: The Twilio.taskrouter domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._workspaces = None
        
    @property
    def workspaces(self) -> WorkspaceList:
        if self._workspaces is None:
            self._workspaces = WorkspaceList(self)
        return self._workspaces

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1>'
