# DomainAddons

Optional add-ons available for a domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsmanagement** | **bool** |  | [optional] 
**emailforwarding** | **bool** |  | [optional] 
**idprotection** | **bool** |  | [optional] 

## Example

```python
from ha_sdk_python.models.domain_addons import DomainAddons

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAddons from a JSON string
domain_addons_instance = DomainAddons.from_json(json)
# print the JSON string representation of the object
print(DomainAddons.to_json())

# convert the object into a dict
domain_addons_dict = domain_addons_instance.to_dict()
# create an instance of DomainAddons from a dict
domain_addons_from_dict = DomainAddons.from_dict(domain_addons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


