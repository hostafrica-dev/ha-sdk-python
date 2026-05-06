# UpdatePowerTaskOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PowerTaskCreateResponseData**](PowerTaskCreateResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.update_power_task_output import UpdatePowerTaskOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePowerTaskOutput from a JSON string
update_power_task_output_instance = UpdatePowerTaskOutput.from_json(json)
# print the JSON string representation of the object
print(UpdatePowerTaskOutput.to_json())

# convert the object into a dict
update_power_task_output_dict = update_power_task_output_instance.to_dict()
# create an instance of UpdatePowerTaskOutput from a dict
update_power_task_output_from_dict = UpdatePowerTaskOutput.from_dict(update_power_task_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


