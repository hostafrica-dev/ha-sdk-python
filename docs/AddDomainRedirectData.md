# AddDomainRedirectData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**domain** | **str** | Domain name when returned by upstream | [optional] 
**url** | **str** | Redirect target URL when returned by upstream | [optional] 
**type** | **str** | Redirect type when returned by upstream (e.g. 301, 302) | [optional] 

## Example

```python
from ha_sdk_python.models.add_domain_redirect_data import AddDomainRedirectData

# TODO update the JSON string below
json = "{}"
# create an instance of AddDomainRedirectData from a JSON string
add_domain_redirect_data_instance = AddDomainRedirectData.from_json(json)
# print the JSON string representation of the object
print(AddDomainRedirectData.to_json())

# convert the object into a dict
add_domain_redirect_data_dict = add_domain_redirect_data_instance.to_dict()
# create an instance of AddDomainRedirectData from a dict
add_domain_redirect_data_from_dict = AddDomainRedirectData.from_dict(add_domain_redirect_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


