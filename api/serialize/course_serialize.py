from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api import models
from api import models

from rest_framework import serializers
# 课程
class CourseSerializer(serializers.ModelSerializer):

    # course_img = serializers.CharField(source='course_img')
    # sub_category = serializers.CharField(source='cosub_category')
    course_type = serializers.CharField(source='get_course_type_display')
    sub_category = serializers.CharField(source='sub_category.name')
    degree_course = serializers.CharField(source='degree_course.name')
    level = serializers.CharField(source='get_level_display')
    status = serializers.CharField(source='get_status_display')
    price_policy =serializers.SerializerMethodField()
    asked_question =serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields =['id','name','course_img','course_type','sub_category','degree_course','brief','level','pub_date',
                 'period','order','status','template_id','price_policy','asked_question']
    def get_asked_question(self,obj):
        queryset = obj.asked_question.all()
        return [{'question':row.question,'answer':row.answer}for row in queryset]

    def get_price_policy(self,obj):
        queryset = obj.price_policy.all()
        return [{'price':row.price,'valid_period':row.get_valid_period_display()}for row in queryset]
       # depth = 1  # 0-10  找层级 表

# 课程详细
class CourseDetailSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(source='course.title')
    # img = serializers.CharField(source='course.course_img')
    # level = serializers.CharField(source='course.get_level_display')

    recommend_courses =serializers.SerializerMethodField()
    teachers =serializers.SerializerMethodField()
    # recommends = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ['hours','course_slogan','video_brief_link','why_study','what_to_study_brief',
                  'career_improvement','prerequisite','recommend_courses','teachers'
                  ]
    def get_recommend_courses(self,obj):
        queryste = obj.recommend_courses.all()
        return [{'name':row.name,'course_type':row.get_course_type_display(),'level':row.get_level_display()}for row in queryste]
    def get_teachers(self,obj):
        queryste = obj.teachers.all()
        return [{'name':row.name,'role':row.get_role_display(),'title':row.title,'signature':row.signature}for row in queryste]
    # def get_recommends(self, obj):  # 一对多 多对多用这种方式
    #     # 获取推荐的所有课程
    #     queryset = obj.recommend_courses.all()
    #
    #     return [{'id': row.id, 'title': row.title} for row in queryset]
