# DomainRedirectInfo

A configured domain HTTP redirect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id | [optional] 
**domain** | **str** | Domain name | [optional] 
**url** | **str** | Redirect target URL | [optional] 
**type** | **str** | Redirect type (e.g. 301, 302, permanent, temporary) | [optional] 
**address** | **str** | Optional redirector address override | [optional] 

## Example

```python
from ha_sdk_python.models.domain_redirect_info import DomainRedirectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRedirectInfo from a JSON string
domain_redirect_info_instance = DomainRedirectInfo.from_json(json)
# print the JSON string representation of the object
print(DomainRedirectInfo.to_json())

# convert the object into a dict
domain_redirect_info_dict = domain_redirect_info_instance.to_dict()
# create an instance of DomainRedirectInfo from a dict
domain_redirect_info_from_dict = DomainRedirectInfo.from_dict(domain_redirect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


