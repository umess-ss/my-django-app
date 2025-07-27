from django_components import Component, register


@register("category_card")
class Category(Component):
    template_file = "category_card.html"

    def get_template_data(self, args, kwargs, slots, context):
        return {
            "category": kwargs["category"]
        }