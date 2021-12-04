from django.shortcuts import get_object_or_404, render,get_list_or_404
from .models import Work
def all_blogs(request):
    # works = Work.objects.all()
    works = Work.objects.order_by('-date')
    return render(request,'blogs/all_blogs.html',{'works':works})


def detail(request,blog_id):
    blog = get_object_or_404(Work,pk=blog_id)
    return render(request,'blogs/detail.html',{'blog':blog})
