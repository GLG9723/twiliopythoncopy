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


class AvailableAddOnExtensionTestCase(IntegrationTestCase):
    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.preview.marketplace.available_add_ons(
                "XBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).extensions("XFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://preview.twilio.com/marketplace/AvailableAddOns/XBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Extensions/XFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "sid": "XFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "available_add_on_sid": "XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Incoming Voice Call",
                "product_name": "Programmable Voice",
                "unique_name": "voice-incoming",
                "url": "https://preview.twilio.com/marketplace/AvailableAddOns/XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions/XFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = (
            self.client.preview.marketplace.available_add_ons(
                "XBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            )
            .extensions("XFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .fetch()
        )

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.preview.marketplace.available_add_ons(
                "XBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).extensions.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://preview.twilio.com/marketplace/AvailableAddOns/XBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Extensions",
            )
        )

    def test_read_full_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "extensions": [
                    {
                        "sid": "XFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "available_add_on_sid": "XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "Incoming Voice Call",
                        "product_name": "Programmable Voice",
                        "unique_name": "voice-incoming",
                        "url": "https://preview.twilio.com/marketplace/AvailableAddOns/XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions/XFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://preview.twilio.com/marketplace/AvailableAddOns/XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/marketplace/AvailableAddOns/XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "extensions"
                }
            }
            """,
            )
        )

        actual = self.client.preview.marketplace.available_add_ons(
            "XBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).extensions.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "extensions": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://preview.twilio.com/marketplace/AvailableAddOns/XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/marketplace/AvailableAddOns/XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "extensions"
                }
            }
            """,
            )
        )

        actual = self.client.preview.marketplace.available_add_ons(
            "XBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).extensions.list()

        self.assertIsNotNone(actual)
