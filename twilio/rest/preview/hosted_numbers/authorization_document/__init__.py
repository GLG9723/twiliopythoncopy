"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
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
from twilio.rest.preview.hosted_numbers.authorization_document.dependent_hosted_number_order import DependentHostedNumberOrderList


class AuthorizationDocumentList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the AuthorizationDocumentList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentList
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/AuthorizationDocuments'.format(**self._solution)
        
        
    
    
    
    def create(self, hosted_number_order_sids, address_sid, email, contact_title, contact_phone_number, cc_emails=values.unset):
        """
        Create the AuthorizationDocumentInstance
        :param list[str] hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param str address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param str contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param str contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
        :param list[str] cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.
        
        :returns: The created AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        data = values.of({ 
            'HostedNumberOrderSids': serialize.map(hosted_number_order_sids, lambda e: e),
            'AddressSid': address_sid,
            'Email': email,
            'ContactTitle': contact_title,
            'ContactPhoneNumber': contact_phone_number,
            'CcEmails': serialize.map(cc_emails, lambda e: e),
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return AuthorizationDocumentInstance(self._version, payload)
    
    
    def stream(self, email=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Streams AuthorizationDocumentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param AuthorizationDocumentStatus status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/api/phone-numbers/hosted-number-authorization-documents#status-values) for more information on each of these statuses.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            email=email,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, email=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Lists AuthorizationDocumentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param AuthorizationDocumentStatus status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/api/phone-numbers/hosted-number-authorization-documents#status-values) for more information on each of these statuses.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance]
        """
        return list(self.stream(
            email=email,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, email=values.unset, status=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AuthorizationDocumentInstance records from the API.
        Request is executed immediately
        
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param AuthorizationDocumentStatus status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/api/phone-numbers/hosted-number-authorization-documents#status-values) for more information on each of these statuses.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentPage
        """
        data = values.of({ 
            'Email': email,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AuthorizationDocumentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AuthorizationDocumentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AuthorizationDocumentPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a AuthorizationDocumentContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        """
        return AuthorizationDocumentContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a AuthorizationDocumentContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentContext
        """
        return AuthorizationDocumentContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.HostedNumbers.AuthorizationDocumentList>'








class AuthorizationDocumentPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AuthorizationDocumentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentPage
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AuthorizationDocumentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        :rtype: twilio.rest.preview.hosted_numbers.authorization_document.AuthorizationDocumentInstance
        """
        return AuthorizationDocumentInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.HostedNumbers.AuthorizationDocumentPage>'





class AuthorizationDocumentContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/AuthorizationDocuments/${sid}'
        
        self._dependent_hosted_number_orders = None
    
    def fetch(self):
        
        """
        Fetch the AuthorizationDocumentInstance

        :returns: The fetched AuthorizationDocumentInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AuthorizationDocumentInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, hosted_number_order_sids, address_sid, email, cc_emails, status, contact_title, contact_phone_number):
        data = values.of({
            'hosted_number_order_sids': hosted_number_order_sids,'address_sid': address_sid,'email': email,'cc_emails': cc_emails,'status': status,'contact_title': contact_title,'contact_phone_number': contact_phone_number,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return AuthorizationDocumentInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.HostedNumbers.AuthorizationDocumentContext>'



class AuthorizationDocumentInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'address_sid' : payload.get('address_sid'),
            'status' : payload.get('status'),
            'email' : payload.get('email'),
            'cc_emails' : payload.get('cc_emails'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AuthorizationDocumentContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def dependent_hosted_number_orders(self):
        return self._proxy.dependent_hosted_number_orders
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.HostedNumbers.AuthorizationDocumentInstance {}>'.format(context)



