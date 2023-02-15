"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
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


class PhoneNumberList(ListResource):

    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the PhoneNumberList
        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to read the PhoneNumber resources.
        
        :returns: twilio.trunking.v1.phone_number..PhoneNumberList
        :rtype: twilio.trunking.v1.phone_number..PhoneNumberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'trunk_sid': trunk_sid,  }
        self._uri = '/Trunks/${trunk_sid}/PhoneNumbers'.format(**self._solution)


    
    
    
    
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
        :rtype: list[twilio.rest.trunking.v1.phone_number.PhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

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
        :rtype: list[twilio.rest.trunking.v1.phone_number.PhoneNumberInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of PhoneNumberInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.phone_number.PhoneNumberPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return PhoneNumberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.phone_number.PhoneNumberPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return PhoneNumberPage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.PhoneNumberList>'








class PhoneNumberPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the PhoneNumberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trunking.v1.phone_number.PhoneNumberPage
        :rtype: twilio.rest.trunking.v1.phone_number.PhoneNumberPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trunking.v1.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.trunking.v1.phone_number.PhoneNumberInstance
        """
        return PhoneNumberInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.PhoneNumberPage>'





class PhoneNumberContext(InstanceContext):
    def __init__(self, version: Version, trunk_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'trunk_sid': trunk_sid, 'sid': sid,  }
        self._uri = '/Trunks/${trunk_sid}/PhoneNumbers/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the PhoneNumberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the PhoneNumberInstance

        :returns: The fetched PhoneNumberInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PhoneNumberInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.PhoneNumberContext>'



class PhoneNumberInstance(InstanceResource):
    def __init__(self, version, payload, trunk_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'address_requirements' : payload.get('address_requirements'),
            'api_version' : payload.get('api_version'),
            'beta' : payload.get('beta'),
            'capabilities' : payload.get('capabilities'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'friendly_name' : payload.get('friendly_name'),
            'links' : payload.get('links'),
            'phone_number' : payload.get('phone_number'),
            'sid' : payload.get('sid'),
            'sms_application_sid' : payload.get('sms_application_sid'),
            'sms_fallback_method' : payload.get('sms_fallback_method'),
            'sms_fallback_url' : payload.get('sms_fallback_url'),
            'sms_method' : payload.get('sms_method'),
            'sms_url' : payload.get('sms_url'),
            'status_callback' : payload.get('status_callback'),
            'status_callback_method' : payload.get('status_callback_method'),
            'trunk_sid' : payload.get('trunk_sid'),
            'url' : payload.get('url'),
            'voice_application_sid' : payload.get('voice_application_sid'),
            'voice_caller_id_lookup' : payload.get('voice_caller_id_lookup'),
            'voice_fallback_method' : payload.get('voice_fallback_method'),
            'voice_fallback_url' : payload.get('voice_fallback_url'),
            'voice_method' : payload.get('voice_method'),
            'voice_url' : payload.get('voice_url'),
        }

        self._context = None
        self._solution = {
            'trunk_sid': trunk_sid or self._properties['trunk_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                trunk_sid=self._solution['trunk_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.PhoneNumberInstance {}>'.format(context)



