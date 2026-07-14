from django.urls import path

from .views import (
    auth_views,
    client_views,
    gmail_views,
    ai_views,
    campaign_views,
    calendar_views,
    views,
)

urlpatterns = [

    # Authentication 
    path("login/", auth_views.login_view, name="login"),
    path("register/", auth_views.register_view, name="register"),
    path("logout/", auth_views.logout_view),

    #clients
    path("clients/", client_views.clients,name="clients"),
    path("clients/edit/<int:cid>/",client_views.edit_client,name="edit_client"),
    path("clients/delete/<int:cid>/",client_views.delete_client,name="delete_client",),

    # Gmail
    path("gmail/connect/", gmail_views.connect_gmail),
    path("gmail/callback/", gmail_views.gmail_callback),
    path("gmail/send/", gmail_views.send_email),

    # AI
    path("ai_chat/", ai_views.chat,name="ai_chat"),
    # path("generate-email/", ai_views.generate_email),

    # Campaign
    path("campaign/create/", campaign_views.create_campaign),
    path("campaign/list/", campaign_views.list_campaigns),

    # Calendar
    path("calendar/connect/", calendar_views.connect_calendar),
    path("calendar/create/", calendar_views.create_meeting),

    # Dashboard
    # path("dashboard/", dashboard.dashboard_data),

    
    path("dashboard/", views.dashboard, name="dashboard"),
    # path("clients/", views.clients, name="clients"),
    path("campaigns/", views.campaigns, name="campaigns"), 
    #path("ai_chat/",views.ai_chat,name="ai_chat"),
    path("meetings/",views.meetings,name="meetings"),
    path("audit/",views.audit,name="audit"),
    path("templates/",views.templates,name="templates"),
]
