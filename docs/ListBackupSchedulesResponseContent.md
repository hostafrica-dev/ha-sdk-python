# ListBackupSchedulesResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**BackupScheduleListResponseData**](BackupScheduleListResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_backup_schedules_response_content import ListBackupSchedulesResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListBackupSchedulesResponseContent from a JSON string
list_backup_schedules_response_content_instance = ListBackupSchedulesResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListBackupSchedulesResponseContent.to_json())

# convert the object into a dict
list_backup_schedules_response_content_dict = list_backup_schedules_response_content_instance.to_dict()
# create an instance of ListBackupSchedulesResponseContent from a dict
list_backup_schedules_response_content_from_dict = ListBackupSchedulesResponseContent.from_dict(list_backup_schedules_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


