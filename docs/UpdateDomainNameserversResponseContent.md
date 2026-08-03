# UpdateDomainNameserversResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**UpdateDomainNameserversData**](UpdateDomainNameserversData.md) |  | 

## Example

```python
from ha_sdk_python.models.update_domain_nameservers_response_content import UpdateDomainNameserversResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainNameserversResponseContent from a JSON string
update_domain_nameservers_response_content_instance = UpdateDomainNameserversResponseContent.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainNameserversResponseContent.to_json())

# convert the object into a dict
update_domain_nameservers_response_content_dict = update_domain_nameservers_response_content_instance.to_dict()
# create an instance of UpdateDomainNameserversResponseContent from a dict
update_domain_nameservers_response_content_from_dict = UpdateDomainNameserversResponseContent.from_dict(update_domain_nameservers_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


