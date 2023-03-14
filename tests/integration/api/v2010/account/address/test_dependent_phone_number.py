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


class DependentPhoneNumberTestCase(IntegrationTestCase):
    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(
                "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).addresses(
                "ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).dependent_phone_numbers.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Addresses/ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/DependentPhoneNumbers.json",
            )
        )

    def test_read_full_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "dependent_phone_numbers": [
                    {
                        "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "3197004499318",
                        "phone_number": "+3197004499318",
                        "voice_url": null,
                        "voice_method": "POST",
                        "voice_fallback_url": null,
                        "voice_fallback_method": "POST",
                        "voice_caller_id_lookup": false,
                        "date_created": "Thu, 23 Feb 2017 10:26:31 -0800",
                        "date_updated": "Thu, 23 Feb 2017 10:26:31 -0800",
                        "sms_url": "",
                        "sms_method": "POST",
                        "sms_fallback_url": "",
                        "sms_fallback_method": "POST",
                        "address_requirements": "any",
                        "capabilities": {
                            "Voice": false,
                            "SMS": true,
                            "MMS": false
                        },
                        "status_callback": "",
                        "status_callback_method": "POST",
                        "api_version": "2010-04-01",
                        "voice_application_sid": null,
                        "sms_application_sid": "",
                        "trunk_sid": null,
                        "emergency_status": "Inactive",
                        "emergency_address_sid": null,
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                    }
                ],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json?Page=0&PageSize=50",
                "next_page_uri": null,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json"
            }
            """,
            )
        )

        actual = (
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .addresses("ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .dependent_phone_numbers.list()
        )

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "dependent_phone_numbers": [],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json?Page=0&PageSize=50",
                "next_page_uri": null,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json"
            }
            """,
            )
        )

        actual = (
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .addresses("ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .dependent_phone_numbers.list()
        )

        self.assertIsNotNone(actual)
