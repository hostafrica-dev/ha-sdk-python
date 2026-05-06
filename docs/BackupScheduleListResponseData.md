# BackupScheduleListResponseData

Response data for backup schedule list operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**schedules** | [**List[BackupSchedule]**](BackupSchedule.md) | List of backup schedules | 

## Example

```python
from hostafrica_sdk_python.models.backup_schedule_list_response_data import BackupScheduleListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BackupScheduleListResponseData from a JSON string
backup_schedule_list_response_data_instance = BackupScheduleListResponseData.from_json(json)
# print the JSON string representation of the object
print(BackupScheduleListResponseData.to_json())

# convert the object into a dict
backup_schedule_list_response_data_dict = backup_schedule_list_response_data_instance.to_dict()
# create an instance of BackupScheduleListResponseData from a dict
backup_schedule_list_response_data_from_dict = BackupScheduleListResponseData.from_dict(backup_schedule_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


