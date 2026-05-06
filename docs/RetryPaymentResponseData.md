# RetryPaymentResponseData

Response data for a retry payment operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order identifier | 
**invoice_id** | **int** | Invoice identifier for this order | 
**total** | [**RetryPaymentTotal**](RetryPaymentTotal.md) |  | 
**payment_status** | [**PaymentStatus**](PaymentStatus.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.retry_payment_response_data import RetryPaymentResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RetryPaymentResponseData from a JSON string
retry_payment_response_data_instance = RetryPaymentResponseData.from_json(json)
# print the JSON string representation of the object
print(RetryPaymentResponseData.to_json())

# convert the object into a dict
retry_payment_response_data_dict = retry_payment_response_data_instance.to_dict()
# create an instance of RetryPaymentResponseData from a dict
retry_payment_response_data_from_dict = RetryPaymentResponseData.from_dict(retry_payment_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


