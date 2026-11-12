# UpdateDomainLockStatusData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**domain** | **str** | Domain name (FQDN) | [optional] 
**lock_status** | **str** | Applied lock state as reported after the update (e.g. locked, unlocked) | [optional] 
**requested_status** | **bool** | Boolean lock value that was requested | [optional] 

## Example

```python
from ha_sdk_python.models.update_domain_lock_status_data import UpdateDomainLockStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainLockStatusData from a JSON string
update_domain_lock_status_data_instance = UpdateDomainLockStatusData.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainLockStatusData.to_json())

# convert the object into a dict
update_domain_lock_status_data_dict = update_domain_lock_status_data_instance.to_dict()
# create an instance of UpdateDomainLockStatusData from a dict
update_domain_lock_status_data_from_dict = UpdateDomainLockStatusData.from_dict(update_domain_lock_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


