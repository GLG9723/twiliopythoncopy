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


class TokenTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .tokens.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Tokens.json',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "username": "dc2d2894d5a9023620c467b0e71cfa6a35457e6679785ed6ae9856fe5bdfa269",
                "ice_servers": [
                    {
                        "urls": "stun:global.stun.twilio.com:3478"
                    },
                    {
                        "username": "dc2d2894d5a9023620c467b0e71cfa6a35457e6679785ed6ae9856fe5bdfa269",
                        "credential": "tE2DajzSJwnsSbc123",
                        "urls": "turn:global.turn.twilio.com:3478?transport=udp"
                    },
                    {
                        "username": "dc2d2894d5a9023620c467b0e71cfa6a35457e6679785ed6ae9856fe5bdfa269",
                        "credential": "tE2DajzSJwnsSbc123",
                        "urls": "turn:global.turn.twilio.com:3478?transport=tcp"
                    },
                    {
                        "username": "dc2d2894d5a9023620c467b0e71cfa6a35457e6679785ed6ae9856fe5bdfa269",
                        "credential": "tE2DajzSJwnsSbc123",
                        "urls": "turn:global.turn.twilio.com:443?transport=tcp"
                    }
                ],
                "date_updated": "Fri, 01 May 2020 01:42:57 +0000",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "ttl": "86400",
                "date_created": "Fri, 01 May 2020 01:42:57 +0000",
                "password": "tE2DajzSJwnsSbc123"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .tokens.create()

        self.assertIsNotNone(actual)
