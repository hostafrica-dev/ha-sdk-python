# ListPowerTasksRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.list_power_tasks_request_content import ListPowerTasksRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListPowerTasksRequestContent from a JSON string
list_power_tasks_request_content_instance = ListPowerTasksRequestContent.from_json(json)
# print the JSON string representation of the object
print(ListPowerTasksRequestContent.to_json())

# convert the object into a dict
list_power_tasks_request_content_dict = list_power_tasks_request_content_instance.to_dict()
# create an instance of ListPowerTasksRequestContent from a dict
list_power_tasks_request_content_from_dict = ListPowerTasksRequestContent.from_dict(list_power_tasks_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


