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
    cart = request.session.get('cart', {})
    course = None
    exam_course = None

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            course = get_object_or_404(Course, pk=item_id)
            exam_course = get_object_or_404(ExamCourse, pk=item_id)
            if not item_id == course.id:
                total += item_data * exam_course.price
                exam_course_count += item_data
                cart_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'exam_course': exam_course,
                })
            else:
                total += item_data * course.price
                course_count += item_data
                cart_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'course': course,
                })
             
    context = {
        'cart_items': cart_items,
        'total': total,
        'course_count': course_count,
        'exam_course_count': exam_course_count
        }

    return context
