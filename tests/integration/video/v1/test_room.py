# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class RoomTestCase(IntegrationTestCase):
    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms("RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://video.twilio.com/v1/Rooms/RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "peer-to-peer",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "unique_name",
                "max_participants": 10,
                "max_participant_duration": 86400,
                "max_concurrent_published_tracks": 0,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": null,
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "audio_only": false,
                "media_region": "us1",
                "empty_room_timeout": 5,
                "unused_room_timeout": 5,
                "end_time": "2015-07-30T20:00:00Z",
                "large_room": false,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings",
                    "recording_rules": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RecordingRules"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms(
            "RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms.create()

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://video.twilio.com/v1/Rooms",
            )
        )

    def test_create_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "peer-to-peer",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "max_concurrent_published_tracks": 0,
                "max_participants": 10,
                "max_participant_duration": 86400,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": null,
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "media_region": "us1",
                "audio_only": false,
                "empty_room_timeout": 5,
                "unused_room_timeout": 5,
                "end_time": "2015-07-30T20:00:00Z",
                "large_room": false,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings",
                    "recording_rules": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RecordingRules"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms.create()

        self.assertIsNotNone(actual)

    def test_create_webrtc_go_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "go",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "room1",
                "max_participants": 10,
                "max_participant_duration": 86400,
                "max_concurrent_published_tracks": 0,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": null,
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "media_region": "us1",
                "audio_only": false,
                "empty_room_timeout": 5,
                "unused_room_timeout": 5,
                "end_time": "2015-07-30T20:00:00Z",
                "large_room": false,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings",
                    "recording_rules": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RecordingRules"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms.create()

        self.assertIsNotNone(actual)

    def test_create_group_rooms_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "group",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "grouproom",
                "max_participants": 50,
                "max_participant_duration": 86400,
                "max_concurrent_published_tracks": 170,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": null,
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "media_region": "us1",
                "audio_only": false,
                "empty_room_timeout": 5,
                "unused_room_timeout": 5,
                "end_time": "2015-07-30T20:00:00Z",
                "large_room": false,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings",
                    "recording_rules": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RecordingRules"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms.create()

        self.assertIsNotNone(actual)

    def test_create_group_rooms_with_audio_only_enabled_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "group",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "grouproom",
                "max_participants": 50,
                "max_participant_duration": 86400,
                "max_concurrent_published_tracks": 170,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": null,
                "record_participants_on_connect": false,
                "video_codecs": [],
                "media_region": "us1",
                "audio_only": true,
                "empty_room_timeout": 5,
                "unused_room_timeout": 5,
                "end_time": "2015-07-30T20:00:00Z",
                "large_room": false,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings",
                    "recording_rules": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RecordingRules"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms.create()

        self.assertIsNotNone(actual)

    def test_create_small_group_rooms_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "group-small",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "SmallDailyStandup",
                "max_participants": 4,
                "max_participant_duration": 86400,
                "max_concurrent_published_tracks": 170,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": null,
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "media_region": "us1",
                "audio_only": false,
                "empty_room_timeout": 5,
                "unused_room_timeout": 5,
                "end_time": "2015-07-30T20:00:00Z",
                "large_room": false,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings",
                    "recording_rules": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RecordingRules"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms.create()

        self.assertIsNotNone(actual)

    def test_create_large_group_rooms_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "group",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "MyWebinar",
                "max_participants": 50,
                "max_participant_duration": 86400,
                "max_concurrent_published_tracks": 16,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": null,
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "media_region": "us1",
                "audio_only": false,
                "empty_room_timeout": 5,
                "unused_room_timeout": 5,
                "end_time": "2015-07-30T20:00:00Z",
                "large_room": false,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings",
                    "recording_rules": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RecordingRules"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms.create()

        self.assertIsNotNone(actual)

    def test_create_large_group_rooms_with_audio_only_enabled_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "in-progress",
                "type": "group",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "MyWebinar",
                "max_participants": 50,
                "max_participant_duration": 86400,
                "max_concurrent_published_tracks": 16,
                "duration": 0,
                "status_callback_method": "POST",
                "status_callback": null,
                "record_participants_on_connect": false,
                "video_codecs": [],
                "media_region": "us1",
                "audio_only": true,
                "empty_room_timeout": 5,
                "unused_room_timeout": 5,
                "end_time": "2015-07-30T20:00:00Z",
                "large_room": false,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings",
                    "recording_rules": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RecordingRules"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms.create()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://video.twilio.com/v1/Rooms",
            )
        )

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "rooms": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "rooms"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms.list()

        self.assertIsNotNone(actual)

    def test_read_with_status_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "rooms": [
                    {
                        "sid": "RM4070b618362c1682b2385b1f9982833c",
                        "status": "completed",
                        "date_created": "2017-04-03T22:21:49Z",
                        "date_updated": "2017-04-03T22:21:51Z",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "type": "peer-to-peer",
                        "enable_turn": true,
                        "unique_name": "RM4070b618362c1682b2385b1f9982833c",
                        "status_callback": null,
                        "status_callback_method": "POST",
                        "end_time": "2017-04-03T22:21:51Z",
                        "duration": 2,
                        "max_participants": 10,
                        "max_participant_duration": 86400,
                        "max_concurrent_published_tracks": 10,
                        "record_participants_on_connect": false,
                        "video_codecs": [
                            "VP8"
                        ],
                        "media_region": "us1",
                        "audio_only": false,
                        "empty_room_timeout": 5,
                        "unused_room_timeout": 5,
                        "large_room": false,
                        "url": "https://video.twilio.com/v1/Rooms/RM4070b618362c1682b2385b1f9982833c",
                        "links": {
                            "participants": "https://video.twilio.com/v1/Rooms/RM4070b618362c1682b2385b1f9982833c/Participants",
                            "recordings": "https://video.twilio.com/v1/Rooms/RM4070b618362c1682b2385b1f9982833c/Recordings",
                            "recording_rules": "https://video.twilio.com/v1/Rooms/RM4070b618362c1682b2385b1f9982833c/RecordingRules"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms?Status=completed&PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms?Status=completed&PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "rooms"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms("RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(
                status="in-progress"
            )

        values = {
            "Status": "in-progress",
        }

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://video.twilio.com/v1/Rooms/RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                data=values,
            )
        )

    def test_update_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "status": "completed",
                "type": "peer-to-peer",
                "sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "enable_turn": true,
                "unique_name": "unique_name",
                "max_participants": 10,
                "max_participant_duration": 86400,
                "max_concurrent_published_tracks": 10,
                "status_callback_method": "POST",
                "status_callback": null,
                "record_participants_on_connect": false,
                "video_codecs": [
                    "VP8"
                ],
                "media_region": "us1",
                "audio_only": false,
                "empty_room_timeout": 5,
                "unused_room_timeout": 5,
                "end_time": "2015-07-30T20:00:00Z",
                "large_room": false,
                "duration": 10,
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",
                    "recordings": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings",
                    "recording_rules": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RecordingRules"
                }
            }
            """,
            )
        )

        actual = self.client.video.v1.rooms(
            "RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).update(status="in-progress")

        self.assertIsNotNone(actual)
