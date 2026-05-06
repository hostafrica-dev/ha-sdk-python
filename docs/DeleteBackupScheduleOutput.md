# DeleteBackupScheduleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.delete_backup_schedule_output import DeleteBackupScheduleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBackupScheduleOutput from a JSON string
delete_backup_schedule_output_instance = DeleteBackupScheduleOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteBackupScheduleOutput.to_json())

# convert the object into a dict
delete_backup_schedule_output_dict = delete_backup_schedule_output_instance.to_dict()
# create an instance of DeleteBackupScheduleOutput from a dict
delete_backup_schedule_output_from_dict = DeleteBackupScheduleOutput.from_dict(delete_backup_schedule_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


