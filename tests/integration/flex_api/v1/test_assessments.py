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


class AssessmentsTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.assessments().create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Accounts/Assessments',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "url": "https://flex-api.twilio.com/v1/Accounts/Assessments"
            }
            '''
        ))

        actual = self.client.flex_api.v1.assessments().create()

        self.assertIsNotNone(actual)
