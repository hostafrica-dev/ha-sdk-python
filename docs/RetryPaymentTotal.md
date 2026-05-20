# RetryPaymentTotal

Total amount breakdown for a retry payment response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Total amount charged | 
**currency** | **str** | Currency code (e.g. USD) | 
**prefix** | **str** | Currency prefix symbol (e.g. US$) | 

## Example

```python
from ha_sdk_python.models.retry_payment_total import RetryPaymentTotal

# TODO update the JSON string below
json = "{}"
# create an instance of RetryPaymentTotal from a JSON string
retry_payment_total_instance = RetryPaymentTotal.from_json(json)
# print the JSON string representation of the object
print(RetryPaymentTotal.to_json())

# convert the object into a dict
retry_payment_total_dict = retry_payment_total_instance.to_dict()
# create an instance of RetryPaymentTotal from a dict
retry_payment_total_from_dict = RetryPaymentTotal.from_dict(retry_payment_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


