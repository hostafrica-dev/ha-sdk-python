# CreateOrderResponseData

Response data for a successful or pending order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order identifier | 
**invoice_id** | **int** | Invoice identifier for this order | 
**order_number** | **str** | Human-readable order reference number | 
**total** | [**CreateOrderTotal**](CreateOrderTotal.md) |  | 
**promo_applied** | **str** | Promotional code that was applied | [optional] 
**payment_method** | **str** | Payment method used (e.g. stripe) | 
**payment_status** | [**PaymentStatus**](PaymentStatus.md) |  | 
**items** | [**CreateOrderItems**](CreateOrderItems.md) |  | 
**payment_error** | [**PaymentError**](PaymentError.md) |  | [optional] 
**warnings** | [**List[OrderWarning]**](OrderWarning.md) | Warnings present when non-critical issues occurred (e.g. autorenew deferred) | [optional] 

## Example

```python
from hostafrica_sdk_python.models.create_order_response_data import CreateOrderResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderResponseData from a JSON string
create_order_response_data_instance = CreateOrderResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateOrderResponseData.to_json())

# convert the object into a dict
create_order_response_data_dict = create_order_response_data_instance.to_dict()
# create an instance of CreateOrderResponseData from a dict
create_order_response_data_from_dict = CreateOrderResponseData.from_dict(create_order_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


