from django.views import generic
from .models import Animal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


# Create your views here.
class index_view(generic.ListView):
    template_name = 'animal/index.html'
    context_object_name = 'animals'
    paginate_by = 5

    def post_list(self, kwargs):
        context = super(Animal, self).get_context_data(kwargs)
        paginator = Paginator(Animal, 1)
        page = self.request.GET.get('page')

        try:
            file_animals = paginator.page(page)
        except PageNotAnInteger:
            file_animals = paginator.page(1)
        except EmptyPage:
            file_animals = paginator.page(paginator.num_pages)

        context['animal'] = file_animals
        return context


    def get_queryset(self):
        animals = Animal.objects.all()

        search_query = self.request.GET.get('search-query', False)

        if not search_query:
            return animals

        return animals.filter(name__contains=search_query)


class CreateAnimalView(generic.CreateView):
    model = Animal
    fields = ['name', 'color', 'type']

#class detail_view(generic.DetailView):
    #model = Animal
    #template_name = 'animal/detail.html'

#class create_animal(CreateView):
    #model = Animal
    #fields = ['name', 'color', 'type']

class UpdateAnimal(UpdateView):
    model = Animal
    fields = ['name', 'color', 'type']

class DeleteAnimal(DeleteView):
    model = Animal
    success_url = reverse_lazy('animal:index')

