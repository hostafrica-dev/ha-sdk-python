# RetryPaymentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**order_id** | **int** | The order identifier to retry payment for | 

## Example

```python
from hostafrica_sdk_python.models.retry_payment_input import RetryPaymentInput

# TODO update the JSON string below
json = "{}"
# create an instance of RetryPaymentInput from a JSON string
retry_payment_input_instance = RetryPaymentInput.from_json(json)
# print the JSON string representation of the object
print(RetryPaymentInput.to_json())

# convert the object into a dict
retry_payment_input_dict = retry_payment_input_instance.to_dict()
# create an instance of RetryPaymentInput from a dict
retry_payment_input_from_dict = RetryPaymentInput.from_dict(retry_payment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


