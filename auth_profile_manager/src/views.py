import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

HARD_CODED_USERS = [
    {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "employee_id": "EMP001",
        "contact_number": "555-1111",
        "password": "alicepass123"
    },
    {
        "name": "Bob Smith",
        "email": "bob@example.com",
        "employee_id": "EMP002",
        "contact_number": "555-2222",
        "password": "bobpass123"
    },
    {
        "name": "Carol Tan",
        "email": "carol@example.com",
        "employee_id": "EMP003",
        "contact_number": "555-3333",
        "password": "carolpass123"
    },
    {
        "name": "David Lee",
        "email": "david@example.com",
        "employee_id": "EMP004",
        "contact_number": "555-4444",
        "password": "davidpass123"
    },
    {
        "name": "Eva Brown",
        "email": "eva@example.com",
        "employee_id": "EMP005",
        "contact_number": "555-5555",
        "password": "evapass123"
    },
    {
        "name": "Frank Miller",
        "email": "frank@example.com",
        "employee_id": "EMP006",
        "contact_number": "555-6666",
        "password": "frankpass123"
    },
    {
        "name": "Grace Kim",
        "email": "grace@example.com",
        "employee_id": "EMP007",
        "contact_number": "555-7777",
        "password": "gracepass123"
    },
    {
        "name": "Hank Patel",
        "email": "hank@example.com",
        "employee_id": "EMP008",
        "contact_number": "555-8888",
        "password": "hankpass123"
    },
    {
        "name": "Ivy Chen",
        "email": "ivy@example.com",
        "employee_id": "EMP009",
        "contact_number": "555-9999",
        "password": "ivypass123"
    },
    {
        "name": "Jack Wu",
        "email": "jack@example.com",
        "employee_id": "EMP010",
        "contact_number": "555-1010",
        "password": "jackpass123"
    },
]

# PUBLIC_INTERFACE


@csrf_exempt
def login_view(request):
    """
    POST /api/login
    Body: { "email": ..., "password": ... }
    Returns 200 and user profile (no password) on success;
    401 and {"error": "..."} on failure.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    try:
        data = json.loads(request.body.decode())
    except Exception:
        return JsonResponse({"error": "Invalid JSON body."}, status=400)
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return JsonResponse({"error": "Both 'email' and 'password' are required."}, status=400)
    for user in HARD_CODED_USERS:
        if user["email"] == email and user["password"] == password:
            profile = {k: v for k, v in user.items() if k != "password"}
            return JsonResponse(profile, status=200)
    return JsonResponse({"error": "Invalid email or password."}, status=401)

