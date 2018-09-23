import traceback

from rest_framework import viewsets
from ..serializers.ruleSerializers import *
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import View
import datetime
from django.http import HttpResponse
import pdb



# Rule Methods
class RuleViewSet(viewsets.ModelViewSet):
    def create(self, request, *args):
        try:
            serializer = RuleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response("Success", status=status.HTTP_201_CREATED)
        except:
            return Response("Unable to create Rules", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, *args, pk=None):
        try:
            rule_obj = Rules.objects.filter(rule_id=pk)
            if rule_obj:
                return Response(RuleSerializer(rule_obj, many=True).data, status=status.HTTP_200_OK)
            else:
                return Response("Rule with particular rule id does not exist.", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Unable to get rule", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request, *args):
        try:
            rule_obj = Rules.objects.all()
            return Response(RuleSerializer(rule_obj, many=True).data,status=status.HTTP_200_OK)
        except:
            return Response("Unable to get Rules", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, *args, pk=None):
        try:
            rule_obj = Rules.objects.filter(rule_id=pk)
            if rule_obj:
                serializer = RuleSerializer(rule_obj[0], data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response("Rule with particular rule id does not exist.", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Unable to Update rule", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def destroy(self, request, *args, pk=None):
        try:
            rule_obj = Rules.objects.filter(rule_id=pk)
            if rule_obj:
                rule_obj.delete()
                return Response("Rule successfully deleted", status=status.HTTP_200_OK)
            else:
                return Response("Rule already deleted or does not exist", status=status.HTTP_200_OK)

        except:
            return Response("Unable to Delete Rule: %s" % traceback.format_exc(), status=status.HTTP_404_NOT_FOUND)


    def filter_data(self, request, *args):
        try:
            result_list = list()
            rule_list = list()
            if 'data' not in request.data:
                return Response("Please provide data",status=status.HTTP_400_BAD_REQUEST)
            if 'rules' not in request.data or type(request.data['rules']) is not list:
                return Response("Please provide rules in list format",status=status.HTTP_400_BAD_REQUEST)

            for each_rule in request.data['rules']:
                each_dict = dict()
                each_rule_obj = Rules.objects.filter(rule_id=each_rule)
                if not each_rule_obj:
                    return Response("Rule with respective id does not exist",status=status.HTTP_400_BAD_REQUEST)
                each_dict['signal'] = each_rule_obj.values()[0]['signal']
                each_dict['value'] = each_rule_obj.values()[0]['value']
                each_dict['value_type'] = each_rule_obj.values()[0]['value_type']
                each_dict['criteria'] = each_rule_obj.values()[0]['criteria']
                rule_list.append(each_dict)

            for each_data in request.data['data']:
                for each_rule in rule_list:
                    signal = each_rule['signal']
                    value = each_rule['value']
                    value_type = each_rule['value_type']
                    criteria = each_rule['criteria']
                    if each_data['signal'] == signal and each_data['value_type'] == value_type:
                        if value_type == 'Datetime':
                            data_date = datetime.datetime.strptime(each_data['value'],"%Y-%m-%d %H:%M:%S")
                            rule_date = datetime.datetime.strptime(value,"%Y-%m-%d %H:%M:%S")
                            if not eval(repr(data_date)+criteria+repr(rule_date)):
                                result_list.append(each_data)
                        elif value_type == 'String':
                            if not eval(repr(each_data['value'])+criteria+repr(value)):
                                result_list.append(each_data)
                        else:
                            if not eval(each_data['value']+criteria+value):
                                result_list.append(each_data)


            return Response(result_list, status=status.HTTP_200_OK)
        except:
            return Response("Unable to filter data: %s" % traceback.format_exc(), status=status.HTTP_404_NOT_FOUND)





# Healthcheck Methods
class healthcheck_view(View):
    def get(self, request):
        return HttpResponse()
