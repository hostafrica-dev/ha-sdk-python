# DomainPricing

Registration, renewal and transfer pricing tiers for a domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainregister** | [**List[DomainPricingEntry]**](DomainPricingEntry.md) |  | [optional] 
**domainrenew** | [**List[DomainPricingEntry]**](DomainPricingEntry.md) |  | [optional] 
**domaintransfer** | [**List[DomainPricingEntry]**](DomainPricingEntry.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.domain_pricing import DomainPricing

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPricing from a JSON string
domain_pricing_instance = DomainPricing.from_json(json)
# print the JSON string representation of the object
print(DomainPricing.to_json())

# convert the object into a dict
domain_pricing_dict = domain_pricing_instance.to_dict()
# create an instance of DomainPricing from a dict
domain_pricing_from_dict = DomainPricing.from_dict(domain_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


