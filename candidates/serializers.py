from rest_framework import serializers

from candidates.models import Technology, Candidate, CandidateTechnology


def get_knowledge_level_from_candidate_technology(technology):
    return CandidateTechnology.objects.filter(pk=technology.id).knowledge_level


class TechnologySerializer(serializers.ModelSerializer):
    # knowledge_level = serializers.SerializerMethodField('get_knowledge_level_from_user')
    class Meta:
        model = Technology
        # fields = '__all__'
        fields = ('id', 'name')
        # readonly_fields = ('canditatetechnology',)


class CandidateTechnologySerializer(serializers.ModelSerializer):
    # techname = serializers.SerializerMethodField('get_name_from_technology')
    # lvl = serializers.SerializerMethodField('get_knowledge_level_from_candidate_technology')
    class Meta:
        model = CandidateTechnology
        # fields = '__all__'
        # fields = ['techname', 'technology_id', 'knowledge_level', 'lvl']
        # fields = ('id', 'knowledge_level')
        fields = '__all__'
        depth = 1

    # def get_name_from_technology(self, technology):
    #     # print(candidate_technology.__dict__)
    #     return technology.name

    def get_knowledge_level_from_candidate_technology(self, technology):
        return CandidateTechnology.objects.filter(pk=technology.id).knowledge_level

class CandidateDetailSerializer(serializers.ModelSerializer):
    # technologies = CandidateTechnologySerializer()
    technologies = TechnologySerializer(many=True, read_only=True)
    # def __init__(self):
    #     super().__init__()
    #     user = None
    #     request = self.context.get("request")
    #     if request and hasattr(request, "user"):
    #         user = request.user
    #     technologies = TechnologySerializer(many=True, context={'user_id': self.user.id})
    class Meta:
        model = Candidate
        fields = ('id', 'f_i_o', 'birth_date', 'added_at', 'description',
                  'feedback', 'place_of_employment', 'salary', 'job_position', 'technologies')
        # read_only_fields = (
        #     'technologies',
        # )
        # extra_kwargs = {'feedback': {'required': False}}

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
