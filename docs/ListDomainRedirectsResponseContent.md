# ListDomainRedirectsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListDomainRedirectsData**](ListDomainRedirectsData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_domain_redirects_response_content import ListDomainRedirectsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListDomainRedirectsResponseContent from a JSON string
list_domain_redirects_response_content_instance = ListDomainRedirectsResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListDomainRedirectsResponseContent.to_json())

# convert the object into a dict
list_domain_redirects_response_content_dict = list_domain_redirects_response_content_instance.to_dict()
# create an instance of ListDomainRedirectsResponseContent from a dict
list_domain_redirects_response_content_from_dict = ListDomainRedirectsResponseContent.from_dict(list_domain_redirects_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


