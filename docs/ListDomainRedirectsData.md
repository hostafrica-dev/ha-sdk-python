# ListDomainRedirectsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**redirects** | [**List[DomainRedirectInfo]**](DomainRedirectInfo.md) |  | 
**limit** | **int** | Pagination limit | [optional] 
**offset** | **int** | Pagination offset | [optional] 

## Example

```python
from ha_sdk_python.models.list_domain_redirects_data import ListDomainRedirectsData

# TODO update the JSON string below
json = "{}"
# create an instance of ListDomainRedirectsData from a JSON string
list_domain_redirects_data_instance = ListDomainRedirectsData.from_json(json)
# print the JSON string representation of the object
print(ListDomainRedirectsData.to_json())

# convert the object into a dict
list_domain_redirects_data_dict = list_domain_redirects_data_instance.to_dict()
# create an instance of ListDomainRedirectsData from a dict
list_domain_redirects_data_from_dict = ListDomainRedirectsData.from_dict(list_domain_redirects_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


