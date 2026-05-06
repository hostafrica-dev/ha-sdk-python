# PowerTaskCreateResponseData

Response data for power task creation operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**task** | [**PowerTask**](PowerTask.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.power_task_create_response_data import PowerTaskCreateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PowerTaskCreateResponseData from a JSON string
power_task_create_response_data_instance = PowerTaskCreateResponseData.from_json(json)
# print the JSON string representation of the object
print(PowerTaskCreateResponseData.to_json())

# convert the object into a dict
power_task_create_response_data_dict = power_task_create_response_data_instance.to_dict()
# create an instance of PowerTaskCreateResponseData from a dict
power_task_create_response_data_from_dict = PowerTaskCreateResponseData.from_dict(power_task_create_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


