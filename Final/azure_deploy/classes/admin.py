from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Course, Attendance, Participation

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('courses',)

class CustomAttendanceAdmin(admin.ModelAdmin):
    fields = ('user', 'course', 'date', 'is_attended')

class CustomParticipationAdmin(admin.ModelAdmin):
    fields = ('user', 'course', 'date', 'amount')

admin.site.register(Attendance, CustomAttendanceAdmin)
admin.site.register(Participation, CustomParticipationAdmin)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = ['username', 'first_name', 'last_name', 'email', 'age', 'degree', 'semester', 'is_staff', 'is_superuser', 'display_courses','photo','face_encoding']
    #edit courses
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('courses','photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {'fields': ('courses','photo')}),
    )

    def display_courses(self, obj):
        return ", ".join([course.name for course in obj.courses.all()])

    display_courses.short_description = 'Courses'
admin.site.register(Course, CourseAdmin)

admin.site.register(CustomUser, CustomUserAdmin)







