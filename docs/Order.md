# Order

A single order entry in the list orders response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Unique order identifier | 
**order_number** | **str** | Human-readable order reference number | 
**invoice_id** | **int** | Associated invoice identifier | 
**placed_at** | **str** | Timestamp when the order was placed (ISO 8601) | 
**currency** | **str** | ISO currency code (e.g. ZAR) | 
**total** | **str** | Total order amount as a decimal string | 
**balance_due** | **str** | Remaining balance due as a decimal string | 
**invoice_status** | **str** | Invoice status (e.g. Paid, Unpaid) | 
**last_attempt** | [**OrderLastAttempt**](OrderLastAttempt.md) |  | [optional] 
**payment_status** | **str** | Payment status (e.g. paid, pending, failed) | 

## Example

```python
from hostafrica_sdk_python.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


