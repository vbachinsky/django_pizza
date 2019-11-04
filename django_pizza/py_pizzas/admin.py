# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from py_pizzas.models import Topping, Dough, Pizza, Ordered_toppings, Snacks, Ordered_snacks, Order, Order_payment, Person, Client_account, Client_account_person, Employee, Client_transaction

admin.site.register(Order)
admin.site.register(Topping)
admin.site.register(Dough)
admin.site.register(Ordered_toppings)
admin.site.register(Pizza)
admin.site.register(Snacks)
admin.site.register(Ordered_snacks)
admin.site.register(Order_payment)
admin.site.register(Person)
admin.site.register(Client_account)
admin.site.register(Client_account_person)
admin.site.register(Employee)
admin.site.register(Client_transaction)