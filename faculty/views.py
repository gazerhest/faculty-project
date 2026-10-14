from django.shortcuts import render, get_object_or_404
from .models import FacultyInfo, Department, Teacher, Program, ExchangeProgram

def index(request):
    faculty_info = FacultyInfo.objects.first()
    context = {
        'faculty_info':faculty_info
    }
    return render(request, 'faculty/index.html', context=context)

def programs_list(request):
    programs = Program.objects.all()
    context = {
        'programs':programs
    }
    return render(request, 'faculty/programs_list.html', context=context)

def program_detail(request, program_id):
    program = get_object_or_404(Program.objects.select_related('department'), id=program_id)
    disciplines_list = [d.strip() for d in program.disciplines.split(',') if d.strip()]
    context = {
        'program':program,
        'disciplines_list':disciplines_list
    }
    return render(request, 'faculty/program_detail.html', context=context)

def departments_list(request):
    departments = Department.objects.prefetch_related('programs').all()
    context = {
        'departments':departments
    }
    return render(request, 'faculty/departments_list.html', context=context)

def department_detail(request, department_id):
    department = get_object_or_404(
        Department.objects.prefetch_related('programs', 'teachers'),
        id=department_id
    )
    context = {
        'department':department
    }
    return render(request, 'faculty/department_detail.html', context=context)

def exchange_list(request):
    programs = ExchangeProgram.objects.all().order_by('deadline')
    context = {
        'programs':programs
    }
    return render(request, 'faculty/exchange_list.html', context=context)
