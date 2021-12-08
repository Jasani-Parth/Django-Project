from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if (int(id)==product.id): #id was originally string
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='cart_total')
def cart_total(products, cart):
    total = 0
    for product in products:
        total = total + cart_quantity(product, cart)
    return total

@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity(product, cart)

@register.filter(name='total_cart_price')
def total_Cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)
    return sum

@register.filter(name='avg_rating')
def avg_rating(reviews):
    total = 0
    count = 0
    for review in reviews:
        total += review.rate
        count+=1
    if count==0:
        avg = 0
    else:
        avg = total/count
    return avg