# PowerTaskListResponseData

Response data for power task list operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**tasks** | [**List[PowerTask]**](PowerTask.md) | List of power tasks | 
**available_actions** | **List[str]** | Available power actions | 
**available_job_types** | **List[str]** | Available job types | 
**dialog_rules** | [**PowerTaskDialogRules**](PowerTaskDialogRules.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.power_task_list_response_data import PowerTaskListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PowerTaskListResponseData from a JSON string
power_task_list_response_data_instance = PowerTaskListResponseData.from_json(json)
# print the JSON string representation of the object
print(PowerTaskListResponseData.to_json())

# convert the object into a dict
power_task_list_response_data_dict = power_task_list_response_data_instance.to_dict()
# create an instance of PowerTaskListResponseData from a dict
power_task_list_response_data_from_dict = PowerTaskListResponseData.from_dict(power_task_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


