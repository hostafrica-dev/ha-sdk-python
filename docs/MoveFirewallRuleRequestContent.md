# MoveFirewallRuleRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**pos** | **int** | Current position/index of the rule to move | 
**target_pos** | **int** | Target position/index for the rule (mutually exclusive with direction) | [optional] 
**direction** | [**FirewallMoveDirection**](FirewallMoveDirection.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.move_firewall_rule_request_content import MoveFirewallRuleRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of MoveFirewallRuleRequestContent from a JSON string
move_firewall_rule_request_content_instance = MoveFirewallRuleRequestContent.from_json(json)
# print the JSON string representation of the object
print(MoveFirewallRuleRequestContent.to_json())

# convert the object into a dict
move_firewall_rule_request_content_dict = move_firewall_rule_request_content_instance.to_dict()
# create an instance of MoveFirewallRuleRequestContent from a dict
move_firewall_rule_request_content_from_dict = MoveFirewallRuleRequestContent.from_dict(move_firewall_rule_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


