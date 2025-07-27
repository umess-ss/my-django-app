from django_components import Component, register


@register("post_card")
class PostCard(Component):
    template_file = "post_card.html"

    def get_template_data(self, args, kwargs, slots, context):
        return {
            "post": kwargs["post"]
        }