# AddDomainRedirectResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**AddDomainRedirectData**](AddDomainRedirectData.md) |  | 

## Example

```python
from ha_sdk_python.models.add_domain_redirect_response_content import AddDomainRedirectResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of AddDomainRedirectResponseContent from a JSON string
add_domain_redirect_response_content_instance = AddDomainRedirectResponseContent.from_json(json)
# print the JSON string representation of the object
print(AddDomainRedirectResponseContent.to_json())

# convert the object into a dict
add_domain_redirect_response_content_dict = add_domain_redirect_response_content_instance.to_dict()
# create an instance of AddDomainRedirectResponseContent from a dict
add_domain_redirect_response_content_from_dict = AddDomainRedirectResponseContent.from_dict(add_domain_redirect_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


