# FirewallRule

Firewall rule structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** | SHA1 digest of the rule | 
**pos** | **int** | Position/priority of the rule | 
**type** | **str** | Rule type (in, out) | 
**action** | **str** | Action to perform (ACCEPT, REJECT, DROP) | 
**iface** | **str** | Network interface name | 
**enable** | **int** | Whether the rule is enabled (1&#x3D;enabled, 0&#x3D;disabled) | 
**comment** | **str** | Comment/description for the rule | [optional] 
**source** | **str** | Source address/network | [optional] 
**dest** | **str** | Destination address/network | [optional] 
**proto** | **str** | Protocol (tcp, udp, icmp, etc) | [optional] 
**dport** | **str** | Destination port | [optional] 
**sport** | **str** | Source port | [optional] 
**macro** | **str** | Firewall macro name | [optional] 
**log** | **str** | Log level | [optional] 

## Example

```python
from ha_sdk_python.models.firewall_rule import FirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRule from a JSON string
firewall_rule_instance = FirewallRule.from_json(json)
# print the JSON string representation of the object
print(FirewallRule.to_json())

# convert the object into a dict
firewall_rule_dict = firewall_rule_instance.to_dict()
# create an instance of FirewallRule from a dict
firewall_rule_from_dict = FirewallRule.from_dict(firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


