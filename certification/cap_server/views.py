from django.db.models import Count
from django.shortcuts import render
from .forms import SearchCertificate
from django.db.models import Avg, Max, Min
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Model, Certification, Operators, Controllers
from .repository import dpc_fft
from django.conf import settings
import datetime
from .serializers import ModelDPCSerializer, CertificateSerializer, CertificateSNRangeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer


def home_page(request):
    return render(request, 'homePage.html')


def search_certificate(request):
    certificate = Certification.manager
    model = Model.manager
    if request.method == 'POST':
        form_request = SearchCertificate(request.POST)
        if form_request.is_valid():
            res = (certificate.filter(model_id=model.get(model_name=form_request.cleaned_data['model']).id,
                                      serial_number__gte=form_request.cleaned_data['serialNumberDown'].upper(),
                                      serial_number__lte=form_request.cleaned_data['serialNumberUp'].upper(),
                                      date_time__gte=form_request.cleaned_data['date_time_first'],
                                      date_time__lte=form_request.cleaned_data['date_time_last'],
                                      verification_stage__in=form_request.cleaned_data['verification'],
                                      result=form_request.cleaned_data['result']).select_related('model'))
            stat = res.values('serial_number').annotate(num=Count('model')).filter(num__gt=1)
            return render(request, 'searchCertificate.html', {'form': form_request, 'res': res, 'stat': stat})
        return render(request, 'searchCertificate.html', {'form': form_request.errors})
    else:
        aggSN = certificate.aggregate(minSN=Min('serial_number'), maxSN=Max('serial_number'))
        form = SearchCertificate(initial={'serialNumberDown': aggSN['minSN'],
                                          'serialNumberUp': aggSN['maxSN'],
                                          'result': True})
        return render(request, 'searchCertificate.html', {'form': form})


def preview_certificate(request):
    if request.method == 'POST':
        certificate = Certification.manager
        pk_certificate = request.POST.getlist('checks')
        lang = request.POST.get('lang')
        if lang == "RUS":
            template = 'certificate.html'
        else:
            template = 'certificate_eng.html'
        forms = certificate.filter(pk__in=pk_certificate).select_related('operator', 'model',
                                                                         'controller', 'base', 'settings')
        prefix = datetime.datetime.now().strftime('%s')
        osc_dir = str(settings.STATIC_URL) + 'temp/osc' + prefix
        fft_dir = str(settings.STATIC_URL) + 'temp/fft' + prefix
        dpc_fft(forms, osc_dir, fft_dir)
        osc_dir_tmp = 'temp/osc' + prefix
        fft_dir_tmp = 'temp/fft' + prefix
        return render(request, template, {'forms': forms, 'osc_dir': osc_dir_tmp, 'fft_dir': fft_dir_tmp})


def statistics(request):
    certificate = Certification.manager
    total = certificate.count()
    forms = certificate.values('model__model_name').annotate(num=Count('model'))
    return render(request, 'statistics.html', {'total': total, 'forms': forms})


@api_view(['GET'])
def dpc_models(request):
    if request.method == 'GET':
        models = Model.manager.order_by('model_name').all()
        serializers = ModelDPCSerializer(models, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def dpc_models_detail(request, pk):
    if request.method == 'GET':
        model = Model.manager.get(id=pk)
        serializers = ModelDPCSerializer(model)
        return Response(serializers.data)


@api_view(['GET'])
def dpc_certificate_detail(request, pk):
    if request.method == 'GET':
        cartificate = Certification.manager.get(id=pk)
        serializers = CertificateSerializer(cartificate)
        return Response(serializers.data)


# @api_view(['GET'])
# def dpc_certificate_detail_range(request, pk):
#     if request.method == 'GET':
#         cartificate = Certification.manager.all()
#         serializers = CertificateSerializer(cartificate)
#         return Response(serializers.data)


@api_view(['GET'])
def dpc_certificate_sn_range(request, pk, stage):
    if request.method == 'GET':
        stage = str(stage).split(',')
        sn_max = Certification.manager.filter(model_id=pk, verification_stage__in=stage).aggregate(Max('serial_number'))
        sn_min = Certification.manager.filter(model_id=pk, verification_stage__in=stage).aggregate(Min('serial_number'))
        return JsonResponse({'sn_max': sn_max.get('serial_number__max'), 'sn_min': sn_min.get('serial_number__min')})


@api_view(['GET'])
def dpc_certificate_sn_range_preview(request, pk, stage, sn_min, sn_max):
    if request.method == 'GET':
        # model = Model.manager.all()
        # serializers = ModelDPCSerializer(models, many=True)
        certificate = Certification.manager
        sn_mn = str(sn_min).upper()
        sn_mx = str(sn_max).upper()
        stage = str(stage).split(',')
        print(pk, stage, sn_min, sn_max)
        res = certificate.filter(model_id=pk,
                                 verification_stage__in=stage,
                                 serial_number__gte=sn_mn,
                                 serial_number__lte=sn_mx)
        print(res)
        # return JsonResponse(list(res), safe=False)
        serializers = CertificateSNRangeSerializer(res, many=True)
        return Response(serializers.data)

# дописать модуль статистики