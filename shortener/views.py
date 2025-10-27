from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL, ClickRecord
from .forms import ShortURLForm
from .utils import get_client_ip


@login_required
def create_short(request):
    # 首頁：顯示表單 + 建立短碼
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            # form.save() 會把表單轉成一個 ShortURL 模型物件 但暫時不要存進資料庫
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('my_links')
    else:
        form = ShortURLForm()
    return render(request, 'shortener/create.html', {'form': form})


@login_required
def my_links(request):
    # 列出自己建立過的短碼
    links = ShortURL.objects.filter(user=request.user).order_by('-created_at')
    base = request.build_absolute_uri('/')  # e.g. http://127.0.0.1:8000/
    return render(request, 'shortener/my_links.html', {'links': links, 'base': base})


def follow(request, code):
    link = get_object_or_404(ShortURL, short_code=code)
    # 點擊 +1（避免併發覆蓋）
    ShortURL.objects.filter(pk=link.pk).update(
        click_count=F('click_count') + 1)
    # 記錄 IP
    ip = get_client_ip(request) or '0.0.0.0'
    ClickRecord.objects.create(short_url=link, ip_address=ip)
    # 轉址
    return redirect(link.original_url)


@login_required
def link_detail(request, code):
    # 只允許擁有者查看
    link = get_object_or_404(ShortURL, short_code=code, user=request.user)
    # 近 100 筆點擊（可視需要調整/分頁）
    records = link.clicks.order_by('-created_at')[:100]
    base = request.build_absolute_uri('/')
    return render(request, 'shortener/link_detail.html', {
        'link': link, 'records': records, 'base': base
    })
