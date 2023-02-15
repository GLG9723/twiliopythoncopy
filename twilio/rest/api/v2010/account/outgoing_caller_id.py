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


class OutgoingCallerIdList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the OutgoingCallerIdList
        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to read.
        
        :returns: twilio.api.v2010.outgoing_caller_id..OutgoingCallerIdList
        :rtype: twilio.api.v2010.outgoing_caller_id..OutgoingCallerIdList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/OutgoingCallerIds.json'.format(**self._solution)


    
    
    
    
    def stream(self, phone_number=values.unset, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams OutgoingCallerIdInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str phone_number: The phone number of the OutgoingCallerId resources to read.
        :param str friendly_name: The string that identifies the OutgoingCallerId resources to read.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.outgoing_caller_id.OutgoingCallerIdInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            phone_number=phone_number,
            friendly_name=friendly_name,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, phone_number=values.unset, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists OutgoingCallerIdInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str phone_number: The phone number of the OutgoingCallerId resources to read.
        :param str friendly_name: The string that identifies the OutgoingCallerId resources to read.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.outgoing_caller_id.OutgoingCallerIdInstance]
        """
        return list(self.stream(
            phone_number=phone_number,
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, phone_number=values.unset, friendly_name=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of OutgoingCallerIdInstance records from the API.
        Request is executed immediately
        
        :param str phone_number: The phone number of the OutgoingCallerId resources to read.
        :param str friendly_name: The string that identifies the OutgoingCallerId resources to read.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.outgoing_caller_id.OutgoingCallerIdPage
        """
        data = values.of({ 
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return OutgoingCallerIdPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of OutgoingCallerIdInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.outgoing_caller_id.OutgoingCallerIdPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return OutgoingCallerIdPage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.OutgoingCallerIdList>'








class OutgoingCallerIdPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the OutgoingCallerIdPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.outgoing_caller_id.OutgoingCallerIdPage
        :rtype: twilio.rest.api.v2010.outgoing_caller_id.OutgoingCallerIdPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of OutgoingCallerIdInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.outgoing_caller_id.OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.outgoing_caller_id.OutgoingCallerIdInstance
        """
        return OutgoingCallerIdInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.OutgoingCallerIdPage>'





class OutgoingCallerIdContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/OutgoingCallerIds/${sid}.json'
        
    
    def delete(self):
        
        

        """
        Deletes the OutgoingCallerIdInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the OutgoingCallerIdInstance

        :returns: The fetched OutgoingCallerIdInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return OutgoingCallerIdInstance(self._version, payload, account_sid=self._solution['account_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return OutgoingCallerIdInstance(self._version, payload, account_sid=self._solution['account_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.OutgoingCallerIdContext>'



class OutgoingCallerIdInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'friendly_name' : payload.get('friendly_name'),
            'account_sid' : payload.get('account_sid'),
            'phone_number' : payload.get('phone_number'),
            'uri' : payload.get('uri'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = OutgoingCallerIdContext(
                self._version,
                account_sid=self._solution['account_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.OutgoingCallerIdInstance {}>'.format(context)



