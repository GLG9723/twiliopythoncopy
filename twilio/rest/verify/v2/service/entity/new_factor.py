"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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



class NewFactorList(ListResource):

    def __init__(self, version: Version, service_sid: str, identity: str):
        """
        Initialize the NewFactorList

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: Customer unique identity for the Entity owner of the Factor. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        
        :returns: twilio.rest.verify.v2.service.entity.new_factor.NewFactorList
        :rtype: twilio.rest.verify.v2.service.entity.new_factor.NewFactorList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'identity': identity,  }
        self._uri = '/Services/${service_sid}/Entities/${identity}/Factors'.format(**self._solution)
        
        
    
    def create(self, friendly_name, factor_type, binding_alg=values.unset, binding_public_key=values.unset, config_app_id=values.unset, config_notification_platform=values.unset, config_notification_token=values.unset, config_sdk_version=values.unset, binding_secret=values.unset, config_time_step=values.unset, config_skew=values.unset, config_code_length=values.unset, config_alg=values.unset, metadata=values.unset):
        """
        Create the NewFactorInstance
        :param str friendly_name: The friendly name of this Factor. This can be any string up to 64 characters, meant for humans to distinguish between Factors. For `factor_type` `push`, this could be a device name. For `factor_type` `totp`, this value is used as the “account name” in constructing the `binding.uri` property. At the same time, we recommend avoiding providing PII.
        :param NewFactorFactorTypes factor_type: 
        :param str binding_alg: The algorithm used when `factor_type` is `push`. Algorithm supported: `ES256`
        :param str binding_public_key: The Ecdsa public key in PKIX, ASN.1 DER format encoded in Base64.  Required when `factor_type` is `push`
        :param str config_app_id: The ID that uniquely identifies your app in the Google or Apple store, such as `com.example.myapp`. It can be up to 100 characters long.  Required when `factor_type` is `push`.
        :param NewFactorNotificationPlatforms config_notification_platform: 
        :param str config_notification_token: For APN, the device token. For FCM, the registration token. It is used to send the push notifications. Must be between 32 and 255 characters long.  Required when `factor_type` is `push`.
        :param str config_sdk_version: The Verify Push SDK version used to configure the factor  Required when `factor_type` is `push`
        :param str binding_secret: The shared secret for TOTP factors encoded in Base32. This can be provided when creating the Factor, otherwise it will be generated.  Used when `factor_type` is `totp`
        :param int config_time_step: Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. The default value is defined at the service level in the property `totp.time_step`. Defaults to 30 seconds if not configured.  Used when `factor_type` is `totp`
        :param int config_skew: The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. The default value is defined at the service level in the property `totp.skew`. If not configured defaults to 1.  Used when `factor_type` is `totp`
        :param int config_code_length: Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. The default value is defined at the service level in the property `totp.code_length`. If not configured defaults to 6.  Used when `factor_type` is `totp`
        :param NewFactorTotpAlgorithms config_alg: 
        :param object metadata: Custom metadata associated with the factor. This is added by the Device/SDK directly to allow for the inclusion of device information. It must be a stringified JSON with only strings values eg. `{\\\"os\\\": \\\"Android\\\"}`. Can be up to 1024 characters in length.
        
        :returns: The created NewFactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.new_factor.NewFactorInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'FactorType': factor_type,
            'Binding.Alg': binding_alg,
            'Binding.PublicKey': binding_public_key,
            'Config.AppId': config_app_id,
            'Config.NotificationPlatform': config_notification_platform,
            'Config.NotificationToken': config_notification_token,
            'Config.SdkVersion': config_sdk_version,
            'Binding.Secret': binding_secret,
            'Config.TimeStep': config_time_step,
            'Config.Skew': config_skew,
            'Config.CodeLength': config_code_length,
            'Config.Alg': config_alg,
            'Metadata': serialize.object(metadata),
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return NewFactorInstance(self._version, payload, service_sid=self._solution['service_sid'], identity=self._solution['identity'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.NewFactorList>'



class NewFactorInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, identity: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'service_sid' : payload.get('service_sid'),
            'entity_sid' : payload.get('entity_sid'),
            'identity' : payload.get('identity'),
            'binding' : payload.get('binding'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'friendly_name' : payload.get('friendly_name'),
            'status' : payload.get('status'),
            'factor_type' : payload.get('factor_type'),
            'config' : payload.get('config'),
            'metadata' : payload.get('metadata'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'identity': identity or self._properties['identity'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = NewFactorContext(
                self._version,
                service_sid=self._solution['service_sid'],identity=self._solution['identity'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.NewFactorInstance {}>'.format(context)



