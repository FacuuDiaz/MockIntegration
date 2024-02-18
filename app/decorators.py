from fastapi import HTTPException
from functools import wraps
def validate_header():
    def decorator(func):
        @wraps(func)
        async def wrapper(cls,request,*args, **kwargs):
            try:
                content = cls.content_type_valid
                content_type = request.headers.get("Content-Type")
                if content == "json" and content_type != "application/json":
                    raise HTTPException(status_code=400, detail="Invalid Content-Type. Must be application/json")
                if content == "xml" and content_type != "application/xml":
                    raise HTTPException(status_code=400, detail="Invalid Content-Type. Must be application/xml")
                return await func(cls,request,*args, **kwargs)
            except Exception as e:
                print(e)
                raise HTTPException(status_code=400, detail=f"Error validating request header. {e}")
        return wrapper
    return decorator