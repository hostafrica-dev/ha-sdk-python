# GetCatalogueInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Optional group identifier to filter catalogue results | [optional] 
**product_id** | **str** | Optional product identifier to filter catalogue results | [optional] 

## Example

```python
from hostafrica_sdk_python.models.get_catalogue_input import GetCatalogueInput

# TODO update the JSON string below
json = "{}"
# create an instance of GetCatalogueInput from a JSON string
get_catalogue_input_instance = GetCatalogueInput.from_json(json)
# print the JSON string representation of the object
print(GetCatalogueInput.to_json())

# convert the object into a dict
get_catalogue_input_dict = get_catalogue_input_instance.to_dict()
# create an instance of GetCatalogueInput from a dict
get_catalogue_input_from_dict = GetCatalogueInput.from_dict(get_catalogue_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


