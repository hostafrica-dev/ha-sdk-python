# ListOrdersOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListOrdersResponseData**](ListOrdersResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_orders_output import ListOrdersOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrdersOutput from a JSON string
list_orders_output_instance = ListOrdersOutput.from_json(json)
# print the JSON string representation of the object
print(ListOrdersOutput.to_json())

# convert the object into a dict
list_orders_output_dict = list_orders_output_instance.to_dict()
# create an instance of ListOrdersOutput from a dict
list_orders_output_from_dict = ListOrdersOutput.from_dict(list_orders_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


