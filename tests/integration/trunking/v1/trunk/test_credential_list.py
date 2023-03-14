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


class CredentialListTestCase(IntegrationTestCase):
    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(
                "TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).credentials_lists("CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://trunking.twilio.com/v1/Trunks/TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/CredentialLists/CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_fetch_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2018-04-28T00:10:23Z",
                "date_updated": "2018-04-28T00:10:23Z",
                "friendly_name": "friendly_name",
                "sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = (
            self.client.trunking.v1.trunks("TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .credentials_lists("CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .fetch()
        )

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(
                "TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).credentials_lists("CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(
            Request(
                "delete",
                "https://trunking.twilio.com/v1/Trunks/TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/CredentialLists/CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            )
        )

    def test_delete_response(self):
        self.holodeck.mock(
            Response(
                204,
                None,
            )
        )

        actual = (
            self.client.trunking.v1.trunks("TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .credentials_lists("CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .delete()
        )

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(
                "TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).credentials_lists.create(
                credential_list_sid="CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            )

        values = {
            "CredentialListSid": "CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        }

        self.holodeck.assert_has_request(
            Request(
                "post",
                "https://trunking.twilio.com/v1/Trunks/TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/CredentialLists",
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
                "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2018-05-02T17:29:30Z",
                "date_updated": "2018-05-02T17:29:30Z",
                "friendly_name": "friendly_name",
                "sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            """,
            )
        )

        actual = self.client.trunking.v1.trunks(
            "TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).credentials_lists.create(
            credential_list_sid="CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        )

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ""))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(
                "TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            ).credentials_lists.list()

        self.holodeck.assert_has_request(
            Request(
                "get",
                "https://trunking.twilio.com/v1/Trunks/TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/CredentialLists",
            )
        )

    def test_read_full_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "credential_lists": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2018-04-27T22:02:11Z",
                        "date_updated": "2018-04-27T22:02:11Z",
                        "friendly_name": "friendly_name",
                        "sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "credential_lists"
                }
            }
            """,
            )
        )

        actual = self.client.trunking.v1.trunks(
            "TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).credentials_lists.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(
            Response(
                200,
                """
            {
                "credential_lists": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "credential_lists"
                }
            }
            """,
            )
        )

        actual = self.client.trunking.v1.trunks(
            "TKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ).credentials_lists.list()

        self.assertIsNotNone(actual)
