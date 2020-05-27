from django.shortcuts import render,HttpResponse,redirect,reverse
from .models import Course, Category
from user.models import User
from django.contrib.auth.decorators import login_required,permission_required
import re
import os
from django.http import StreamingHttpResponse
# Create your views here.

@permission_required(perm = '',login_url='')
def index_handler(request):
    context = request.context
    category_s = Category.objects.all()
    course_data_s = []
    for category in category_s:
        course_data_s.append(
            {
                'category': category.name,
                'course_s': category.course_set.all()
            }
        )
    context['course_data_s'] = course_data_s
    return render(request, 'index.html', context)



def course_handler(request,course_id):
    context = request.context
    try:
        course = Course.objects.get(id = course_id)
        session_user = request.session.get('session_user',None)
        if session_user:
            context['view_perssion'] = User.objects.filter(id = session_user.get('id'),userBuyer_set__id = course.id).exists()
        context['course'] = course
        return render(request,'course.html',context)
    except Exception as e:
        print(e)
        return HttpResponse(status = 200)



def video_handler(request,course_id):
    context = request.context
    try:
        course = Course.objects.get(id = course_id)
        session_user = request.session['session_user']
        #判断用户是否购买
        boolean_buyed = User.objects.filter(id = session_user.get('id'),userBuyer_set__id = course_id).exists()
        if boolean_buyed:
            context['course'] = course
            return render(request, 'video.html',context)
        else:
            return redirect(reverse('course_course',args=(course.id,)))
    except:
        return HttpResponse(status = 404)


def videoStream_handler(request,course_id):
    context = request.context
    def read_video(filepath,length,offset):
        with open(filepath,'rb') as f:
            #跳过offset
            f.seek(offset)
            while True:
                data = f.read(length)
                if data:yield data
                else:
                    break

    try:
        course = Course.objects.get(id=course_id)
        session_user = request.session['session_user']
        # 判断用户是否购买
        boolean_buyed = User.objects.filter(id=session_user.get('id'), userBuyer_set__id=course_id).exists()
        if boolean_buyed:
            context['course'] = course
            size = os.path.getsize(course.fileName.__str__())
            request_range = request.headers.get('range')
            start_bytes = re.findall('=(\d+)-',request_range)
            start_bytes = int(start_bytes[0]) if start_bytes else 0
            last_bytes = start_bytes +1024 * 1024
            last_bytes = min(last_bytes,size - 1)
            length = last_bytes - start_bytes + 1
            #StreamingHttpResponse（生成器，状态码） 三个参数
            response = StreamingHttpResponse(
                read_video(course.fileName.__str__(),
                           length=length,
                           offset = start_bytes,),
                status = 206
            )

            response['Content-Length'] = str(length)
            response['Content-Range'] = 'bytes %s-%s/%s' %(start_bytes,last_bytes,size)#初始位置 结束位置 大小
            return response
        else:

            return redirect(reverse('course_course', args=(course.id,)))
    except:
        return HttpResponse(status=404)