"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class DeliveryReceiptList(ListResource):

    def __init__(self, version: Version, conversation_sid: str, message_sid: str):
        """
        Initialize the DeliveryReceiptList

        :param Version version: Version that contains the resource
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
        :param message_sid: The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.
        
        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptList
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'conversation_sid': conversation_sid, 'message_sid': message_sid,  }
        self._uri = '/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts'.format(**self._solution)
        
        
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams DeliveryReceiptInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DeliveryReceiptInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of DeliveryReceiptInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return DeliveryReceiptPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DeliveryReceiptInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return DeliveryReceiptPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a DeliveryReceiptContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        """
        return DeliveryReceiptContext(self._version, conversation_sid=self._solution['conversation_sid'], message_sid=self._solution['message_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a DeliveryReceiptContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        """
        return DeliveryReceiptContext(self._version, conversation_sid=self._solution['conversation_sid'], message_sid=self._solution['message_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.DeliveryReceiptList>'




class DeliveryReceiptPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the DeliveryReceiptPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptPage
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeliveryReceiptInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        """
        return DeliveryReceiptInstance(self._version, payload, conversation_sid=self._solution['conversation_sid'], message_sid=self._solution['message_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.DeliveryReceiptPage>'




class DeliveryReceiptContext(InstanceContext):

    def __init__(self, version: Version, conversation_sid: str, message_sid: str, sid: str):
        """
        Initialize the DeliveryReceiptContext

        :param Version version: Version that contains the resource
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.:param message_sid: The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.:param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'conversation_sid': conversation_sid,
            'message_sid': message_sid,
            'sid': sid,
        }
        self._uri = '/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the DeliveryReceiptInstance
        

        :returns: The fetched DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DeliveryReceiptInstance(
            self._version,
            payload,
            conversation_sid=self._solution['conversation_sid'],
            message_sid=self._solution['message_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.DeliveryReceiptContext {}>'.format(context)

class DeliveryReceiptInstance(InstanceResource):

    class DeliveryStatus(object):
        READ = "read"
        FAILED = "failed"
        DELIVERED = "delivered"
        UNDELIVERED = "undelivered"
        SENT = "sent"

    def __init__(self, version, payload, conversation_sid: str, message_sid: str, sid: str=None):
        """
        Initialize the DeliveryReceiptInstance
        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'conversation_sid': payload.get('conversation_sid'),
            'sid': payload.get('sid'),
            'message_sid': payload.get('message_sid'),
            'channel_message_sid': payload.get('channel_message_sid'),
            'participant_sid': payload.get('participant_sid'),
            'status': payload.get('status'),
            'error_code': deserialize.integer(payload.get('error_code')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'conversation_sid': conversation_sid, 'message_sid': message_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DeliveryReceiptContext for this DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        """
        if self._context is None:
            self._context = DeliveryReceiptContext(self._version, conversation_sid=self._solution['conversation_sid'], message_sid=self._solution['message_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this participant.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def conversation_sid(self):
        """
        :returns: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
        :rtype: str
        """
        return self._properties['conversation_sid']
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def message_sid(self):
        """
        :returns: The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to
        :rtype: str
        """
        return self._properties['message_sid']
    
    @property
    def channel_message_sid(self):
        """
        :returns: A messaging channel-specific identifier for the message delivered to participant e.g. `SMxx` for SMS, `WAxx` for Whatsapp etc. 
        :rtype: str
        """
        return self._properties['channel_message_sid']
    
    @property
    def participant_sid(self):
        """
        :returns: The unique ID of the participant the delivery receipt belongs to.
        :rtype: str
        """
        return self._properties['participant_sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: DeliveryReceiptInstance.DeliveryStatus
        """
        return self._properties['status']
    
    @property
    def error_code(self):
        """
        :returns: The message [delivery error code](https://www.twilio.com/docs/sms/api/message-resource#delivery-related-errors) for a `failed` status, 
        :rtype: int
        """
        return self._properties['error_code']
    
    @property
    def date_created(self):
        """
        :returns: The date that this resource was created.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated. `null` if the delivery receipt has not been updated.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: An absolute API resource URL for this delivery receipt.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the DeliveryReceiptInstance
        

        :returns: The fetched DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.DeliveryReceiptInstance {}>'.format(context)


