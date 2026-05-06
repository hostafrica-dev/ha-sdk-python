# CreatePowerTaskInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**power_task_action** | **str** | Power action to perform (start, stop, restart) | 
**start_date** | **str** | Start date in Y-m-d format (e.g., 2026-03-25) | 
**description** | **str** | Description of the power task | [optional] 
**start_time** | **str** | Start time in HH:MM or HH:MM:SS format | [optional] 
**end_date** | **str** | End date in Y-m-d format (e.g., 2026-12-31) | [optional] 
**end_time** | **str** | End time in HH:MM or HH:MM:SS format | [optional] 
**job_type** | **str** | Job type: oneTime, daily, or weekly | [optional] 
**job_time** | **str** | Job execution time in HH:MM or HH:MM:SS format | [optional] 
**job_hour** | **int** | Job hour (alternative to job_time) | [optional] 
**job_minutes** | **int** | Job minutes (alternative to job_time) | [optional] 
**days** | **List[str]** | Days of the week for weekly jobs (array of mon, tue, wed, thu, fri, sat, sun) | [optional] 

## Example

```python
from hostafrica_sdk_python.models.create_power_task_input import CreatePowerTaskInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePowerTaskInput from a JSON string
create_power_task_input_instance = CreatePowerTaskInput.from_json(json)
# print the JSON string representation of the object
print(CreatePowerTaskInput.to_json())

# convert the object into a dict
create_power_task_input_dict = create_power_task_input_instance.to_dict()
# create an instance of CreatePowerTaskInput from a dict
create_power_task_input_from_dict = CreatePowerTaskInput.from_dict(create_power_task_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


