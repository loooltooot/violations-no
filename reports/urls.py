from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'reports'
urlpatterns = [
    path('register/', views.RegisterView.as_view(extra_context={'title': _('Register')}), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.LoginUserView.as_view(extra_context={'title': _('Log in')}), name='login'),
    path('', views.IndexView.as_view(extra_context={'title': _('Home')}), name='index'),
    path('newreport/', views.CreateReportView.as_view(extra_context={'title': _('Create report')}), name='newreport'),
    path('report/<int:pk>/delete/', views.DeleteReportView.as_view(extra_context={'title': _('Delete report')}), name='deletereport'),
    path('report/admin/', views.admin_report_vote_proxy, name='votereport_proxy'),
    path('report/admin/<int:pk>/', views.AdminReportVoteView.as_view(extra_context={'title': _('Report status')}), name='votereport'),
    path('report/admin/<int:pk>/vote', views.change_report_status, name='changereportstatus'),
]