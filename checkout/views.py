from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import Orderform

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = Orderform()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51P4Imb1667nhNLM4ErmG81qbioe871N8A6cKAHH7Jo2CXTXKjHk0RgJFR3T9vn4juJZmEQkKznUzndvjKSDuhn0i00tXKXZYuW',
        'client_secret': 'test secret',
    }

    return render(request, template, context)