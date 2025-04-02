import django_filters
from .models import Job
class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['title','description','job_type','experince','category']
        # exclude = [
        #     'owner','published_at','image','salary','vacancy','slug'
        # ]