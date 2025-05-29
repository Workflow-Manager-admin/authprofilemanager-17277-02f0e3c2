import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .users import USERS

# PUBLIC_INTERFACE
@csrf_exempt
def login_view(request):
    """
    Handle POST /api/login for user authentication with hardcoded in-memory data.
    Request: JSON with 'email' and 'password'.
    On success: 200 and user profile (excluding password).
    On failure: 401 and JSON error message.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    try:
        data = json.loads(request.body.decode())
    except Exception:
        return JsonResponse({"error": "Invalid JSON body."}, status=400)

    # Validate inputs
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return JsonResponse({"error": "Both 'email' and 'password' are required."}, status=400)

    # Authenticate user
    for user in USERS:
        if user["email"] == email and user["password"] == password:
            profile = {
                key: value
                for key, value in user.items()
                if key != "password"
            }
            return JsonResponse(profile, status=200)
    return JsonResponse({"error": "Invalid email or password."}, status=401)
