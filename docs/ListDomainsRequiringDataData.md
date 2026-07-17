# ListDomainsRequiringDataData

Domains requiring additional registrar or contact data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**domains** | [**List[DomainRequiringDataInfo]**](DomainRequiringDataInfo.md) | Pending domains needing additional registrar or contact data | 
**total_count** | **int** | Count of domains returned | 
**requires_additional_fields** | **bool** | True when any domain has missing required fields | 

## Example

```python
from ha_sdk_python.models.list_domains_requiring_data_data import ListDomainsRequiringDataData

# TODO update the JSON string below
json = "{}"
# create an instance of ListDomainsRequiringDataData from a JSON string
list_domains_requiring_data_data_instance = ListDomainsRequiringDataData.from_json(json)
# print the JSON string representation of the object
print(ListDomainsRequiringDataData.to_json())

# convert the object into a dict
list_domains_requiring_data_data_dict = list_domains_requiring_data_data_instance.to_dict()
# create an instance of ListDomainsRequiringDataData from a dict
list_domains_requiring_data_data_from_dict = ListDomainsRequiringDataData.from_dict(list_domains_requiring_data_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


