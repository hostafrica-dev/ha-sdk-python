# CreatePowerTaskOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PowerTaskCreateResponseData**](PowerTaskCreateResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_power_task_output import CreatePowerTaskOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePowerTaskOutput from a JSON string
create_power_task_output_instance = CreatePowerTaskOutput.from_json(json)
# print the JSON string representation of the object
print(CreatePowerTaskOutput.to_json())

# convert the object into a dict
create_power_task_output_dict = create_power_task_output_instance.to_dict()
# create an instance of CreatePowerTaskOutput from a dict
create_power_task_output_from_dict = CreatePowerTaskOutput.from_dict(create_power_task_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


