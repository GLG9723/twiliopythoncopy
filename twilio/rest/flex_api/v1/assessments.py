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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class AssessmentsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the AssessmentsList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsList
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    

    def get(self):
        """
        Constructs a AssessmentsContext
        
        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        """
        return AssessmentsContext(self._version)

    def __call__(self):
        """
        Constructs a AssessmentsContext
        
        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        """
        return AssessmentsContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.AssessmentsList>'

class AssessmentsContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the AssessmentsContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
        }
        self._uri = '/Accounts/Assessments'.format(**self._solution)
        
    
    def create(self):
        """
        Create the AssessmentsInstance
        

        :returns: The created AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        data = values.of({ 
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)

        return AssessmentsInstance(
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
        return '<Twilio.FlexApi.V1.AssessmentsContext {}>'.format(context)

class AssessmentsInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the AssessmentsInstance
        :returns: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        super().__init__(version)

        self._properties = { 
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssessmentsContext for this AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsContext
        """
        if self._context is None:
            self._context = AssessmentsContext(self._version,)
        return self._context
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    def create(self):
        """
        Create the AssessmentsInstance
        

        :returns: The created AssessmentsInstance
        :rtype: twilio.rest.flex_api.v1.assessments.AssessmentsInstance
        """
        return self._proxy.create()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.AssessmentsInstance {}>'.format(context)


