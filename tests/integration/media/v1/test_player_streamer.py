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


class PlayerStreamerTestCase(IntegrationTestCase):
    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.media.v1.player_streamer(
                "VJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://media.twilio.com/v1/PlayerStreamers/VJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
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
                "status": "created",
                "video": true,
                "sid": "VJcafebabecafebabecafebabecafebabe",
                "status_callback": "http://www.example.com",
                "status_callback_method": "POST",
                "ended_reason": null,
                "url": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe",
                "max_duration": 300,
                "links": {
                    "timed_metadata": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe/TimedMetadata",
                    "playback_grant": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe/PlaybackGrant"
                }
            }
            """,
            )
        )

        actual = self.client.media.v1.player_streamer(
            "VJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.media.v1.player_streamer.create()

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://media.twilio.com/v1/PlayerStreamers",
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
                "status": "created",
                "video": true,
                "sid": "VJcafebabecafebabecafebabecafebabe",
                "status_callback": "http://www.example.com",
                "status_callback_method": "POST",
                "ended_reason": null,
                "url": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe",
                "max_duration": 300,
                "links": {
                    "timed_metadata": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe/TimedMetadata",
                    "playback_grant": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe/PlaybackGrant"
                }
            }
            """,
            )
        )

        actual = self.client.media.v1.player_streamer.create()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.media.v1.player_streamer(
                "VJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).update(status="ended")

        values = {
            "Status": "ended",
        }

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://media.twilio.com/v1/PlayerStreamers/VJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
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
                "date_updated": "2015-07-30T20:01:00Z",
                "status": "ended",
                "video": true,
                "sid": "VJcafebabecafebabecafebabecafebabe",
                "status_callback": "http://www.example.com",
                "status_callback_method": "POST",
                "ended_reason": "ended-via-api",
                "url": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe",
                "max_duration": 300,
                "links": {
                    "timed_metadata": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe/TimedMetadata",
                    "playback_grant": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe/PlaybackGrant"
                }
            }
            """,
            )
        )

        actual = self.client.media.v1.player_streamer(
            "VJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).update(status="ended")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.media.v1.player_streamer.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://media.twilio.com/v1/PlayerStreamers",
            )
        )

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "page": 0,
                    "page_size": 10,
                    "first_page_url": "https://media.twilio.com/v1/PlayerStreamers?Status=started&Order=asc&PageSize=10&Page=0",
                    "previous_page_url": null,
                    "url": "https://media.twilio.com/v1/PlayerStreamers?Status=started&Order=asc&PageSize=10&Page=0",
                    "next_page_url": null,
                    "key": "player_streamers"
                },
                "player_streamers": []
            }
            """,
            )
        )

        actual = self.client.media.v1.player_streamer.list()

        self.assertIsNotNone(actual)

    def test_read_items_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "page": 0,
                    "page_size": 10,
                    "first_page_url": "https://media.twilio.com/v1/PlayerStreamers?Status=ended&Order=desc&PageSize=10&Page=0",
                    "previous_page_url": null,
                    "url": "https://media.twilio.com/v1/PlayerStreamers?Status=ended&Order=desc&PageSize=10&Page=0",
                    "next_page_url": null,
                    "key": "player_streamers"
                },
                "player_streamers": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:01:00Z",
                        "status": "ended",
                        "video": true,
                        "sid": "VJcafebabecafebabecafebabecafebabe",
                        "status_callback": "http://www.example.com",
                        "status_callback_method": "POST",
                        "ended_reason": "ended-via-api",
                        "url": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe",
                        "max_duration": 300,
                        "links": {
                            "timed_metadata": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe/TimedMetadata",
                            "playback_grant": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe/PlaybackGrant"
                        }
                    }
                ]
            }
            """,
            )
        )

        actual = self.client.media.v1.player_streamer.list()

        self.assertIsNotNone(actual)

    def test_read_items_page_larger_than_max_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "page": 0,
                    "page_size": 100,
                    "first_page_url": "https://media.twilio.com/v1/PlayerStreamers?Status=ended&Order=desc&PageSize=100&Page=0",
                    "previous_page_url": null,
                    "url": "https://media.twilio.com/v1/PlayerStreamers?Status=ended&Order=desc&PageSize=100&Page=0",
                    "next_page_url": null,
                    "key": "player_streamers"
                },
                "player_streamers": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:01:00Z",
                        "status": "ended",
                        "video": true,
                        "sid": "VJcafebabecafebabecafebabecafebabe",
                        "status_callback": "http://www.example.com",
                        "status_callback_method": "POST",
                        "ended_reason": "ended-via-api",
                        "url": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe",
                        "max_duration": 300,
                        "links": {
                            "timed_metadata": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe/TimedMetadata",
                            "playback_grant": "https://media.twilio.com/v1/PlayerStreamers/VJcafebabecafebabecafebabecafebabe/PlaybackGrant"
                        }
                    }
                ]
            }
            """,
            )
        )

        actual = self.client.media.v1.player_streamer.list()

        self.assertIsNotNone(actual)
