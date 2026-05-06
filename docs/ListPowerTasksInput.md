# ListPowerTasksInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.list_power_tasks_input import ListPowerTasksInput

# TODO update the JSON string below
json = "{}"
# create an instance of ListPowerTasksInput from a JSON string
list_power_tasks_input_instance = ListPowerTasksInput.from_json(json)
# print the JSON string representation of the object
print(ListPowerTasksInput.to_json())

# convert the object into a dict
list_power_tasks_input_dict = list_power_tasks_input_instance.to_dict()
# create an instance of ListPowerTasksInput from a dict
list_power_tasks_input_from_dict = ListPowerTasksInput.from_dict(list_power_tasks_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


