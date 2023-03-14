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


class HighriskSpecialPrefixTestCase(IntegrationTestCase):
    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.voice.v1.dialing_permissions.countries(
                "US"
            ).highrisk_special_prefixes.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://voice.twilio.com/v1/DialingPermissions/Countries/US/HighRiskSpecialPrefixes",
            )
        )

    def test_read_lv_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "content": [
                    {
                        "prefix": "+37181"
                    },
                    {
                        "prefix": "+3719000"
                    }
                ],
                "meta": {
                    "first_page_url": "https://voice.twilio.com/v1/DialingPermissions/Countries/LV/HighRiskSpecialPrefixes?PageSize=50&Page=0",
                    "key": "content",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://voice.twilio.com/v1/DialingPermissions/Countries/LV/HighRiskSpecialPrefixes?PageSize=50&Page=0"
                }
            }
            """,
            )
        )

        actual = self.client.voice.v1.dialing_permissions.countries(
            "US"
        ).highrisk_special_prefixes.list()

        self.assertIsNotNone(actual)
