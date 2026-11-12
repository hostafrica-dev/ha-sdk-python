# DeleteDomainRedirectRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.delete_domain_redirect_request_content import DeleteDomainRedirectRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDomainRedirectRequestContent from a JSON string
delete_domain_redirect_request_content_instance = DeleteDomainRedirectRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteDomainRedirectRequestContent.to_json())

# convert the object into a dict
delete_domain_redirect_request_content_dict = delete_domain_redirect_request_content_instance.to_dict()
# create an instance of DeleteDomainRedirectRequestContent from a dict
delete_domain_redirect_request_content_from_dict = DeleteDomainRedirectRequestContent.from_dict(delete_domain_redirect_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


