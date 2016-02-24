
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'detector/index.html'
    #context_object_name = 'latest_question_list'

class SearchView(generic.TemplateView):
    template_name = 'detector/search.html'
    #context_object_name = 'latest_question_list'
