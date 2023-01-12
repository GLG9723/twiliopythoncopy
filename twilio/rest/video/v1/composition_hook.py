"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
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




class CompositionHookContext(InstanceContext):
    def __init__(self, version: V1, sid: str):
        # TODO: needs autogenerated docs
        super(CompositionHookContextList, self).__init__(version)

        # Path Solution
        self._solution = { sid,  }
        self._uri = '/CompositionHooks/${sid}'
        
        
        def delete(self):
            
            
            """
            Deletes the CompositionHookInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the CompositionHookInstance

            :returns: The fetched CompositionHookInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return CompositionHookInstance(
                self._version,
                payload,
                sid=self._solution['sid'],
            )
            
            
        
        def update(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return CompositionHookInstance(self._version, payload, sid=self._solution['sid'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.CompositionHookContext>'



class CompositionHookInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super(CompositionHookInstance, self).__init__(version)
        self._properties = { 
            'account_sid' = payload.get('account_sid'),
            'friendly_name' = payload.get('friendly_name'),
            'enabled' = payload.get('enabled'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'sid' = payload.get('sid'),
            'audio_sources' = payload.get('audio_sources'),
            'audio_sources_excluded' = payload.get('audio_sources_excluded'),
            'video_layout' = payload.get('video_layout'),
            'resolution' = payload.get('resolution'),
            'trim' = payload.get('trim'),
            'format' = payload.get('format'),
            'status_callback' = payload.get('status_callback'),
            'status_callback_method' = payload.get('status_callback_method'),
            'url' = payload.get('url'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = CompositionHookContext(
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
        return '<Twilio.Api.V1.CompositionHookInstance {}>'.format(context)



class CompositionHookListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super(CompositionHookListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/CompositionHooks'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return CompositionHookInstance(self._version, payload, )
            
        
        def page(self, enabled, date_created_after, date_created_before, friendly_name, page_size):
            
            data = values.of({
                'enabled': enabled,'date_created_after': date_created_after,'date_created_before': date_created_before,'friendly_name': friendly_name,'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return CompositionHookPage(self._version, payload, )
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.CompositionHookListInstance>'

