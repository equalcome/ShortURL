def get_client_ip(request):
    # 反向代理下，可能會有多個 IP，用第一個
    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    if xff:
        # 可能長這樣： "203.0.113.5, 70.41.3.18, 150.172.238.178"
        ip = xff.split(',')[0].strip()
        return ip
    return request.META.get('REMOTE_ADDR', '')
