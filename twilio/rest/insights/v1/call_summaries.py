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


class CallSummariesList(ListResource):

    def __init__(self, version):
        """
        Initialize the CallSummariesList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.insights.v1.call_summaries.CallSummariesList
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesList
        """
        super(CallSummariesList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Voice/Summaries'.format(**self._solution)

    def stream(self, from_=values.unset, to=values.unset, from_carrier=values.unset,
               to_carrier=values.unset, from_country_code=values.unset,
               to_country_code=values.unset, branded=values.unset,
               verified_caller=values.unset, has_tag=values.unset,
               start_time=values.unset, end_time=values.unset,
               call_type=values.unset, call_state=values.unset,
               direction=values.unset, processing_state=values.unset,
               sort_by=values.unset, subaccount=values.unset,
               abnormal_session=values.unset, limit=None, page_size=None):
        """
        Streams CallSummariesInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode from_: The from
        :param unicode to: The to
        :param unicode from_carrier: The from_carrier
        :param unicode to_carrier: The to_carrier
        :param unicode from_country_code: The from_country_code
        :param unicode to_country_code: The to_country_code
        :param bool branded: The branded
        :param bool verified_caller: The verified_caller
        :param bool has_tag: The has_tag
        :param unicode start_time: The start_time
        :param unicode end_time: The end_time
        :param unicode call_type: The call_type
        :param unicode call_state: The call_state
        :param unicode direction: The direction
        :param CallSummariesInstance.ProcessingStateRequest processing_state: The processing_state
        :param CallSummariesInstance.SortBy sort_by: The sort_by
        :param unicode subaccount: The subaccount
        :param bool abnormal_session: The abnormal_session
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.call_summaries.CallSummariesInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            from_=from_,
            to=to,
            from_carrier=from_carrier,
            to_carrier=to_carrier,
            from_country_code=from_country_code,
            to_country_code=to_country_code,
            branded=branded,
            verified_caller=verified_caller,
            has_tag=has_tag,
            start_time=start_time,
            end_time=end_time,
            call_type=call_type,
            call_state=call_state,
            direction=direction,
            processing_state=processing_state,
            sort_by=sort_by,
            subaccount=subaccount,
            abnormal_session=abnormal_session,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, from_=values.unset, to=values.unset, from_carrier=values.unset,
             to_carrier=values.unset, from_country_code=values.unset,
             to_country_code=values.unset, branded=values.unset,
             verified_caller=values.unset, has_tag=values.unset,
             start_time=values.unset, end_time=values.unset, call_type=values.unset,
             call_state=values.unset, direction=values.unset,
             processing_state=values.unset, sort_by=values.unset,
             subaccount=values.unset, abnormal_session=values.unset, limit=None,
             page_size=None):
        """
        Lists CallSummariesInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode from_: The from
        :param unicode to: The to
        :param unicode from_carrier: The from_carrier
        :param unicode to_carrier: The to_carrier
        :param unicode from_country_code: The from_country_code
        :param unicode to_country_code: The to_country_code
        :param bool branded: The branded
        :param bool verified_caller: The verified_caller
        :param bool has_tag: The has_tag
        :param unicode start_time: The start_time
        :param unicode end_time: The end_time
        :param unicode call_type: The call_type
        :param unicode call_state: The call_state
        :param unicode direction: The direction
        :param CallSummariesInstance.ProcessingStateRequest processing_state: The processing_state
        :param CallSummariesInstance.SortBy sort_by: The sort_by
        :param unicode subaccount: The subaccount
        :param bool abnormal_session: The abnormal_session
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.call_summaries.CallSummariesInstance]
        """
        return list(self.stream(
            from_=from_,
            to=to,
            from_carrier=from_carrier,
            to_carrier=to_carrier,
            from_country_code=from_country_code,
            to_country_code=to_country_code,
            branded=branded,
            verified_caller=verified_caller,
            has_tag=has_tag,
            start_time=start_time,
            end_time=end_time,
            call_type=call_type,
            call_state=call_state,
            direction=direction,
            processing_state=processing_state,
            sort_by=sort_by,
            subaccount=subaccount,
            abnormal_session=abnormal_session,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, from_=values.unset, to=values.unset, from_carrier=values.unset,
             to_carrier=values.unset, from_country_code=values.unset,
             to_country_code=values.unset, branded=values.unset,
             verified_caller=values.unset, has_tag=values.unset,
             start_time=values.unset, end_time=values.unset, call_type=values.unset,
             call_state=values.unset, direction=values.unset,
             processing_state=values.unset, sort_by=values.unset,
             subaccount=values.unset, abnormal_session=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CallSummariesInstance records from the API.
        Request is executed immediately

        :param unicode from_: The from
        :param unicode to: The to
        :param unicode from_carrier: The from_carrier
        :param unicode to_carrier: The to_carrier
        :param unicode from_country_code: The from_country_code
        :param unicode to_country_code: The to_country_code
        :param bool branded: The branded
        :param bool verified_caller: The verified_caller
        :param bool has_tag: The has_tag
        :param unicode start_time: The start_time
        :param unicode end_time: The end_time
        :param unicode call_type: The call_type
        :param unicode call_state: The call_state
        :param unicode direction: The direction
        :param CallSummariesInstance.ProcessingStateRequest processing_state: The processing_state
        :param CallSummariesInstance.SortBy sort_by: The sort_by
        :param unicode subaccount: The subaccount
        :param bool abnormal_session: The abnormal_session
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CallSummariesInstance
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesPage
        """
        data = values.of({
            'From': from_,
            'To': to,
            'FromCarrier': from_carrier,
            'ToCarrier': to_carrier,
            'FromCountryCode': from_country_code,
            'ToCountryCode': to_country_code,
            'Branded': branded,
            'VerifiedCaller': verified_caller,
            'HasTag': has_tag,
            'StartTime': start_time,
            'EndTime': end_time,
            'CallType': call_type,
            'CallState': call_state,
            'Direction': direction,
            'ProcessingState': processing_state,
            'SortBy': sort_by,
            'Subaccount': subaccount,
            'AbnormalSession': abnormal_session,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return CallSummariesPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CallSummariesInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CallSummariesInstance
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CallSummariesPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallSummariesList>'


class CallSummariesPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CallSummariesPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.call_summaries.CallSummariesPage
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesPage
        """
        super(CallSummariesPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CallSummariesInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.call_summaries.CallSummariesInstance
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesInstance
        """
        return CallSummariesInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallSummariesPage>'


class CallSummariesInstance(InstanceResource):

    class AnsweredBy(object):
        UNKNOWN = "unknown"
        MACHINE_START = "machine_start"
        MACHINE_END_BEEP = "machine_end_beep"
        MACHINE_END_SILENCE = "machine_end_silence"
        MACHINE_END_OTHER = "machine_end_other"
        HUMAN = "human"
        FAX = "fax"

    class CallType(object):
        CARRIER = "carrier"
        SIP = "sip"
        TRUNKING = "trunking"
        CLIENT = "client"

    class CallState(object):
        RINGING = "ringing"
        COMPLETED = "completed"
        BUSY = "busy"
        FAIL = "fail"
        NOANSWER = "noanswer"
        CANCELED = "canceled"
        ANSWERED = "answered"
        UNDIALED = "undialed"

    class ProcessingState(object):
        COMPLETE = "complete"
        PARTIAL = "partial"

    class CallDirection(object):
        OUTBOUND_API = "outbound_api"
        OUTBOUND_DIAL = "outbound_dial"
        INBOUND = "inbound"
        TRUNKING_ORIGINATING = "trunking_originating"
        TRUNKING_TERMINATING = "trunking_terminating"

    class SortBy(object):
        START_TIME = "start_time"
        END_TIME = "end_time"

    class ProcessingStateRequest(object):
        COMPLETED = "completed"
        STARTED = "started"
        PARTIAL = "partial"
        ALL = "all"

    def __init__(self, version, payload):
        """
        Initialize the CallSummariesInstance

        :returns: twilio.rest.insights.v1.call_summaries.CallSummariesInstance
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesInstance
        """
        super(CallSummariesInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'call_sid': payload.get('call_sid'),
            'answered_by': payload.get('answered_by'),
            'call_type': payload.get('call_type'),
            'call_state': payload.get('call_state'),
            'processing_state': payload.get('processing_state'),
            'created_time': deserialize.iso8601_datetime(payload.get('created_time')),
            'start_time': deserialize.iso8601_datetime(payload.get('start_time')),
            'end_time': deserialize.iso8601_datetime(payload.get('end_time')),
            'duration': deserialize.integer(payload.get('duration')),
            'connect_duration': deserialize.integer(payload.get('connect_duration')),
            'from_': payload.get('from'),
            'to': payload.get('to'),
            'carrier_edge': payload.get('carrier_edge'),
            'client_edge': payload.get('client_edge'),
            'sdk_edge': payload.get('sdk_edge'),
            'sip_edge': payload.get('sip_edge'),
            'tags': payload.get('tags'),
            'url': payload.get('url'),
            'attributes': payload.get('attributes'),
            'properties': payload.get('properties'),
            'trust': payload.get('trust'),
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def call_sid(self):
        """
        :returns: The call_sid
        :rtype: unicode
        """
        return self._properties['call_sid']

    @property
    def answered_by(self):
        """
        :returns: The answered_by
        :rtype: CallSummariesInstance.AnsweredBy
        """
        return self._properties['answered_by']

    @property
    def call_type(self):
        """
        :returns: The call_type
        :rtype: CallSummariesInstance.CallType
        """
        return self._properties['call_type']

    @property
    def call_state(self):
        """
        :returns: The call_state
        :rtype: CallSummariesInstance.CallState
        """
        return self._properties['call_state']

    @property
    def processing_state(self):
        """
        :returns: The processing_state
        :rtype: CallSummariesInstance.ProcessingState
        """
        return self._properties['processing_state']

    @property
    def created_time(self):
        """
        :returns: The created_time
        :rtype: datetime
        """
        return self._properties['created_time']

    @property
    def start_time(self):
        """
        :returns: The start_time
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def end_time(self):
        """
        :returns: The end_time
        :rtype: datetime
        """
        return self._properties['end_time']

    @property
    def duration(self):
        """
        :returns: The duration
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def connect_duration(self):
        """
        :returns: The connect_duration
        :rtype: unicode
        """
        return self._properties['connect_duration']

    @property
    def from_(self):
        """
        :returns: The from
        :rtype: dict
        """
        return self._properties['from_']

    @property
    def to(self):
        """
        :returns: The to
        :rtype: dict
        """
        return self._properties['to']

    @property
    def carrier_edge(self):
        """
        :returns: The carrier_edge
        :rtype: dict
        """
        return self._properties['carrier_edge']

    @property
    def client_edge(self):
        """
        :returns: The client_edge
        :rtype: dict
        """
        return self._properties['client_edge']

    @property
    def sdk_edge(self):
        """
        :returns: The sdk_edge
        :rtype: dict
        """
        return self._properties['sdk_edge']

    @property
    def sip_edge(self):
        """
        :returns: The sip_edge
        :rtype: dict
        """
        return self._properties['sip_edge']

    @property
    def tags(self):
        """
        :returns: The tags
        :rtype: list[unicode]
        """
        return self._properties['tags']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def attributes(self):
        """
        :returns: The attributes
        :rtype: dict
        """
        return self._properties['attributes']

    @property
    def properties(self):
        """
        :returns: The properties
        :rtype: dict
        """
        return self._properties['properties']

    @property
    def trust(self):
        """
        :returns: The trust
        :rtype: dict
        """
        return self._properties['trust']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallSummariesInstance>'
