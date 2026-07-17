# DomainAvailabilityResult

Availability record for a single domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Fully qualified domain name | 
**premium** | **bool** | Whether the domain is a premium domain | [optional] 
**status** | **str** | Availability status: \&quot;available\&quot; or \&quot;unavailable\&quot; | 
**addons** | [**DomainAddons**](DomainAddons.md) |  | [optional] 
**pricing** | [**DomainPricing**](DomainPricing.md) |  | [optional] 
**requires_additional_info** | **bool** | Whether the domain requires additional registration information | [optional] 
**additional_info** | **object** | Opaque additional registration data from upstream | [optional] 
**group** | **str** | Product group from upstream | [optional] 
**register_url** | **str** | Checkout URL for available domains, enriched server-side | [optional] 

## Example

```python
from ha_sdk_python.models.domain_availability_result import DomainAvailabilityResult

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAvailabilityResult from a JSON string
domain_availability_result_instance = DomainAvailabilityResult.from_json(json)
# print the JSON string representation of the object
print(DomainAvailabilityResult.to_json())

# convert the object into a dict
domain_availability_result_dict = domain_availability_result_instance.to_dict()
# create an instance of DomainAvailabilityResult from a dict
domain_availability_result_from_dict = DomainAvailabilityResult.from_dict(domain_availability_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


