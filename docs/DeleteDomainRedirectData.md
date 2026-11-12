# DeleteDomainRedirectData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**deleted** | **bool** | True when upstream confirmed deletion | [optional] 
**domain** | **str** | Domain name when returned by upstream | [optional] 

## Example

```python
from ha_sdk_python.models.delete_domain_redirect_data import DeleteDomainRedirectData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDomainRedirectData from a JSON string
delete_domain_redirect_data_instance = DeleteDomainRedirectData.from_json(json)
# print the JSON string representation of the object
print(DeleteDomainRedirectData.to_json())

# convert the object into a dict
delete_domain_redirect_data_dict = delete_domain_redirect_data_instance.to_dict()
# create an instance of DeleteDomainRedirectData from a dict
delete_domain_redirect_data_from_dict = DeleteDomainRedirectData.from_dict(delete_domain_redirect_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


