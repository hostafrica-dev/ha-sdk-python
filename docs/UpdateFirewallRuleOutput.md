# UpdateFirewallRuleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.update_firewall_rule_output import UpdateFirewallRuleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFirewallRuleOutput from a JSON string
update_firewall_rule_output_instance = UpdateFirewallRuleOutput.from_json(json)
# print the JSON string representation of the object
print(UpdateFirewallRuleOutput.to_json())

# convert the object into a dict
update_firewall_rule_output_dict = update_firewall_rule_output_instance.to_dict()
# create an instance of UpdateFirewallRuleOutput from a dict
update_firewall_rule_output_from_dict = UpdateFirewallRuleOutput.from_dict(update_firewall_rule_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


