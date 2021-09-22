from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

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
    print(cart)
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    
    try:
        course = None
        exam_course = None
        cart = request.session.get('cart', {"course": {}, "exam_course": {}})
        print(cart)
        print(item_id)
        print(type(item_id))

        item_type = request.POST['item_type']
        print(f'item type: {item_type}')
        
        if 'item_type' in request.POST:
            item_type = request.POST['item_type']
            print(item_type)

        if item_type == 'course':
            
            if item_id in cart['courses'].keys():
                del cart['courses'][item_id]
        elif item_type == 'exam_course':
            
            if item_id in cart['exam_courses'].keys():
                del cart['exam_courses'][item_id]
               
        print(item_type)
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        print(e)
        return HttpResponse(status=500)


def clear_cart(request):
    """Remove courses from the cart"""
    request.session['cart'] = {"courses": {}, "exam_courses": {}}
  
    return redirect('home')
