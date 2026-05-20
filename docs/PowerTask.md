# PowerTask

Individual power task item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Task ID | 
**hosting_id** | **int** | Hosting/service ID | 
**description** | **str** | Task description | [optional] 
**action** | **str** | Power action (start, stop, restart) | 
**start** | **str** | Task start date/time (ISO 8601 format) | 
**end** | **str** | Task end date/time (ISO 8601 format, null if no end) | [optional] 
**job_type** | **str** | Job type (oneTime, daily, weekly) | 
**job_time** | **str** | Job execution time (HH:MM:SS format) | 
**days** | **List[str]** | Days of week for weekly jobs (empty array for oneTime/daily) | 
**last_run** | **str** | Last run timestamp (null if never run) | [optional] 

## Example

```python
from ha_sdk_python.models.power_task import PowerTask

# TODO update the JSON string below
json = "{}"
# create an instance of PowerTask from a JSON string
power_task_instance = PowerTask.from_json(json)
# print the JSON string representation of the object
print(PowerTask.to_json())

# convert the object into a dict
power_task_dict = power_task_instance.to_dict()
# create an instance of PowerTask from a dict
power_task_from_dict = PowerTask.from_dict(power_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


