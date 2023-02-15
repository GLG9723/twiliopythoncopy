"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.api.v2010.conference.participants import ParticipantList
from twilio.rest.api.v2010.conference.recordings import RecordingList


class ConferenceList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the ConferenceList
        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference resource(s) to read.
        
        :returns: twilio.api.v2010.conference..ConferenceList
        :rtype: twilio.api.v2010.conference..ConferenceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/Conferences.json'.format(**self._solution)


    
    
    
    def stream(self, date_created=values.unset, date_created_before=values.unset, date_created_after=values.unset, date_updated=values.unset, date_updated_before=values.unset, date_updated_after=values.unset, friendly_name=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Streams ConferenceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param date date_created: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`.
        :param date date_created_before: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`.
        :param date date_created_after: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`.
        :param date date_updated: The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`.
        :param date date_updated_before: The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`.
        :param date date_updated_after: The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`.
        :param str friendly_name: The string that identifies the Conference resources to read.
        :param ConferenceStatus status: The status of the resources to read. Can be: `init`, `in-progress`, or `completed`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.conference.ConferenceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            date_created=date_created,
            date_created_before=date_created_before,
            date_created_after=date_created_after,
            date_updated=date_updated,
            date_updated_before=date_updated_before,
            date_updated_after=date_updated_after,
            friendly_name=friendly_name,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, date_created=values.unset, date_created_before=values.unset, date_created_after=values.unset, date_updated=values.unset, date_updated_before=values.unset, date_updated_after=values.unset, friendly_name=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Lists ConferenceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param date date_created: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`.
        :param date date_created_before: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`.
        :param date date_created_after: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`.
        :param date date_updated: The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`.
        :param date date_updated_before: The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`.
        :param date date_updated_after: The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`.
        :param str friendly_name: The string that identifies the Conference resources to read.
        :param ConferenceStatus status: The status of the resources to read. Can be: `init`, `in-progress`, or `completed`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.conference.ConferenceInstance]
        """
        return list(self.stream(
            date_created=date_created,
            date_created_before=date_created_before,
            date_created_after=date_created_after,
            date_updated=date_updated,
            date_updated_before=date_updated_before,
            date_updated_after=date_updated_after,
            friendly_name=friendly_name,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, date_created=values.unset, date_created_before=values.unset, date_created_after=values.unset, date_updated=values.unset, date_updated_before=values.unset, date_updated_after=values.unset, friendly_name=values.unset, status=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ConferenceInstance records from the API.
        Request is executed immediately
        
        :param date date_created: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`.
        :param date date_created_before: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`.
        :param date date_created_after: The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that started on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify  conferences that started on or after midnight on a date, use `>=YYYY-MM-DD`.
        :param date date_updated: The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`.
        :param date date_updated_before: The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`.
        :param date date_updated_after: The `date_updated` value, specified as `YYYY-MM-DD`, of the resources to read. To read conferences that were last updated on or before midnight on a date, use `<=YYYY-MM-DD`, and to specify conferences that were last updated on or after midnight on a given date, use  `>=YYYY-MM-DD`.
        :param str friendly_name: The string that identifies the Conference resources to read.
        :param ConferenceStatus status: The status of the resources to read. Can be: `init`, `in-progress`, or `completed`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ConferenceInstance
        :rtype: twilio.rest.api.v2010.conference.ConferencePage
        """
        data = values.of({ 
            'DateCreated': date_created,
            'DateCreated&lt;': date_created_before,
            'DateCreated&gt;': date_created_after,
            'DateUpdated': date_updated,
            'DateUpdated&lt;': date_updated_before,
            'DateUpdated&gt;': date_updated_after,
            'FriendlyName': friendly_name,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ConferencePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ConferenceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ConferenceInstance
        :rtype: twilio.rest.api.v2010.conference.ConferencePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ConferencePage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConferenceList>'






class ConferencePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ConferencePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.conference.ConferencePage
        :rtype: twilio.rest.api.v2010.conference.ConferencePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ConferenceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.conference.ConferenceInstance
        :rtype: twilio.rest.api.v2010.conference.ConferenceInstance
        """
        return ConferenceInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConferencePage>'





class ConferenceContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/Conferences/${sid}.json'
        
        self._participants = None
        self._recordings = None
    
    def fetch(self):
        
        """
        Fetch the ConferenceInstance

        :returns: The fetched ConferenceInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ConferenceInstance(self._version, payload, account_sid=self._solution['account_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ConferenceInstance(self._version, payload, account_sid=self._solution['account_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConferenceContext>'



class ConferenceInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'api_version' : payload.get('api_version'),
            'friendly_name' : payload.get('friendly_name'),
            'region' : payload.get('region'),
            'sid' : payload.get('sid'),
            'status' : payload.get('status'),
            'uri' : payload.get('uri'),
            'subresource_uris' : payload.get('subresource_uris'),
            'reason_conference_ended' : payload.get('reason_conference_ended'),
            'call_sid_ending_conference' : payload.get('call_sid_ending_conference'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ConferenceContext(
                self._version,
                account_sid=self._solution['account_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def participants(self):
        return self._proxy.participants
    @property
    def recordings(self):
        return self._proxy.recordings
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ConferenceInstance {}>'.format(context)



