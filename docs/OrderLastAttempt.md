# OrderLastAttempt

Details of the most recent payment attempt for an order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | Timestamp of the attempt (ISO 8601) | 
**status** | **str** | Attempt status (e.g. paid, failed) | 
**code** | **str** | Error code from the payment provider, if applicable | [optional] 
**message** | **str** | Human-readable message from the payment provider, if applicable | [optional] 

## Example

```python
from ha_sdk_python.models.order_last_attempt import OrderLastAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLastAttempt from a JSON string
order_last_attempt_instance = OrderLastAttempt.from_json(json)
# print the JSON string representation of the object
print(OrderLastAttempt.to_json())

# convert the object into a dict
order_last_attempt_dict = order_last_attempt_instance.to_dict()
# create an instance of OrderLastAttempt from a dict
order_last_attempt_from_dict = OrderLastAttempt.from_dict(order_last_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


