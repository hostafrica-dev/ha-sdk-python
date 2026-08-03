# ListDnsCreateCandidatesResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListDnsCreateCandidatesData**](ListDnsCreateCandidatesData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_dns_create_candidates_response_content import ListDnsCreateCandidatesResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListDnsCreateCandidatesResponseContent from a JSON string
list_dns_create_candidates_response_content_instance = ListDnsCreateCandidatesResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListDnsCreateCandidatesResponseContent.to_json())

# convert the object into a dict
list_dns_create_candidates_response_content_dict = list_dns_create_candidates_response_content_instance.to_dict()
# create an instance of ListDnsCreateCandidatesResponseContent from a dict
list_dns_create_candidates_response_content_from_dict = ListDnsCreateCandidatesResponseContent.from_dict(list_dns_create_candidates_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


