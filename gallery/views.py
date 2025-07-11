from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Comment
from django.contrib.auth.decorators import login_required


def gallery(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/gallery.html', {'photos': photos})


@login_required
def upload_photo(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption')

        if image:
            photo = Photo.objects.create(
                image=image,
                user=request.user,
                caption=caption
            )
            return redirect('photo_detail', pk=photo.pk)

    return render(request, 'gallery/upload_photo.html')


@login_required
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                user=request.user,
                photo=photo,
                text=text
            )
            return redirect('photo_detail', pk=photo.pk)
    
    return render(request, 'gallery/photo_detail.html', {'photo': photo})