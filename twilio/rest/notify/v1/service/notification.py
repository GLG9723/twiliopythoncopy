r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Notify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Dict, List, Optional
from twilio.base import deserialize, serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class NotificationInstance(InstanceResource):
    class Priority(object):
        HIGH = "high"
        LOW = "low"

    def __init__(self, version, payload, service_sid: str):
        """
        Initialize the NotificationInstance
        """
        super().__init__(version)

        self._sid: Optional[str] = payload.get("sid")
        self._account_sid: Optional[str] = payload.get("account_sid")
        self._service_sid: Optional[str] = payload.get("service_sid")
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self._identities: Optional[List[str]] = payload.get("identities")
        self._tags: Optional[List[str]] = payload.get("tags")
        self._segments: Optional[List[str]] = payload.get("segments")
        self._priority: Optional["NotificationInstance.Priority"] = payload.get(
            "priority"
        )
        self._ttl: Optional[int] = deserialize.integer(payload.get("ttl"))
        self._title: Optional[str] = payload.get("title")
        self._body: Optional[str] = payload.get("body")
        self._sound: Optional[str] = payload.get("sound")
        self._action: Optional[str] = payload.get("action")
        self._data: Optional[Dict[str, object]] = payload.get("data")
        self._apn: Optional[Dict[str, object]] = payload.get("apn")
        self._gcm: Optional[Dict[str, object]] = payload.get("gcm")
        self._fcm: Optional[Dict[str, object]] = payload.get("fcm")
        self._sms: Optional[Dict[str, object]] = payload.get("sms")
        self._facebook_messenger: Optional[Dict[str, object]] = payload.get(
            "facebook_messenger"
        )
        self._alexa: Optional[Dict[str, object]] = payload.get("alexa")

        self._solution = {
            "service_sid": service_sid,
        }

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that we created to identify the Notification resource.
        """
        return self._sid

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resource.
        """
        return self._account_sid

    @property
    def service_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) the resource is associated with.
        """
        return self._service_sid

    @property
    def date_created(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        """
        return self._date_created

    @property
    def identities(self) -> Optional[List[str]]:
        """
        :returns: The list of `identity` values of the Users to notify. We will attempt to deliver notifications only to Bindings with an identity in this list.
        """
        return self._identities

    @property
    def tags(self) -> Optional[List[str]]:
        """
        :returns: The tags that select the Bindings to notify. Notifications will be attempted only to Bindings that have all of the tags listed in this property.
        """
        return self._tags

    @property
    def segments(self) -> Optional[List[str]]:
        """
        :returns: The list of Segments to notify. The [Segment](https://www.twilio.com/docs/notify/api/segment-resource) resource is deprecated. Use the `tags` property, instead.
        """
        return self._segments

    @property
    def priority(self) -> Optional["NotificationInstance.Priority"]:
        return self._priority

    @property
    def ttl(self) -> Optional[int]:
        """
        :returns: How long, in seconds, the notification is valid. Can be an integer between 0 and 2,419,200, which is 4 weeks, the default and the maximum supported time to live (TTL). Delivery should be attempted if the device is offline until the TTL elapses. Zero means that the notification delivery is attempted immediately, only once, and is not stored for future delivery. SMS does not support this property.
        """
        return self._ttl

    @property
    def title(self) -> Optional[str]:
        """
        :returns: The notification title. For FCM and GCM, this translates to the `data.twi_title` value. For APNS, this translates to the `aps.alert.title` value. SMS does not support this property. This field is not visible on iOS phones and tablets but appears on Apple Watch and Android devices.
        """
        return self._title

    @property
    def body(self) -> Optional[str]:
        """
        :returns: The notification text. For FCM and GCM, translates to `data.twi_body`. For APNS, translates to `aps.alert.body`. For SMS, translates to `body`. SMS requires either this `body` value, or `media_urls` attribute defined in the `sms` parameter of the notification.
        """
        return self._body

    @property
    def sound(self) -> Optional[str]:
        """
        :returns: The name of the sound to be played for the notification. For FCM and GCM, this Translates to `data.twi_sound`.  For APNS, this translates to `aps.sound`.  SMS does not support this property.
        """
        return self._sound

    @property
    def action(self) -> Optional[str]:
        """
        :returns: The actions to display for the notification. For APNS, translates to the `aps.category` value. For GCM, translates to the `data.twi_action` value. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        """
        return self._action

    @property
    def data(self) -> Optional[Dict[str, object]]:
        """
        :returns: The custom key-value pairs of the notification's payload. For FCM and GCM, this value translates to `data` in the FCM and GCM payloads. FCM and GCM [reserve certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref) that cannot be used in those channels. For APNS, attributes of `data` are inserted into the APNS payload as custom properties outside of the `aps` dictionary. In all channels, we reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed and are rejected as 400 Bad request with no delivery attempted. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        """
        return self._data

    @property
    def apn(self) -> Optional[Dict[str, object]]:
        """
        :returns: The APNS-specific payload that overrides corresponding attributes in the generic payload for APNS Bindings. This property maps to the APNS `Payload` item, therefore the `aps` key must be used to change standard attributes. Adds custom key-value pairs to the root of the dictionary. See the [APNS documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) for more details. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed.
        """
        return self._apn

    @property
    def gcm(self) -> Optional[Dict[str, object]]:
        """
        :returns: The GCM-specific payload that overrides corresponding attributes in the generic payload for GCM Bindings.  This property maps to the root JSON dictionary. Target parameters `to`, `registration_ids`, and `notification_key` are not allowed. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed.
        """
        return self._gcm

    @property
    def fcm(self) -> Optional[Dict[str, object]]:
        """
        :returns: The FCM-specific payload that overrides corresponding attributes in the generic payload for FCM Bindings. This property maps to the root JSON dictionary. See the [FCM documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#downstream) for more details. Target parameters `to`, `registration_ids`, `condition`, and `notification_key` are not allowed in this parameter. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed. FCM also [reserves certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref), which cannot be used in that channel.
        """
        return self._fcm

    @property
    def sms(self) -> Optional[Dict[str, object]]:
        """
        :returns: The SMS-specific payload that overrides corresponding attributes in the generic payload for SMS Bindings.  Each attribute in this value maps to the corresponding `form` parameter of the Twilio [Message](https://www.twilio.com/docs/sms/api/message-resource) resource.  These parameters of the Message resource are supported in snake case format: `body`, `media_urls`, `status_callback`, and `max_price`.  The `status_callback` parameter overrides the corresponding parameter in the messaging service, if configured. The `media_urls` property expects a JSON array.
        """
        return self._sms

    @property
    def facebook_messenger(self) -> Optional[Dict[str, object]]:
        """
        :returns: Deprecated.
        """
        return self._facebook_messenger

    @property
    def alexa(self) -> Optional[Dict[str, object]]:
        """
        :returns: Deprecated.
        """
        return self._alexa

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Notify.V1.NotificationInstance {}>".format(context)


