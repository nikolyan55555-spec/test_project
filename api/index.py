# api/index.py

# Удалите этот импорт:
# from vercel_runtime import Request, Response

# Функция handler принимает стандартный объект запроса (request)
def handler(request):
    """
    Простой обработчик Vercel Function.
    """
    # Этот текст вы увидите в браузере после успешного развертывания
    response_text = "Привет от Vercel Python!"
    
    # Просто возвращаем строку. Vercel сам обернет её в Response object.
    return response_text

