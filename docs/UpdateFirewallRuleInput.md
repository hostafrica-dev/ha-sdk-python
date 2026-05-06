# UpdateFirewallRuleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**pos** | **int** | Position/index of the rule to update | 
**comment** | **str** | Comment/description for the rule | [optional] 
**rule_action** | [**FirewallRuleAction**](FirewallRuleAction.md) |  | [optional] 

## Example

```python
from hostafrica_sdk_python.models.update_firewall_rule_input import UpdateFirewallRuleInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFirewallRuleInput from a JSON string
update_firewall_rule_input_instance = UpdateFirewallRuleInput.from_json(json)
# print the JSON string representation of the object
print(UpdateFirewallRuleInput.to_json())

# convert the object into a dict
update_firewall_rule_input_dict = update_firewall_rule_input_instance.to_dict()
# create an instance of UpdateFirewallRuleInput from a dict
update_firewall_rule_input_from_dict = UpdateFirewallRuleInput.from_dict(update_firewall_rule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


