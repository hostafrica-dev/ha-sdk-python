# DeleteDomainRedirectResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**DeleteDomainRedirectData**](DeleteDomainRedirectData.md) |  | 

## Example

```python
from ha_sdk_python.models.delete_domain_redirect_response_content import DeleteDomainRedirectResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDomainRedirectResponseContent from a JSON string
delete_domain_redirect_response_content_instance = DeleteDomainRedirectResponseContent.from_json(json)
# print the JSON string representation of the object
print(DeleteDomainRedirectResponseContent.to_json())

# convert the object into a dict
delete_domain_redirect_response_content_dict = delete_domain_redirect_response_content_instance.to_dict()
# create an instance of DeleteDomainRedirectResponseContent from a dict
delete_domain_redirect_response_content_from_dict = DeleteDomainRedirectResponseContent.from_dict(delete_domain_redirect_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


