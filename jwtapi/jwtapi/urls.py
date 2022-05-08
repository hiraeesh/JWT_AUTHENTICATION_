
from django.contrib import admin
from django.db import router
from django.urls import path,include
from jwtfirst import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



router=DefaultRouter()
router.register('studentapi', views.StudentModelViewset, basename='student')

# router.register('stuapi',views.StudentModelViewset, basename='stapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),

]
