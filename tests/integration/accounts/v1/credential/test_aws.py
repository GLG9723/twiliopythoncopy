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


class AwsTestCase(IntegrationTestCase):
    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.accounts.v1.credentials.aws.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://accounts.twilio.com/v1/Credentials/AWS",
            )
        )

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "credentials": [],
                "meta": {
                    "first_page_url": "https://accounts.twilio.com/v1/Credentials/AWS?PageSize=50&Page=0",
                    "key": "credentials",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://accounts.twilio.com/v1/Credentials/AWS?PageSize=50&Page=0"
                }
            }
            """,
            )
        )

        actual = self.client.accounts.v1.credentials.aws.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "credentials": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-31T04:00:00Z",
                        "date_updated": "2015-07-31T04:00:00Z",
                        "friendly_name": "friendly_name",
                        "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://accounts.twilio.com/v1/Credentials/AWS/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://accounts.twilio.com/v1/Credentials/AWS?PageSize=50&Page=0",
                    "key": "credentials",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://accounts.twilio.com/v1/Credentials/AWS?PageSize=50&Page=0"
                }
            }
            """,
            )
        )

        actual = self.client.accounts.v1.credentials.aws.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.accounts.v1.credentials.aws.create(
                credentials="AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
            )

        values = {
            "Credentials": "AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        }

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://accounts.twilio.com/v1/Credentials/AWS",
                data=values,
            )
        )

    def test_create_response(self):
        self.holodeck.mock(
            Response(
                201,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-31T04:00:00Z",
                "date_updated": "2015-07-31T04:00:00Z",
                "friendly_name": "friendly_name",
                "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://accounts.twilio.com/v1/Credentials/AWS/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = self.client.accounts.v1.credentials.aws.create(
            credentials="AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        )

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.accounts.v1.credentials.aws(
                "CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://accounts.twilio.com/v1/Credentials/AWS/CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-31T04:00:00Z",
                "date_updated": "2015-07-31T04:00:00Z",
                "friendly_name": "friendly_name",
                "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://accounts.twilio.com/v1/Credentials/AWS/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = self.client.accounts.v1.credentials.aws(
            "CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.accounts.v1.credentials.aws(
                "CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).update()

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://accounts.twilio.com/v1/Credentials/AWS/CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_update_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-31T04:00:00Z",
                "date_updated": "2015-07-31T04:00:00Z",
                "friendly_name": "friendly_name",
                "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://accounts.twilio.com/v1/Credentials/AWS/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = self.client.accounts.v1.credentials.aws(
            "CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.accounts.v1.credentials.aws(
                "CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).delete()

        self.holodeck.assert_has_request(
            Request(
                "delete",
                "https://accounts.twilio.com/v1/Credentials/AWS/CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_delete_response(self):
        self.holodeck.mock(
            Response(
                204,
                None,
            )
        )

        actual = self.client.accounts.v1.credentials.aws(
            "CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).delete()

        self.assertTrue(actual)
