# MoveFirewallRuleResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**FirewallMoveResponseData**](FirewallMoveResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.move_firewall_rule_response_content import MoveFirewallRuleResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of MoveFirewallRuleResponseContent from a JSON string
move_firewall_rule_response_content_instance = MoveFirewallRuleResponseContent.from_json(json)
# print the JSON string representation of the object
print(MoveFirewallRuleResponseContent.to_json())

# convert the object into a dict
move_firewall_rule_response_content_dict = move_firewall_rule_response_content_instance.to_dict()
# create an instance of MoveFirewallRuleResponseContent from a dict
move_firewall_rule_response_content_from_dict = MoveFirewallRuleResponseContent.from_dict(move_firewall_rule_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


