"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Media
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.media.v1.media_processor import MediaProcessorList
from twilio.rest.media.v1.media_recording import MediaRecordingList
from twilio.rest.media.v1.player_streamer import PlayerStreamerList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Media

        :param domain: The Twilio.media domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._media_processor = None
        self._media_recording = None
        self._player_streamer = None
        
    @property
    def media_processor(self) -> MediaProcessorListInstance:
        if self._media_processor is None:
            self._media_processor = MediaProcessorListInstance(self)
        return self._media_processor

    @property
    def media_recording(self) -> MediaRecordingListInstance:
        if self._media_recording is None:
            self._media_recording = MediaRecordingListInstance(self)
        return self._media_recording

    @property
    def player_streamer(self) -> PlayerStreamerListInstance:
        if self._player_streamer is None:
            self._player_streamer = PlayerStreamerListInstance(self)
        return self._player_streamer

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Media.V1>'
