from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html",
                  context={"bands": bands})

def about(request):
    return HttpResponse("<h1> A propos </h1> <p> Nous adorons merch ! </p>")

def listings(request):
    listings = Listing.objects.all()
    return HttpResponse(f"""
        <h1>Liste des annonces !</h1>
        <p>Quelques exemples de titres pour ces annonces :<p>
        <ul>
            <li>{listings[0].title}</li>
            <li>{listings[1].title}</li>
            <li>{listings[2].title}</li>
        </ul>
""")

def contact(request):
    return HttpResponse("<h1> Contactez-nous </h1> <p> Numéro </p>")


