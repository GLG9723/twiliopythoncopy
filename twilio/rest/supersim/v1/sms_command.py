"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
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


class SmsCommandList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SmsCommandList
        :param Version version: Version that contains the resource
        
        :returns: twilio.supersim.v1.sms_command..SmsCommandList
        :rtype: twilio.supersim.v1.sms_command..SmsCommandList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/SmsCommands'.format(**self._solution)


    
    
    
    def stream(self, sim=values.unset, status=values.unset, direction=values.unset, limit=None, page_size=None):
        """
        Streams SmsCommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param SmsCommandStatus status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param SmsCommandDirection direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sms_command.SmsCommandInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            sim=sim,
            status=status,
            direction=direction,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, sim=values.unset, status=values.unset, direction=values.unset, limit=None, page_size=None):
        """
        Lists SmsCommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param SmsCommandStatus status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param SmsCommandDirection direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.sms_command.SmsCommandInstance]
        """
        return list(self.stream(
            sim=sim,
            status=status,
            direction=direction,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, sim=values.unset, status=values.unset, direction=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SmsCommandInstance records from the API.
        Request is executed immediately
        
        :param str sim: The SID or unique name of the Sim resource that SMS Command was sent to or from.
        :param SmsCommandStatus status: The status of the SMS Command. Can be: `queued`, `sent`, `delivered`, `received` or `failed`. See the [SMS Command Status Values](https://www.twilio.com/docs/iot/supersim/api/smscommand-resource#status-values) for a description of each.
        :param SmsCommandDirection direction: The direction of the SMS Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandPage
        """
        data = values.of({ 
            'Sim': sim,
            'Status': status,
            'Direction': direction,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SmsCommandPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SmsCommandInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SmsCommandPage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SmsCommandList>'






class SmsCommandPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SmsCommandPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.sms_command.SmsCommandPage
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SmsCommandInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        :rtype: twilio.rest.supersim.v1.sms_command.SmsCommandInstance
        """
        return SmsCommandInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SmsCommandPage>'





class SmsCommandContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/SmsCommands/${sid}'
        
    
    def fetch(self):
        
        """
        Fetch the SmsCommandInstance

        :returns: The fetched SmsCommandInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SmsCommandInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.SmsCommandContext>'



class SmsCommandInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'sim_sid' : payload.get('sim_sid'),
            'payload' : payload.get('payload'),
            'status' : payload.get('status'),
            'direction' : payload.get('direction'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SmsCommandContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.SmsCommandInstance {}>'.format(context)



