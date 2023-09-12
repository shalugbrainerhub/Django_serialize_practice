from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View
from .models import *
from testapp.mixin import SerializeMixin
from django.core.serializers import serialize

# Create your views here.


# def emp_data_view(request):
#     emp_data={
#         'eno':100,
#         'ename':'abcd',
#         'esal':1000,
#         'eaddr':'mumbai',
#     }
#     resp='Employee Number:{}Employee Name:{}Employee Salary:{}Employee Address:{}'.format(emp_data['eno'], emp_data['ename'], emp_data['esal'], emp_data['eaddr'])

#     return HttpResponse(resp)



# def emp_data_json_view(request):
#      emp_data={
#         'eno':100,
#         'ename':'abcd',
#         'esal':1000,
#         'eaddr':'mumbai',
#     }
#     #  converting python dict into JSON

#      json_data=json.dumps(emp_data)  

#      return HttpResponse(json_data, content_type='application/json')


# def emp_data_jsonresponse_view(request):
#       emp_data={
#         'eno':100,
#         'ename':'abcd',
#         'esal':1000,
#         'eaddr':'mumbai',
#     }
      
#       return JsonResponse(emp_data)



# from django.views.generic import View
# # class JsonCBV(View):
# #      def get(self, request, *args, **kwargs):
# #            emp_data={
# #             'eno':100,
# #             'ename':'abcd',
# #             'esal':1000,
# #             'eaddr':'mumbai',
# #             }
# #            return JsonResponse(emp_data)
    
      
# from testapp.mixin import HttpResponseMixin

# class JsonCBV2(HttpResponseMixin,View):
#      def get(self, request, *args, **kwargs):
#           json_data=json.dumps({'msg':'This is from get method..............'})
#           return self.render_to_http_response(json_data)
#         #   return HttpResponse(json_data, content_type='application/json')
          
#      def post(self, request, *args, **kwargs):
#           json_data=json.dumps({'msg':'This is from post method'})
#           return self.render_to_http_response(json_data)
#         #   return HttpResponse(json_data, content_type='application/json')
     
#      def put(self, request, *args, **kwargs):
#           json_data=json.dumps({'msg':'This is from put method'})
#           return self.render_to_http_response(json_data)
#         #   return HttpResponse(json_data, content_type='application/json')
     
#      def delete(self, request, *args, **kwargs):
#           json_data=json.dumps({'msg':'This is from delete method'})
#           return self.render_to_http_response(json_data)
#         #   return HttpResponse(json_data, content_type='application/json')
    
    

from django.core.serializers import serialize


class EmployeeDetailsCBV(View):
    def get(self, request, id, *args, **kwargs):
        emp=Employee.objects.get(id=id)
        # emp_data={
        #     'eno':emp.eno,
        #     'ename':emp.ename,
        #     'esal':emp.esal,
        #     'eaddr':emp.eaddr,
        # }

        # json_data=json.dumps(emp_data)
        json_data=serialize('json',[emp,])
        return HttpResponse(json_data, content_type='application/json')


class EmployeeListCBV( SerializeMixin,View):
    def get(self, request, *args, **kwargs):
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json')




