# ListBackupSchedulesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**BackupScheduleListResponseData**](BackupScheduleListResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_backup_schedules_output import ListBackupSchedulesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListBackupSchedulesOutput from a JSON string
list_backup_schedules_output_instance = ListBackupSchedulesOutput.from_json(json)
# print the JSON string representation of the object
print(ListBackupSchedulesOutput.to_json())

# convert the object into a dict
list_backup_schedules_output_dict = list_backup_schedules_output_instance.to_dict()
# create an instance of ListBackupSchedulesOutput from a dict
list_backup_schedules_output_from_dict = ListBackupSchedulesOutput.from_dict(list_backup_schedules_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


