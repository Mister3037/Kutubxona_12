from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('kitab/', kitob_soni),
    path('ismlar', ismida_a),
    path('talaba/<int:son>/', talaba_id ),
    path('hammasi/', hamma_muallif),
    path('malumot/<int:son>/', tanlangan),
    path('kitob/', hamma_kitoblar),
    path('information/<int:raqam>/', kitob),
    path('rekord', record),
    path('delete/<int:raqam>/', student_ochirish),
    path('talabas/', studentlar),
    path('drop/<int:son>/', kitob_ochirish),
    path('search/<int:son>/', book),
    path('allrekord/', all),
    path('patch/', tirik_muallif),
    path('saxifamax/', sahifa),
    path('engkop/', kitobi_kop),
    path('recordsana/', rekordsana),
    path('mualliftirik/', tmuallif),
    path('muallif_ochir/<int:son>/', muallif_ochir),
    path('mualliflar/', mualliflar),
    path('fanlar/', fanlar),
    path('fanochir/<int:son>/', fanochir),
    path('yonalish/', yonalish),
    path('yonalishochir/<int:son>/', yonalishochir),
    path('ustoz/', ustoz),


]

