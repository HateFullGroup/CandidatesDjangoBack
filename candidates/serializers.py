from rest_framework import serializers

from candidates.models import Technology, Candidate


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'
        # fields = ('id', 'name')
        # readonly_fields = ('canditatetechnology',)

class CandidateDetailSerializer(serializers.ModelSerializer):
    technology = TechnologySerializer(many=True)
    class Meta:
        model = Candidate
        fields = ('id', 'f_i_o', 'birth_date', 'added_at', 'description',
                  'feedback', 'place_of_employment', 'salary', 'job_position', 'technology')

# phone_number = models.CharField(max_length=255, verbose_name='Телефон')
#     f_i_o = models.CharField(max_length=255, verbose_name='ФИО', null=False)
#     birth_date = models.DateTimeField(verbose_name='Дата рождения', null=False)
#     added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
#     description = models.CharField(max_length=255, verbose_name='Описание', null=False)
#     feedback = models.CharField(max_length=255, verbose_name='Отзыв', null=False)
#     place_of_employment = models.CharField(max_length=255, verbose_name='Место работы', null=False)
#     salary = models.IntegerField(default=0)
#     job_position = models.CharField(max_length=255, verbose_name='Место работы', null=False)
#     # candidate_technologies = models.ForeignKey('CandidateTechnologies', on_delete=models.PROTECT(), related_name='candidate_technology')
#     technology = models.ManyToManyField('Technology')