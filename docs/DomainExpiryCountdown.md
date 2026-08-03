# DomainExpiryCountdown

Countdown until domain expiry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**years** | **int** |  | 
**months** | **int** |  | 
**days** | **int** |  | 

## Example

```python
from ha_sdk_python.models.domain_expiry_countdown import DomainExpiryCountdown

# TODO update the JSON string below
json = "{}"
# create an instance of DomainExpiryCountdown from a JSON string
domain_expiry_countdown_instance = DomainExpiryCountdown.from_json(json)
# print the JSON string representation of the object
print(DomainExpiryCountdown.to_json())

# convert the object into a dict
domain_expiry_countdown_dict = domain_expiry_countdown_instance.to_dict()
# create an instance of DomainExpiryCountdown from a dict
domain_expiry_countdown_from_dict = DomainExpiryCountdown.from_dict(domain_expiry_countdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


