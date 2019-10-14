# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class DialogueList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid):
        """
        Initialize the DialogueList

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.

        :returns: twilio.rest.preview.understand.assistant.dialogue.DialogueList
        :rtype: twilio.rest.preview.understand.assistant.dialogue.DialogueList
        """
        super(DialogueList, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, }

    def get(self, sid):
        """
        Constructs a DialogueContext

        :param sid: The sid

        :returns: twilio.rest.preview.understand.assistant.dialogue.DialogueContext
        :rtype: twilio.rest.preview.understand.assistant.dialogue.DialogueContext
        """
        return DialogueContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a DialogueContext

        :param sid: The sid

        :returns: twilio.rest.preview.understand.assistant.dialogue.DialogueContext
        :rtype: twilio.rest.preview.understand.assistant.dialogue.DialogueContext
        """
        return DialogueContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.DialogueList>'


class DialoguePage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the DialoguePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param assistant_sid: The unique ID of the parent Assistant.

        :returns: twilio.rest.preview.understand.assistant.dialogue.DialoguePage
        :rtype: twilio.rest.preview.understand.assistant.dialogue.DialoguePage
        """
        super(DialoguePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DialogueInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.understand.assistant.dialogue.DialogueInstance
        :rtype: twilio.rest.preview.understand.assistant.dialogue.DialogueInstance
        """
        return DialogueInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.DialoguePage>'


class DialogueContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid, sid):
        """
        Initialize the DialogueContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The assistant_sid
        :param sid: The sid

        :returns: twilio.rest.preview.understand.assistant.dialogue.DialogueContext
        :rtype: twilio.rest.preview.understand.assistant.dialogue.DialogueContext
        """
        super(DialogueContext, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid, }
        self._uri = '/Assistants/{assistant_sid}/Dialogues/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a DialogueInstance

        :returns: Fetched DialogueInstance
        :rtype: twilio.rest.preview.understand.assistant.dialogue.DialogueInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return DialogueInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.DialogueContext {}>'.format(context)


class DialogueInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, assistant_sid, sid=None):
        """
        Initialize the DialogueInstance

        :returns: twilio.rest.preview.understand.assistant.dialogue.DialogueInstance
        :rtype: twilio.rest.preview.understand.assistant.dialogue.DialogueInstance
        """
        super(DialogueInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'assistant_sid': payload.get('assistant_sid'),
            'sid': payload.get('sid'),
            'data': payload.get('data'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DialogueContext for this DialogueInstance
        :rtype: twilio.rest.preview.understand.assistant.dialogue.DialogueContext
        """
        if self._context is None:
            self._context = DialogueContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Field.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def assistant_sid(self):
        """
        :returns: The unique ID of the parent Assistant.
        :rtype: unicode
        """
        return self._properties['assistant_sid']

    @property
    def sid(self):
        """
        :returns: The unique ID of the Dialogue
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def data(self):
        """
        :returns: The dialogue memory object as json
        :rtype: dict
        """
        return self._properties['data']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a DialogueInstance

        :returns: Fetched DialogueInstance
        :rtype: twilio.rest.preview.understand.assistant.dialogue.DialogueInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.DialogueInstance {}>'.format(context)
