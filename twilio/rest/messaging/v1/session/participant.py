# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ParticipantList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, session_sid):
        """
        Initialize the ParticipantList

        :param Version version: Version that contains the resource
        :param session_sid: The SID of the Session for the participant

        :returns: twilio.rest.messaging.v1.session.participant.ParticipantList
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantList
        """
        super(ParticipantList, self).__init__(version)

        # Path Solution
        self._solution = {'session_sid': session_sid, }
        self._uri = '/Sessions/{session_sid}/Participants'.format(**self._solution)

    def create(self, attributes=values.unset, twilio_address=values.unset,
               date_created=values.unset, date_updated=values.unset,
               identity=values.unset, user_address=values.unset):
        """
        Create the ParticipantInstance

        :param unicode attributes: A JSON string that stores application-specific data
        :param unicode twilio_address: The address of the Twilio phone number that the participant is in contact with
        :param datetime date_created: The ISO 8601 date and time in GMT when the resource was created
        :param datetime date_updated: The ISO 8601 date and time in GMT when the resource was updated
        :param unicode identity: The string that identifies the resource's User
        :param unicode user_address: The address of the participant's device

        :returns: The created ParticipantInstance
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantInstance
        """
        data = values.of({
            'Identity': identity,
            'UserAddress': user_address,
            'Attributes': attributes,
            'TwilioAddress': twilio_address,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return ParticipantInstance(self._version, payload, session_sid=self._solution['session_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams ParticipantInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.messaging.v1.session.participant.ParticipantInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.session.participant.ParticipantInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return ParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ParticipantPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ParticipantContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.session.participant.ParticipantContext
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantContext
        """
        return ParticipantContext(self._version, session_sid=self._solution['session_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ParticipantContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.session.participant.ParticipantContext
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantContext
        """
        return ParticipantContext(self._version, session_sid=self._solution['session_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.ParticipantList>'


class ParticipantPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the ParticipantPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param session_sid: The SID of the Session for the participant

        :returns: twilio.rest.messaging.v1.session.participant.ParticipantPage
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantPage
        """
        super(ParticipantPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ParticipantInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.session.participant.ParticipantInstance
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantInstance
        """
        return ParticipantInstance(self._version, payload, session_sid=self._solution['session_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.ParticipantPage>'


class ParticipantContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, session_sid, sid):
        """
        Initialize the ParticipantContext

        :param Version version: Version that contains the resource
        :param session_sid: The SID of the Session with the participant to fetch
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.session.participant.ParticipantContext
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantContext
        """
        super(ParticipantContext, self).__init__(version)

        # Path Solution
        self._solution = {'session_sid': session_sid, 'sid': sid, }
        self._uri = '/Sessions/{session_sid}/Participants/{sid}'.format(**self._solution)

    def update(self, attributes=values.unset, date_created=values.unset,
               date_updated=values.unset):
        """
        Update the ParticipantInstance

        :param unicode attributes: A JSON string that stores application-specific data
        :param datetime date_created: The ISO 8601 date and time in GMT when the resource was created
        :param datetime date_updated: The ISO 8601 date and time in GMT when the resource was updated

        :returns: The updated ParticipantInstance
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantInstance
        """
        data = values.of({
            'Attributes': attributes,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return ParticipantInstance(
            self._version,
            payload,
            session_sid=self._solution['session_sid'],
            sid=self._solution['sid'],
        )

    def fetch(self):
        """
        Fetch the ParticipantInstance

        :returns: The fetched ParticipantInstance
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ParticipantInstance(
            self._version,
            payload,
            session_sid=self._solution['session_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the ParticipantInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.ParticipantContext {}>'.format(context)


class ParticipantInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class ParticipantType(object):
        CHAT = "chat"
        SMS = "sms"

    def __init__(self, version, payload, session_sid, sid=None):
        """
        Initialize the ParticipantInstance

        :returns: twilio.rest.messaging.v1.session.participant.ParticipantInstance
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantInstance
        """
        super(ParticipantInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'messaging_service_sid': payload.get('messaging_service_sid'),
            'session_sid': payload.get('session_sid'),
            'sid': payload.get('sid'),
            'identity': payload.get('identity'),
            'twilio_address': payload.get('twilio_address'),
            'user_address': payload.get('user_address'),
            'attributes': payload.get('attributes'),
            'type': payload.get('type'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'session_sid': session_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ParticipantContext for this ParticipantInstance
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantContext
        """
        if self._context is None:
            self._context = ParticipantContext(
                self._version,
                session_sid=self._solution['session_sid'],
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
    def service_sid(self):
        """
        :returns: The SID of the Service the session belongs to
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def messaging_service_sid(self):
        """
        :returns: The SID of the SMS Service the session belongs to
        :rtype: unicode
        """
        return self._properties['messaging_service_sid']

    @property
    def session_sid(self):
        """
        :returns: The SID of the Session for the participant
        :rtype: unicode
        """
        return self._properties['session_sid']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def identity(self):
        """
        :returns: The string that identifies the resource's User
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def twilio_address(self):
        """
        :returns: The address of the Twilio phone number that the participant is in contact with
        :rtype: unicode
        """
        return self._properties['twilio_address']

    @property
    def user_address(self):
        """
        :returns: The address of the participant's device
        :rtype: unicode
        """
        return self._properties['user_address']

    @property
    def attributes(self):
        """
        :returns: The JSON string that stores application-specific data
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def type(self):
        """
        :returns: The type of messaging used by the participant
        :rtype: ParticipantInstance.ParticipantType
        """
        return self._properties['type']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the participant
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, attributes=values.unset, date_created=values.unset,
               date_updated=values.unset):
        """
        Update the ParticipantInstance

        :param unicode attributes: A JSON string that stores application-specific data
        :param datetime date_created: The ISO 8601 date and time in GMT when the resource was created
        :param datetime date_updated: The ISO 8601 date and time in GMT when the resource was updated

        :returns: The updated ParticipantInstance
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantInstance
        """
        return self._proxy.update(
            attributes=attributes,
            date_created=date_created,
            date_updated=date_updated,
        )

    def fetch(self):
        """
        Fetch the ParticipantInstance

        :returns: The fetched ParticipantInstance
        :rtype: twilio.rest.messaging.v1.session.participant.ParticipantInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the ParticipantInstance

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
        return '<Twilio.Messaging.V1.ParticipantInstance {}>'.format(context)
