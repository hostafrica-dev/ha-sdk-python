# RetryPaymentOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**RetryPaymentResponseData**](RetryPaymentResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.retry_payment_output import RetryPaymentOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RetryPaymentOutput from a JSON string
retry_payment_output_instance = RetryPaymentOutput.from_json(json)
# print the JSON string representation of the object
print(RetryPaymentOutput.to_json())

# convert the object into a dict
retry_payment_output_dict = retry_payment_output_instance.to_dict()
# create an instance of RetryPaymentOutput from a dict
retry_payment_output_from_dict = RetryPaymentOutput.from_dict(retry_payment_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


