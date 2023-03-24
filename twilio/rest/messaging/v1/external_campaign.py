r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ExternalCampaignInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the ExternalCampaignInstance
        """
        super().__init__(version)

        self._sid: Optional[str] = payload.get("sid")
        self._account_sid: Optional[str] = payload.get("account_sid")
        self._campaign_id: Optional[str] = payload.get("campaign_id")
        self._messaging_service_sid: Optional[str] = payload.get(
            "messaging_service_sid"
        )
        self._date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )

        self._solution = {}

    @property
    def sid(self) -> Optional[str]:
        """
        :returns: The unique string that identifies a US A2P Compliance resource `QE2c6890da8086d771620e9b13fadeba0b`.
        """
        return self._sid

    @property
    def account_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Campaign belongs to.
        """
        return self._account_sid

    @property
    def campaign_id(self) -> Optional[str]:
        """
        :returns: ID of the preregistered campaign.
        """
        return self._campaign_id

    @property
    def messaging_service_sid(self) -> Optional[str]:
        """
        :returns: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.
        """
        return self._messaging_service_sid

    @property
    def date_created(self) -> Optional[datetime]:
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        """
        return self._date_created

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.ExternalCampaignInstance {}>".format(context)


class ExternalCampaignList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ExternalCampaignList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Services/PreregisteredUsa2p"

    def create(self, campaign_id, messaging_service_sid) -> ExternalCampaignInstance:
        """
        Create the ExternalCampaignInstance

        :param str campaign_id: ID of the preregistered campaign.
        :param str messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.

        :returns: The created ExternalCampaignInstance
        """
        data = values.of(
            {
                "CampaignId": campaign_id,
                "MessagingServiceSid": messaging_service_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ExternalCampaignInstance(self._version, payload)

    async def create_async(
        self, campaign_id, messaging_service_sid
    ) -> ExternalCampaignInstance:
        """
        Asynchronously create the ExternalCampaignInstance

        :param str campaign_id: ID of the preregistered campaign.
        :param str messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.

        :returns: The created ExternalCampaignInstance
        """
        data = values.of(
            {
                "CampaignId": campaign_id,
                "MessagingServiceSid": messaging_service_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ExternalCampaignInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.ExternalCampaignList>"
