from django.shortcuts import render
from . models import allos
from . models import ayurs
from . models import disps
from . models import neuts
from . models import pharms
from . models import respis
from . models import surgis
from . models import applys
from . models import bels
from . models import cervis
from . models import fingers
from . models import fracts
from . models import gells
from . models import kneees
from . models import neops
from . models import tracts
from . models import wrists
from . models import cathes
from . models import dias
from . models import flus
from . models import bloods
from . models import bps
from . models import capss
from . models import cleans
from . models import clothss
from . models import dialys
from . models import fums
from . models import glovess
from . models import googless
from . models import icus
from . models import masks
from . models import oxys
from . models import pmss
from . models import pulses
from . models import sans
from . models import shoes
from . models import sucs
from . models import syringes
from . models import vents

# Create your views here.

def orth(request):
    return render(request, "orth.html")
    
def allopathic(request):
    allo = allos.objects.all()

    return render(request, "allopathic.html", {'allo': allo})

def ayurvedic(request):
    ayur = ayurs.objects.all()

    return render(request, "ayurvedic.html", {'ayur': ayur})

def disposals(request):
    disp = disps.objects.all()

    return render(request, "disposals.html", {'disp': disp})

def neu(request):
    neut = neuts.objects.all()

    return render(request, "neu.html", {'neut': neut})

def pharmacy(request):
    pharm = pharms.objects.all()

    return render(request, "pharmacy.html", {'pharm': pharm})

def resp(request):
    respi = respis.objects.all()

    return render(request, "resp.html", {'respi': respi})

def surgicals(request):
    surgi = surgis.objects.all()

    return render(request, "surgicals.html", {'surgi': surgi})

def app(request):
    apply = applys.objects.all()

    return render(request, "app.html", {'apply': apply})

def belt(request):
    bel = bels.objects.all()

    return render(request, "belt.html", {'bel': bel})

def cerv(request):
    cervi = cervis.objects.all()

    return render(request, "cerv.html", {'cervi': cervi})

def fing(request):
    finger = fingers.objects.all()

    return render(request, "fing.html", {'finger': finger})

def frac(request):
    fract = fracts.objects.all()

    return render(request, "frac.html", {'fract': fract})

def gel(request):
    gell = gells.objects.all()

    return render(request, "gel.html", {'gell': gell})

def knee(request):
    kneee = kneees.objects.all()

    return render(request, "knee.html", {'kneee': kneee})

def neo(request):
    neop = neops.objects.all()

    return render(request, "neo.html", {'neop': neop})

def trac(request):
    tract = tracts.objects.all()

    return render(request, "trac.html", {'tract': tract})

def wri(request):
    wrist = wrists.objects.all()

    return render(request, "wri.html", {'wrist': wrist})

def cath(request):
    cathe = cathes.objects.all()
    return render(request, "cath.html",{'cathe' : cathe})

def diag(request):
    dia = dias.objects.all()
    return render(request, "diag.html",{'dia' : dia})

def fluid(request):
    flu = flus.objects.all()
    return render(request, "fluid.html",{'flu' : flu})


def blood(request):
    bloo = bloods.objects.all()

    return render(request, "blood.html", {'bloo': bloo})

def bp(request):
    bpress = bps.objects.all()

    return render(request, "bp.html", {'bpress': bpress})

def cap(request):
    caps = capss.objects.all()

    return render(request, "cap.html", {'caps': caps})

def clean(request):
    clean = cleanss.objects.all()

    return render(request, "clean.html", {'clean': clean})

def cloth(request):
    cloths = clothss.objects.all()

    return render(request, "cloth.html", {'cloths': cloths})

def dialysis(request):
    dialy = dialys.objects.all()

    return render(request, "dialysis.html", {'dialy': dialy})

def fum(request):
    fum = fums.objects.all()

    return render(request, "fum.html", {'fum': fum})

def gloves(request):
    gloves = glovess.objects.all()

    return render(request, "gloves.html", {'gloves': gloves})

def googles(request):
    googles = googless.objects.all()

    return render(request, "googles.html", {'googles': googles})

def icu(request):
    icu = icus.objects.all()

    return render(request, "icu.html", {'icu': icu})

def mask(request):
    mask = masks.objects.all()

    return render(request, "mask.html", {'mask': mask})

def oxy(request):
    oxy = oxys.objects.all()

    return render(request, "oxy.html", {'oxy': oxy})

def pms(request):
    pms = pmss.objects.all()

    return render(request, "pms.html", {'pms': pms})

def pulse(request):
    pulse = pulses.objects.all()

    return render(request, "pulse.html", {'pilse': pulse})

def san(request):
    san = sans.objects.all()

    return render(request, "san.html", {'san': san})

def shoe(request):
    shoe = shoes.objects.all()

    return render(request, "shoe.html", {'shoe': shoe})

def suc(request):
    suc = sucs.objects.all()

    return render(request, "suc.html", {'suc': suc})

def Syringe(request):
    syringe = syringes.objects.all()
    return render(request, "Syringe.html",{'syringe' : syringe})

def vent(request):
    vent = vents.objects.all()
    return render(request, "vent.html",{'vent' : vent})




