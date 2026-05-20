# CreateOrderResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**CreateOrderResponseData**](CreateOrderResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.create_order_response_content import CreateOrderResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderResponseContent from a JSON string
create_order_response_content_instance = CreateOrderResponseContent.from_json(json)
# print the JSON string representation of the object
print(CreateOrderResponseContent.to_json())

# convert the object into a dict
create_order_response_content_dict = create_order_response_content_instance.to_dict()
# create an instance of CreateOrderResponseContent from a dict
create_order_response_content_from_dict = CreateOrderResponseContent.from_dict(create_order_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


