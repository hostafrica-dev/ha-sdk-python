# DomainPricingEntry

A single period/price pair for domain pricing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **int** |  | 
**price** | **str** | Price as a decimal string with two decimal places | 

## Example

```python
from ha_sdk_python.models.domain_pricing_entry import DomainPricingEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPricingEntry from a JSON string
domain_pricing_entry_instance = DomainPricingEntry.from_json(json)
# print the JSON string representation of the object
print(DomainPricingEntry.to_json())

# convert the object into a dict
domain_pricing_entry_dict = domain_pricing_entry_instance.to_dict()
# create an instance of DomainPricingEntry from a dict
domain_pricing_entry_from_dict = DomainPricingEntry.from_dict(domain_pricing_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


