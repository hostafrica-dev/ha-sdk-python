# BackupSchedule

Individual backup schedule item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Schedule ID | 
**starttime** | **str** | Start time for backup (HH:MM format) | 
**dow** | **str** | Days of week (comma-separated) | 
**compress** | [**CompressionType**](CompressionType.md) |  | 
**mode** | **str** | Backup mode | 
**mailto** | **str** | Email address for notifications (null if not set) | [optional] 

## Example

```python
from hostafrica_sdk_python.models.backup_schedule import BackupSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of BackupSchedule from a JSON string
backup_schedule_instance = BackupSchedule.from_json(json)
# print the JSON string representation of the object
print(BackupSchedule.to_json())

# convert the object into a dict
backup_schedule_dict = backup_schedule_instance.to_dict()
# create an instance of BackupSchedule from a dict
backup_schedule_from_dict = BackupSchedule.from_dict(backup_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


