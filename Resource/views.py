# coding: utf-8


# class MainView(TemplateView):
#     template_name = 'list_resource.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MainView, self).get_context_data(**kwargs)
#         context.update({
#             'Resource': Resource.objects.all(),
#             'Need':Need.objects.all(),
#         })
#         return context
#
# class ResourceListView(ListView):
#     template_name = 'list_resource.html'
#     model = Resource
#     context_object_name = 'Resource'
#
# class ResourceDetailView(DetailView):
#     template_name = 'view_resource.html'
#     model = Resource
#     context_object_name = 'Resource'
#
# class ResourceCreateView(CreateView):
#     template_name = 'create_resource.html'
#     model = Resource
#     context_object_name = 'Resource'
#     fields = ('name', 'weight', 'volume','count',)
#     success_url = reverse_lazy('create_resource')
# #///////////////////////////////$NEED$//////////////////////////////////////////////////////////////////////////////////
# class NeedListView(ListView):
#     template_name = 'list_need.html'
#     model = Need
#     context_object_name = 'Need'
#
# class NeedDetailView(DetailView):
#     template_name = 'view_need.html'
#     model = Need
#     context_object_name = 'Need'
#
# class NeedCreateView(CreateView):
#     template_name = 'create_need.html'
#     model = Need
#     context_object_name = 'Need'
#     fields = ('id_resource', 'number_of_resource', 'priority','perfomance',)
#     success_url = reverse_lazy('create_need')
# #/////////////////////////////////////$PointOfConsuming$////////////////////////////////////////////////////////////////////
#
# class MainView(TemplateView):
#     template_name = 'list_pointofconsuming.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MainView, self).get_context_data(**kwargs)
#         context.update({
#             'PointOfConsuming':PointOfConsuming.objects.all(),
#         })
#         return context
#
# class PointOfConsumingListView(ListView):
#     template_name = 'list_pointofconsuming.html'
#     model =  PointOfConsuming
#     context_object_name = 'PointOfConsuming'
#
# class PointOfConsumingDetailView(DetailView):
#     template_name = 'view_pointofconsuming.html'
#     model = PointOfConsuming
#     context_object_name = 'PointOfConsuming'
#
# class PointOfConsumingCreateView(CreateView):
#     template_name = 'create_pointofconsuming.html'
#     model = PointOfConsuming
#     context_object_name = 'PointOfConsuming'
#     fields = ('id_geography_point','fio','telephone',)
#     success_url = reverse_lazy('create_pointofconsuming')

