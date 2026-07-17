# DomainRequiringDataAdditionalField

Additional registrar field required for a pending domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Field key to use when saving additional domain data | 
**displayname** | **str** | Human-readable label for the field | 
**type** | **str** | Input type (e.g. text) | 
**required** | **bool** | Whether the field must be provided | 
**value** | **str** | Current value; empty when not yet supplied | 

## Example

```python
from ha_sdk_python.models.domain_requiring_data_additional_field import DomainRequiringDataAdditionalField

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRequiringDataAdditionalField from a JSON string
domain_requiring_data_additional_field_instance = DomainRequiringDataAdditionalField.from_json(json)
# print the JSON string representation of the object
print(DomainRequiringDataAdditionalField.to_json())

# convert the object into a dict
domain_requiring_data_additional_field_dict = domain_requiring_data_additional_field_instance.to_dict()
# create an instance of DomainRequiringDataAdditionalField from a dict
domain_requiring_data_additional_field_from_dict = DomainRequiringDataAdditionalField.from_dict(domain_requiring_data_additional_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


