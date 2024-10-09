from django.shortcuts import render, redirect

from django.core.handlers.wsgi import WSGIRequest
from .models import Ad, Category


def home_page(request: WSGIRequest):

    if request.method == "POST":
        category_id = request.POST["category"]
        title = request.POST["nomi"]
        description = request.POST["qisqa_malumot"]
        price = request.POST["narxi"]
        owner = request.POST["egasi"]
        phone = request.POST["telefon_raqami"]
        image = request.FILES["rasmi"]
        condition = request.POST["holati"]

        print(category_id, title, description, price, owner, phone, image, condition)

        nomi = Ad.objects.create(
            category_id=category_id,
            title=title,
            description=description,
            price=price,
            owner=owner,
            phone=phone,
            image=image,
            condition=condition,
        )
        
    ads = Ad.objects.all()
    categories = Category.objects.all()

    context = {"ads": ads, "categories": categories}

    return render(request, "index.html", context)


def ad_detail(request, id):

    ad = Ad.objects.get(id=id)
 
    if request.method == "POST":
        title = request.POST["nomi"]
        description = request.POST["qisqa_malumot"]
        price = request.POST["narxi"]
        owner = request.POST["egasi"]
        phone = request.POST["telefon_raqami"]
        condition = request.POST["holati"]

        image = request.FILES.get("rasmi", None)

        print(title, description, price, owner, phone, image, condition)

        ad.title = title
        ad.description = description
        ad.price = price
        ad.owner = owner
        ad.phone = phone
        ad.condition = condition

        if image:
            ad.image = image

        ad.save()

    context = {"ad": ad}

    return render(request, "ad_detail.html", context)



def delete_ad(request, id):
    ad = Ad.objects.get(id=id)

    ad.delete()

    return redirect("home_page")