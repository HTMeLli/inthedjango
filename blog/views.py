from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Supplement


def supplement_list(request):
    supplements = Supplement.objects.order_by('id')
    return render(request, 'blog/supplement_list.html', {'supplements': supplements})

# def supplement_detail(request, pk):
#     supplement = get_object_or_404(Supplement, pk=pk)
#     return render(request, 'blog/supplement_detail.html', {'supplements': supplements})
