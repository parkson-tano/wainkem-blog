from .models import Category, Post, ContactUs
from django.db.models import Q

def category_renderer(request):
    return {
        'all_categories': Category.objects.all(),
        'popular_foot':  Post.objects.filter(
            status='published').order_by('view_count')[:3],
        'trend' : Post.objects.filter(
            Q(status='published') & Q(view_count__gte=10))[:7],
        'contactus' : ContactUs.objects.get(id=1)
    }
