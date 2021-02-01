"""TestTrainer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from questions import views as question_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )

router = routers.DefaultRouter()
router.register(r'questions', question_views.QuestionViewSet)
router.register(r'options', question_views.OptionViewSet)
router.register(r'groups', question_views.GroupViewSet)
router.register(r'category', question_views.CategoryViewSet)
# router.register(r'questionn', question_views.QuestionnaireViewSet)
# router.register(r'reviewset', question_views.ReviewViewSet)
# router.register(r'dashboard', question_views.DahboardViewSet)
router.register(r'flipcard', question_views.FlipcardViewSet)
router.register(r'userset', question_views.UserViewSet)
# router.register(r'userdata', question_views.userdata)
# router.register(r'answewr', question_views.QuestionAnswerViewSet)
# router.register(r'groups', question_views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('admin/doc/', include('django.contrib.admindocs.urls')),
                  path('api/', include(router.urls)),
                  path('api/memos/', question_views.memo_add),
                  path('api/userinfo/', question_views.userdata, name='userdata' ),
                  path('api/answer/', question_views.answer_add),
                  path('api/review/', question_views.review),
                  path('api/dashboarddata/', question_views.dashboard),
                  path('api/questionnaiere/', question_views.practice_test),
                  path('api/heatmap/', question_views.heatmap),
                  path('api/realtest/', question_views.real_test),
                  path('api/handin/', question_views.practice_hand_in),
                  path('api/prefs/', question_views.prefs),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/logout/', question_views.logout, name='logout'),
                  path('api/registeruser/', question_views.UserCreate.as_view(), name='user_register'),
                  path('register/', TokenObtainPairView.as_view(), name='token_register'),
                  # Submit your refresh token to this path to obtain a new access token
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  # Return 'Mods' model objects
                  # path('mods/', question_views.ModsView.as_view(), name='mods_view'),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('baton/', include('baton.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
