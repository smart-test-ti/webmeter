from fastapi import APIRouter

router = APIRouter()


@router.get("/api/language")
async def language():
   response = {'status':1}
   return response