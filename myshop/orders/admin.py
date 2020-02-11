from django.contrib import admin
from .models import Order, OrderItem
from django.shortcuts import reverse
from django.utils.safestring import mark_safe
import csv
import datetime
from django.http import HttpResponse


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


def order_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id])))


def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('orders:admin_order_pdf', args=[obj.id])))


order_pdf.short_description = "PDF bill"



# not yet added csv safer for Admin

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', order_detail, order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]




admin.site.register(Order, OrderAdmin)
