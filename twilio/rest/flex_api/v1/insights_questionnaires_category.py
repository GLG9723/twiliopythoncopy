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
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InsightsQuestionnairesCategoryList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InsightsQuestionnairesCategoryList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryList
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Insights/QM/Categories'.format(**self._solution)
        
        
    
    
    
    def create(self, name, token=values.unset):
        """
        Create the InsightsQuestionnairesCategoryInstance

        :param str name: The name of this category.
        :param str token: The Token HTTP request header
        
        :returns: The created InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        data = values.of({ 
            'Name': name,
        })
        headers = values.of({'Token': token, })
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return InsightsQuestionnairesCategoryInstance(self._version, payload)

    async def create_async(self, name, token=values.unset):
        """
        Asynchronously create the InsightsQuestionnairesCategoryInstance

        :param str name: The name of this category.
        :param str token: The Token HTTP request header
        
        :returns: The created InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        data = values.of({ 
            'Name': name,
        })
        headers = values.of({'Token': token, })
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return InsightsQuestionnairesCategoryInstance(self._version, payload)
    
    
    def stream(self, token=values.unset, limit=None, page_size=None):
        """
        Streams InsightsQuestionnairesCategoryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str token: The Token HTTP request header
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            token=token,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, token=values.unset, limit=None, page_size=None):
        """
        Asynchronously streams InsightsQuestionnairesCategoryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str token: The Token HTTP request header
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            token=token,
            page_size=limits['page_size']
        )

        return await self._version.stream_async(page, limits['limit'])

    def list(self, token=values.unset, limit=None, page_size=None):
        """
        Lists InsightsQuestionnairesCategoryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str token: The Token HTTP request header
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance]
        """
        return list(self.stream(
            token=token,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, token=values.unset, limit=None, page_size=None):
        """
        Asynchronously lists InsightsQuestionnairesCategoryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str token: The Token HTTP request header
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance]
        """
        return list(await self.stream_async(
            token=token,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, token=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of InsightsQuestionnairesCategoryInstance records from the API.
        Request is executed immediately
        
        :param str token: The Token HTTP request header
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryPage
        """
        data = values.of({ 
            'Token': token,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return InsightsQuestionnairesCategoryPage(self._version, response, self._solution)

    async def page_async(self, token=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronously retrieve a single page of InsightsQuestionnairesCategoryInstance records from the API.
        Request is executed immediately
        
        :param str token: The Token HTTP request header
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryPage
        """
        data = values.of({ 
            'Token': token,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return InsightsQuestionnairesCategoryPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InsightsQuestionnairesCategoryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return InsightsQuestionnairesCategoryPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of InsightsQuestionnairesCategoryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return InsightsQuestionnairesCategoryPage(self._version, response, self._solution)


    def get(self, category_id):
        """
        Constructs a InsightsQuestionnairesCategoryContext
        
        :param category_id: The ID of the category to be update
        
        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        """
        return InsightsQuestionnairesCategoryContext(self._version, category_id=category_id)

    def __call__(self, category_id):
        """
        Constructs a InsightsQuestionnairesCategoryContext
        
        :param category_id: The ID of the category to be update
        
        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        """
        return InsightsQuestionnairesCategoryContext(self._version, category_id=category_id)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryList>'








class InsightsQuestionnairesCategoryPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the InsightsQuestionnairesCategoryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryPage
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InsightsQuestionnairesCategoryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        return InsightsQuestionnairesCategoryInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryPage>'




class InsightsQuestionnairesCategoryInstance(InstanceResource):

    def __init__(self, version, payload, category_id: str=None):
        """
        Initialize the InsightsQuestionnairesCategoryInstance
        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'category_id': payload.get('category_id'),
            'name': payload.get('name'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'category_id': category_id or self._properties['category_id'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InsightsQuestionnairesCategoryContext for this InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        """
        if self._context is None:
            self._context = InsightsQuestionnairesCategoryContext(self._version, category_id=self._solution['category_id'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Insights resource and owns this resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def category_id(self):
        """
        :returns: The unique ID for the category
        :rtype: str
        """
        return self._properties['category_id']
    
    @property
    def name(self):
        """
        :returns: The name of this category.
        :rtype: str
        """
        return self._properties['name']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    
    def delete(self, token=values.unset):
        """
        Deletes the InsightsQuestionnairesCategoryInstance
        
        :params str token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(token=token, )
    async def delete_async(self, token=values.unset):
        """
        Asynchronous coroutine that deletes the InsightsQuestionnairesCategoryInstance
        
        :params str token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async(token=token, )
    
    
    def update(self, name, token=values.unset):
        """
        Update the InsightsQuestionnairesCategoryInstance
        
        :params str name: The name of this category.
        :params str token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        return self._proxy.update(name=name, token=token, )

    async def update_async(self, name, token=values.unset):
        """
        Asynchronous coroutine to update the InsightsQuestionnairesCategoryInstance
        
        :params str name: The name of this category.
        :params str token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        return await self._proxy.update_async(name=name, token=token, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryInstance {}>'.format(context)

class InsightsQuestionnairesCategoryContext(InstanceContext):

    def __init__(self, version: Version, category_id: str):
        """
        Initialize the InsightsQuestionnairesCategoryContext

        :param Version version: Version that contains the resource
        :param category_id: The ID of the category to be update

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'category_id': category_id,
        }
        self._uri = '/Insights/QM/Categories/{category_id}'.format(**self._solution)
        
    
    
    def delete(self, token=values.unset):
        """
        Deletes the InsightsQuestionnairesCategoryInstance

        :param str token: The Token HTTP request header
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'Token': token, })
        
        return self._version.delete(method='DELETE', uri=self._uri, headers=headers)

    async def delete_async(self, token=values.unset):
        """
        Asynchronous coroutine that deletes the InsightsQuestionnairesCategoryInstance

        :param str token: The Token HTTP request header
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'Token': token, })
        
        return await self._version.delete_async(method='DELETE', uri=self._uri, headers=headers)
    
    
    def update(self, name, token=values.unset):
        """
        Update the InsightsQuestionnairesCategoryInstance
        
        :params str name: The name of this category.
        :params str token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        data = values.of({ 
            'Name': name,
        })
        headers = values.of({'Token': token, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return InsightsQuestionnairesCategoryInstance(
            self._version,
            payload,
            category_id=self._solution['category_id']
        )

    async def update_async(self, name, token=values.unset):
        """
        Asynchronous coroutine to update the InsightsQuestionnairesCategoryInstance
        
        :params str name: The name of this category.
        :params str token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        data = values.of({ 
            'Name': name,
        })
        headers = values.of({'Token': token, })

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data, headers=headers)

        return InsightsQuestionnairesCategoryInstance(
            self._version,
            payload,
            category_id=self._solution['category_id']
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryContext {}>'.format(context)


