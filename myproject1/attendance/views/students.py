from django.views import generic

from ..models.students import Student

class StudentListView(generic.ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'attendance/students/student_list.html'
    
class StudentDetailView(generic.DetailView):
    model = Student
    context_object_name ='student_detail'
    template_name = 'attendance/students/student_detail.html'
    
class StudentCreateView(generic.CreateView):
    model = Student
    fields = [
        'fname',
        'lname',
        'document_type',
        'document_number',
        'cohorte'
    ]
    template_name = 'attendance/students/student_form.html'