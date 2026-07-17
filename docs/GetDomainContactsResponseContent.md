# GetDomainContactsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**GetDomainContactsData**](GetDomainContactsData.md) |  | 

## Example

```python
from ha_sdk_python.models.get_domain_contacts_response_content import GetDomainContactsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainContactsResponseContent from a JSON string
get_domain_contacts_response_content_instance = GetDomainContactsResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetDomainContactsResponseContent.to_json())

# convert the object into a dict
get_domain_contacts_response_content_dict = get_domain_contacts_response_content_instance.to_dict()
# create an instance of GetDomainContactsResponseContent from a dict
get_domain_contacts_response_content_from_dict = GetDomainContactsResponseContent.from_dict(get_domain_contacts_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


