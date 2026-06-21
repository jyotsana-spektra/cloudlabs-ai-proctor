from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def chat_route_status():
    return {
        "message": "Chat route is available"
    }
