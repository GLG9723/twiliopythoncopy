# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class ExportConfigurationTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.bulk_exports.export_configuration(resource_type="resource_type").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/BulkExports/Exports/resource_type/Configuration',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "url": "https://preview.twilio.com/BulkExports/Exports/Calls/Configuration",
                "enabled": true,
                "webhook_url": "",
                "webhook_method": "",
                "resource_type": "Calls"
            }
            '''
        ))

        actual = self.client.preview.bulk_exports.export_configuration(resource_type="resource_type").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.bulk_exports.export_configuration(resource_type="resource_type").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/BulkExports/Exports/resource_type/Configuration',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "url": "https://preview.twilio.com/BulkExports/Exports/Calls/Configuration",
                "enabled": true,
                "webhook_url": "",
                "resource_type": "Calls",
                "webhook_method": ""
            }
            '''
        ))

        actual = self.client.preview.bulk_exports.export_configuration(resource_type="resource_type").update()

        self.assertIsNotNone(actual)
