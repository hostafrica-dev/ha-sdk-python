# EditBackupScheduleRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**schedule_id** | **str** | Backup schedule ID to edit | 
**starttime** | **str** | Time in HH:MM format (e.g., &#39;03:00&#39;). Hours must be between 00-23, minutes must be between 00-59 | 
**dow** | [**List[DayOfWeek]**](DayOfWeek.md) | Days of week when backup should run | 
**compress** | [**CompressionType**](CompressionType.md) |  | 
**mode** | [**BackupModeType**](BackupModeType.md) |  | 
**mailto** | **bool** | Email notification setting. Set to true to send notifications to client&#39;s email, false or omit to disable | [optional] 

## Example

```python
from ha_sdk_python.models.edit_backup_schedule_request_content import EditBackupScheduleRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of EditBackupScheduleRequestContent from a JSON string
edit_backup_schedule_request_content_instance = EditBackupScheduleRequestContent.from_json(json)
# print the JSON string representation of the object
print(EditBackupScheduleRequestContent.to_json())

# convert the object into a dict
edit_backup_schedule_request_content_dict = edit_backup_schedule_request_content_instance.to_dict()
# create an instance of EditBackupScheduleRequestContent from a dict
edit_backup_schedule_request_content_from_dict = EditBackupScheduleRequestContent.from_dict(edit_backup_schedule_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


