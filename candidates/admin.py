from django.contrib import admin


# Register your models here.
from django.forms import ModelForm
from django import forms
from candidates.models import Technology, Candidate, CandidateTechnology


class CandidatesForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea, label="Описание")
    feedback = forms.CharField(widget=forms.Textarea, label="Отзыв")
    class Meta:
        model = Candidate
        fields = '__all__'


class CanditatesAdmin(admin.ModelAdmin):
    save_as = True
    form = CandidatesForm

    list_display = ('id', 'f_i_o', 'phone_number', 'birth_date', 'added_at', 'description',
              'feedback', 'place_of_employment', 'salary', 'job_position')
    fields = ('f_i_o', 'phone_number', 'birth_date', 'added_at', 'description',
              'feedback', 'place_of_employment', 'salary', 'job_position')
    list_display_links = ('id', 'f_i_o')
    search_fields = ('f_i_o', )
    # list_filter = ('technologies', )
    readonly_fields = ('added_at', )
    # list_display = [field.name for field in Candidate._meta.get_fields()]
    # list_display = ('id', 'f_i_o', 'number', 'created_at', 'updated_at', 'is_published')
    # list_display_links = ('id', 'title')
    # search_fields = ('title', 'content')
    # list_editable = ('is_published',)

    # number = models.CharField(max_length=255, verbose_name='Телефон')
    # f_i_o = models.CharField(max_length=255, verbose_name='ФИО', null=False)
    # birth_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата рождения', null=False)
    # added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    # description = models.CharField(max_length=255, verbose_name='Описание', null=False)
    # feedback = models.CharField(max_length=255, verbose_name='Отзыв', null=False)
    # place_of_employment = models.CharField(max_length=255, verbose_name='Место работы', null=False)
    # salary = models.IntegerField(default=0)



class TechnologiesAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    search_fields = ('title',)


class CandidateTechnologyAdmin(admin.ModelAdmin):
    id = forms.CharField(label="connection_id")
    list_display = ('id', 'candidate', 'technology', 'candidate_id', 'technology_id')
    # fields = ('candidate', 'technology')
    search_fields = ('candidate', 'technology')
    list_filter = ('technology',)
    # search_fields =
admin.site.register(Technology, TechnologiesAdmin)
admin.site.register(Candidate, CanditatesAdmin)
admin.site.register(CandidateTechnology, CandidateTechnologyAdmin)