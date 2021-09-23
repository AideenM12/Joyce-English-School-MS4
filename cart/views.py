from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


# Create your views here.


def cart(request):
    """ A view to return the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    item_to_add = item_id
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    item_type = request.POST.get('item_type')
    cart = request.session.get('cart', {"courses": {}, "exam_courses": {}})
    
    if request.user.is_authenticated:
        if item_type == "courses":
            if item_id in list(cart['courses'].keys()):
                cart['courses'][item_id] += quantity
                messages.success(request, f'Added course to your cart')
            else:
                cart['courses'][item_id] = quantity
                messages.success(request, f'Added course to your cart')
           
        elif item_type == "exam_courses":
            if item_id in list(cart['exam_courses'].keys()):
                cart['exam_courses'][item_id] += quantity
            else:
                cart['exam_courses'][item_id] = quantity

      
        if cart.items():            
            for key, value in request.POST.items():
                if item_type in request.POST == cart["courses"].keys():                
                    if item_id in request.POST == cart['courses'][item_to_add]:
                        print(item_id)
                        print(item_to_add)
                        messages.error(
                        request, 'You already have added a course to your cart.')
                        return redirect('home')
               # elif key and value in request.session['cart'] == cart['exam_courses'][item_id]:
                 #   messages.error(
                  #  request, 'You already have added a course to your cart.')
                   # return redirect('home')
                

         # if request.user.is_authenticated and cart.items():
        #   if item_type == "courses":
         #      if item_id in cart == cart['courses'][item_id]:
       # for item_id, item_data in cart[key].items():
        #                if key == "courses" and value == cart[value]:
    
       # if item_type == "courses":
        #    if cart.items():
         #   if item_id in list(cart['courses'].keys()):
          #      messages.error(
           #     request, 'You already have added a course to your cart.')
            #    return redirect('home')
        #elif item_type == "exam_courses":
         #    if item_id in list(cart['exam_courses'].keys()):
          #      messages.error(
           #     request, 'You already have added a course to your cart.')
            #    return redirect('home')
    #cart[id] = cart.get(id, quantity)
    


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
