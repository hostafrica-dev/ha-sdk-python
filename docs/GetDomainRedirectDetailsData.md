# GetDomainRedirectDetailsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**domain_id** | **str** | Domain service id | [optional] 
**domain** | **str** | Domain name | [optional] 
**url** | **str** | Redirect target URL when configured | [optional] 
**type** | **str** | Redirect type when configured | [optional] 
**address** | **str** | Optional redirector address override | [optional] 
**dns** | [**DomainRedirectDnsStatus**](DomainRedirectDnsStatus.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.get_domain_redirect_details_data import GetDomainRedirectDetailsData

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainRedirectDetailsData from a JSON string
get_domain_redirect_details_data_instance = GetDomainRedirectDetailsData.from_json(json)
# print the JSON string representation of the object
print(GetDomainRedirectDetailsData.to_json())

# convert the object into a dict
get_domain_redirect_details_data_dict = get_domain_redirect_details_data_instance.to_dict()
# create an instance of GetDomainRedirectDetailsData from a dict
get_domain_redirect_details_data_from_dict = GetDomainRedirectDetailsData.from_dict(get_domain_redirect_details_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


