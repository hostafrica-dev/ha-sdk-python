# CreateBackupScheduleRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**starttime** | **str** | Time in HH:MM format (e.g., &#39;03:00&#39;). Hours must be between 00-23, minutes must be between 00-59 | 
**dow** | [**List[DayOfWeek]**](DayOfWeek.md) | Days of week when backup should run | 
**compress** | [**CompressionType**](CompressionType.md) |  | 
**mode** | [**BackupModeType**](BackupModeType.md) |  | 
**mailto** | **bool** | Email notification setting. Set to true to send notifications to client&#39;s email, false or omit to disable | [optional] 

## Example

```python
from ha_sdk_python.models.create_backup_schedule_request_content import CreateBackupScheduleRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBackupScheduleRequestContent from a JSON string
create_backup_schedule_request_content_instance = CreateBackupScheduleRequestContent.from_json(json)
# print the JSON string representation of the object
print(CreateBackupScheduleRequestContent.to_json())

# convert the object into a dict
create_backup_schedule_request_content_dict = create_backup_schedule_request_content_instance.to_dict()
# create an instance of CreateBackupScheduleRequestContent from a dict
create_backup_schedule_request_content_from_dict = CreateBackupScheduleRequestContent.from_dict(create_backup_schedule_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


