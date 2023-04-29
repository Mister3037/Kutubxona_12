from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def kitob_soni(request):
    content = {
        'barcha_kitoblar': Talaba.objects.filter(kitob_soni__gt=0)
    }
    return render(request, 'kitob_soni.html', content)

def ismida_a(request):
    content = {
        "ismlar": Talaba.objects.filter(ism__contains="A")
    }
    return render(request, "ism.html", content)

def talaba_id(request, son):
    content = {
        'bitta_talaba': Talaba.objects.get(id=son)
    }
    return render(request, 'talaba.html', content)


def hamma_muallif(request):
    content = {
        'muallif_ism': Muallif.objects.filter(ism__contains='A')
    }
    return render(request, 'mualliflar.html', content)

def tanlangan(request, son):
    content= {
        'malumotlar': Muallif.objects.get(id=son)
    }
    return render(request, 'barcha.html', content)

def hamma_kitoblar(request):
    soz = request.GET.get('qidiruv')
    if soz == "" or soz is None:

        content = {
        "kitoblar": Kitob.objects.all()
        }
    else:
        content = {
            "kitoblar": Kitob.objects.filter(nom__contains=soz)
        }
    return render(request, 'hamma_kitoblar.html', content)

def kitob(request, raqam):
    content = {
        "kitob_malumolari": Kitob.objects.get(id=raqam)
    }
    return render(request, 'information.html', content)


def record(request):
    soz = request.GET.get('Qidiruv')



def studentlar(request):
    content = {
        "talaba": Talaba.objects.all()
    }
    return render(request, 'talabalaruz.html', content)


def student_ochirish(request, raqam):
    Talaba.objects.filter(id=raqam).delete()
    return redirect("/talabas/")

def kitob_ochirish(request, son):
    Kitob.objects.filter(id=son).delete()
    return redirect("/kitob/")


def book(request, son):
    content = {
    "book_id":Kitob.objects.get(id=son)
    }
    return render(request, "searchid.html", content)


def all(request):
    soz = request.GET.get('Search')
    if soz == " ":


        content = {
        "all_record": Record.objects.all()
    }
    else:
        content = {
            "all_record": Record.objects.filter(talaba_fk__contains=soz)
        }
        return render(request, "allrecords.html", content)




def tirik_muallif(request):
    content = {
    "trik":Muallif.objects.filter(tirik=True)
    }
    return render(request, "tirikmuallif.html", content)

def sahifa(request):
    content = {
        "sahifak": Kitob.objects.all().order_by('-sahifa')[:3]
    }
    return render(request, "sahifamax.html", content)

def kitobi_kop(request):
    content = {
        "maxkitob": Muallif.objects.all().order_by('-kitob_soni')[3]
    }
    return render(request, "kitoblarikop.html", content)

def rekordsana(request):
    content = {
        'rec': Record.objects.all().order_by('-onlingan_sana')[:3]
    }
    return render(request, "sanarecord.html", content)

def tmuallif(request):
    content = {
        'muallift': Kitob.objects.filter(tirik="Tirik")
    }

def muallif_ochir(request, son):
    Muallif.objects.filter(id=son).delete()
    return redirect("/mualliflar/")

def mualliflar(request):
    soz = request.GET.get('qidiruv')
    if soz == "" or soz is None:

     content = {
        'muallif_i': Muallif.objects.all()
    }
    else:
        content = {
            'muallif_i': Muallif.objects.filter(ism__contains=soz)
        }
    return render(request, "muallifism.html", content)

def fanlar(request):
    soz = request.GET.get('qidiruv')
    if soz == "" or soz is None:

        content = {
        "fanlaruz": Fan.objects.all()
        }
    else:
        content = {
            "fanlaruz": Fan.objects.filter(fan__contains=soz)
        }
    return render(request, "fanuz.html", content)

def fanochir(request, son):
    Fan.objects.filter(id=son).delete()
    return redirect('/fanlar/')

def yonalish(request):
    content = {
        'yonalishlar': Yonalish.objects.all()
    }
    return render(request, "Yonalish.html", content)

def yonalishochir(request, son):
    Yonalish.objects.filter(id=son).delete()
    return redirect('/yonalish/')

def ustoz(request):
     soz = request.GET.get('search')
     if soz == " " or soz is None:
         content = {
             "ustozism": Ustoz.objects.all()
         }
     else:
         content = {
             "ustozism": Ustoz.objects.filter(ism__contains=soz)
             return render(request, "ustozuz.html", content)




