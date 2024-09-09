from django.shortcuts import render,redirect,get_object_or_404
from .models import Plat,Comment
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def plat(request,id):
    plat=Plat.objects.get(id=id)
    return render(request, 'plats/plat.html',{'plat': plat})

def plats(request):
    category = request.GET.get('category', '')  # Get the selected category from the URL parameter

    plat_list = Plat.objects.all()

    if category:
        plat_list = plat_list.filter(categorie__nom__icontains=category)  # Filter plats by category

    paginator = Paginator(plat_list, 3)  # Display 3 plats per page

    page_number = request.GET.get('page')
    plats = paginator.get_page(page_number)

    wishlist_produits = request.user.wishlist.produits.all() if request.user.is_authenticated else []

    return render(request, 'plats/plats.html', {'plat': plats, 'wishlist_produits': wishlist_produits, 'paginator': paginator})




def search(request):
    plat_title = request.GET.get('plat-title', '')

    plats = Plat.objects.filter(nom__icontains=plat_title)

    return render(request, 'plats/plats.html', {'plat': plats})


def plat_details(request, id):
    plat = get_object_or_404(Plat, id=id)
    wishlist_produits = request.user.wishlist.produits.all() if request.user.is_authenticated else []
    comments = Comment.objects.filter(plat=plat)
    
    if request.method == 'POST':
        comment_content = request.POST.get('comment')
        comment = Comment.objects.create(plat=plat, client=request.user, content=comment_content)
        return redirect('plat_details', id=id)
    
    if request.method == 'GET' and 'delete_comment' in request.GET:
        comment_id = request.GET.get('delete_comment')
        comment = get_object_or_404(Comment, id=comment_id)
        
        if comment.client == request.user:
            comment.delete()
            messages.success(request, 'Comment deleted successfully.')
        else:
            messages.error(request, 'You do not have permission to delete this comment.')
        
        return redirect('plat_details', id=id)

    context = {
        'plat': plat,
        'wishlist_produits': wishlist_produits,
        'comments': comments,
    }
    return render(request, 'plats/plat.html', context)

