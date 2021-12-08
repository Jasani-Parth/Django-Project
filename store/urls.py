from django.urls import path

from store.models.review import Review
from store.views import transporter_signup
from .views import home, login, signup, cart, orders, order_page, review, product, order_update, edit, vendor_login, vendor_signup, vendor_home, transporter_home, transporter_login, transporter_signup, add_product, delete_product, modify_product, modify_form, my_profile
from .views.login import logout
from .views.vendor_login import vendor_logout
from .views.transporter_login import transporter_logout
from .views.checkout import Checkout
from .views.addstatus import AddStatus


urlpatterns = [
    path('my_profile', my_profile.My_Profile.as_view(), name='my_profile'),
    path('', home.Index.as_view(), name='homepage'),
    path('vendor_home', vendor_home.VendorIndex.as_view(), name='vendor_homepage'),
    path('transporter_home', transporter_home.TransporterIndex.as_view(), name='transporter_homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('vendor_signup', vendor_signup.VendorSignup.as_view(), name='vendor_signup'),
    path('transporter_signup', transporter_signup.TransporterSignup.as_view(), name='transporter_signup'),
    path('edit', edit.Edit.as_view(), name='edit'),
    path('login', login.Login.as_view(), name='login'),
    path('vendor_login', vendor_login.VendorLogin.as_view(), name='vendor_login'),
    path('transporter_login', transporter_login.TransporterLogin.as_view(), name='transporter_login'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('addstatus', AddStatus.as_view(), name='addstatus'),
    path('logout', logout, name='logout'),
    path('vendor_logout', vendor_logout, name='vendor_logout'),
    path('transporter_logout', transporter_logout, name='transporter_logout'),
    path('review', review.Reviews.as_view(), name='review'),
    path('product', product.ProductView.as_view(), name='product_page'),
    path('orders', orders.Orders.as_view(), name='orders'),
    path('tracker', order_update.OrderUpdate.as_view(), name='tracker'),
    path('add_product', add_product.AddProduct.as_view(), name='add_product'),
    path('delete_product', delete_product.DeleteProduct.as_view(), name='delete_product'),
    path('modify_product', modify_product.ModifyProduct.as_view(), name='modify product'),
    path('modify_product_form', modify_form.ModifyProductForm.as_view()),
    path('order_page',order_page.OrderPage.as_view())
]