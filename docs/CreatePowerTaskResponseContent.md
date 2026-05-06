# CreatePowerTaskResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PowerTaskCreateResponseData**](PowerTaskCreateResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_power_task_response_content import CreatePowerTaskResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePowerTaskResponseContent from a JSON string
create_power_task_response_content_instance = CreatePowerTaskResponseContent.from_json(json)
# print the JSON string representation of the object
print(CreatePowerTaskResponseContent.to_json())

# convert the object into a dict
create_power_task_response_content_dict = create_power_task_response_content_instance.to_dict()
# create an instance of CreatePowerTaskResponseContent from a dict
create_power_task_response_content_from_dict = CreatePowerTaskResponseContent.from_dict(create_power_task_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


