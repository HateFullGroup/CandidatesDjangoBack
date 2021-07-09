from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.fields import Field, ReadOnlyField

from candidates.models import Technology, Candidate, CandidateTechnology

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'name')

class CandidateTechnologySerializer(serializers.ModelSerializer):
    # candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())
    technology = serializers.IntegerField(write_only=True)
    technology_id = serializers.SerializerMethodField()
    candidate = serializers.IntegerField(required=False, write_only=True)
    technology_name = serializers.SerializerMethodField()

    class Meta:
        model = CandidateTechnology
        fields = ('knowledge_level', 'technology', 'technology_name', 'technology_id', 'candidate')
        extra_kwargs = {"candidate": {"required": False, "allow_null": True},
                        "technology": {"write_only": True},
                        }
        validators = []


    def get_technology_name(self, ct):
        return ct.technology.name

    def get_technology_id(self, ct):
        return ct.technology.id



class CandidateDetailSerializer(serializers.ModelSerializer):

    candidatetechnology_set = CandidateTechnologySerializer(many=True, partial=True)
    added_at = serializers.DateTimeField(format="%d.%m.%Y", read_only=True, )
    birth_date = serializers.DateTimeField(format="%d.%m.%Y", input_formats=['%d-%m-%Y', "%d.%m.%Y"])

    def validate_candidatetechnology_set(self, ct_set):
        technologies_used = []
        for ct in ct_set:
            if ct['technology'] in technologies_used:
                raise serializers.ValidationError('Unique constraint failed')
            technologies_used.append(ct['technology'])
        return ct_set

    class Meta:
        model = Candidate
        fields = ('id', 'f_i_o', 'birth_date', 'added_at', 'description', 'phone_number',
                  'feedback', 'place_of_employment', 'salary', 'job_position',
                  "candidatetechnology_set")
        read_only_fields = ('added_at',)

    def create(self, validated_data):
        # breakpoint()
        technologies_data = validated_data.pop('candidatetechnology_set')
        candidate = Candidate.objects.create(**validated_data)
        for technology in technologies_data:
            technology_object = Technology.objects.filter(pk=technology["technology"]).first()
            CandidateTechnology.objects.create(candidate=candidate,
                                               technology=technology_object,
                                               knowledge_level=technology['knowledge_level'])
        return CandidateDetailSerializer(candidate).data

    def update(self, instance, validated_data):
        instance.candidatetechnology_set.all().delete()
        candidatetechnology_set = validated_data.pop('candidatetechnology_set', None)
        for technology in candidatetechnology_set:
            technology_object = Technology.objects.filter(pk=technology["technology"]).first()
            CandidateTechnology.objects.create(candidate=instance,
                                               technology=technology_object,
                                               knowledge_level=technology['knowledge_level'])
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return CandidateDetailSerializer(instance).data

