from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


#signup
def signup(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'registration/login.html', context)

     

#dashboard
def dashboard(request):
    return render(request,'main/dashboard.html',{})

#about
def about(request):
    return render(request,'main/about.html',{})

#barware
def barware(request):
    return render(request,'main/barware.html',{})   

#blue-label
def blue_label(request):
    return render(request,'main/blue-label.html',{})
    
#blue-swift
def blue_swift(request):
    return render(request,'main/blue-swift.html',{})    

#brandy-section
def brandy_section(request):
    return render(request,'main/brandy-section.html',{})   

#cart
def cart(request):
    return render(request,'main/cart.html',{})    

#champagne-section
def Champagne_section(request):
    return render(request,'main/Champagne-section.html',{})   

#Chateau-m.html
def Chateau_m(request):
    return render(request,'main/Chateau-m.html',{})  

#Chateau-Margaux
def Chateau_Margaux(request):
    return render(request,'main/Chateau-Margaux.html',{})

#checkout.html
def checkout(request):
    return render(request,'main/chechout.html',{})  

#ciroc
def ciroc(request):
    return render(request,'main/ciroc.html',{})     

#clase-azul
def clase_azul(request):
    return render(request,'main/clase-azul.html',{})     

#coming-soon
def coming_soon(request):
    return render(request,'main/coming-soon.html',{})    

#faq
def faq(request):
    return render(request,'main/faq.html',{})       

#gin-section
def gin_section(request):
    return render(request,'main/gin-section.html',{})         

#hennessy
def hennessy(request):
    return render(request,'main/hennessy.html',{})

#hennesy-vsop-desc-cl70
def hennesy_vsop_desc_cl70(request):
    return render(request,'main/hennesy-vsop-desc-70cl.html',{})

#hennesy-vsop-desc
def hennesy_vsop_desc(request):
    return render(request,'main/hennesy-vsop-desc.html',{}) 

#hennesy-xo-1lr
def hennesy_xo_lr1(request):
    return render(request,'main/hennesy-xo-1lr.html',{})  

#hennesy-xo
def hennesy_xo(request):
    return render(request,'main/hennesy-xo.html',{})

#index
def index(request):
    return render(request,'main/index.html',{})

#jack-daniels
def jack_daniels(request):
    return render(request,'main/jack-daniels.html',{})

#jack-honey
def jack_honey(request):
    return render(request,'main/jack-honey.html',{})

#jameson
def jameson(request):
    return render(request,'main/jameson.html',{})   

#johnniewalker
def johnniewalker(request):
    return render(request,'main/johnniewalker.html',{}) 

#limited-edition
def limited_edition(request):
    return render(request,'main/limited-edition.html',{})  

#liquer-section
def liquer_section(request):
    return render(request,'main/liquer-section.html',{}) 

#martell-vsop
def martell_vsop(request):
    return render(request,'main/martell-vsop.html',{})   

#martell
def martell(request):
    return render(request,'main/martell.html',{}) 


#Moet-Imperial
def Moet_Imperial(request):
    return render(request,'main/Moet-Imperial.html',{})      


#Moet-Rose-Imperia
def Moet_Rose_Imperia(request):
    return render(request,'main/Moet-Rose-Imperia.html',{})  


#privacy
def privacy(request):
    return render(request,'main/privacy.html',{})  


#remymartins
def remymartins(request):
    return render(request,'main/remymartins.html',{}) 

#rum-section
def rum_section(request):
    return render(request,'main/rum-section.html',{})     


#tequila-section
def tequila_section(request):
    return render(request,'main/tequila-section.html',{}) 

#terms
def terms(request):
    return render(request,'main/terms.html',{})     


#vodka-section
def vodka_section(request):
    return render(request,'main/vodka-section.html',{})     

#whisky-section
def whisky_section(request):
    return render(request,'main/whisky-section.html',{})     

#wine-section
def wine_section(request):
    return render(request,'main/wine-section.html',{})  

#brand-drink-desc/courvoisier-vs
def courvoisier_vs(request):
    return render(request,'main/brand-drink-desc/courvoisier-vs.html',{})  

