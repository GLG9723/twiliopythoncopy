# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class WebChannelsList(ListResource):

    def __init__(self, version):
        """
        Initialize the WebChannelsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v2.web_channels.WebChannelsList
        :rtype: twilio.rest.flex_api.v2.web_channels.WebChannelsList
        """
        super(WebChannelsList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/WebChats'.format(**self._solution)

    def create(self, address_sid, chat_friendly_name=values.unset,
               customer_friendly_name=values.unset,
               pre_engagement_data=values.unset):
        """
        Create the WebChannelsInstance

        :param unicode address_sid: The SID of the Conversations Address
        :param unicode chat_friendly_name: The Conversation's friendly name
        :param unicode customer_friendly_name: The Conversation participant's friendly name
        :param unicode pre_engagement_data: The pre-engagement data

        :returns: The created WebChannelsInstance
        :rtype: twilio.rest.flex_api.v2.web_channels.WebChannelsInstance
        """
        data = values.of({
            'AddressSid': address_sid,
            'ChatFriendlyName': chat_friendly_name,
            'CustomerFriendlyName': customer_friendly_name,
            'PreEngagementData': pre_engagement_data,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return WebChannelsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V2.WebChannelsList>'


class WebChannelsPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the WebChannelsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v2.web_channels.WebChannelsPage
        :rtype: twilio.rest.flex_api.v2.web_channels.WebChannelsPage
        """
        super(WebChannelsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WebChannelsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v2.web_channels.WebChannelsInstance
        :rtype: twilio.rest.flex_api.v2.web_channels.WebChannelsInstance
        """
        return WebChannelsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V2.WebChannelsPage>'


class WebChannelsInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the WebChannelsInstance

        :returns: twilio.rest.flex_api.v2.web_channels.WebChannelsInstance
        :rtype: twilio.rest.flex_api.v2.web_channels.WebChannelsInstance
        """
        super(WebChannelsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'conversation_sid': payload.get('conversation_sid'),
            'identity': payload.get('identity'),
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def conversation_sid(self):
        """
        :returns: The unique string representing the Conversation resource created
        :rtype: unicode
        """
        return self._properties['conversation_sid']

    @property
    def identity(self):
        """
        :returns: The unique string representing the User created
        :rtype: unicode
        """
        return self._properties['identity']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V2.WebChannelsInstance>'
