"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
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

from twilio.base.page import Page




class ByocTrunkContext(InstanceContext):
    def __init__(self, version: V1, sid: str):
        # TODO: needs autogenerated docs
        super(ByocTrunkContextList, self).__init__(version)

        # Path Solution
        self._solution = { sid,  }
        self._uri = '/ByocTrunks/${sid}'
        
        
        def delete(self):
            
            
            """
            Deletes the ByocTrunkInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the ByocTrunkInstance

            :returns: The fetched ByocTrunkInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return ByocTrunkInstance(
                self._version,
                payload,
                sid=self._solution['sid'],
            )
            
            
        
        def update(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return ByocTrunkInstance(self._version, payload, sid=self._solution['sid'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ByocTrunkContext>'



class ByocTrunkInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super(ByocTrunkInstance, self).__init__(version)
        self._properties = { 
            'account_sid' = payload.get('account_sid'),
            'sid' = payload.get('sid'),
            'friendly_name' = payload.get('friendly_name'),
            'voice_url' = payload.get('voice_url'),
            'voice_method' = payload.get('voice_method'),
            'voice_fallback_url' = payload.get('voice_fallback_url'),
            'voice_fallback_method' = payload.get('voice_fallback_method'),
            'status_callback_url' = payload.get('status_callback_url'),
            'status_callback_method' = payload.get('status_callback_method'),
            'cnam_lookup_enabled' = payload.get('cnam_lookup_enabled'),
            'connection_policy_sid' = payload.get('connection_policy_sid'),
            'from_domain_sid' = payload.get('from_domain_sid'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'url' = payload.get('url'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ByocTrunkContext(
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
        return '<Twilio.Api.V1.ByocTrunkInstance {}>'.format(context)



class ByocTrunkListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super(ByocTrunkListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/ByocTrunks'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return ByocTrunkInstance(self._version, payload, )
            
        
        def page(self, page_size):
            
            data = values.of({
                'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return ByocTrunkPage(self._version, payload, )
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.ByocTrunkListInstance>'

