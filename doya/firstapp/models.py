from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class voluteers(models.Model):
    pass


class best_volunteers(models.Model):
    pass


area_lst = (('Seoul', '서울특별시'), ('Incheon', '인천광역시'), ('Gyeonggi-do', '경기도'), ('Gangwon-do', '강원도'),
            ('Chungcheongnam-do', '충청남도'), ('Sejong', '세종특별자치시'), ('Daejeon', '대전광역시'), ('Chungcheongbuk-do', '충청북도'),
            ('Gyeongsangbuk-do', '경상북도'), ('Gyeongsangnam-do', '경상남도'), ('Daegu', '대구광역시'), ('Jeollabuk-do', '전라북도'), 
            ('Jeollanam-do', '전라남도'), ('Gwangju', '광주광역시'), ('Ulsan', '울산광역시'), ('Busan', '부산광역시'), ('Jeju', '제주특별자치시도'))

voluteer_type_lst = (('type_1', '자연환경보호활동'), ('type_2', '지역사회봉사활동'), ('type_3', '기술지원'), ('type_4', '업무보조'), 
                    ('type_5', '정서지원'), ('type_6', '기타봉사'), ('type_7', '생활지원'), ('type_8', '전문봉사'))

affiliation_lst = (('volunteer', '자원봉사자'),('agency', '기관'))


class write_post(models.Model):
    title = models.CharField(max_length=50, blank=True)

    area = models.CharField(choices=area_lst, max_length=17, null=True, blank=True)
    term = models.CharField(max_length=100, blank=True)
    volunteer_type = models.CharField(choices=voluteer_type_lst, max_length=8, null=True, blank=True)
    how_many = models.IntegerField(null=True, blank=True)
    
    photo = models.ImageField(blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True)

    hits = models.IntegerField(null=True, blank=True)

    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    phone_num = models.CharField(max_length=30)
    affiliation = models.CharField(choices=affiliation_lst, max_length=9, null=True, blank=True)