"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.autopilot.v1.assistant import AssistantListInstance
from twilio.rest.autopilot.v1.restore_assistant import RestoreAssistantListInstance


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of autopilot

        :param domain: The Twilio.autopilot domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._assistants = None
        self._restore_assistant = None
        
    @property
    def assistants(self) -> AssistantListInstance:
        if self._assistants is None:
            self._assistants = AssistantListInstance(self)
        return self._assistants

    @property
    def restore_assistant(self) -> RestoreAssistantListInstance:
        if self._restore_assistant is None:
            self._restore_assistant = RestoreAssistantListInstance(self)
        return self._restore_assistant

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.autopilot.V1>'
