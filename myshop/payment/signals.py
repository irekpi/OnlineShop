from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from io import BytesIO
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import Order
import weasyprint


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # payment was succ
        order = get_object_or_404(Order, id=ipn_obj.invoice)
        # mark the order as paid
        order.paid = True
        order.save()
    # create email
    subject = 'My shop message{}'.format(order.id)
    message = 'Attached Pdf of your shopping'
    email = EmailMessage(subject, message, 'admin@myshop.myshop', [order.email])

    # generate PDF
    html = render_to_string('orders/order/pdf.html', context={'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    # attach pdf
    email.attach('order_{}.pdf'.format(order.id), out.getvalue(), 'application/pdf')

    # send email
    email.send()
valid_ipn_received.connect(payment_notification)