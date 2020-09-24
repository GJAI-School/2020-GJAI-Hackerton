from django.shortcuts import render, redirect
from.models import write_post

# Create your views here.
def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')

def logout(request):
    return redirect('main.html')



row_per_page = 10

def post(request):
    post_lst = write_post.objects.order_by('-id')[0:10]
    current_page = 1
    total_cnt = write_post.objects.all().count()

    helper = page_helper()
    total_page_lst = helper.getTotalPage_lst(total_cnt, row_per_page)

    return render(request, 'post.html',
                            {'post_lst' : post_lst,
                            'total_cnt' : total_cnt,
                            'current_page' : current_page,
                            'total_page_lst' : total_page_lst})


class page_helper:
    def __init__(self):
        self.total_pages = 0
        self.total_page_lst = 0
    
    def getTotalPage_lst(self, total_cnt, row_per_page):
        if ((total_cnt % row_per_page == 0)):
            self.total_pages = total_cnt // row_per_page
            print('get total page #1')

        else:
            self.total_pages = (total_cnt // row_per_page) + 1
            print('get total_page #2')

        self.total_page_lst = []
        for j in range(self.total_pages):
            self.total_page_lst.append(j + 1)
    
        return self.total_page_lst



def page(request):
    return render(request, 'page.html')


area_lst = {'Seoul' : '서울특별시', 'Incheon' : '인천광역시', 'Gyeonggi-do' : '경기도', 'Gangwon-do' : '강원도',
            'Chungcheongnam-do' : '충청남도', 'Sejong' : '세종특별자치시', 'Daejeon' : '대전광역시', 'Chungcheongbuk-do' : '충청북도',
            'Gyeongsangbuk-do' : '경상북도', 'Gyeongsangnam-do' : '경상남도', 'Daegu' : '대구광역시', 'Jeollabuk-do' : '전라북도', 
            'Jeollanam-do' : '전라남도', 'Gwangju' : '광주광역시', 'Ulsan' : '울산광역시', 'Busan' : '부산광역시', 'Jeju' : '제주특별자치시도'}

voluteer_type_lst = {'type_1' : '자연환경보호활동', 'type_2' : '지역사회봉사활동', 'type_3' : '기술지원', 'type_4' : '업무보조', 
                    'type_5' : '정서지원', 'type_6' : '기타봉사', 'type_7' : '생활지원', 'type_8' : '전문봉사'}

affiliation_lst = {'volunteer' : '자원봉사자', 'agency' : '기관'}


def write_page(request):
    context = {
        'area_lst' : area_lst,
        'voluteer_type_lst' : voluteer_type_lst,
        'affiliation_lst' : affiliation_lst
    }

    return render(request, 'write_page.html', context)
