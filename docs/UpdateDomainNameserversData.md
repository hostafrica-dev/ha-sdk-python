# UpdateDomainNameserversData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**domain** | **str** | Domain name (FQDN) | [optional] 
**nameservers** | [**DomainNameservers**](DomainNameservers.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.update_domain_nameservers_data import UpdateDomainNameserversData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainNameserversData from a JSON string
update_domain_nameservers_data_instance = UpdateDomainNameserversData.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainNameserversData.to_json())

# convert the object into a dict
update_domain_nameservers_data_dict = update_domain_nameservers_data_instance.to_dict()
# create an instance of UpdateDomainNameserversData from a dict
update_domain_nameservers_data_from_dict = UpdateDomainNameserversData.from_dict(update_domain_nameservers_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


