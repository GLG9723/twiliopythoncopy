"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
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



class SettingList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SettingList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.insights.v1.setting.SettingList
        :rtype: twilio.rest.insights.v1.setting.SettingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    

    def get(self):
        """
        Constructs a SettingContext
        
        :returns: twilio.rest.insights.v1.setting.SettingContext
        :rtype: twilio.rest.insights.v1.setting.SettingContext
        """
        return SettingContext(self._version)

    def __call__(self):
        """
        Constructs a SettingContext
        
        :returns: twilio.rest.insights.v1.setting.SettingContext
        :rtype: twilio.rest.insights.v1.setting.SettingContext
        """
        return SettingContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.SettingList>'

class SettingContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the SettingContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.insights.v1.setting.SettingContext
        :rtype: twilio.rest.insights.v1.setting.SettingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
        }
        self._uri = '/Voice/Settings'.format(**self._solution)
        
    
    def fetch(self, subaccount_sid=values.unset):
        """
        Fetch the SettingInstance
        
        :params str subaccount_sid: 

        :returns: The fetched SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        
        data = values.of({ 
            'SubaccountSid': subaccount_sid,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return SettingInstance(
            self._version,
            payload,
            
        )
        
    def update(self, advanced_features=values.unset, voice_trace=values.unset, subaccount_sid=values.unset):
        """
        Update the SettingInstance
        
        :params bool advanced_features: 
        :params bool voice_trace: 
        :params str subaccount_sid: 

        :returns: The updated SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        data = values.of({ 
            'AdvancedFeatures': advanced_features,
            'VoiceTrace': voice_trace,
            'SubaccountSid': subaccount_sid,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SettingInstance(
            self._version,
            payload
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.SettingContext {}>'.format(context)

class SettingInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the SettingInstance
        :returns: twilio.rest.insights.v1.setting.SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'advanced_features': payload.get('advanced_features'),
            'voice_trace': payload.get('voice_trace'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SettingContext for this SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingContext
        """
        if self._context is None:
            self._context = SettingContext(self._version,)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def advanced_features(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['advanced_features']
    
    @property
    def voice_trace(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['voice_trace']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self, subaccount_sid=values.unset):
        """
        Fetch the SettingInstance
        
        :params str subaccount_sid: 

        :returns: The fetched SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        return self._proxy.fetch(subaccount_sid=subaccount_sid, )
    
    def update(self, advanced_features=values.unset, voice_trace=values.unset, subaccount_sid=values.unset):
        """
        Update the SettingInstance
        
        :params bool advanced_features: 
        :params bool voice_trace: 
        :params str subaccount_sid: 

        :returns: The updated SettingInstance
        :rtype: twilio.rest.insights.v1.setting.SettingInstance
        """
        return self._proxy.update(advanced_features=advanced_features, voice_trace=voice_trace, subaccount_sid=subaccount_sid, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.SettingInstance {}>'.format(context)


