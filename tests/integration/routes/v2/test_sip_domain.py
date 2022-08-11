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


class SipDomainTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.routes.v2.sip_domains("sip_domain").create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://routes.twilio.com/v2/SipDomains/sip_domain',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "url": "https://routes.twilio.com/v2/SipDomains/test.sip.twilio.com",
                "sip_domain": "test.sip.twilio.com",
                "sid": "QQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "voice_region": "au1",
                "date_created": "2020-08-07T22:29:24Z",
                "date_updated": "2020-08-07T22:29:24Z"
            }
            '''
        ))

        actual = self.client.routes.v2.sip_domains("sip_domain").create()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.routes.v2.sip_domains("sip_domain").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://routes.twilio.com/v2/SipDomains/sip_domain',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "url": "https://routes.twilio.com/v2/SipDomains/test.sip.twilio.com",
                "sip_domain": "test.sip.twilio.com",
                "sid": "QQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "voice_region": "au1",
                "date_created": "2020-08-07T22:29:24Z",
                "date_updated": "2020-08-07T22:29:24Z"
            }
            '''
        ))

        actual = self.client.routes.v2.sip_domains("sip_domain").update()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.routes.v2.sip_domains("sip_domain").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://routes.twilio.com/v2/SipDomains/sip_domain',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "url": "https://routes.twilio.com/v2/SipDomains/test.sip.twilio.com",
                "account_sid": "AC00000000000000000000000000000000",
                "sid": "QQ00000000000000000000000000000000",
                "sip_domain": "test.sip.twilio.com",
                "friendly_name": "string",
                "voice_region": "string",
                "date_created": "2022-06-02T22:33:47Z",
                "date_updated": "2022-06-02T22:33:47Z"
            }
            '''
        ))

        actual = self.client.routes.v2.sip_domains("sip_domain").fetch()

        self.assertIsNotNone(actual)
