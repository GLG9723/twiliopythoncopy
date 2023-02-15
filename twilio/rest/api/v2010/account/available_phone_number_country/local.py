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


class LocalList(ListResource):

    def __init__(self, version: Version, account_sid: str, country_code: str):
        """
        Initialize the LocalList
        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
        :param country_code: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
        
        :returns: twilio.api.v2010.local..LocalList
        :rtype: twilio.api.v2010.local..LocalList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'country_code': country_code,  }
        self._uri = '/Accounts/${account_sid}/AvailablePhoneNumbers/${country_code}/Local.json'.format(**self._solution)


    
    def stream(self, area_code=values.unset, contains=values.unset, sms_enabled=values.unset, mms_enabled=values.unset, voice_enabled=values.unset, exclude_all_address_required=values.unset, exclude_local_address_required=values.unset, exclude_foreign_address_required=values.unset, beta=values.unset, near_number=values.unset, near_lat_long=values.unset, distance=values.unset, in_postal_code=values.unset, in_region=values.unset, in_rate_center=values.unset, in_lata=values.unset, in_locality=values.unset, fax_enabled=values.unset, limit=None, page_size=None):
        """
        Streams LocalInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int area_code: The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada.
        :param str contains: The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource?code-sample=code-find-phone-numbers-by-number-pattern) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource?code-sample=code-find-phone-numbers-by-character-pattern). If specified, this value must have at least two characters.
        :param bool sms_enabled: Whether the phone numbers can receive text messages. Can be: `true` or `false`.
        :param bool mms_enabled: Whether the phone numbers can receive MMS messages. Can be: `true` or `false`.
        :param bool voice_enabled: Whether the phone numbers can receive calls. Can be: `true` or `false`.
        :param bool exclude_all_address_required: Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
        :param bool exclude_local_address_required: Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
        :param bool exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
        :param bool beta: Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param str near_number: Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada.
        :param str near_lat_long: Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada.
        :param int distance: The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada.
        :param str in_postal_code: Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada.
        :param str in_region: Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada.
        :param str in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada.
        :param str in_lata: Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada.
        :param str in_locality: Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number.
        :param bool fax_enabled: Whether the phone numbers can receive faxes. Can be: `true` or `false`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.local.LocalInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            area_code=area_code,
            contains=contains,
            sms_enabled=sms_enabled,
            mms_enabled=mms_enabled,
            voice_enabled=voice_enabled,
            exclude_all_address_required=exclude_all_address_required,
            exclude_local_address_required=exclude_local_address_required,
            exclude_foreign_address_required=exclude_foreign_address_required,
            beta=beta,
            near_number=near_number,
            near_lat_long=near_lat_long,
            distance=distance,
            in_postal_code=in_postal_code,
            in_region=in_region,
            in_rate_center=in_rate_center,
            in_lata=in_lata,
            in_locality=in_locality,
            fax_enabled=fax_enabled,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, area_code=values.unset, contains=values.unset, sms_enabled=values.unset, mms_enabled=values.unset, voice_enabled=values.unset, exclude_all_address_required=values.unset, exclude_local_address_required=values.unset, exclude_foreign_address_required=values.unset, beta=values.unset, near_number=values.unset, near_lat_long=values.unset, distance=values.unset, in_postal_code=values.unset, in_region=values.unset, in_rate_center=values.unset, in_lata=values.unset, in_locality=values.unset, fax_enabled=values.unset, limit=None, page_size=None):
        """
        Lists LocalInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int area_code: The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada.
        :param str contains: The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource?code-sample=code-find-phone-numbers-by-number-pattern) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource?code-sample=code-find-phone-numbers-by-character-pattern). If specified, this value must have at least two characters.
        :param bool sms_enabled: Whether the phone numbers can receive text messages. Can be: `true` or `false`.
        :param bool mms_enabled: Whether the phone numbers can receive MMS messages. Can be: `true` or `false`.
        :param bool voice_enabled: Whether the phone numbers can receive calls. Can be: `true` or `false`.
        :param bool exclude_all_address_required: Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
        :param bool exclude_local_address_required: Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
        :param bool exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
        :param bool beta: Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param str near_number: Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada.
        :param str near_lat_long: Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada.
        :param int distance: The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada.
        :param str in_postal_code: Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada.
        :param str in_region: Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada.
        :param str in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada.
        :param str in_lata: Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada.
        :param str in_locality: Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number.
        :param bool fax_enabled: Whether the phone numbers can receive faxes. Can be: `true` or `false`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.local.LocalInstance]
        """
        return list(self.stream(
            area_code=area_code,
            contains=contains,
            sms_enabled=sms_enabled,
            mms_enabled=mms_enabled,
            voice_enabled=voice_enabled,
            exclude_all_address_required=exclude_all_address_required,
            exclude_local_address_required=exclude_local_address_required,
            exclude_foreign_address_required=exclude_foreign_address_required,
            beta=beta,
            near_number=near_number,
            near_lat_long=near_lat_long,
            distance=distance,
            in_postal_code=in_postal_code,
            in_region=in_region,
            in_rate_center=in_rate_center,
            in_lata=in_lata,
            in_locality=in_locality,
            fax_enabled=fax_enabled,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, area_code=values.unset, contains=values.unset, sms_enabled=values.unset, mms_enabled=values.unset, voice_enabled=values.unset, exclude_all_address_required=values.unset, exclude_local_address_required=values.unset, exclude_foreign_address_required=values.unset, beta=values.unset, near_number=values.unset, near_lat_long=values.unset, distance=values.unset, in_postal_code=values.unset, in_region=values.unset, in_rate_center=values.unset, in_lata=values.unset, in_locality=values.unset, fax_enabled=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of LocalInstance records from the API.
        Request is executed immediately
        
        :param int area_code: The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada.
        :param str contains: The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource?code-sample=code-find-phone-numbers-by-number-pattern) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumberlocal-resource?code-sample=code-find-phone-numbers-by-character-pattern). If specified, this value must have at least two characters.
        :param bool sms_enabled: Whether the phone numbers can receive text messages. Can be: `true` or `false`.
        :param bool mms_enabled: Whether the phone numbers can receive MMS messages. Can be: `true` or `false`.
        :param bool voice_enabled: Whether the phone numbers can receive calls. Can be: `true` or `false`.
        :param bool exclude_all_address_required: Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
        :param bool exclude_local_address_required: Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
        :param bool exclude_foreign_address_required: Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
        :param bool beta: Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param str near_number: Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada.
        :param str near_lat_long: Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada.
        :param int distance: The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada.
        :param str in_postal_code: Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada.
        :param str in_region: Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada.
        :param str in_rate_center: Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada.
        :param str in_lata: Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada.
        :param str in_locality: Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number.
        :param bool fax_enabled: Whether the phone numbers can receive faxes. Can be: `true` or `false`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of LocalInstance
        :rtype: twilio.rest.api.v2010.local.LocalPage
        """
        data = values.of({ 
            'AreaCode': area_code,
            'Contains': contains,
            'SmsEnabled': sms_enabled,
            'MmsEnabled': mms_enabled,
            'VoiceEnabled': voice_enabled,
            'ExcludeAllAddressRequired': exclude_all_address_required,
            'ExcludeLocalAddressRequired': exclude_local_address_required,
            'ExcludeForeignAddressRequired': exclude_foreign_address_required,
            'Beta': beta,
            'NearNumber': near_number,
            'NearLatLong': near_lat_long,
            'Distance': distance,
            'InPostalCode': in_postal_code,
            'InRegion': in_region,
            'InRateCenter': in_rate_center,
            'InLata': in_lata,
            'InLocality': in_locality,
            'FaxEnabled': fax_enabled,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return LocalPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of LocalInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of LocalInstance
        :rtype: twilio.rest.api.v2010.local.LocalPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return LocalPage(self._version, response, self._solution)


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.LocalList>'


class LocalPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the LocalPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.local.LocalPage
        :rtype: twilio.rest.api.v2010.local.LocalPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of LocalInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.local.LocalInstance
        :rtype: twilio.rest.api.v2010.local.LocalInstance
        """
        return LocalInstance(self._version, payload, account_sid=self._solution['account_sid'], country_code=self._solution['country_code'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.LocalPage>'







