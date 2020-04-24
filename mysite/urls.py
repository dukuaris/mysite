# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from mysite.views import HomeView, UserCreateView, UserCreateDoneTV


urlpatterns = [
    path('admin/', admin.site.urls),
    # shkim
    # path('accounts/', include('django.contrib.auth.urls')),
    # # path('accounts/register/', UserCreateView.as_view(), name='register'),
    # # path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    # #
    # # path('', HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
    # path('photo/', include('photo.urls')),
    # path('visual/', include('visual.urls')),
    # path('crawl/', include('crawl.urls')),
    # path('django_plotly_dash/', include('django_plotly_dash.urls')),

] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
