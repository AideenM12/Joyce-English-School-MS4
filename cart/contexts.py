from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course
from exam_courses.models import ExamCourse


def cart_contents(request):

    cart_items = []
    total = 0
    course_count = 0
    exam_course_count = 0
    cart = request.session.get('cart', {"courses": {}, "exam_courses": {}})
    course = None
    exam_course = None

    for key, value in cart.items():
        for item_id, item_data in cart[key].items():
            if key == "courses":
                course = get_object_or_404(Course, pk=item_id)
                # if item_id == course.id:
                total += item_data * course.price
                course_count += item_data
                cart_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'course': course,
                })
            elif key == "exam_courses":
                exam_course = get_object_or_404(ExamCourse, pk=item_id)
                # if item_id != exam_course.id:
                total += item_data * exam_course.price
                exam_course_count += item_data
                cart_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'exam_course': exam_course,
                })
        print(cart_items)

    grand_total = total
    context = {
        'cart_items': cart_items,
        'total': total,
        'course_count': course_count,
        'exam_course_count': exam_course_count,
        'grand_total': grand_total,
    }

    return context
