from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm
from .models import Customer


def index(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Sucessfully Login !!")
            return redirect("home")
        else:
            messages.error(request, "Sorry Something Went Wrong !!")
            return redirect("home")
    return render(request, "index.html", {"customers": customers})


def logout_user(request):
    logout(request)
    messages.warning(request, "Sucessfully Logout !!")
    return redirect("home")


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(request, username=username, password=password)
                login(request, user)
                messages.success(request, "Sucessfully Registered !!")
                return redirect("home")
        else:
            form = SignUpForm()
    return render(request, "register.html", {"form": form})


def customer(request, pk):
    if request.user.is_authenticated:
        record = Customer.objects.get(pk=pk)
        return render(request, "customer.html", {"record": record})
    else:
        messages.warning(request, "You Must be Logged In !!")
        return redirect("home")


def delete_customer(request, pk):
    if request.user.is_authenticated:
        record = Customer.objects.get(pk=pk)
        record.delete()
        messages.success(request, "Sucessfully Deleted!!")
        return redirect("home")
    else:
        messages.warning(request, "You Must be Logged In !!")
        return redirect("home")


def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Sucessfully Added!!")
                return redirect("home")
        return render(request, "add_customer.html", {"form": form})
    else:
        messages.warning(request, "You Must be Logged In!!")
        return redirect("home")


def update_customer(request,pk):
    if request.user.is_authenticated:
        record = Customer.objects.get(pk=pk)
        form = AddCustomerForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Sucessfully Updated!!")
            return redirect("home")
        return render(request, "update_customer.html", {"form": form})
    else:
        messages.warning(request, "You Must be Logged In!!")
        return redirect("home")
