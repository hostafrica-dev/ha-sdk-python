# DomainAvailableFeatures

Feature flags and priced addons available for a domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eppcode** | **bool** | Whether EPP/auth code retrieval is available | [optional] 
**dnssec** | **bool** | Whether DNSSEC management is available | [optional] 
**private_nameservers** | **bool** | Whether private/custom nameservers are supported | [optional] 
**redirector** | **bool** | Whether domain redirect is available | [optional] 
**dnsmanagement** | [**DomainAddonFeature**](DomainAddonFeature.md) |  | [optional] 
**emailforwarding** | [**DomainAddonFeature**](DomainAddonFeature.md) |  | [optional] 
**idprotection** | [**DomainAddonFeature**](DomainAddonFeature.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.domain_available_features import DomainAvailableFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAvailableFeatures from a JSON string
domain_available_features_instance = DomainAvailableFeatures.from_json(json)
# print the JSON string representation of the object
print(DomainAvailableFeatures.to_json())

# convert the object into a dict
domain_available_features_dict = domain_available_features_instance.to_dict()
# create an instance of DomainAvailableFeatures from a dict
domain_available_features_from_dict = DomainAvailableFeatures.from_dict(domain_available_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


