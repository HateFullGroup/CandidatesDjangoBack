from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.fields import Field, ReadOnlyField

from candidates.models import Technology, Candidate, CandidateTechnology



class TechnologySerializer(serializers.ModelSerializer):
    # knowledge_level = serializers.SerializerMethodField('get_knowledge_level_from_user')
    # lvl = serializers.SerializerMethodField()
    # lvl = serializers.CharField(read_only=True, source="candidatetechnology.knowledge_level")
    class Meta:
        model = Technology
        # fields = '__all__'
        fields = ('id', 'name')
        # readonly_fields = ('canditatetechnology',)
    # def get_lvl(self):



class CandidateTechnologySerializer(serializers.ModelSerializer):

    # technology = serializers.IntegerField(write_only=True)

    candidate = serializers.IntegerField(required=False, write_only=True)
    technology_name = serializers.SerializerMethodField()
    def get_technology_name(self, ct):
        # return Technology.objects.first(id=self.technology).name

        return ct.technology.name

    # def validate(self, attrs):
    #     breakpoint()
    #     return attrs
    # def validate_technology(self, attrs):
    #     breakpoint()
    #     return attrs
    # optional_fields = ['candidate', ]

    # def __init__(self, *args, **kwargs):
    #
    #     # Don't return emails when listing users
    #     if kwargs['context']['view'].action == 'list':
    #         del self.fields['email']
    #
    #     super().__init__(*args, **kwargs)

    # def to_representation(self, instance):
    #     self._context["request"] = self.parent.context["request"]
    #     return super().to_representation(instance)

    class Meta:
        model = CandidateTechnology
        # fields = ('candidate_id', 'technology_id', 'knowledge_level')
        # depth = 1
        fields = ('knowledge_level', 'technology', 'technology_name', 'candidate')
        extra_kwargs = {"candidate": {"required": False, "allow_null": True},
                        "technology": {"write_only": True},
                        }
        validators = []
    # def get_validation_exclusions(self):
    #     exclusions = super(CandidateTechnologySerializer, self).get_validation_exclusions()
    #     return exclusions + ['candidate']
    # extra_kwargs = {
    #     'security_question': {'write_only': True},
    #     'security_question_answer': {'write_only': True},
    #     'password': {'write_only': True}
    # }

class CandidateDetailSerializer(serializers.ModelSerializer):
    # Apply custom validation either here, or in the view.
    # def validate(self, attrs):
    #     pass

    # technologies = ReadOnlyField(source='get_technologies')
    # candidatetechnology_set = CandidateTechnologySerializer(many=True, write_only=True)
    candidatetechnology_set = CandidateTechnologySerializer(many=True, partial=True)

    # serializer = CommentSerializer(comment, data={'content': u'foo bar'}, partial=True)

    #
    # def validate_candidatetechnology_set(self, a = 5):
    #     breakpoint()
    #     a = 5

    class Meta:
        model = Candidate
        fields = ('id', 'f_i_o', 'birth_date', 'added_at', 'description',
                  'feedback', 'place_of_employment', 'salary', 'job_position',
                  "candidatetechnology_set")
        # fields = ('id', 'f_i_o', 'birth_date', 'added_at', 'description',
        #           'feedback', 'place_of_employment', 'salary', 'job_position', 'technologies', "candidatetechnology_set")
        read_only_fields = ('added_at',)
        # extra_kwargs = {
        #     'technologies': {'required': False},
        # }
        # depth = 3

    # def get_technologies(self, candidate):
    #     candidate = Candidate.objects.filter(id=self.id)\
    #         .prefetch_related('candidatetechnology_set', 'technology_set').first()
    #     technologies = candidate.technology_set.all()
    #     candidate_technologies = candidate.candidatetechnology_set.all()
    #     return {t.name: ct.knowledge_level for (t, ct) in zip(technologies, candidate_technologies)}
    #
    # def perform_create(self, serializer):
    #     # The request user is et as author automatically.
    #     candidatetechnology_set.save(candidate=self.request.user)

    def create(self, validated_data):

        technologies_data = validated_data.pop('candidatetechnology_set')
        candidate = Candidate(**validated_data)
        candidate.save()
        # candidate = Candidate.objects.create(**validated_data)
        # breakpoint()
        # self.candidatetechnology_set.save(candidate=candidate)
        # print(technologies_data)
        # breakpoint()


        for technology in technologies_data:
            technology.pop("candidate", None)
            technology_object = Technology.objects.filter(pk=technology["technology"]).first()
            # breakpoint()
            # CandidateTechnology.objects.create(candidate=candidate,
            #                                    technology=technology.technology_id,
            #                                    knowledge_level=technology.knowledge_level)
            # breakpoint()
            # CandidateTechnology.objects.create(candidate_id=candidate.id,
            #                                    technology=technology_object,
            #                                    knowledge_level=technology['knowledge_level'])


            CandidateTechnology.objects.create(candidate=candidate,
                                               technology=technology_object,
                                               knowledge_level=technology['knowledge_level'])
        return CandidateDetailSerializer(candidate).data