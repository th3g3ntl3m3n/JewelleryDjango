from django.conf.urls import url, include
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^$', views.index, name='home'),
    url(r'^jewellery/$', views.index),
    # url(r'^/rings/$', views.showRings, name='rings'),
    # url(r'^/neckless/$', views.showNeckless, name = 'neckless'),
    url(r'^about/$', views.about, name='about'),
    url(r'^thank/$', views.thankYouPage , name='thank'),
    url(r'^register/$', views.register, name='register'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^addToCart/(?P<qty>([^/]+))/(?P<buy_id>[0-9]+)/$', views.setQty, name = 'qty'),
    url(r'^detail/(?P<product_id>[0-9]+)/$', views.detailproduct, name='detail'),
    url(r'^detail/(?P<product_id>[0-9]+)/saved$', views.saveReview, name='saveReview'),
    url(r'^addToCart/(?P<product_id>[0-9]+)/$',views.addToCart, name = 'addToCart'),
    url(r'^addToCart/(?P<buy_id>[0-9]+)/unbuy$', views.removeFromCart, name = 'remove'),
    url(r'^checkout/$', views.checkout, name='checkout'),
]
