r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class NotificationInstance(InstanceResource):

    """
    :ivar sid: A 34 character string that uniquely identifies this Notification.
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar service_sid: The unique SID identifier of the Service.
    :ivar entity_sid: The unique SID identifier of the Entity.
    :ivar identity: Customer unique identity for the Entity owner of the Challenge. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
    :ivar challenge_sid: The unique SID identifier of the Challenge.
    :ivar priority: The priority of the notification. For `push` Challenges it's always `high` which sends the notification immediately, and can wake up a sleeping device.
    :ivar ttl: How long, in seconds, the notification is valid. Max: 5 minutes
    :ivar date_created: The date that this Notification was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        identity: str,
        challenge_sid: str,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.entity_sid: Optional[str] = payload.get("entity_sid")
        self.identity: Optional[str] = payload.get("identity")
        self.challenge_sid: Optional[str] = payload.get("challenge_sid")
        self.priority: Optional[str] = payload.get("priority")
        self.ttl: Optional[int] = deserialize.integer(payload.get("ttl"))
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )

        self._solution = {
            "service_sid": service_sid,
            "identity": identity,
            "challenge_sid": challenge_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.NotificationInstance {}>".format(context)


class NotificationList(ListResource):
    def __init__(
        self, version: Version, service_sid: str, identity: str, challenge_sid: str
    ):
        """
        Initialize the NotificationList

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: Customer unique identity for the Entity owner of the Challenge. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        :param challenge_sid: The unique SID identifier of the Challenge.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "identity": identity,
            "challenge_sid": challenge_sid,
        }
        self._uri = "/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications".format(
            **self._solution
        )

    def create(self, ttl=values.unset) -> NotificationInstance:
        """
        Create the NotificationInstance

        :param int ttl: How long, in seconds, the notification is valid. Can be an integer between 0 and 300. Default is 300. Delivery is attempted until the TTL elapses, even if the device is offline. 0 means that the notification delivery is attempted immediately, only once, and is not stored for future delivery.

        :returns: The created NotificationInstance
        """
        data = values.of(
            {
                "Ttl": ttl,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return NotificationInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
            challenge_sid=self._solution["challenge_sid"],
        )

    async def create_async(self, ttl=values.unset) -> NotificationInstance:
        """
        Asynchronously create the NotificationInstance

        :param int ttl: How long, in seconds, the notification is valid. Can be an integer between 0 and 300. Default is 300. Delivery is attempted until the TTL elapses, even if the device is offline. 0 means that the notification delivery is attempted immediately, only once, and is not stored for future delivery.

        :returns: The created NotificationInstance
        """
        data = values.of(
            {
                "Ttl": ttl,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return NotificationInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
            challenge_sid=self._solution["challenge_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.NotificationList>"
