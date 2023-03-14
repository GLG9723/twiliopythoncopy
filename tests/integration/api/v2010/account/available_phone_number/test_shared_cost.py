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


class SharedCostTestCase(IntegrationTestCase):
    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(
                "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).available_phone_numbers("US").shared_cost.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/AvailablePhoneNumbers/US/SharedCost.json",
            )
        )

    def test_read_full_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "available_phone_numbers": [
                    {
                        "address_requirements": "none",
                        "beta": false,
                        "capabilities": {
                            "mms": false,
                            "sms": true,
                            "voice": false
                        },
                        "friendly_name": "+4759440374",
                        "iso_country": "NO",
                        "lata": null,
                        "latitude": null,
                        "locality": null,
                        "longitude": null,
                        "phone_number": "+4759440374",
                        "postal_code": null,
                        "rate_center": null,
                        "region": null
                    }
                ],
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/SharedCost.json"
            }
            """,
            )
        )

        actual = (
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .available_phone_numbers("US")
            .shared_cost.list()
        )

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "available_phone_numbers": [],
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/SharedCost.json"
            }
            """,
            )
        )

        actual = (
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .available_phone_numbers("US")
            .shared_cost.list()
        )

        self.assertIsNotNone(actual)
