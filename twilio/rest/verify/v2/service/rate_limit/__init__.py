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
from twilio.rest.verify.v2.service.rate_limit.bucket import BucketList


class RateLimitList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the RateLimitList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the resource is associated with

        :returns: twilio.rest.verify.v2.service.rate_limit.RateLimitList
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitList
        """
        super(RateLimitList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/RateLimits'.format(**self._solution)

    def create(self, unique_name, description=values.unset):
        """
        Create the RateLimitInstance

        :param unicode unique_name: A unique, developer assigned name of this Rate Limit.
        :param unicode description: Description of this Rate Limit

        :returns: The created RateLimitInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitInstance
        """
        data = values.of({'UniqueName': unique_name, 'Description': description, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return RateLimitInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams RateLimitInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.verify.v2.service.rate_limit.RateLimitInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists RateLimitInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.rate_limit.RateLimitInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of RateLimitInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RateLimitInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return RateLimitPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RateLimitInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RateLimitInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return RateLimitPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a RateLimitContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.verify.v2.service.rate_limit.RateLimitContext
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitContext
        """
        return RateLimitContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a RateLimitContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.verify.v2.service.rate_limit.RateLimitContext
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitContext
        """
        return RateLimitContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.RateLimitList>'


class RateLimitPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the RateLimitPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the resource is associated with

        :returns: twilio.rest.verify.v2.service.rate_limit.RateLimitPage
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitPage
        """
        super(RateLimitPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RateLimitInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.rate_limit.RateLimitInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitInstance
        """
        return RateLimitInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.RateLimitPage>'


class RateLimitContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the RateLimitContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the resource is associated with
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.verify.v2.service.rate_limit.RateLimitContext
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitContext
        """
        super(RateLimitContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/RateLimits/{sid}'.format(**self._solution)

        # Dependents
        self._buckets = None

    def update(self, description=values.unset):
        """
        Update the RateLimitInstance

        :param unicode description: Description of this Rate Limit

        :returns: The updated RateLimitInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitInstance
        """
        data = values.of({'Description': description, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return RateLimitInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def fetch(self):
        """
        Fetch the RateLimitInstance

        :returns: The fetched RateLimitInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RateLimitInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the RateLimitInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    @property
    def buckets(self):
        """
        Access the buckets

        :returns: twilio.rest.verify.v2.service.rate_limit.bucket.BucketList
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketList
        """
        if self._buckets is None:
            self._buckets = BucketList(
                self._version,
                service_sid=self._solution['service_sid'],
                rate_limit_sid=self._solution['sid'],
            )
        return self._buckets

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.RateLimitContext {}>'.format(context)


class RateLimitInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the RateLimitInstance

        :returns: twilio.rest.verify.v2.service.rate_limit.RateLimitInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitInstance
        """
        super(RateLimitInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'service_sid': payload.get('service_sid'),
            'account_sid': payload.get('account_sid'),
            'unique_name': payload.get('unique_name'),
            'description': payload.get('description'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: RateLimitContext for this RateLimitInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitContext
        """
        if self._context is None:
            self._context = RateLimitContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Rate Limit.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def unique_name(self):
        """
        :returns: A unique, developer assigned name of this Rate Limit.
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def description(self):
        """
        :returns: Description of this Rate Limit
        :rtype: unicode
        """
        return self._properties['description']

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
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The URLs of related resources
        :rtype: unicode
        """
        return self._properties['links']

    def update(self, description=values.unset):
        """
        Update the RateLimitInstance

        :param unicode description: Description of this Rate Limit

        :returns: The updated RateLimitInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitInstance
        """
        return self._proxy.update(description=description, )

    def fetch(self):
        """
        Fetch the RateLimitInstance

        :returns: The fetched RateLimitInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the RateLimitInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def buckets(self):
        """
        Access the buckets

        :returns: twilio.rest.verify.v2.service.rate_limit.bucket.BucketList
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketList
        """
        return self._proxy.buckets

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.RateLimitInstance {}>'.format(context)
