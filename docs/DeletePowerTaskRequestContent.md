# DeletePowerTaskRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**task_id** | **int** | Power task ID to delete | 

## Example

```python
from hostafrica_sdk_python.models.delete_power_task_request_content import DeletePowerTaskRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePowerTaskRequestContent from a JSON string
delete_power_task_request_content_instance = DeletePowerTaskRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeletePowerTaskRequestContent.to_json())

# convert the object into a dict
delete_power_task_request_content_dict = delete_power_task_request_content_instance.to_dict()
# create an instance of DeletePowerTaskRequestContent from a dict
delete_power_task_request_content_from_dict = DeletePowerTaskRequestContent.from_dict(delete_power_task_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


