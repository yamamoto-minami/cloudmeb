from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from cloudmeb.categories.models import Category

class CategoryResource(ModelResource):

	class Meta:
		queryset = Category.objects.all().distinct()
		resource_name = 'category'
		allowed_methods = ['get']
		filtering = {
			'name': ALL,
		}
