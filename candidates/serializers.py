
from rest_framework import serializers
from rest_framework.fields import Field, ReadOnlyField

from candidates.models import Technology, Candidate, CandidateTechnology


def get_knowledge_level_from_candidate_technology(technology):
    return CandidateTechnology.objects.filter(pk=technology.id).knowledge_level


class TechnologySerializer(serializers.ModelSerializer):
    # knowledge_level = serializers.SerializerMethodField('get_knowledge_level_from_user')
    # lvl = serializers.SerializerMethodField()
    # lvl = serializers.CharField(read_only=True, source="candidatetechnology.knowledge_level")
    class Meta:
        model = Technology
        # fields = '__all__'
        fields = ('id', 'name', 'lvl')
        # readonly_fields = ('canditatetechnology',)
    # def get_lvl(self):



class CandidateTechnologySerializer(serializers.ModelSerializer):


    # techname = serializers.SerializerMethodField('get_name_from_technology')
    # lvl = serializers.SerializerMethodField('get_knowledge_level_from_candidate_technology')
    lvl = serializers.SerializerMethodField()
    # tech = serializers.CharField(read_only=True, source="technology.name")
    class Meta:
        model = CandidateTechnology
        # fields = '__all__'
        # fields = ['techname', 'technology_id', 'knowledge_level', 'lvl']
        # fields = ('id', 'knowledge_level')
        # fields = '__all__'
        fields = ('knowledge_level', 'lvl', 'id','tech')
        depth = 0

    # def to_internal_value(self, data): self.initial_data = data
 
    # def get_name_from_technology(self, technology):
    #     # print(candidate_technology.__dict__)
    #     return technology.name
    def get_lvl(self, a):
        # print('new', self.initial_data.__dict__, end='\n\n\n')


        # print(self.initial_data)
        # print('a', a.__dict__, end='\n\n\n')
        # c =  CandidateTechnology.objects.first(candidate_id=self.data['id'], technology_id=a.id)
        # print(c)
        return 'xd'

    def get_knowledge_level_from_candidate_technology(self, technology):
        return CandidateTechnology.objects.filter(pk=technology.id).knowledge_level

class CandidateDetailSerializer(serializers.ModelSerializer):




    # technologies = CandidateTechnologySerializer()

    # technologies = CandidateTechnologySerializer( many=True)
    # a = serializers.SerializerMethodField(source='get_technologies')

    technologies = ReadOnlyField(source='get_technologies')

    # def get_technologies(self, obj):
    #     # print(obj.__dict__)
    #     queryset = CandidateTechnology.objects.filter(id=obj.id)
    #     # print(obj.id)
    #     # print(queryset)
    #     for x in queryset:
    #         print(x)
    #     # serializer = CandidateTechnologySerializer(queryset)
    #     return serializer.data

    # technologies = CandidateTechnologySerializer(many=True)


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
        depth = 3
        read_only_fields = (
            'a',
        )
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
