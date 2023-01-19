# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.flex_api.v1.interaction.interaction_channel import InteractionChannelList


class InteractionList(ListResource):

    def __init__(self, version):
        """
        Initialize the InteractionList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.interaction.InteractionList
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionList
        """
        super(InteractionList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Interactions'.format(**self._solution)

    def create(self, channel, routing):
        """
        Create the InteractionInstance

        :param dict channel: The Interaction's channel
        :param dict routing: The Interaction's routing logic

        :returns: The created InteractionInstance
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionInstance
        """
        data = values.of({'Channel': serialize.object(channel), 'Routing': serialize.object(routing), })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return InteractionInstance(self._version, payload, )

    def get(self, sid):
        """
        Constructs a InteractionContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.flex_api.v1.interaction.InteractionContext
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionContext
        """
        return InteractionContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a InteractionContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.flex_api.v1.interaction.InteractionContext
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionContext
        """
        return InteractionContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InteractionList>'


class InteractionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the InteractionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.interaction.InteractionPage
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionPage
        """
        super(InteractionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InteractionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.interaction.InteractionInstance
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionInstance
        """
        return InteractionInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InteractionPage>'


class InteractionContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the InteractionContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.flex_api.v1.interaction.InteractionContext
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionContext
        """
        super(InteractionContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Interactions/{sid}'.format(**self._solution)

        # Dependents
        self._channels = None

    def fetch(self):
        """
        Fetch the InteractionInstance

        :returns: The fetched InteractionInstance
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return InteractionInstance(self._version, payload, sid=self._solution['sid'], )

    @property
    def channels(self):
        """
        Access the channels

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelList
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelList
        """
        if self._channels is None:
            self._channels = InteractionChannelList(self._version, interaction_sid=self._solution['sid'], )
        return self._channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InteractionContext {}>'.format(context)


class InteractionInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the InteractionInstance

        :returns: twilio.rest.flex_api.v1.interaction.InteractionInstance
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionInstance
        """
        super(InteractionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'channel': payload.get('channel'),
            'routing': payload.get('routing'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: InteractionContext for this InteractionInstance
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionContext
        """
        if self._context is None:
            self._context = InteractionContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def channel(self):
        """
        :returns: The Interaction's channel
        :rtype: dict
        """
        return self._properties['channel']

    @property
    def routing(self):
        """
        :returns: A JSON Object representing the routing rules for the Interaction Channel
        :rtype: dict
        """
        return self._properties['routing']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the InteractionInstance

        :returns: The fetched InteractionInstance
        :rtype: twilio.rest.flex_api.v1.interaction.InteractionInstance
        """
        return self._proxy.fetch()

    @property
    def channels(self):
        """
        Access the channels

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelList
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelList
        """
        return self._proxy.channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InteractionInstance {}>'.format(context)
