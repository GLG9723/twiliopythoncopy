# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class PhoneNumberList(ListResource):
    """  """

    def __init__(self, version, trunk_sid):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk that handles calls to the phone number

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberList
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberList
        """
        super(PhoneNumberList, self).__init__(version)

        # Path Solution
        self._solution = {'trunk_sid': trunk_sid, }
        self._uri = '/Trunks/{trunk_sid}/PhoneNumbers'.format(**self._solution)

    def create(self, phone_number_sid):
        """
        Create a new PhoneNumberInstance

        :param unicode phone_number_sid: The SID of the Incoming Phone Number that you want to associate with the trunk

        :returns: Newly created PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        data = values.of({'PhoneNumberSid': phone_number_sid, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return PhoneNumberInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams PhoneNumberInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists PhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return PhoneNumberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return PhoneNumberPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a PhoneNumberContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, trunk_sid=self._solution['trunk_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a PhoneNumberContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, trunk_sid=self._solution['trunk_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.PhoneNumberList>'


class PhoneNumberPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the PhoneNumberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param trunk_sid: The SID of the Trunk that handles calls to the phone number

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberPage
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberPage
        """
        super(PhoneNumberPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        return PhoneNumberInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.PhoneNumberPage>'


class PhoneNumberContext(InstanceContext):
    """  """

    def __init__(self, version, trunk_sid, sid):
        """
        Initialize the PhoneNumberContext

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to fetch the PhoneNumber resource
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        """
        super(PhoneNumberContext, self).__init__(version)

        # Path Solution
        self._solution = {'trunk_sid': trunk_sid, 'sid': sid, }
        self._uri = '/Trunks/{trunk_sid}/PhoneNumbers/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a PhoneNumberInstance

        :returns: Fetched PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the PhoneNumberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.PhoneNumberContext {}>'.format(context)


class PhoneNumberInstance(InstanceResource):
    """  """

    class AddressRequirement(object):
        NONE = "none"
        ANY = "any"
        LOCAL = "local"
        FOREIGN = "foreign"

    def __init__(self, version, payload, trunk_sid, sid=None):
        """
        Initialize the PhoneNumberInstance

        :returns: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        super(PhoneNumberInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'address_requirements': payload.get('address_requirements'),
            'api_version': payload.get('api_version'),
            'beta': payload.get('beta'),
            'capabilities': payload.get('capabilities'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'links': payload.get('links'),
            'phone_number': payload.get('phone_number'),
            'sid': payload.get('sid'),
            'sms_application_sid': payload.get('sms_application_sid'),
            'sms_fallback_method': payload.get('sms_fallback_method'),
            'sms_fallback_url': payload.get('sms_fallback_url'),
            'sms_method': payload.get('sms_method'),
            'sms_url': payload.get('sms_url'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'trunk_sid': payload.get('trunk_sid'),
            'url': payload.get('url'),
            'voice_application_sid': payload.get('voice_application_sid'),
            'voice_caller_id_lookup': payload.get('voice_caller_id_lookup'),
            'voice_fallback_method': payload.get('voice_fallback_method'),
            'voice_fallback_url': payload.get('voice_fallback_url'),
            'voice_method': payload.get('voice_method'),
            'voice_url': payload.get('voice_url'),
        }

        # Context
        self._context = None
        self._solution = {'trunk_sid': trunk_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                trunk_sid=self._solution['trunk_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def address_requirements(self):
        """
        :returns: Whether the phone number requires an Address registered with Twilio
        :rtype: PhoneNumberInstance.AddressRequirement
        """
        return self._properties['address_requirements']

    @property
    def api_version(self):
        """
        :returns: The API version used to start a new TwiML session
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def beta(self):
        """
        :returns: Whether the phone number is new to the Twilio platform
        :rtype: bool
        """
        return self._properties['beta']

    @property
    def capabilities(self):
        """
        :returns: Indicate if a phone can receive calls or messages
        :rtype: unicode
        """
        return self._properties['capabilities']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def links(self):
        """
        :returns: The URLs of related resources
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def phone_number(self):
        """
        :returns: The phone number in E.164 format
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def sms_application_sid(self):
        """
        :returns: The SID of the application that handles SMS messages sent to the phone number
        :rtype: unicode
        """
        return self._properties['sms_application_sid']

    @property
    def sms_fallback_method(self):
        """
        :returns: The HTTP method used with sms_fallback_url
        :rtype: unicode
        """
        return self._properties['sms_fallback_method']

    @property
    def sms_fallback_url(self):
        """
        :returns: The URL that we call when an error occurs while retrieving or executing the TwiML
        :rtype: unicode
        """
        return self._properties['sms_fallback_url']

    @property
    def sms_method(self):
        """
        :returns: The HTTP method to use with sms_url
        :rtype: unicode
        """
        return self._properties['sms_method']

    @property
    def sms_url(self):
        """
        :returns: The URL we call when the phone number receives an incoming SMS message
        :rtype: unicode
        """
        return self._properties['sms_url']

    @property
    def status_callback(self):
        """
        :returns: The URL to send status information to your application
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method we use to call status_callback
        :rtype: unicode
        """
        return self._properties['status_callback_method']

    @property
    def trunk_sid(self):
        """
        :returns: The SID of the Trunk that handles calls to the phone number
        :rtype: unicode
        """
        return self._properties['trunk_sid']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def voice_application_sid(self):
        """
        :returns: The SID of the application that handles calls to the phone number
        :rtype: unicode
        """
        return self._properties['voice_application_sid']

    @property
    def voice_caller_id_lookup(self):
        """
        :returns: Whether to lookup the caller's name
        :rtype: bool
        """
        return self._properties['voice_caller_id_lookup']

    @property
    def voice_fallback_method(self):
        """
        :returns: The HTTP method that we use to call voice_fallback_url
        :rtype: unicode
        """
        return self._properties['voice_fallback_method']

    @property
    def voice_fallback_url(self):
        """
        :returns: The URL we call when an error occurs in TwiML
        :rtype: unicode
        """
        return self._properties['voice_fallback_url']

    @property
    def voice_method(self):
        """
        :returns: The HTTP method used with the voice_url
        :rtype: unicode
        """
        return self._properties['voice_method']

    @property
    def voice_url(self):
        """
        :returns: The URL we call when the phone number receives a call
        :rtype: unicode
        """
        return self._properties['voice_url']

    def fetch(self):
        """
        Fetch a PhoneNumberInstance

        :returns: Fetched PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.trunk.phone_number.PhoneNumberInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the PhoneNumberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.PhoneNumberInstance {}>'.format(context)
