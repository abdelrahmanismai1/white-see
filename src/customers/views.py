from django.shortcuts import render

from django.db.models import Q
from django.views.generic import ListView

from .models import Customer
# Create your views here.
class CustomerListView(ListView):
    model = Customer
    template_name= "customer/customer_list.html"
    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval)
            query.add(Q(text__icontains=strval), Q.OR)
            customer_list = self.model.objects.filter(query).select_related().order_by('-updated_at')[:10]
        else :
            customer_list = self.model.objects.all().order_by('-updated_at')[:10]

        ctx = {'customer_list' : customer_list, 'search': strval}
        return render(request, self.template_name, ctx)