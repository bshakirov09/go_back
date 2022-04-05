#Django
from django.urls import path
#Project
from terms.views.contact_us import CreateContactUsView,GetContactUsView
from terms.views.faq import CreateFAQView,GetFAQView
from terms.views.legal_notices import CreateLegalNoticesView,GetLegalNoticesView
from terms.views.safety_resource_centre import CreateSafetyResourceCentreView, GetSafetyResourceCentreView
from terms.views.privacy_policy import CreatePrivacyPolicyView,GetPrivacyPolicyView
from terms.views.terms import CreateTermsView,GetTermsView


urlpatterns = [
    path('add-contact-us/', CreateContactUsView.as_view(),name='add-contact-us'),
    path('get-contact-us/', GetContactUsView.as_view(),name='get-contact-us'),
    path('add-faq/', CreateFAQView.as_view(),name='add-faq'),
    path('get-faq/', GetFAQView.as_view(),name='get-faq'),
    path('add-legal-notices/', CreateLegalNoticesView.as_view(),name='add-legal-notices'),
    path('get-legal-notices/', GetLegalNoticesView.as_view(),name='get-legal-notices'),
    path('add-safety-resource-centre/', CreateSafetyResourceCentreView.as_view(),name='add-safety-resource-centre'),
    path('get-safety-resource-centre/', GetSafetyResourceCentreView.as_view(),name='get-safety-resource-centre'),
    path('add-privacy-policy/', CreatePrivacyPolicyView.as_view(),name='add-privacy-policy'),
    path('get-privacy-policy/', GetPrivacyPolicyView.as_view(),name='get-privacy-policy'),
    path('add-terms/', CreateTermsView.as_view(),name='add-terms'),
    path('get-terms/', GetTermsView.as_view(),name='get-terms')
]