# CreateBackupScheduleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_backup_schedule_output import CreateBackupScheduleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBackupScheduleOutput from a JSON string
create_backup_schedule_output_instance = CreateBackupScheduleOutput.from_json(json)
# print the JSON string representation of the object
print(CreateBackupScheduleOutput.to_json())

# convert the object into a dict
create_backup_schedule_output_dict = create_backup_schedule_output_instance.to_dict()
# create an instance of CreateBackupScheduleOutput from a dict
create_backup_schedule_output_from_dict = CreateBackupScheduleOutput.from_dict(create_backup_schedule_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


