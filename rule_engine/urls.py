from django.conf.urls import url, include
from .views.ruleViews import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/v1/rule', RuleViewSet ,base_name='rules')


urlpatterns = [
    url(r'^api/v1/filterdata', RuleViewSet.as_view({'post': 'filter_data'}), name='filter_data'),
    url(r'^api/v1/health',  healthcheck_view.as_view()),
    url(r'^', include(router.urls)),
]
