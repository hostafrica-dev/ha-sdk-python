# ListPowerTasksResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PowerTaskListResponseData**](PowerTaskListResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_power_tasks_response_content import ListPowerTasksResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListPowerTasksResponseContent from a JSON string
list_power_tasks_response_content_instance = ListPowerTasksResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListPowerTasksResponseContent.to_json())

# convert the object into a dict
list_power_tasks_response_content_dict = list_power_tasks_response_content_instance.to_dict()
# create an instance of ListPowerTasksResponseContent from a dict
list_power_tasks_response_content_from_dict = ListPowerTasksResponseContent.from_dict(list_power_tasks_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


