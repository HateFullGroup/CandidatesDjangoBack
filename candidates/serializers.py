from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.fields import Field, ReadOnlyField

from candidates.models import Technology, Candidate, CandidateTechnology

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'name')

class CandidateTechnologySerializer(serializers.ModelSerializer):

    technology = serializers.IntegerField(write_only=True)
    candidate = serializers.IntegerField(required=False, write_only=True)
    technology_name = serializers.SerializerMethodField()

    def get_technology_name(self, ct):
        return ct.technology.name

    class Meta:
        model = CandidateTechnology
        fields = ('knowledge_level', 'technology', 'technology_name', 'candidate')
        extra_kwargs = {"candidate": {"required": False, "allow_null": True},
                        "technology": {"write_only": True},
                        }
        validators = []

    # def validate(self, data):
    #     breakpoint()
    #     if data['start_date'] > data['end_date']:
    #         raise serializers.ValidationError("finish must occur after start")
    #     return data

class CandidateDetailSerializer(serializers.ModelSerializer):
    candidatetechnology_set = CandidateTechnologySerializer(many=True, partial=True)
    class Meta:
        model = Candidate
        fields = ('id', 'f_i_o', 'birth_date', 'added_at', 'description', 'phone_number',
                  'feedback', 'place_of_employment', 'salary', 'job_position',
                  "candidatetechnology_set")
        read_only_fields = ('added_at',)
        # extra_kwargs = {
        #             "id": {"write_only": True},
        #                 }

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

        candidatetechnology_set = validated_data.pop('candidatetechnology_set', None)
        # instance.nr = validated_data.get('nr', instance.nr)
        # instance.title = validated_data.get('title', instance.title)
        # breakpoint()
        # instance.super().
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        instance.candidatetechnology_set.all().delete()



        # breakpoint()
        # serializer =
        # Candidate.objects.filter(pk=instance.pk).update(**validated_data)
        # instance.save()
        # breakpoint()

        # items = validated_data.get('items')

        # def update(self, instance, validated_data):

        # breakpoint()

        # for item in candidatetechnology_set:
        #     item_id = item.get('id', None)
        #     if item_id:
        #         inv_item = InvoiceItem.objects.get(id=item_id, invoice=instance)
        #         inv_item.name = item.get('name', inv_item.name)
        #         inv_item.price = item.get('price', inv_item.price)
        #         inv_item.save()
        #     else:
        #         InvoiceItem.objects.create(account=instance, **item)


        # result = {}
        #
        # for key, value in input_raw.items():
        #     if value not in result.values():
        #         result[key] = value

        # candidatetechnology_set_clean = {}

        # technologies_set_clean = {}
        # for technology in candidatetechnology_set:
        #     if technology['technology'] not in technologies_set_clean:
        #         technologies_set_clean[technology['technology']] = technology['knowledge_level']
        # breakpoint()

        return CandidateDetailSerializer(instance).data