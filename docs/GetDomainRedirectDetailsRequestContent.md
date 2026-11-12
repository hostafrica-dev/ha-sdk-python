# GetDomainRedirectDetailsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.get_domain_redirect_details_request_content import GetDomainRedirectDetailsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainRedirectDetailsRequestContent from a JSON string
get_domain_redirect_details_request_content_instance = GetDomainRedirectDetailsRequestContent.from_json(json)
# print the JSON string representation of the object
print(GetDomainRedirectDetailsRequestContent.to_json())

# convert the object into a dict
get_domain_redirect_details_request_content_dict = get_domain_redirect_details_request_content_instance.to_dict()
# create an instance of GetDomainRedirectDetailsRequestContent from a dict
get_domain_redirect_details_request_content_from_dict = GetDomainRedirectDetailsRequestContent.from_dict(get_domain_redirect_details_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


