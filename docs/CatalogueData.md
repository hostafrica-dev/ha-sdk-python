# CatalogueData

Top-level data payload for the GetCatalogue response. When product_id is specified, product is populated instead of groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**CatalogueCurrency**](CatalogueCurrency.md) |  | 
**groups** | [**List[CatalogueGroup]**](CatalogueGroup.md) | Product groups with nested products, plans, and config options. Present when no product_id filter is applied. | [optional] 
**product** | [**CatalogueProduct**](CatalogueProduct.md) |  | [optional] 

## Example

```python
from hostafrica_sdk_python.models.catalogue_data import CatalogueData

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueData from a JSON string
catalogue_data_instance = CatalogueData.from_json(json)
# print the JSON string representation of the object
print(CatalogueData.to_json())

# convert the object into a dict
catalogue_data_dict = catalogue_data_instance.to_dict()
# create an instance of CatalogueData from a dict
catalogue_data_from_dict = CatalogueData.from_dict(catalogue_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


