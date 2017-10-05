from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .utils import BrainTreePayment 


def index(request):
    client_token = BrainTreePayment().generate_client_token()
    return render_to_response("checkouts/new.html", {"data": {"client_token": client_token}})

def add_new_card(request):
    client_token = BrainTreePayment().generate_client_token()
    if request.method == 'GET':
        return render(request, "checkouts/add_card.html", {"client_token": client_token})
    # once callback is send from braintree they will send the payment_method_nonce 
    return render(request, "checkouts/add_card.html", {
    	"client_token": client_token, "payment_method_nonce": request.POST['payment_method_nonce']
    })

