from django.urls import path, include
from rest_framework import routers
from checker.views import check_news

from . import api
from . import views


router = routers.DefaultRouter()
router.register("source", api.sourceViewSet)
router.register("news", api.newsViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("checker/source/", views.sourceListView.as_view(), name="checker_source_list"),
    path("checker/source/create/", views.sourceCreateView.as_view(), name="checker_source_create"),
    path("checker/source/detail/<int:pk>/", views.sourceDetailView.as_view(), name="checker_source_detail"),
    path("checker/source/update/<int:pk>/", views.sourceUpdateView.as_view(), name="checker_source_update"),
    path("checker/source/delete/<int:pk>/", views.sourceDeleteView.as_view(), name="checker_source_delete"),

    path("checker/source/check/<int:pk>/", check_news, name="check_source_news"),

    path("checker/news/", views.newsListView.as_view(), name="checker_news_list"),
    path("checker/news/create/", views.newsCreateView.as_view(), name="checker_news_create"),
    path("checker/news/detail/<int:pk>/", views.newsDetailView.as_view(), name="checker_news_detail"),
    path("checker/news/update/<int:pk>/", views.newsUpdateView.as_view(), name="checker_news_update"),
    path("checker/news/delete/<int:pk>/", views.newsDeleteView.as_view(), name="checker_news_delete"),
)
