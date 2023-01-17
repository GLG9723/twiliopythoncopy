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

# 


class NotificationContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/Notifications/${sid}.json'
        
    
    def fetch(self):
        
        """
        Fetch the NotificationInstance

        :returns: The fetched NotificationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return NotificationInstance(self._version, payload, account_sid=self._solution['account_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NotificationContext>'



class NotificationInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'api_version' : payload.get('api_version'),
            'call_sid' : payload.get('call_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'error_code' : payload.get('error_code'),
            'log' : payload.get('log'),
            'message_date' : payload.get('message_date'),
            'message_text' : payload.get('message_text'),
            'more_info' : payload.get('more_info'),
            'request_method' : payload.get('request_method'),
            'request_url' : payload.get('request_url'),
            'request_variables' : payload.get('request_variables'),
            'response_body' : payload.get('response_body'),
            'response_headers' : payload.get('response_headers'),
            'sid' : payload.get('sid'),
            'uri' : payload.get('uri'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = NotificationContext(
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
        return '<Twilio.Api.V2010.NotificationInstance {}>'.format(context)



class NotificationListInstance(ListResource):
    def __init__(self, version: Version, account_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/Notifications.json'
        
    
    """
    def page(self, log, message_date, message_date, message_date, page_size):
        
        data = values.of({
            'log': log,'message_date': message_date,'message_date': message_date,'message_date': message_date,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return NotificationPage(self._version, payload, account_sid=self._solution['account_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NotificationListInstance>'

