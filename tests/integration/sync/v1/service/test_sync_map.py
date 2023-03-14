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


class SyncMapTestCase(IntegrationTestCase):
    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.sync.v1.services(
                "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).sync_maps("MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://sync.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Maps/MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "created_by": "created_by",
                "date_expires": "2015-07-30T21:00:00Z",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "links": {
                    "items": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items",
                    "permissions": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Permissions"
                },
                "revision": "revision",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = (
            self.client.sync.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .sync_maps("MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .fetch()
        )

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.sync.v1.services(
                "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).sync_maps("MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(
            Request(
                "delete",
                "https://sync.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Maps/MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
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
            self.client.sync.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .sync_maps("MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .delete()
        )

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.sync.v1.services(
                "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).sync_maps.create()

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://sync.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Maps",
            )
        )

    def test_create_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "created_by": "created_by",
                "date_expires": "2015-07-30T21:00:00Z",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "links": {
                    "items": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items",
                    "permissions": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Permissions"
                },
                "revision": "revision",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = self.client.sync.v1.services(
            "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).sync_maps.create()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.sync.v1.services(
                "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).sync_maps("MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://sync.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Maps/MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_update_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "created_by": "created_by",
                "date_expires": "2015-07-30T21:00:00Z",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "links": {
                    "items": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items",
                    "permissions": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Permissions"
                },
                "revision": "revision",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = (
            self.client.sync.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .sync_maps("MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .update()
        )

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.sync.v1.services(
                "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).sync_maps.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://sync.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Maps",
            )
        )

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "maps": [],
                "meta": {
                    "first_page_url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps?PageSize=50&Page=0",
                    "key": "maps",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps?PageSize=50&Page=0"
                }
            }
            """,
            )
        )

        actual = self.client.sync.v1.services(
            "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).sync_maps.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "maps": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "created_by": "created_by",
                        "date_expires": "2015-07-30T21:00:00Z",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "links": {
                            "items": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items",
                            "permissions": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Permissions"
                        },
                        "revision": "revision",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "unique_name",
                        "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps?PageSize=50&Page=0",
                    "key": "maps",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps?PageSize=50&Page=0"
                }
            }
            """,
            )
        )

        actual = self.client.sync.v1.services(
            "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).sync_maps.list()

        self.assertIsNotNone(actual)
