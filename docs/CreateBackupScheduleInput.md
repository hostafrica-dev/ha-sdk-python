# CreateBackupScheduleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**starttime** | **str** | Time in HH:MM format (e.g., &#39;03:00&#39;). Hours must be between 00-23, minutes must be between 00-59 | 
**dow** | **List[str]** | Days of week when backup should run. Valid values: mon, tue, wed, thu, fri, sat, sun. Provide as an array of day names. | 
**compress** | [**CompressionType**](CompressionType.md) |  | 
**mode** | **str** | Backup mode. Valid values: &#39;snapshot&#39;, &#39;suspend&#39;, &#39;stop&#39; | 
**mailto** | **bool** | Email notification setting. Set to true to send notifications to client&#39;s email, false or omit to disable | [optional] 

## Example

```python
from hostafrica_sdk_python.models.create_backup_schedule_input import CreateBackupScheduleInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBackupScheduleInput from a JSON string
create_backup_schedule_input_instance = CreateBackupScheduleInput.from_json(json)
# print the JSON string representation of the object
print(CreateBackupScheduleInput.to_json())

# convert the object into a dict
create_backup_schedule_input_dict = create_backup_schedule_input_instance.to_dict()
# create an instance of CreateBackupScheduleInput from a dict
create_backup_schedule_input_from_dict = CreateBackupScheduleInput.from_dict(create_backup_schedule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


