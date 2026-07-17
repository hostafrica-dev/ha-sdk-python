# GetDomainResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**GetDomainData**](GetDomainData.md) |  | 

## Example

```python
from ha_sdk_python.models.get_domain_response_content import GetDomainResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainResponseContent from a JSON string
get_domain_response_content_instance = GetDomainResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetDomainResponseContent.to_json())

# convert the object into a dict
get_domain_response_content_dict = get_domain_response_content_instance.to_dict()
# create an instance of GetDomainResponseContent from a dict
get_domain_response_content_from_dict = GetDomainResponseContent.from_dict(get_domain_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


