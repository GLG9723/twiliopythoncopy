"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
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


class MemberContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, channel_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Channels/${channel_sid}/Members/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the MemberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the MemberInstance

        :returns: The fetched MemberInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MemberInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return MemberInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.MemberContext>'



class MemberInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, channel_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'channel_sid' : payload.get('channel_sid'),
            'service_sid' : payload.get('service_sid'),
            'identity' : payload.get('identity'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'role_sid' : payload.get('role_sid'),
            'last_consumed_message_index' : payload.get('last_consumed_message_index'),
            'last_consumption_timestamp' : payload.get('last_consumption_timestamp'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'channel_sid': channel_sid or self._properties['channel_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = MemberContext(
                self._version,
                service_sid=self._solution['service_sid'],channel_sid=self._solution['channel_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.MemberInstance {}>'.format(context)



class MemberList(ListResource):
    def __init__(self, version: Version, service_sid: str, channel_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid,  }
        self._uri = '/Services/${service_sid}/Channels/${channel_sid}/Members'
        

    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return MemberInstance(self._version, payload, service_sid=self._solution['service_sid']channel_sid=self._solution['channel_sid'])
        
    """

    """
    def page(self, identity, page_size):
        
        data = values.of({
            'identity': identity,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return MemberPage(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.MemberList>'

