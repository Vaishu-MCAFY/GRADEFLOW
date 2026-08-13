from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import StudentForm
from .upload_csv import upload_students_from_csv
from .mongodb import get_all_students
from .serializers import StudentSerializer

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "admin123":
            return redirect("dashboard")

        return render(request, "login.html", {
            "error": "Invalid Username or Password"
        })

    return render(request, "login.html")

def dashboard(request):

    context = {
        "total_students": 0,
        "average_marks": 0,
        "highest_marks": 0,
        "lowest_marks": 0,
        "topper": "",
        "at_risk_students": 0,
    }

    return render(request, "dashboard.html", context)

def student_list(request):

    students = get_all_students()

    return render(
        request,
        "student_list.html",
        {"students": students}
    )

def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(
        request,
        "add_student.html",
        {"form": form}
    )

def edit_student(request, student_id):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(
        request,
        "edit_student.html",
        {"form": form}
    )


def delete_student(request, student_id):

    return redirect("student_list")

def analytics(request):

    analytics_data = {
        "average": 0,
        "highest": 0,
        "lowest": 0,
        "topper": "",
        "at_risk": [],
    }

    return render(
        request,
        "analytics.html",
        analytics_data
    )

def upload_csv(request):

    if request.method == "POST":

        if "csv_file" not in request.FILES:
            return render(
                request,
                "upload.html",
                {"error": "Please select a CSV file."}
            )

        file = request.FILES["csv_file"]

        file_path = file.name

        with open(file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        total = upload_students_from_csv(file_path)

        return render(
            request,
            "upload.html",
            {
                "success": f"{total} students uploaded successfully."
            }
        )

    return render(request, "upload.html")

@api_view(["GET"])
def student_api(request):

    students = get_all_students()

    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)