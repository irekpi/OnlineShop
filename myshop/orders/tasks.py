# from celery import task
# from django.core.mail import send_mail
# from .models import Order
#
#
# @task
# def order_created(order_id):
#     """
#     Task to send an e-mail notification when an order is successfully created.
#     """
#
#     order = Order.objects.get(id=order_id)
#     subject = 'Order nr {}'.format(order_id)
#     message = 'Dear {} \n You placed an order {}'.format(order.first_name, order.id)
#     mail_sent = send_mail(subject,
#                           message,
#                           'admin@admin.admin',
#                           [order.email])
#     return mail_sent