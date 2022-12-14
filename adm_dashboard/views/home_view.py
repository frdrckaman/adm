from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = f"adm_dashboard/bootstrap/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context.update(
        # )
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

