from rest_framework import serializers
from .models import Model, Certification, Base


class ModelDPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('id', 'model_name', 'form_certificate', )


class BaseDPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        exclude = ('zonder_line', 'acoustic_insulation_line')


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('id', 'model_name', 'form_certificate', 'model_postfix', 'application',
                  'intended_use_rus', 'intended_use_eng', )


class CertificateSerializer(serializers.ModelSerializer):

    # model = serializers.SlugRelatedField(slug_field="model_name", read_only=True)
    operator = serializers.SlugRelatedField(slug_field="name_rus", read_only=True)
    controller = serializers.SlugRelatedField(slug_field="name_rus", read_only=True)
    base = BaseDPCSerializer(many=False, read_only=True)
    model = ModelSerializer(many=False, read_only=True)

    class Meta:
        model = Certification
        # fields = ('id', 'model', 'afc_maximum_s_rel', 'echo_pulse_duration', 'afc_frequency_maximum',
        #           'operator', 'controller', 'base', )
        exclude = ('ascan',)


class CertificateSNRangeSerializer(serializers.ModelSerializer):
    model = serializers.SlugRelatedField(slug_field="model_name", read_only=True)
    operator = serializers.SlugRelatedField(slug_field="name_rus", read_only=True)
    controller = serializers.SlugRelatedField(slug_field="name_rus", read_only=True)

    class Meta:
        model = Certification
        # fields = ('id', 'model_id',)
        # fields = ('id', 'afc_maximum_s_rel', 'echo_pulse_duration', 'afc_frequency_maximum',)
        exclude = ('ascan', )
