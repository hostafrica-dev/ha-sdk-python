# ListDomainsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListDomainsData**](ListDomainsData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_domains_response_content import ListDomainsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListDomainsResponseContent from a JSON string
list_domains_response_content_instance = ListDomainsResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListDomainsResponseContent.to_json())

# convert the object into a dict
list_domains_response_content_dict = list_domains_response_content_instance.to_dict()
# create an instance of ListDomainsResponseContent from a dict
list_domains_response_content_from_dict = ListDomainsResponseContent.from_dict(list_domains_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


