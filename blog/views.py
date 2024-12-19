from django.shortcuts import render ,get_object_or_404
from .models import Blog
from django.core.paginator import Paginator


# Create your views here.
def blog(request, category=None):
    if category is not None:
        blog = Blog.objects.filter(category__title=category, status=True)
        
    else:
        blog = Blog.objects.all()
        
    blog_paginate = Paginator(blog, 2)
    first_page = 1
    last_page = blog_paginate.num_pages

    try:
        page_number = request.GET.get("page")
        blog = blog_paginate.get_page(page_number)
    except:
        page_number = first_page
        blog = blog_paginate.get_page(first_page)
    
    context = {
        "blogs":blog,
        "first" : first_page,
        "last" : last_page,
        "page_num": int(page_number),
        "page_num_1": int(page_number)-1,
        "page_num_2": int(page_number)-2,
        "page_nump1": int(page_number)+1,
        "page_nump2":int(page_number)+2,
        "last_3": int(last_page)-3,
        "last_2": int(last_page)-2,
        "last_1": int(last_page)-1
    }


    return render(request, 'blog/blog.html', context=context)    

def blog_detail(request ):
   
    return render(request,'blog/blog-details.html' )
