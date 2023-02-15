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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.base.page import Page

# 


class DeliveryReceiptContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str, conversation_sid: str, message_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid, 'conversation_sid': conversation_sid, 'message_sid': message_sid, 'sid': sid,  }
        self._uri = '/Services/${chat_service_sid}/Conversations/${conversation_sid}/Messages/${message_sid}/Receipts/${sid}'
        
    
    def fetch(self):
        
        """
        Fetch the DeliveryReceiptInstance

        :returns: The fetched DeliveryReceiptInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DeliveryReceiptInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'], message_sid=self._solution['message_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.DeliveryReceiptContext>'



class DeliveryReceiptInstance(InstanceResource):
    def __init__(self, version, payload, chat_service_sid: str, conversation_sid: str, message_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'chat_service_sid' : payload.get('chat_service_sid'),
            'conversation_sid' : payload.get('conversation_sid'),
            'message_sid' : payload.get('message_sid'),
            'sid' : payload.get('sid'),
            'channel_message_sid' : payload.get('channel_message_sid'),
            'participant_sid' : payload.get('participant_sid'),
            'status' : payload.get('status'),
            'error_code' : payload.get('error_code'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'chat_service_sid': chat_service_sid or self._properties['chat_service_sid'],'conversation_sid': conversation_sid or self._properties['conversation_sid'],'message_sid': message_sid or self._properties['message_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = DeliveryReceiptContext(
                self._version,
                chat_service_sid=self._solution['chat_service_sid'],conversation_sid=self._solution['conversation_sid'],message_sid=self._solution['message_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.DeliveryReceiptInstance {}>'.format(context)



class DeliveryReceiptList(ListResource):
    def __init__(self, version: Version, chat_service_sid: str, conversation_sid: str, message_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid, 'conversation_sid': conversation_sid, 'message_sid': message_sid,  }
        self._uri = '/Services/${chat_service_sid}/Conversations/${conversation_sid}/Messages/${message_sid}/Receipts'
        

    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return DeliveryReceiptPage(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'], message_sid=self._solution['message_sid'], )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.DeliveryReceiptList>'

