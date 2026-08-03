# ListDnsCreateCandidatesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**candidates** | [**List[DnsCreateCandidateInfo]**](DnsCreateCandidateInfo.md) | Domains and services eligible for new DNS zones | 
**total** | **int** |  | 

## Example

```python
from ha_sdk_python.models.list_dns_create_candidates_data import ListDnsCreateCandidatesData

# TODO update the JSON string below
json = "{}"
# create an instance of ListDnsCreateCandidatesData from a JSON string
list_dns_create_candidates_data_instance = ListDnsCreateCandidatesData.from_json(json)
# print the JSON string representation of the object
print(ListDnsCreateCandidatesData.to_json())

# convert the object into a dict
list_dns_create_candidates_data_dict = list_dns_create_candidates_data_instance.to_dict()
# create an instance of ListDnsCreateCandidatesData from a dict
list_dns_create_candidates_data_from_dict = ListDnsCreateCandidatesData.from_dict(list_dns_create_candidates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


