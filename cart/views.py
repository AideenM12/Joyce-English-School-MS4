from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def cart(request):
    """ A view to return the cart page """

    return render(request, 'cart/cart.html')


@login_required
def add_to_cart(request, item_id):
    """ Add a course/exam_course to the cart """
    item_to_add = item_id
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    item_type = request.POST.get('item_type')
    cart = request.session.get('cart', {"courses": {}, "exam_courses": {}})

    if request.user.is_authenticated:
        if item_type == "courses":
            if item_id in list(cart['courses'].keys()):
                cart['courses'][item_id] += quantity
                messages.success(request, 'Added course to your cart')
            else:
                cart['courses'][item_id] = quantity
                messages.success(request, 'Added course to your cart')
        elif item_type == "exam_courses":
            if item_id in list(cart['exam_courses'].keys()):
                cart['exam_courses'][item_id] += quantity
            else:
                cart['exam_courses'][item_id] = quantity

        request.session['cart'] = cart
        return redirect(redirect_url)


@login_required
def remove_from_cart(request, item_id):
    """A view to remove an item from the cart"""
    try:
        course = None
        exam_course = None
        cart = request.session.get('cart', {"course": {}, "exam_course": {}})
        item_type = request.POST['item_type']

        if 'item_type' in request.POST:
            item_type = request.POST['item_type']

        if item_type == 'course':
            if item_id in cart['courses'].keys():
                del cart['courses'][item_id]
        elif item_type == 'exam_course':
            if item_id in cart['exam_courses'].keys():
                del cart['exam_courses'][item_id]

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


@login_required
def clear_cart(request):
    """Remove all items from the cart"""
    request.session['cart'] = {"courses": {}, "exam_courses": {}}

    return redirect('home')
