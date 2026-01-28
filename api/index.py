# api/index.py

from vercel_runtime import Request, Response

def handler(request: Request) -> Response:
    """
    Простой обработчик Vercel Function.
    """
    # Этот текст вы увидите в браузере после успешного развертывания
    response_text = "Привет от Vercel Python!"
    
    return Response(response_text, headers={"Content-Type": "text/plain"})
