from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.contrib.auth.decorators import permission_required

from .models import Models
from .forms import ModelsForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView


def forecasts_home(request):
    forecasts = Models.objects.all().order_by('-date')
    paginator = Paginator(forecasts, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'forecasts/forecasts.html', {'forecasts': forecasts, 'page_obj': page_obj})


class ContactListView(ListView):
    paginate_by = 2
    model = Models


class ForecastsDetailViews(DetailView):
    model = Models
    templates_name = 'forecasts/models_detail.html'
    context_object_name = 'forecast'


class ForecastsUpdateViews(UpdateView):
    model = Models
    templates_name = 'forecasts/models_form.html'
    form_class = ModelsForm


class ForecastsDeleteViews(DeleteView):
    model = Models
    success_url = '/forecasts'
    templates_name = 'forecasts/models_confirm_delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ModelsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forecasts_home')
        else:
            error = 'Форма была неверной'

    form = ModelsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'forecasts/create.html', data)





