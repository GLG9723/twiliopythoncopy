"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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



class InsightsSegmentsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InsightsSegmentsList
        :param Version version: Version that contains the resource
        
        :returns: twilio.flex_api.v1.insights_segments..InsightsSegmentsList
        :rtype: twilio.flex_api.v1.insights_segments..InsightsSegmentsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = ''.format(**self._solution)


    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsSegmentsList>'


class InsightsSegmentsContext(InstanceContext):
    def __init__(self, version: Version, segment_id: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'segment_id': segment_id,  }
        self._uri = '/Insights/Segments/${segment_id}'
        
    
    def fetch(self, token):
        
        """
        Fetch the InsightsSegmentsInstance

        :returns: The fetched InsightsSegmentsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return InsightsSegmentsInstance(self._version, payload, segment_id=self._solution['segment_id'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsSegmentsContext>'



class InsightsSegmentsInstance(InstanceResource):
    def __init__(self, version, payload, segment_id: str):
        super().__init__(version)
        self._properties = { 
            'segment_id' : payload.get('segment_id'),
            'external_id' : payload.get('external_id'),
            'queue' : payload.get('queue'),
            'external_contact' : payload.get('external_contact'),
            'external_segment_link_id' : payload.get('external_segment_link_id'),
            'date' : payload.get('date'),
            'account_id' : payload.get('account_id'),
            'external_segment_link' : payload.get('external_segment_link'),
            'agent_id' : payload.get('agent_id'),
            'agent_phone' : payload.get('agent_phone'),
            'agent_name' : payload.get('agent_name'),
            'agent_team_name' : payload.get('agent_team_name'),
            'agent_team_name_in_hierarchy' : payload.get('agent_team_name_in_hierarchy'),
            'agent_link' : payload.get('agent_link'),
            'customer_phone' : payload.get('customer_phone'),
            'customer_name' : payload.get('customer_name'),
            'customer_link' : payload.get('customer_link'),
            'segment_recording_offset' : payload.get('segment_recording_offset'),
            'media' : payload.get('media'),
            'assessment_type' : payload.get('assessment_type'),
            'assessment_percentage' : payload.get('assessment_percentage'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'segment_id': segment_id or self._properties['segment_id'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = InsightsSegmentsContext(
                self._version,
                segment_id=self._solution['segment_id'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsSegmentsInstance {}>'.format(context)



