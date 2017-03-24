from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from cloudmeb.solutions.models import Solution

class SolutionResource(ModelResource):
	solution_categories = fields.ToManyField('cloudmeb.categories.api.CategoryResource', 'solution_categories', full=True, null=True)
	solution_values = fields.ToManyField('cloudmeb.values.api.ValueResource', 'solution_values', full=True, null=True)
	solution_benefits = fields.ToManyField('cloudmeb.benefits.api.BenefitResource', 'solution_benefits', full=True, null=True)

	class Meta:
		queryset = Solution.objects.all().distinct()
		resource_name = 'solution'
		allowed_methods = ['get']
		filtering = {
			'name': ALL,
			'solution_categories': ALL_WITH_RELATIONS,
			'solution_values': ALL_WITH_RELATIONS,
			'solution_benefits': ALL_WITH_RELATIONS,
		}
