# CreateFirewallRuleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_firewall_rule_output import CreateFirewallRuleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallRuleOutput from a JSON string
create_firewall_rule_output_instance = CreateFirewallRuleOutput.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallRuleOutput.to_json())

# convert the object into a dict
create_firewall_rule_output_dict = create_firewall_rule_output_instance.to_dict()
# create an instance of CreateFirewallRuleOutput from a dict
create_firewall_rule_output_from_dict = CreateFirewallRuleOutput.from_dict(create_firewall_rule_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


