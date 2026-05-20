# PaymentError

Error detail returned when payment fails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code from the payment provider | 
**message** | **str** | Human-readable error message from the payment provider | 

## Example

```python
from ha_sdk_python.models.payment_error import PaymentError

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentError from a JSON string
payment_error_instance = PaymentError.from_json(json)
# print the JSON string representation of the object
print(PaymentError.to_json())

# convert the object into a dict
payment_error_dict = payment_error_instance.to_dict()
# create an instance of PaymentError from a dict
payment_error_from_dict = PaymentError.from_dict(payment_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


