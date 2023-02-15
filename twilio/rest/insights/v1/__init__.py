"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.insights.v1.call import CallList
from twilio.rest.insights.v1.call_summaries import CallSummariesList
from twilio.rest.insights.v1.conference import ConferenceList
from twilio.rest.insights.v1.room import RoomList
from twilio.rest.insights.v1.setting import SettingList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Insights

        :param domain: The Twilio.insights domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._calls = None
        self._call_summaries = None
        self._conferences = None
        self._rooms = None
        self._settings = None
        
    @property
    def calls(self) -> CallList:
        if self._calls is None:
            self._calls = CallList(self)
        return self._calls

    @property
    def call_summaries(self) -> CallSummariesList:
        if self._call_summaries is None:
            self._call_summaries = CallSummariesList(self)
        return self._call_summaries

    @property
    def conferences(self) -> ConferenceList:
        if self._conferences is None:
            self._conferences = ConferenceList(self)
        return self._conferences

    @property
    def rooms(self) -> RoomList:
        if self._rooms is None:
            self._rooms = RoomList(self)
        return self._rooms

    @property
    def settings(self) -> SettingList:
        if self._settings is None:
            self._settings = SettingList(self)
        return self._settings

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1>'
