# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base import serialize
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class TollfreeVerificationTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.tollfree_verifications("HHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Tollfree/Verifications/HHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "customer_profile_sid": "BU3344409f7e067e279523808d267e2d85",
                "trust_product_sid": "BU3344409f7e067e279523808d267e2d88",
                "regulated_item_sid": "RA3344409f7e067e279523808d267e2d89",
                "date_created": "2021-01-27T14:18:35Z",
                "date_updated": "2021-01-27T14:18:36Z",
                "business_name": "Agent",
                "business_street_address": "927 Terrace St",
                "business_street_address2": "Unit 4",
                "business_city": "Tempe",
                "business_state_province_region": "AZ",
                "business_postal_code": "85281",
                "business_country": "USA",
                "business_website": "www.ghost.com",
                "business_contact_first_name": "Vikram",
                "business_contact_last_name": "Amar",
                "business_contact_email": "vikram@gmail.com",
                "business_contact_phone": "+16504988765",
                "notification_email": "vikram@gmail.com",
                "use_case_categories": [
                    "2FA",
                    "MARKETING"
                ],
                "use_case_summary": "test",
                "production_message_sample": "test1",
                "opt_in_image_urls": [
                    "https://zipwhiptestbusiness.com/images/image1.jpg",
                    "https://zipwhiptestbusiness.com/images/image2.jpg"
                ],
                "opt_in_type": "VERBAL",
                "message_volume": "1,000",
                "additional_information": "info",
                "tollfree_phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "TWILIO_APPROVED",
                "url": "https://messaging.twilio.com/v1/Tollfree/Verifications/HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "resource_links": {
                    "customer_profile": "https://trusthub.twilio.com/v1/CustomerProfiles/BU3344409f7e067e279523808d267e2d85",
                    "trust_product": "https://trusthub.twilio.com/v1/TrustProducts/BU3344409f7e067e279523808d267e2d88",
                    "channel_endpoint_assignment": "https://trusthub.twilio.com/v1/TrustProducts/BU3344409f7e067e279523808d267e2d88/ChannelEndpointAssignments/RA3344409f7e067e279523808d267e2d89"
                }
            }
            '''
        ))

        actual = self.client.messaging.v1.tollfree_verifications("HHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.tollfree_verifications.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Tollfree/Verifications',
        ))

    def test_read_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://messaging.twilio.com/v1/Tollfree/Verifications?Status=TWILIO_APPROVED&TollfreePhoneNumberSid=PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0",
                    "previous_page_url": null,
                    "next_page_url": null,
                    "key": "verifications",
                    "url": "https://messaging.twilio.com/v1/Tollfree/Verifications?Status=TWILIO_APPROVED&TollfreePhoneNumberSid=PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0"
                },
                "verifications": [
                    {
                        "sid": "HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "customer_profile_sid": "BU3344409f7e067e279523808d267e2d85",
                        "trust_product_sid": "BU3344409f7e067e279523808d267e2d88",
                        "regulated_item_sid": "RA3344409f7e067e279523808d267e2d89",
                        "date_created": "2021-01-27T14:18:35Z",
                        "date_updated": "2021-01-27T14:18:36Z",
                        "business_name": "Agent",
                        "business_street_address": "927 Terrace St",
                        "business_street_address2": "Unit 4",
                        "business_city": "Tempe",
                        "business_state_province_region": "AZ",
                        "business_postal_code": "85281",
                        "business_country": "USA",
                        "business_website": "www.ghost.com",
                        "business_contact_first_name": "Vikram",
                        "business_contact_last_name": "Amar",
                        "business_contact_email": "vikram@gmail.com",
                        "business_contact_phone": "+16504988765",
                        "notification_email": "vikram@gmail.com",
                        "use_case_categories": [
                            "2FA",
                            "MARKETING"
                        ],
                        "use_case_summary": "test",
                        "production_message_sample": "test1",
                        "opt_in_image_urls": [
                            "https://zipwhiptestbusiness.com/images/image1.jpg",
                            "https://zipwhiptestbusiness.com/images/image2.jpg"
                        ],
                        "opt_in_type": "VERBAL",
                        "message_volume": "1,000",
                        "additional_information": "info",
                        "tollfree_phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "TWILIO_APPROVED",
                        "url": "https://messaging.twilio.com/v1/Tollfree/Verifications/HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "resource_links": {
                            "customer_profile": "https://trusthub.twilio.com/v1/CustomerProfiles/BU3344409f7e067e279523808d267e2d85",
                            "trust_product": "https://trusthub.twilio.com/v1/TrustProducts/BU3344409f7e067e279523808d267e2d88",
                            "channel_endpoint_assignment": "https://trusthub.twilio.com/v1/TrustProducts/BU3344409f7e067e279523808d267e2d88/ChannelEndpointAssignments/RA3344409f7e067e279523808d267e2d89"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.messaging.v1.tollfree_verifications.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.tollfree_verifications.create(business_name="business_name", business_website="business_website", notification_email="notification_email", use_case_categories=['use_case_categories'], use_case_summary="use_case_summary", production_message_sample="production_message_sample", opt_in_image_urls=['opt_in_image_urls'], opt_in_type="VERBAL", message_volume="message_volume", tollfree_phone_number_sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        values = {
            'BusinessName': "business_name",
            'BusinessWebsite': "business_website",
            'NotificationEmail': "notification_email",
            'UseCaseCategories': serialize.map(['use_case_categories'], lambda e: e),
            'UseCaseSummary': "use_case_summary",
            'ProductionMessageSample': "production_message_sample",
            'OptInImageUrls': serialize.map(['opt_in_image_urls'], lambda e: e),
            'OptInType': "VERBAL",
            'MessageVolume': "message_volume",
            'TollfreePhoneNumberSid': "PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://messaging.twilio.com/v1/Tollfree/Verifications',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "regulated_item_sid": null,
                "customer_profile_sid": "BU3344409f7e067e279523808d267e2d85",
                "trust_product_sid": null,
                "status": "PENDING_REVIEW",
                "date_created": "2021-01-27T14:18:35Z",
                "date_updated": "2021-01-27T14:18:36Z",
                "business_name": "Agent",
                "business_street_address": "927 Terrace St",
                "business_street_address2": "Unit 4",
                "business_city": "Tempe",
                "business_state_province_region": "AZ",
                "business_postal_code": "85281",
                "business_country": "USA",
                "business_website": "www.ghost.com",
                "business_contact_first_name": "Vikram",
                "business_contact_last_name": "Amar",
                "business_contact_email": "vikram@gmail.com",
                "business_contact_phone": "+16504988765",
                "notification_email": "vikram@gmail.com",
                "use_case_categories": [
                    "2FA",
                    "MARKETING"
                ],
                "use_case_summary": "test",
                "production_message_sample": "test1",
                "opt_in_image_urls": [
                    "https://zipwhiptestbusiness.com/images/image1.jpg",
                    "https://zipwhiptestbusiness.com/images/image2.jpg"
                ],
                "opt_in_type": "VERBAL",
                "message_volume": "1,000",
                "additional_information": "info",
                "tollfree_phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "resource_links": {},
                "url": "https://messaging.twilio.com/v1/Tollfree/Verifications/HHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.messaging.v1.tollfree_verifications.create(business_name="business_name", business_website="business_website", notification_email="notification_email", use_case_categories=['use_case_categories'], use_case_summary="use_case_summary", production_message_sample="production_message_sample", opt_in_image_urls=['opt_in_image_urls'], opt_in_type="VERBAL", message_volume="message_volume", tollfree_phone_number_sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        self.assertIsNotNone(actual)
