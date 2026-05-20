# DeleteBackupScheduleRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**schedule_id** | **str** | Backup schedule ID to delete | 

## Example

```python
from ha_sdk_python.models.delete_backup_schedule_request_content import DeleteBackupScheduleRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBackupScheduleRequestContent from a JSON string
delete_backup_schedule_request_content_instance = DeleteBackupScheduleRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteBackupScheduleRequestContent.to_json())

# convert the object into a dict
delete_backup_schedule_request_content_dict = delete_backup_schedule_request_content_instance.to_dict()
# create an instance of DeleteBackupScheduleRequestContent from a dict
delete_backup_schedule_request_content_from_dict = DeleteBackupScheduleRequestContent.from_dict(delete_backup_schedule_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


