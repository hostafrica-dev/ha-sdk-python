# MoveFirewallRuleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**FirewallMoveResponseData**](FirewallMoveResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.move_firewall_rule_output import MoveFirewallRuleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of MoveFirewallRuleOutput from a JSON string
move_firewall_rule_output_instance = MoveFirewallRuleOutput.from_json(json)
# print the JSON string representation of the object
print(MoveFirewallRuleOutput.to_json())

# convert the object into a dict
move_firewall_rule_output_dict = move_firewall_rule_output_instance.to_dict()
# create an instance of MoveFirewallRuleOutput from a dict
move_firewall_rule_output_from_dict = MoveFirewallRuleOutput.from_dict(move_firewall_rule_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


