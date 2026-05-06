# CreateOrderOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**CreateOrderResponseData**](CreateOrderResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_order_output import CreateOrderOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderOutput from a JSON string
create_order_output_instance = CreateOrderOutput.from_json(json)
# print the JSON string representation of the object
print(CreateOrderOutput.to_json())

# convert the object into a dict
create_order_output_dict = create_order_output_instance.to_dict()
# create an instance of CreateOrderOutput from a dict
create_order_output_from_dict = CreateOrderOutput.from_dict(create_order_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


