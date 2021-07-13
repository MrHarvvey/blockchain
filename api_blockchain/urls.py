from django.urls import path
from .views import transfer_normal, transaction_history
urlpatterns = [
	#Leave as empty string for base url
	path('transfer_normal/', transfer_normal, name="Transfer Normal"),
    path('transaction_history/', transaction_history, name="Transaction History"),
]
