"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InteractionChannelParticipantList(ListResource):
    def __init__(self, version: Version, interaction_sid: str, channel_sid: str):
        """
        Initialize the InteractionChannelParticipantList

        :param Version version: Version that contains the resource
        :param interaction_sid: The Interaction Sid for this channel.
        :param channel_sid: The Channel Sid for this Participant.

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantList
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "interaction_sid": interaction_sid,
            "channel_sid": channel_sid,
        }
        self._uri = "/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants".format(
            **self._solution
        )

    def create(self, type, media_properties):
        """
        Create the InteractionChannelParticipantInstance

        :param InteractionChannelParticipantInstance.Type type:
        :param object media_properties: JSON representing the Media Properties for the new Participant.

        :returns: The created InteractionChannelParticipantInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantInstance
        """
        data = values.of(
            {
                "Type": type,
                "MediaProperties": serialize.object(media_properties),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionChannelParticipantInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams InteractionChannelParticipantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists InteractionChannelParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of InteractionChannelParticipantInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionChannelParticipantInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InteractionChannelParticipantPage(
            self._version, response, self._solution
        )

    def get_page(self, target_url):
        """
        Retrieve a specific page of InteractionChannelParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InteractionChannelParticipantInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InteractionChannelParticipantPage(
            self._version, response, self._solution
        )

    def get(self, sid):
        """
        Constructs a InteractionChannelParticipantContext

        :param sid: The unique string created by Twilio to identify an Interaction Channel resource.

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantContext
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantContext
        """
        return InteractionChannelParticipantContext(
            self._version,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a InteractionChannelParticipantContext

        :param sid: The unique string created by Twilio to identify an Interaction Channel resource.

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantContext
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantContext
        """
        return InteractionChannelParticipantContext(
            self._version,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.InteractionChannelParticipantList>"


class InteractionChannelParticipantPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the InteractionChannelParticipantPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantPage
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InteractionChannelParticipantInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantInstance
        """
        return InteractionChannelParticipantInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.InteractionChannelParticipantPage>"


class InteractionChannelParticipantInstance(InstanceResource):
    class Type(object):
        SUPERVISOR = "supervisor"
        CUSTOMER = "customer"
        EXTERNAL = "external"
        AGENT = "agent"
        UNKNOWN = "unknown"

    def __init__(
        self, version, payload, interaction_sid: str, channel_sid: str, sid: str = None
    ):
        """
        Initialize the InteractionChannelParticipantInstance

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "type": payload.get("type"),
            "interaction_sid": payload.get("interaction_sid"),
            "channel_sid": payload.get("channel_sid"),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {
            "interaction_sid": interaction_sid,
            "channel_sid": channel_sid,
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InteractionChannelParticipantContext for this InteractionChannelParticipantInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantContext
        """
        if self._context is None:
            self._context = InteractionChannelParticipantContext(
                self._version,
                interaction_sid=self._solution["interaction_sid"],
                channel_sid=self._solution["channel_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string created by Twilio to identify an Interaction Channel Participant resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def type(self):
        """
        :returns:
        :rtype: InteractionChannelParticipantInstance.Type
        """
        return self._properties["type"]

    @property
    def interaction_sid(self):
        """
        :returns: The Interaction Sid for this channel.
        :rtype: str
        """
        return self._properties["interaction_sid"]

    @property
    def channel_sid(self):
        """
        :returns: The Channel Sid for this Participant.
        :rtype: str
        """
        return self._properties["channel_sid"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def update(self, status):
        """
        Update the InteractionChannelParticipantInstance

        :param InteractionChannelParticipantInstance.Status status:

        :returns: The updated InteractionChannelParticipantInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantInstance
        """
        return self._proxy.update(
            status=status,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InteractionChannelParticipantInstance {}>".format(
            context
        )


class InteractionChannelParticipantContext(InstanceContext):
    def __init__(
        self, version: Version, interaction_sid: str, channel_sid: str, sid: str
    ):
        """
        Initialize the InteractionChannelParticipantContext

        :param Version version: Version that contains the resource
        :param interaction_sid: The Interaction Sid for this channel.
        :param channel_sid: The Channel Sid for this Participant.
        :param sid: The unique string created by Twilio to identify an Interaction Channel resource.

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantContext
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "interaction_sid": interaction_sid,
            "channel_sid": channel_sid,
            "sid": sid,
        }
        self._uri = "/Interactions/{interaction_sid}/Channels/{channel_sid}/Participants/{sid}".format(
            **self._solution
        )

    def update(self, status):
        """
        Update the InteractionChannelParticipantInstance

        :param InteractionChannelParticipantInstance.Status status:

        :returns: The updated InteractionChannelParticipantInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant.InteractionChannelParticipantInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return InteractionChannelParticipantInstance(
            self._version,
            payload,
            interaction_sid=self._solution["interaction_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InteractionChannelParticipantContext {}>".format(
            context
        )
