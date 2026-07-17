# DomainRequiringDataInfo

Pending domain requiring additional registrar or contact data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id | 
**domain** | **str** | Fully qualified domain name | 
**status** | **str** | Domain status (e.g. Pending) | 
**domain_type** | **str** | Domain operation type (e.g. Register) | 
**tld** | **str** | Top-level domain suffix (e.g. .co.za) | 
**additional_fields** | [**List[DomainRequiringDataAdditionalField]**](DomainRequiringDataAdditionalField.md) | Additional registrar fields required for this TLD | 

## Example

```python
from ha_sdk_python.models.domain_requiring_data_info import DomainRequiringDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRequiringDataInfo from a JSON string
domain_requiring_data_info_instance = DomainRequiringDataInfo.from_json(json)
# print the JSON string representation of the object
print(DomainRequiringDataInfo.to_json())

# convert the object into a dict
domain_requiring_data_info_dict = domain_requiring_data_info_instance.to_dict()
# create an instance of DomainRequiringDataInfo from a dict
domain_requiring_data_info_from_dict = DomainRequiringDataInfo.from_dict(domain_requiring_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


