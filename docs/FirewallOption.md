# FirewallOption

Option structure for interfaces, macros, and protocols

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Option value | 
**label** | **str** | Human-readable label | 

## Example

```python
from ha_sdk_python.models.firewall_option import FirewallOption

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallOption from a JSON string
firewall_option_instance = FirewallOption.from_json(json)
# print the JSON string representation of the object
print(FirewallOption.to_json())

# convert the object into a dict
firewall_option_dict = firewall_option_instance.to_dict()
# create an instance of FirewallOption from a dict
firewall_option_from_dict = FirewallOption.from_dict(firewall_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


