r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class SubscribeRulesList(ListResource):
    def __init__(self, version: Version, room_sid: str, participant_sid: str):
        """
        Initialize the SubscribeRulesList

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the Room resource where the subscribe rules to update apply.
        :param participant_sid: The SID of the Participant resource to update the Subscribe Rules.

        :returns: twilio.rest.video.v1.room.participant.subscribe_rules.SubscribeRulesList
        :rtype: twilio.rest.video.v1.room.participant.subscribe_rules.SubscribeRulesList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
            "participant_sid": participant_sid,
        }
        self._uri = (
            "/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules".format(
                **self._solution
            )
        )

    def fetch(self):
        """
        Asynchronously fetch the SubscribeRulesInstance

        :returns: The fetched SubscribeRulesInstance
        :rtype: twilio.rest.video.v1.room.participant.subscribe_rules.SubscribeRulesInstance
        """
        payload = self._version.fetch(method="GET", uri=self._uri)

        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    async def fetch_async(self):
        """
        Asynchronously fetch the SubscribeRulesInstance

        :returns: The fetched SubscribeRulesInstance
        :rtype: twilio.rest.video.v1.room.participant.subscribe_rules.SubscribeRulesInstance
        """
        payload = await self._version.fetch_async(method="GET", uri=self._uri)

        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    def update(self, rules=values.unset):
        """
        Update the SubscribeRulesInstance

        :param object rules: A JSON-encoded array of subscribe rules. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information.

        :returns: The created SubscribeRulesInstance
        :rtype: twilio.rest.video.v1.room.participant.subscribe_rules.SubscribeRulesInstance
        """
        data = values.of(
            {
                "Rules": serialize.object(rules),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    async def update_async(self, rules=values.unset):
        """
        Asynchronously update the SubscribeRulesInstance

        :param object rules: A JSON-encoded array of subscribe rules. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information.

        :returns: The created SubscribeRulesInstance
        :rtype: twilio.rest.video.v1.room.participant.subscribe_rules.SubscribeRulesInstance
        """
        data = values.of(
            {
                "Rules": serialize.object(rules),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SubscribeRulesInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Video.V1.SubscribeRulesList>"


class SubscribeRulesInstance(InstanceResource):
    def __init__(self, version, payload, room_sid: str, participant_sid: str):
        """
        Initialize the SubscribeRulesInstance

        :returns: twilio.rest.video.v1.room.participant.subscribe_rules.SubscribeRulesInstance
        :rtype: twilio.rest.video.v1.room.participant.subscribe_rules.SubscribeRulesInstance
        """
        super().__init__(version)

        self._properties = {
            "participant_sid": payload.get("participant_sid"),
            "room_sid": payload.get("room_sid"),
            "rules": payload.get("rules"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
        }

        self._context = None
        self._solution = {
            "room_sid": room_sid,
            "participant_sid": participant_sid,
        }

    @property
    def participant_sid(self):
        """
        :returns: The SID of the Participant resource for the Subscribe Rules.
        :rtype: str
        """
        return self._properties["participant_sid"]

    @property
    def room_sid(self):
        """
        :returns: The SID of the Room resource for the Subscribe Rules
        :rtype: str
        """
        return self._properties["room_sid"]

    @property
    def rules(self):
        """
        :returns: A collection of Subscribe Rules that describe how to include or exclude matching tracks. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information.
        :rtype: list[VideoV1RoomRoomParticipantRoomParticipantSubscribeRuleRules]
        """
        return self._properties["rules"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.SubscribeRulesInstance {}>".format(context)
