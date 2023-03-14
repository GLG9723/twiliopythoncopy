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


class BindingTestCase(IntegrationTestCase):
    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.chat.v2.services(
                "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).bindings.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Bindings",
            )
        )

    def test_read_full_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "bindings"
                },
                "bindings": [
                    {
                        "sid": "BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2016-10-21T11:37:03Z",
                        "date_updated": "2016-10-21T11:37:03Z",
                        "endpoint": "TestUser-endpoint",
                        "identity": "TestUser",
                        "binding_type": "gcm",
                        "credential_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "message_types": [
                            "removed_from_channel",
                            "new_message",
                            "added_to_channel",
                            "invited_to_channel"
                        ],
                        "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings/BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "user": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/TestUser"
                        }
                    }
                ]
            }
            """,
            )
        )

        actual = self.client.chat.v2.services(
            "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).bindings.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "bindings"
                },
                "bindings": []
            }
            """,
            )
        )

        actual = self.client.chat.v2.services(
            "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).bindings.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.chat.v2.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").bindings(
                "BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Bindings/BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "sid": "BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2016-10-21T11:37:03Z",
                "date_updated": "2016-10-21T11:37:03Z",
                "endpoint": "TestUser-endpoint",
                "identity": "TestUser",
                "binding_type": "gcm",
                "credential_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "message_types": [
                    "removed_from_channel",
                    "new_message",
                    "added_to_channel",
                    "invited_to_channel"
                ],
                "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings/BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "user": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/TestUser"
                }
            }
            """,
            )
        )

        actual = (
            self.client.chat.v2.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .bindings("BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .fetch()
        )

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.chat.v2.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").bindings(
                "BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).delete()

        self.holodeck.assert_has_request(
            Request(
                "delete",
                "https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Bindings/BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_delete_response(self):
        self.holodeck.mock(
            Response(
                204,
                None,
            )
        )

        actual = (
            self.client.chat.v2.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .bindings("BSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .delete()
        )

        self.assertTrue(actual)
