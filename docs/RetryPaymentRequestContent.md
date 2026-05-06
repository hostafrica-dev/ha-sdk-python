# RetryPaymentRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**order_id** | **int** | The order identifier to retry payment for | 

## Example

```python
from hostafrica_sdk_python.models.retry_payment_request_content import RetryPaymentRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of RetryPaymentRequestContent from a JSON string
retry_payment_request_content_instance = RetryPaymentRequestContent.from_json(json)
# print the JSON string representation of the object
print(RetryPaymentRequestContent.to_json())

# convert the object into a dict
retry_payment_request_content_dict = retry_payment_request_content_instance.to_dict()
# create an instance of RetryPaymentRequestContent from a dict
retry_payment_request_content_from_dict = RetryPaymentRequestContent.from_dict(retry_payment_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


