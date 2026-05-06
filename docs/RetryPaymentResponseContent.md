# RetryPaymentResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**RetryPaymentResponseData**](RetryPaymentResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.retry_payment_response_content import RetryPaymentResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of RetryPaymentResponseContent from a JSON string
retry_payment_response_content_instance = RetryPaymentResponseContent.from_json(json)
# print the JSON string representation of the object
print(RetryPaymentResponseContent.to_json())

# convert the object into a dict
retry_payment_response_content_dict = retry_payment_response_content_instance.to_dict()
# create an instance of RetryPaymentResponseContent from a dict
retry_payment_response_content_from_dict = RetryPaymentResponseContent.from_dict(retry_payment_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


