from django import template

register = template.Library()


@register.filter(name='customer_price')
def customer_price(stock, price_type):
    return stock.customer_price(price_type)
