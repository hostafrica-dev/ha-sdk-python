# CreateOrderTotal

Total amount breakdown for an order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Total amount charged (decimal string, e.g. \&quot;2333.33\&quot;) | 
**currency** | **str** | Currency code (e.g. USD) | 
**prefix** | **str** | Currency prefix symbol (e.g. $) | 

## Example

```python
from ha_sdk_python.models.create_order_total import CreateOrderTotal

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderTotal from a JSON string
create_order_total_instance = CreateOrderTotal.from_json(json)
# print the JSON string representation of the object
print(CreateOrderTotal.to_json())

# convert the object into a dict
create_order_total_dict = create_order_total_instance.to_dict()
# create an instance of CreateOrderTotal from a dict
create_order_total_from_dict = CreateOrderTotal.from_dict(create_order_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


