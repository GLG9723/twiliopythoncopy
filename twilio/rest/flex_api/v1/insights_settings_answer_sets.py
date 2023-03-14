r"""
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

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class InsightsSettingsAnswerSetsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InsightsSettingsAnswerSetsList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.flex_api.v1.insights_settings_answer_sets.InsightsSettingsAnswerSetsList
        :rtype: twilio.rest.flex_api.v1.insights_settings_answer_sets.InsightsSettingsAnswerSetsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Insights/QM/Settings/AnswerSets'.format(**self._solution)
        
        
    
    def fetch(self):
        """
        Asynchronously fetch the InsightsSettingsAnswerSetsInstance

        :returns: The fetched InsightsSettingsAnswerSetsInstance
        :rtype: twilio.rest.flex_api.v1.insights_settings_answer_sets.InsightsSettingsAnswerSetsInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri)

        return InsightsSettingsAnswerSetsInstance(self._version, payload)

    async def fetch_async(self):
        """
        Asynchronously fetch the InsightsSettingsAnswerSetsInstance

        :returns: The fetched InsightsSettingsAnswerSetsInstance
        :rtype: twilio.rest.flex_api.v1.insights_settings_answer_sets.InsightsSettingsAnswerSetsInstance
        """
        payload = await self._version.fetch_async(method='GET', uri=self._uri)

        return InsightsSettingsAnswerSetsInstance(self._version, payload)
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsSettingsAnswerSetsList>'

class InsightsSettingsAnswerSetsInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the InsightsSettingsAnswerSetsInstance
        :returns: twilio.rest.flex_api.v1.insights_settings_answer_sets.InsightsSettingsAnswerSetsInstance
        :rtype: twilio.rest.flex_api.v1.insights_settings_answer_sets.InsightsSettingsAnswerSetsInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'answer_sets': payload.get('answer_sets'),
            'answer_set_categories': payload.get('answer_set_categories'),
            'not_applicable': payload.get('not_applicable'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Insights resource and owns this resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def answer_sets(self):
        """
        :returns: The lis of answer sets
        :rtype: dict
        """
        return self._properties['answer_sets']
    
    @property
    def answer_set_categories(self):
        """
        :returns: The list of answer set categories
        :rtype: dict
        """
        return self._properties['answer_set_categories']
    
    @property
    def not_applicable(self):
        """
        :returns: The details for not applicable answer set
        :rtype: dict
        """
        return self._properties['not_applicable']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsSettingsAnswerSetsInstance {}>'.format(context)