class NotificationList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the NotificationList

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to create the resource under.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Notifications".format(**self._solution)

    def create(
        self,
        body=values.unset,
        priority=values.unset,
        ttl=values.unset,
        title=values.unset,
        sound=values.unset,
        action=values.unset,
        data=values.unset,
        apn=values.unset,
        gcm=values.unset,
        sms=values.unset,
        facebook_messenger=values.unset,
        fcm=values.unset,
        segment=values.unset,
        alexa=values.unset,
        to_binding=values.unset,
        delivery_callback_url=values.unset,
        identity=values.unset,
        tag=values.unset,
    ) -> NotificationInstance:
        """
        Create the NotificationInstance

        :param str body: The notification text. For FCM and GCM, translates to `data.twi_body`. For APNS, translates to `aps.alert.body`. For SMS, translates to `body`. SMS requires either this `body` value, or `media_urls` attribute defined in the `sms` parameter of the notification.
        :param &quot;NotificationInstance.Priority&quot; priority:
        :param int ttl: How long, in seconds, the notification is valid. Can be an integer between 0 and 2,419,200, which is 4 weeks, the default and the maximum supported time to live (TTL). Delivery should be attempted if the device is offline until the TTL elapses. Zero means that the notification delivery is attempted immediately, only once, and is not stored for future delivery. SMS does not support this property.
        :param str title: The notification title. For FCM and GCM, this translates to the `data.twi_title` value. For APNS, this translates to the `aps.alert.title` value. SMS does not support this property. This field is not visible on iOS phones and tablets but appears on Apple Watch and Android devices.
        :param str sound: The name of the sound to be played for the notification. For FCM and GCM, this Translates to `data.twi_sound`.  For APNS, this translates to `aps.sound`.  SMS does not support this property.
        :param str action: The actions to display for the notification. For APNS, translates to the `aps.category` value. For GCM, translates to the `data.twi_action` value. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        :param object data: The custom key-value pairs of the notification's payload. For FCM and GCM, this value translates to `data` in the FCM and GCM payloads. FCM and GCM [reserve certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref) that cannot be used in those channels. For APNS, attributes of `data` are inserted into the APNS payload as custom properties outside of the `aps` dictionary. In all channels, we reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed and are rejected as 400 Bad request with no delivery attempted. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        :param object apn: The APNS-specific payload that overrides corresponding attributes in the generic payload for APNS Bindings. This property maps to the APNS `Payload` item, therefore the `aps` key must be used to change standard attributes. Adds custom key-value pairs to the root of the dictionary. See the [APNS documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) for more details. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed.
        :param object gcm: The GCM-specific payload that overrides corresponding attributes in the generic payload for GCM Bindings.  This property maps to the root JSON dictionary. See the [GCM documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref) for more details. Target parameters `to`, `registration_ids`, and `notification_key` are not allowed. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed. GCM also [reserves certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref).
        :param object sms: The SMS-specific payload that overrides corresponding attributes in the generic payload for SMS Bindings.  Each attribute in this value maps to the corresponding `form` parameter of the Twilio [Message](https://www.twilio.com/docs/sms/send-messages) resource.  These parameters of the Message resource are supported in snake case format: `body`, `media_urls`, `status_callback`, and `max_price`.  The `status_callback` parameter overrides the corresponding parameter in the messaging service, if configured. The `media_urls` property expects a JSON array.
        :param object facebook_messenger: Deprecated.
        :param object fcm: The FCM-specific payload that overrides corresponding attributes in the generic payload for FCM Bindings. This property maps to the root JSON dictionary. See the [FCM documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#downstream) for more details. Target parameters `to`, `registration_ids`, `condition`, and `notification_key` are not allowed in this parameter. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed. FCM also [reserves certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref), which cannot be used in that channel.
        :param List[str] segment: The Segment resource is deprecated. Use the `tag` parameter, instead.
        :param object alexa: Deprecated.
        :param List[str] to_binding: The destination address specified as a JSON string.  Multiple `to_binding` parameters can be included but the total size of the request entity should not exceed 1MB. This is typically sufficient for 10,000 phone numbers.
        :param str delivery_callback_url: URL to send webhooks.
        :param List[str] identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Delivery will be attempted only to Bindings with an Identity in this list. No more than 20 items are allowed in this list.
        :param List[str] tag: A tag that selects the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 5 tags. The implicit tag `all` is available to notify all Bindings in a Service instance. Similarly, the implicit tags `apn`, `fcm`, `gcm`, `sms` and `facebook-messenger` are available to notify all Bindings in a specific channel.

        :returns: The created NotificationInstance
        """
        data = values.of(
            {
                "Body": body,
                "Priority": priority,
                "Ttl": ttl,
                "Title": title,
                "Sound": sound,
                "Action": action,
                "Data": serialize.object(data),
                "Apn": serialize.object(apn),
                "Gcm": serialize.object(gcm),
                "Sms": serialize.object(sms),
                "FacebookMessenger": serialize.object(facebook_messenger),
                "Fcm": serialize.object(fcm),
                "Segment": serialize.map(segment, lambda e: e),
                "Alexa": serialize.object(alexa),
                "ToBinding": serialize.map(to_binding, lambda e: e),
                "DeliveryCallbackUrl": delivery_callback_url,
                "Identity": serialize.map(identity, lambda e: e),
                "Tag": serialize.map(tag, lambda e: e),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return NotificationInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        body=values.unset,
        priority=values.unset,
        ttl=values.unset,
        title=values.unset,
        sound=values.unset,
        action=values.unset,
        data=values.unset,
        apn=values.unset,
        gcm=values.unset,
        sms=values.unset,
        facebook_messenger=values.unset,
        fcm=values.unset,
        segment=values.unset,
        alexa=values.unset,
        to_binding=values.unset,
        delivery_callback_url=values.unset,
        identity=values.unset,
        tag=values.unset,
    ) -> NotificationInstance:
        """
        Asynchronously create the NotificationInstance

        :param str body: The notification text. For FCM and GCM, translates to `data.twi_body`. For APNS, translates to `aps.alert.body`. For SMS, translates to `body`. SMS requires either this `body` value, or `media_urls` attribute defined in the `sms` parameter of the notification.
        :param &quot;NotificationInstance.Priority&quot; priority:
        :param int ttl: How long, in seconds, the notification is valid. Can be an integer between 0 and 2,419,200, which is 4 weeks, the default and the maximum supported time to live (TTL). Delivery should be attempted if the device is offline until the TTL elapses. Zero means that the notification delivery is attempted immediately, only once, and is not stored for future delivery. SMS does not support this property.
        :param str title: The notification title. For FCM and GCM, this translates to the `data.twi_title` value. For APNS, this translates to the `aps.alert.title` value. SMS does not support this property. This field is not visible on iOS phones and tablets but appears on Apple Watch and Android devices.
        :param str sound: The name of the sound to be played for the notification. For FCM and GCM, this Translates to `data.twi_sound`.  For APNS, this translates to `aps.sound`.  SMS does not support this property.
        :param str action: The actions to display for the notification. For APNS, translates to the `aps.category` value. For GCM, translates to the `data.twi_action` value. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        :param object data: The custom key-value pairs of the notification's payload. For FCM and GCM, this value translates to `data` in the FCM and GCM payloads. FCM and GCM [reserve certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref) that cannot be used in those channels. For APNS, attributes of `data` are inserted into the APNS payload as custom properties outside of the `aps` dictionary. In all channels, we reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed and are rejected as 400 Bad request with no delivery attempted. For SMS, this parameter is not supported and is omitted from deliveries to those channels.
        :param object apn: The APNS-specific payload that overrides corresponding attributes in the generic payload for APNS Bindings. This property maps to the APNS `Payload` item, therefore the `aps` key must be used to change standard attributes. Adds custom key-value pairs to the root of the dictionary. See the [APNS documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html) for more details. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed.
        :param object gcm: The GCM-specific payload that overrides corresponding attributes in the generic payload for GCM Bindings.  This property maps to the root JSON dictionary. See the [GCM documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref) for more details. Target parameters `to`, `registration_ids`, and `notification_key` are not allowed. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed. GCM also [reserves certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref).
        :param object sms: The SMS-specific payload that overrides corresponding attributes in the generic payload for SMS Bindings.  Each attribute in this value maps to the corresponding `form` parameter of the Twilio [Message](https://www.twilio.com/docs/sms/send-messages) resource.  These parameters of the Message resource are supported in snake case format: `body`, `media_urls`, `status_callback`, and `max_price`.  The `status_callback` parameter overrides the corresponding parameter in the messaging service, if configured. The `media_urls` property expects a JSON array.
        :param object facebook_messenger: Deprecated.
        :param object fcm: The FCM-specific payload that overrides corresponding attributes in the generic payload for FCM Bindings. This property maps to the root JSON dictionary. See the [FCM documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#downstream) for more details. Target parameters `to`, `registration_ids`, `condition`, and `notification_key` are not allowed in this parameter. We reserve keys that start with `twi_` for future use. Custom keys that start with `twi_` are not allowed. FCM also [reserves certain keys](https://firebase.google.com/docs/cloud-messaging/http-server-ref), which cannot be used in that channel.
        :param List[str] segment: The Segment resource is deprecated. Use the `tag` parameter, instead.
        :param object alexa: Deprecated.
        :param List[str] to_binding: The destination address specified as a JSON string.  Multiple `to_binding` parameters can be included but the total size of the request entity should not exceed 1MB. This is typically sufficient for 10,000 phone numbers.
        :param str delivery_callback_url: URL to send webhooks.
        :param List[str] identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Delivery will be attempted only to Bindings with an Identity in this list. No more than 20 items are allowed in this list.
        :param List[str] tag: A tag that selects the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 5 tags. The implicit tag `all` is available to notify all Bindings in a Service instance. Similarly, the implicit tags `apn`, `fcm`, `gcm`, `sms` and `facebook-messenger` are available to notify all Bindings in a specific channel.

        :returns: The created NotificationInstance
        """
        data = values.of(
            {
                "Body": body,
                "Priority": priority,
                "Ttl": ttl,
                "Title": title,
                "Sound": sound,
                "Action": action,
                "Data": serialize.object(data),
                "Apn": serialize.object(apn),
                "Gcm": serialize.object(gcm),
                "Sms": serialize.object(sms),
                "FacebookMessenger": serialize.object(facebook_messenger),
                "Fcm": serialize.object(fcm),
                "Segment": serialize.map(segment, lambda e: e),
                "Alexa": serialize.object(alexa),
                "ToBinding": serialize.map(to_binding, lambda e: e),
                "DeliveryCallbackUrl": delivery_callback_url,
                "Identity": serialize.map(identity, lambda e: e),
                "Tag": serialize.map(tag, lambda e: e),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return NotificationInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Notify.V1.NotificationList>"
