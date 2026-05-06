# UpdatePowerTaskResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PowerTaskCreateResponseData**](PowerTaskCreateResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.update_power_task_response_content import UpdatePowerTaskResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePowerTaskResponseContent from a JSON string
update_power_task_response_content_instance = UpdatePowerTaskResponseContent.from_json(json)
# print the JSON string representation of the object
print(UpdatePowerTaskResponseContent.to_json())

# convert the object into a dict
update_power_task_response_content_dict = update_power_task_response_content_instance.to_dict()
# create an instance of UpdatePowerTaskResponseContent from a dict
update_power_task_response_content_from_dict = UpdatePowerTaskResponseContent.from_dict(update_power_task_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


