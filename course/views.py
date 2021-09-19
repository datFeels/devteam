from django.shortcuts import redirect, render, get_object_or_404
from .forms import CourseForm, LectureForm
from .models import Course, Lecture
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory


@login_required(login_url='/login/')
def course_list(request):
    courses = Course.objects.all()
    qs_m1 = Lecture.objects.all().filter(course=17)
    qs_m2 = Lecture.objects.all().filter(course=18)
    qs_v1 = Lecture.objects.all().filter(course=19)
    qs_p1 = Lecture.objects.all().filter(course=20)
    context = {
        "courses": courses,
        "m1s": qs_m1,
        "m2s": qs_m2,
        "v1s": qs_v1,
        "p1s": qs_p1,
    }
    return render(request, "course/list.html", context)


@login_required(login_url='/login/')
def course_create_view(request):
    # look at whats being POSTED
    print(request.POST)
    # showing whatever in context in template
    form = CourseForm(request.POST or None)
    context = {
        "form": form,
    }
    # using model form
    if form.is_valid():
        form.save()
        context['form'] = CourseForm()
        return redirect('course-list')
    return render(request, "course/create.html", context=context)


@login_required(login_url='/login/')
def course_update_view(request, id=None):
    obj = Course.objects.all().filter(id=id).first()
    form = CourseForm(request.POST or None, instance=obj)
    LectureFormset = modelformset_factory(Lecture, form=LectureForm, extra=0)
    qs = Lecture.objects.all().filter(course=obj.id)
    formset = LectureFormset(request.POST or None, queryset=qs)
    # getting the object from model and parameter
    context = {
        "form": form,
        "formset": formset,
        "object": obj,
    }
    # using model form
    if all([form.is_valid(), formset.is_valid()]):
        # saving the course forms
        parent = form.save(commit=False)
        parent.save()
        # taking all the forms in formsets
        for form in formset:
            child = form.save(commit=False)
            # setting the course as the course's id
            child.course = parent
            child.save()
        context['message'] = 'Data saved.'
        return redirect("course-list")
    else:
        print("not working")
    return render(request, "course/update.html", context)
