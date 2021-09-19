from django.shortcuts import render, redirect

# Create your views here.


def cart(request):
    """ A view to return the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    item_type = request.POST.get('item_type')
    cart = request.session.get('cart', {"courses": {}, "exam_courses": {}})

    if item_type == "courses":
        if item_id in list(cart['courses'].keys()):
            cart['courses'][item_id] += quantity
        else:
            cart['courses'][item_id] = quantity
    elif item_type == "exam_courses":
        if item_id in list(cart['exam_courses'].keys()):
            cart['exam_courses'][item_id] += quantity
        else:
            cart['exam_courses'][item_id] = quantity

    
    request.session['cart'] = cart
    return redirect(redirect_url)
    
