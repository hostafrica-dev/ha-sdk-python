# ListPowerTasksOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PowerTaskListResponseData**](PowerTaskListResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_power_tasks_output import ListPowerTasksOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListPowerTasksOutput from a JSON string
list_power_tasks_output_instance = ListPowerTasksOutput.from_json(json)
# print the JSON string representation of the object
print(ListPowerTasksOutput.to_json())

# convert the object into a dict
list_power_tasks_output_dict = list_power_tasks_output_instance.to_dict()
# create an instance of ListPowerTasksOutput from a dict
list_power_tasks_output_from_dict = ListPowerTasksOutput.from_dict(list_power_tasks_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


