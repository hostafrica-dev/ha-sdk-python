# GetDomainData

Response data for get-domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**domain** | [**DomainInfo**](DomainInfo.md) |  | 

## Example

```python
from ha_sdk_python.models.get_domain_data import GetDomainData

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainData from a JSON string
get_domain_data_instance = GetDomainData.from_json(json)
# print the JSON string representation of the object
print(GetDomainData.to_json())

# convert the object into a dict
get_domain_data_dict = get_domain_data_instance.to_dict()
# create an instance of GetDomainData from a dict
get_domain_data_from_dict = GetDomainData.from_dict(get_domain_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


