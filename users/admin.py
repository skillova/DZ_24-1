from django.contrib import admin

from users.models import User, Payment


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number', 'country', 'avatar')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_payment', 'paid_course', 'paid_lesson', 'payment_amount', 'payment_method')
