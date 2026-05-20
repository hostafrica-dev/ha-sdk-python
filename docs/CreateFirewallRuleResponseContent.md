# CreateFirewallRuleResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.create_firewall_rule_response_content import CreateFirewallRuleResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFirewallRuleResponseContent from a JSON string
create_firewall_rule_response_content_instance = CreateFirewallRuleResponseContent.from_json(json)
# print the JSON string representation of the object
print(CreateFirewallRuleResponseContent.to_json())

# convert the object into a dict
create_firewall_rule_response_content_dict = create_firewall_rule_response_content_instance.to_dict()
# create an instance of CreateFirewallRuleResponseContent from a dict
create_firewall_rule_response_content_from_dict = CreateFirewallRuleResponseContent.from_dict(create_firewall_rule_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


