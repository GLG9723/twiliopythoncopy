# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.exceptions import TwilioException
from twilio.http.response import Response


class CountryTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.pricing.v1.phone_numbers \
                                  .countries.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://pricing.twilio.com/v1/PhoneNumbers/Countries',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "countries": [
                    {
                        "country": "Austria",
                        "iso_country": "AT",
                        "url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries/AT"
                    }
                ],
                "meta": {
                    "first_page_url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0",
                    "key": "countries",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 1,
                    "previous_page_url": null,
                    "url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0"
                }
            }
            '''
        ))

        actual = self.client.pricing.v1.phone_numbers \
                                       .countries.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "countries": [],
                "meta": {
                    "first_page_url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0",
                    "key": "countries",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 1,
                    "previous_page_url": null,
                    "url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0"
                }
            }
            '''
        ))

        actual = self.client.pricing.v1.phone_numbers \
                                       .countries.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.pricing.v1.phone_numbers \
                                  .countries(iso_country="US").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://pricing.twilio.com/v1/PhoneNumbers/Countries/US',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "country": "Estonia",
                "iso_country": "EE",
                "phone_number_prices": [
                    {
                        "base_price": 3.0,
                        "current_price": 3.0,
                        "type": "mobile"
                    },
                    {
                        "base_price": 1.0,
                        "current_price": 1.0,
                        "type": "national"
                    }
                ],
                "price_unit": "usd",
                "url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries/US"
            }
            '''
        ))

        actual = self.client.pricing.v1.phone_numbers \
                                       .countries(iso_country="US").fetch()

        self.assertIsNotNone(actual)
