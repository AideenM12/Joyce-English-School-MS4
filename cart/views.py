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


def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {"courses": {}, "exam_courses": {}})



def clear_cart(request, item_id):
    """Remove courses from the cart"""
   # quantity = 1
    #item_type = request.session.get('item_type')
    request.session['cart'] = {"courses": {}, "exam_courses": {}}
   # print(cart)
   # print(f"ITEM TYPE: {item_type}")
   # if 'courses' in cart.keys():
   #     cart['courses'].pop(item_id)
   #     print(f"NEW CART: {cart}")
   # elif 'exam_courses' in cart.keys():
   #     cart['exam_courses'].pop(item_id)
   #     print(f"NEW CART: {cart}")
   # for key, value in cart.items():
   #     print(key, value)
   #     for item_id, item_data in cart[key].items():
   #         if 'courses' in cart.keys():
   #             if item_id in list(cart['courses'].keys()):
   #                 cart['courses'][item_type].pop(item_id)
   #             else:
   #                 cart['courses'][item_id] = quantity
   #         elif 'exam_courses' in cart.keys():
   #             if item_id in list(cart['exam_courses'].keys()):
   
   #                 if key in cart:
    #                    cart = {"exam_courses": {}}
     #                   cart['exam_courses'][item_type].pop(item_id)
      #                      print(item_type)
       #             else:
        #                cart['exam_courses'][item_id] = quantity
   # print(item_type)
   # request.session['cart'] = cart

    return redirect('home')
