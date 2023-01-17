"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
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

# 


class StepContextContext(InstanceContext):
    def __init__(self, version: Version, flow_sid: str, engagement_sid: str, step_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid, 'engagement_sid': engagement_sid, 'step_sid': step_sid,  }
        self._uri = '/Flows/${flow_sid}/Engagements/${engagement_sid}/Steps/${step_sid}/Context'
        
    
    def fetch(self):
        
        """
        Fetch the StepContextInstance

        :returns: The fetched StepContextInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return StepContextInstance(self._version, payload, flow_sid=self._solution['flow_sid'], engagement_sid=self._solution['engagement_sid'], step_sid=self._solution['step_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.StepContextContext>'



class StepContextInstance(InstanceResource):
    def __init__(self, version, payload, flow_sid: str, engagement_sid: str, step_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'context' : payload.get('context'),
            'engagement_sid' : payload.get('engagement_sid'),
            'flow_sid' : payload.get('flow_sid'),
            'step_sid' : payload.get('step_sid'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'flow_sid': flow_sid or self._properties['flow_sid'],'engagement_sid': engagement_sid or self._properties['engagement_sid'],'step_sid': step_sid or self._properties['step_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = StepContextContext(
                self._version,
                flow_sid=self._solution['flow_sid'],engagement_sid=self._solution['engagement_sid'],step_sid=self._solution['step_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.StepContextInstance {}>'.format(context)



class StepContextListInstance(ListResource):
    def __init__(self, version: Version, flow_sid: str, engagement_sid: str, step_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid, 'engagement_sid': engagement_sid, 'step_sid': step_sid,  }
        self._uri = ''
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.StepContextListInstance>'

