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


class SchemaVersionTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.events.v1.schemas("id") \
                                 .versions.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://events.twilio.com/v1/Schemas/id/Versions',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "schema_versions": [],
                "meta": {
                    "page": 0,
                    "page_size": 10,
                    "first_page_url": "https://events.twilio.com/v1/Schemas/Messaging.MessageStatus/Versions?PageSize=10&Page=0",
                    "previous_page_url": null,
                    "url": "https://events.twilio.com/v1/Schemas/Messaging.MessageStatus/Versions?PageSize=10&Page=0",
                    "next_page_url": null,
                    "key": "schema_versions"
                }
            }
            '''
        ))

        actual = self.client.events.v1.schemas("id") \
                                      .versions.list()

        self.assertIsNotNone(actual)

    def test_read_results_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "schema_versions": [
                    {
                        "id": "Messaging.MessageStatus",
                        "version": 1,
                        "public": true,
                        "date_created": "2015-07-30T20:00:00Z",
                        "url": "https://events.twilio.com/v1/Schemas/Messaging.MessageStatus/Versions/1",
                        "raw": "https://events-schemas.twilio.com/Messaging.MessageStatus/1"
                    },
                    {
                        "id": "Messaging.MessageStatus",
                        "version": 2,
                        "public": true,
                        "date_created": "2015-07-30T20:00:00Z",
                        "url": "https://events.twilio.com/v1/Schemas/Messaging.MessageStatus/Versions/2",
                        "raw": "https://events-schemas.twilio.com/Messaging.MessageStatus/2"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://events.twilio.com/v1/Schemas/Messaging.MessageStatus/Versions?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://events.twilio.com/v1/Schemas/Messaging.MessageStatus/Versions?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "schema_versions"
                }
            }
            '''
        ))

        actual = self.client.events.v1.schemas("id") \
                                      .versions.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.events.v1.schemas("id") \
                                 .versions(1).fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://events.twilio.com/v1/Schemas/id/Versions/1',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "id": "Messaging.MessageStatus",
                "version": 1,
                "public": true,
                "date_created": "2015-07-30T20:00:00Z",
                "url": "https://events.twilio.com/v1/Schemas/Messaging.MessageStatus/Versions/1",
                "raw": "https://events-schemas.twilio.com/Messaging.MessageStatus/1"
            }
            '''
        ))

        actual = self.client.events.v1.schemas("id") \
                                      .versions(1).fetch()

        self.assertIsNotNone(actual)
