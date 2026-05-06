# OrderWarning

A warning message in the order response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Warning code | 
**message** | **str** | Human-readable warning message | 

## Example

```python
from hostafrica_sdk_python.models.order_warning import OrderWarning

# TODO update the JSON string below
json = "{}"
# create an instance of OrderWarning from a JSON string
order_warning_instance = OrderWarning.from_json(json)
# print the JSON string representation of the object
print(OrderWarning.to_json())

# convert the object into a dict
order_warning_dict = order_warning_instance.to_dict()
# create an instance of OrderWarning from a dict
order_warning_from_dict = OrderWarning.from_dict(order_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