#brand-drink-desc/courvoisier-vsop
def courvoisier_vsop(request):
    return render(request,'main/brand-drink-desc/courvoisier-vsop.html',{}) 

#brand-drink-desc/courvoisier-xo
def courvoisier_xo(request):
    return render(request,'main/brand-drink-desc/courvoisier-xo.html',{}) 

#brand-drink-desc/hennessy-black
def hennessy_black(request):
    return render(request,'main/brand-drink-desc/hennessy-black.html',{}) 

#brand-drink-desc/martell-vs
def martell_vs(request):
    return render(request,'main/brand-drink-desc/martell-vs.html',{})

#brand-drink-desc/martell-xo
def martell_xo(request):
    return render(request,'main/brand-drink-desc/martell-xo.html',{})

#brand-drink-desc/remy-martin-vs
def remy_martin_vs(request):
    return render(request,'main/brand-drink-desc/remy-martin-vs.html',{})    

#brand-drink-desc/remy-martin-vsop
def remy_martin_vsop(request):
    return render(request,'main/brand-drink-desc/remy-martin-vsop.html',{})     

#brand-drink-desc/remy-martin-xo
def remy_martin_xo(request):
    return render(request,'main/brand-drink-desc/remy-martin-xo.html',{})    

#champ-drink-desc/dom-perignon-2000
def dom_perignon_2000(request):
    return render(request,'main/champ-drink-desc/dom-perignon-2000.html',{})   

#champ-drink-desc/dom-perignon-2006
def dom_perignon_2006(request):
    return render(request,'main/champ-drink-desc/dom-perignon-2006.html',{})         

#champ-drink-desc/dom-perignon-2008
def dom_perignon_2008(request):
    return render(request,'main/champ-drink-desc/dom-perignon-2008.html',{})      

#champ-drink-desc/moet-ice-imperial
def moet_ice_imperial(request):
    return render(request,'main/champ-drink-desc/moet-ice-imperial.html',{})  

#champ-drink-desc/moet-nectar-imperial
def moet_nectar_imperial(request):
    return render(request,'main/champ-drink-desc/moet-nectar-imperial.html',{})  

#champ-drink-desc/moet-rose-imperial
def moet_rose_imperial(request):
    return render(request,'main/champ-drink-desc/moet-rose-imperial.html',{})            

#champ-drink-desc/veuve-clicqout-rose-demi-sec
def veuve_clicqout_rose_demi_sec(request):
    return render(request,'main/champ-drink-desc/veuve-clicqout-rose-demi-sec.html',{})     

#gin-drink-desc/beefeater-london-dry-gin-75cl
def beefeater_london_dry_gin_cl75(request):
    return render(request,'main/gin-drink-desc/beefeater-london-dry-gin-75cl.html',{})  


#gin-drink-desc/beefeater-london-dry-gin
def beefeater_london_dry_gin(request):
    return render(request,'main/gin-drink-desc/beefeater-london-dry-gin.html',{}) 
    
#gin-drink-desc/bombay-dry-gin
def bombay_dry_gin(request):
    return render(request,'main/gin-drink-desc/bombay-dry-gin.html',{})     

#gin-drink-desc/bombay-sapphire
def bombay_sapphire(request):
    return render(request,'main/gin-drink-desc/bombay-sapphire.html',{})    


#gin-drink-desc/tanqueray-london-dry-gin
def tanqueray_london_dry_gin(request):
    return render(request,'main/gin-drink-desc/tanqueray-london-dry-gin.html',{})        

#liquer-drink-desc/cointreau
def cointreau(request):
    return render(request,'main/liquer-drink-desc/cointreau.html',{})     

#other-pages/delivery
def delivery(request):
    return render(request,'main/other-pages/delivery.html',{})      

#other-pages/help-center
def help_center(request):
    return render(request,'main/other-pages/help_center.html',{}) 


#other-pages/track-order
def track_order(request):
    return render(request,'main/other-pages/track_order.html',{})