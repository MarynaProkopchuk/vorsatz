from django.shortcuts import render, redirect
from .forms import OnTapForm
from .models import OnTap


def on_tap_create_view(request):
    if request.method == "POST":
        form = OnTapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("on_tap:on_tap_list")
        else:
            # Додаткове відлагодження: роздрукуйте помилки форми
            print(form.errors)
    else:
        form = OnTapForm()

    return render(request, "on_tap/on_tap_create.html", {"form": form})


def on_tap_list_view(request):
    on_tap_items = OnTap.objects.all()
    return render(request, "on_tap/on_tap_list.html", {"on_tap_items": on_tap_items})
