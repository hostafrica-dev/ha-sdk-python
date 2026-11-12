# AddDomainRedirectRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 
**url** | **str** | Redirect target URL (absolute http(s) URL) | 
**type** | **str** | Redirect type: 301, 302, permanent, or temporary | 
**address** | **str** | Optional redirector address override (passed through when present) | [optional] 
**override** | **bool** | When true, force-replace conflicting @/www A records that do not point at the redirector | [optional] 

## Example

```python
from ha_sdk_python.models.add_domain_redirect_request_content import AddDomainRedirectRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of AddDomainRedirectRequestContent from a JSON string
add_domain_redirect_request_content_instance = AddDomainRedirectRequestContent.from_json(json)
# print the JSON string representation of the object
print(AddDomainRedirectRequestContent.to_json())

# convert the object into a dict
add_domain_redirect_request_content_dict = add_domain_redirect_request_content_instance.to_dict()
# create an instance of AddDomainRedirectRequestContent from a dict
add_domain_redirect_request_content_from_dict = AddDomainRedirectRequestContent.from_dict(add_domain_redirect_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


