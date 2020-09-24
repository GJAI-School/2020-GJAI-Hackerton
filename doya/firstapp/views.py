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





def post(request):
    row_per_page = 10

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
            self.total_pages = total_cnt / row_per_page
            print('get total page #1')

        else:
            self.total_pages = (total_cnt / row_per_page) + 1
            print('get total_page #2')

        self.total_page_lst = []
        for j in range(self.total_pages):
            self.total_page_lst.append(j + 1)
    
        return self.total_page_lst



def page(request):
    return render(request, 'page.html')


def write_page(request):
    return render(request, 'write_page.html')
