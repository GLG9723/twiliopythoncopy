r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Bulk Messaging and Broadcast
    Bulk Sending is a public Twilio REST API for 1:Many Message creation up to 100 recipients. Broadcast is a public Twilio REST API for 1:Many Message creation up to 10,000 recipients via file upload.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional
from twilio.base import deserialize

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class MessageInstance(InstanceResource):
    """
    :ivar total_message_count: The number of Messages processed in the request, equal to the sum of success_count and error_count.
    :ivar success_count: The number of Messages successfully created.
    :ivar error_count: The number of Messages unsuccessfully processed in the request.
    :ivar message_receipts:
    :ivar failed_message_receipts:
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.total_message_count: Optional[int] = deserialize.integer(
            payload.get("total_message_count")
        )
        self.success_count: Optional[int] = deserialize.integer(
            payload.get("success_count")
        )
        self.error_count: Optional[int] = deserialize.integer(
            payload.get("error_count")
        )
        self.message_receipts: Optional[List[str]] = payload.get("message_receipts")
        self.failed_message_receipts: Optional[List[str]] = payload.get(
            "failed_message_receipts"
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.PreviewMessaging.V1.MessageInstance>"


class MessageList(ListResource):

    class CreateMessagesRequest:
        """
        :ivar messages:
        :ivar from_: A Twilio phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, an [alphanumeric sender ID](https://www.twilio.com/docs/sms/send-messages#use-an-alphanumeric-sender-id), or a [Channel Endpoint address](https://www.twilio.com/docs/sms/channels#channel-addresses) that is enabled for the type of message you want to send. Phone numbers or [short codes](https://www.twilio.com/docs/sms/api/short-code) purchased from Twilio also work here. You cannot, for example, spoof messages from a private cell phone number. If you are using `messaging_service_sid`, this parameter must be empty.
        :ivar messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/sms/services#send-a-message-with-copilot) you want to associate with the Message. Set this parameter to use the [Messaging Service Settings and Copilot Features](https://www.twilio.com/console/sms/services) you have configured and leave the `from` parameter empty. When only this parameter is set, Twilio will use your enabled Copilot Features to select the `from` phone number for delivery.
        :ivar body: The text of the message you want to send. Can be up to 1,600 characters in length.
        :ivar content_sid: The SID of the preconfigured [Content Template](https://www.twilio.com/docs/content-api/create-and-send-your-first-content-api-template#create-a-template) you want to associate with the Message. Must be used in conjuction with a preconfigured [Messaging Service Settings and Copilot Features](https://www.twilio.com/console/sms/services) When this parameter is set, Twilio will use your configured content template and the provided `ContentVariables`. This Twilio product is currently in Private Beta.
        :ivar media_url: The URL of the media to send with the message. The media can be of type `gif`, `png`, and `jpeg` and will be formatted correctly on the recipient's device. The media size limit is 5MB for supported file types (JPEG, PNG, GIF) and 500KB for [other types](https://www.twilio.com/docs/sms/accepted-mime-types) of accepted media. To send more than one image in the message body, provide multiple `media_url` parameters in the POST request. You can include up to 10 `media_url` parameters per message. You can send images in an SMS message in only the US and Canada.
        :ivar status_callback: The URL we should call using the \"status_callback_method\" to send status information to your application. If specified, we POST these message status changes to the URL - queued, failed, sent, delivered, or undelivered. Twilio will POST its [standard request parameters](https://www.twilio.com/docs/messaging/twiml#request-parameters) as well as some additional parameters including \"MessageSid\", \"MessageStatus\", and \"ErrorCode\". If you include this parameter with the \"messaging_service_sid\", we use this URL instead of the Status Callback URL of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api). URLs must contain a valid hostname and underscores are not allowed.
        :ivar validity_period: How long in seconds the message can remain in our outgoing message queue. After this period elapses, the message fails and we call your status callback. Can be between 1 and the default value of 14,400 seconds. After a message has been accepted by a carrier, however, we cannot guarantee that the message will not be queued after this period. We recommend that this value be at least 5 seconds.
        :ivar send_at: The time at which Twilio will send the message. This parameter can be used to schedule a message to be sent at a particular time. Must be in ISO 8601 format.
        :ivar schedule_type: This parameter indicates your intent to schedule a message. Pass the value `fixed` to schedule a message at a fixed time. This parameter works in conjuction with the `SendAt` parameter.
        :ivar shorten_urls: Determines the usage of Click Tracking. Setting it to `true` will instruct Twilio to replace all links in the Message with a shortened version based on the associated Domain Sid and track clicks on them. If this parameter is not set on an API call, we will use the value set on the Messaging Service. If this parameter is not set and the value is not configured on the Messaging Service used this will default to `false`.
        :ivar send_as_mms: If set to True, Twilio will deliver the message as a single MMS message, regardless of the presence of media.
        :ivar max_price: The maximum total price in US dollars that you will pay for the message to be delivered. Can be a decimal value that has up to 4 decimal places. All messages are queued for delivery and the message cost is checked before the message is sent. If the cost exceeds max_price, the message will fail and a status of Failed is sent to the status callback. If MaxPrice is not set, the message cost is not checked.
        :ivar attempt: Total number of attempts made ( including this ) to send out the message regardless of the provider used
        :ivar smart_encoded: This parameter indicates whether to detect Unicode characters that have a similar GSM-7 character and replace them. Can be true or false.
        :ivar force_delivery: This parameter allows Twilio to send SMS traffic to carriers without checking/caring whether the destination number is a mobile or a landline.
        :ivar application_sid: The SID of the application that should receive message status. We POST a message_sid parameter and a message_status parameter with a value of sent or failed to the application's message_status_callback. If a status_callback parameter is also passed, it will be ignored and the application's message_status_callback parameter will be used.
        """

        def __init__(self, payload: Dict[str, Any]):

            self.messages: Optional[List[MessageList.MessagingV1Message]] = payload.get(
                "messages"
            )
            self.from_: Optional[str] = payload.get("from_")
            self.messaging_service_sid: Optional[str] = payload.get(
                "messaging_service_sid"
            )
            self.body: Optional[str] = payload.get("body")
            self.content_sid: Optional[str] = payload.get("content_sid")
            self.media_url: Optional[List[str]] = payload.get("media_url")
            self.status_callback: Optional[str] = payload.get("status_callback")
            self.validity_period: Optional[int] = payload.get("validity_period")
            self.send_at: Optional[str] = payload.get("send_at")
            self.schedule_type: Optional[str] = payload.get("schedule_type")
            self.shorten_urls: Optional[bool] = payload.get("shorten_urls")
            self.send_as_mms: Optional[bool] = payload.get("send_as_mms")
            self.max_price: Optional[float] = payload.get("max_price")
            self.attempt: Optional[int] = payload.get("attempt")
            self.smart_encoded: Optional[bool] = payload.get("smart_encoded")
            self.force_delivery: Optional[bool] = payload.get("force_delivery")
            self.application_sid: Optional[str] = payload.get("application_sid")

        def to_dict(self):
            return {
                "messages": [messages.to_dict() for messages in self.messages],
                "from": self.from_,
                "messaging_service_sid": self.messaging_service_sid,
                "body": self.body,
                "content_sid": self.content_sid,
                "media_url": self.media_url,
                "status_callback": self.status_callback,
                "validity_period": self.validity_period,
                "send_at": self.send_at,
                "schedule_type": self.schedule_type,
                "shorten_urls": self.shorten_urls,
                "send_as_mms": self.send_as_mms,
                "max_price": self.max_price,
                "attempt": self.attempt,
                "smart_encoded": self.smart_encoded,
                "force_delivery": self.force_delivery,
                "application_sid": self.application_sid,
            }

    class MessagingV1Message:
        """
        :ivar to: The destination phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format for SMS/MMS or [Channel user address](https://www.twilio.com/docs/sms/channels#channel-addresses) for other 3rd-party channels.
        :ivar body: The text of the message you want to send. Can be up to 1,600 characters in length. Overrides the request-level body and content template if provided.
        :ivar content_variables: Key-value pairs of variable names to substitution values. Refer to the [Twilio Content API Resources](https://www.twilio.com/docs/content-api/content-api-resources#send-a-message-with-preconfigured-content) for more details.
        """

        def __init__(self, payload: Dict[str, Any]):

            self.to: Optional[str] = payload.get("to")
            self.body: Optional[str] = payload.get("body")
            self.content_variables: Optional[dict[str, str]] = payload.get(
                "content_variables"
            )

        def to_dict(self):
            return {
                "to": self.to,
                "body": self.body,
                "content_variables": self.content_variables,
            }

    def __init__(self, version: Version):
        """
        Initialize the MessageList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Messages"

    def create(self, create_messages_request: CreateMessagesRequest) -> MessageInstance:
        """
        Create the MessageInstance

        :param create_messages_request:

        :returns: The created MessageInstance
        """
        data = create_messages_request.to_dict()

        headers = {"Content-Type": "application/json"}

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return MessageInstance(self._version, payload)

    async def create_async(
        self, create_messages_request: CreateMessagesRequest
    ) -> MessageInstance:
        """
        Asynchronously create the MessageInstance

        :param create_messages_request:

        :returns: The created MessageInstance
        """
        data = create_messages_request.to_dict()

        headers = {"Content-Type": "application/json"}

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return MessageInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.PreviewMessaging.V1.MessageList>"
