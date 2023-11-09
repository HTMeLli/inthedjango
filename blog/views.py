from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Supplement, ActiveIngredient


def supplement_list(request):
    supplements = Supplement.objects.order_by('id')
    ingredients = ActiveIngredient.objects.all()
    return render(
        request,
        'blog/supplement_list.html', 
        {
            'supplements': supplements,
            'ingredients': ingredients
        }
    )

# def supplement_detail(request, pk):
#     supplement = get_object_or_404(Supplement, pk=pk)
#     return render(request, 'blog/supplement_detail.html', {'supplements': supplements})
