# CreateOrderItems

Line items grouped by type in the order response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[CreateOrderProductItem]**](CreateOrderProductItem.md) | Product line items in the order | [optional] 
**domains** | [**List[CreateOrderDomainItem]**](CreateOrderDomainItem.md) | Domain line items in the order | [optional] 

## Example

```python
from hostafrica_sdk_python.models.create_order_items import CreateOrderItems

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderItems from a JSON string
create_order_items_instance = CreateOrderItems.from_json(json)
# print the JSON string representation of the object
print(CreateOrderItems.to_json())

# convert the object into a dict
create_order_items_dict = create_order_items_instance.to_dict()
# create an instance of CreateOrderItems from a dict
create_order_items_from_dict = CreateOrderItems.from_dict(create_order_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


