# UpdateDomainContactsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 
**contacts** | [**DomainContactUpdates**](DomainContactUpdates.md) |  | 

## Example

```python
from ha_sdk_python.models.update_domain_contacts_request_content import UpdateDomainContactsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainContactsRequestContent from a JSON string
update_domain_contacts_request_content_instance = UpdateDomainContactsRequestContent.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainContactsRequestContent.to_json())

# convert the object into a dict
update_domain_contacts_request_content_dict = update_domain_contacts_request_content_instance.to_dict()
# create an instance of UpdateDomainContactsRequestContent from a dict
update_domain_contacts_request_content_from_dict = UpdateDomainContactsRequestContent.from_dict(update_domain_contacts_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


