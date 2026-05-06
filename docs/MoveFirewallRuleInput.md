# MoveFirewallRuleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**pos** | **int** | Current position/index of the rule to move | 
**target_pos** | **int** | Target position/index for the rule (mutually exclusive with direction) | [optional] 
**direction** | [**FirewallMoveDirection**](FirewallMoveDirection.md) |  | [optional] 

## Example

```python
from hostafrica_sdk_python.models.move_firewall_rule_input import MoveFirewallRuleInput

# TODO update the JSON string below
json = "{}"
# create an instance of MoveFirewallRuleInput from a JSON string
move_firewall_rule_input_instance = MoveFirewallRuleInput.from_json(json)
# print the JSON string representation of the object
print(MoveFirewallRuleInput.to_json())

# convert the object into a dict
move_firewall_rule_input_dict = move_firewall_rule_input_instance.to_dict()
# create an instance of MoveFirewallRuleInput from a dict
move_firewall_rule_input_from_dict = MoveFirewallRuleInput.from_dict(move_firewall_rule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


