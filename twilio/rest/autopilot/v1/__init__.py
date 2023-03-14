r"""
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
from twilio.rest.autopilot.v1.assistant import AssistantList
from twilio.rest.autopilot.v1.restore_assistant import RestoreAssistantList


class V1(Version):
    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Autopilot

        :param domain: The Twilio.autopilot domain
        """
        super().__init__(domain)
        self.version = "v1"
        self._assistants = None
        self._restore_assistant = None

    @property
    def assistants(self) -> AssistantList:
        """
        :rtype: twilio.rest.autopilot.v1.assistant.AssistantList
        """
        if self._assistants is None:
            self._assistants = AssistantList(self)
        return self._assistants

    @property
    def restore_assistant(self) -> RestoreAssistantList:
        """
        :rtype: twilio.rest.autopilot.v1.restore_assistant.RestoreAssistantList
        """
        if self._restore_assistant is None:
            self._restore_assistant = RestoreAssistantList(self)
        return self._restore_assistant

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Autopilot.V1>"
