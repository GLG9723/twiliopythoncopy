# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class NewKeyList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the NewKeyList

        :param Version version: Version that contains the resource
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.new_key.NewKeyList
        :rtype: twilio.rest.api.v2010.account.new_key.NewKeyList
        """
        super(NewKeyList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/Keys.json'.format(**self._solution)

    def create(self, friendly_name=values.unset):
        """
        Create a new NewKeyInstance

        :param unicode friendly_name: A string to describe the resource

        :returns: Newly created NewKeyInstance
        :rtype: twilio.rest.api.v2010.account.new_key.NewKeyInstance
        """
        data = values.of({'FriendlyName': friendly_name, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return NewKeyInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NewKeyList>'


class NewKeyPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the NewKeyPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.new_key.NewKeyPage
        :rtype: twilio.rest.api.v2010.account.new_key.NewKeyPage
        """
        super(NewKeyPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NewKeyInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.new_key.NewKeyInstance
        :rtype: twilio.rest.api.v2010.account.new_key.NewKeyInstance
        """
        return NewKeyInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NewKeyPage>'


class NewKeyInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid):
        """
        Initialize the NewKeyInstance

        :returns: twilio.rest.api.v2010.account.new_key.NewKeyInstance
        :rtype: twilio.rest.api.v2010.account.new_key.NewKeyInstance
        """
        super(NewKeyInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'secret': payload.get('secret'),
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, }

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def secret(self):
        """
        :returns: The secret your application uses to sign Access Tokens and to authenticate to the REST API.
        :rtype: unicode
        """
        return self._properties['secret']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NewKeyInstance>'
