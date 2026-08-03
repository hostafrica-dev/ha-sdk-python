# UpdateDomainContactsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**domain_id** | **str** | Domain service id when returned by upstream | [optional] 

## Example

```python
from ha_sdk_python.models.update_domain_contacts_data import UpdateDomainContactsData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainContactsData from a JSON string
update_domain_contacts_data_instance = UpdateDomainContactsData.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainContactsData.to_json())

# convert the object into a dict
update_domain_contacts_data_dict = update_domain_contacts_data_instance.to_dict()
# create an instance of UpdateDomainContactsData from a dict
update_domain_contacts_data_from_dict = UpdateDomainContactsData.from_dict(update_domain_contacts_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


