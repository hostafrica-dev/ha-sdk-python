# UpdateDomainLockStatusResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**UpdateDomainLockStatusData**](UpdateDomainLockStatusData.md) |  | 

## Example

```python
from ha_sdk_python.models.update_domain_lock_status_response_content import UpdateDomainLockStatusResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainLockStatusResponseContent from a JSON string
update_domain_lock_status_response_content_instance = UpdateDomainLockStatusResponseContent.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainLockStatusResponseContent.to_json())

# convert the object into a dict
update_domain_lock_status_response_content_dict = update_domain_lock_status_response_content_instance.to_dict()
# create an instance of UpdateDomainLockStatusResponseContent from a dict
update_domain_lock_status_response_content_from_dict = UpdateDomainLockStatusResponseContent.from_dict(update_domain_lock_status_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


