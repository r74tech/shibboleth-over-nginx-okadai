# coding: UTF-8

from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
def shibboleth(request: Request):
    if "auth_type" not in request.headers:
        return {"error": "No Shibboleth headers found"}
    shibboleth = {
        "auth_type": request.headers["auth_type"],
        "remote_user": request.headers["remote_user"],
        "systemid": request.headers["systemid"],
        # "okadaiid": request.headers["okadaiid"],
        # "userclass": request.headers["userclass"],
        "username": request.headers["username"].encode("latin-1").decode("utf-8"),
        "email": request.headers["email"],
        "studentNO": request.headers["studentNO"],
        # "staffNO": request.headers["staffNO"],
        "shib-handler": request.headers["shib-handler"],
        "shib-identity-provider": request.headers["shib-identity-provider"],
    }

    return shibboleth
    


if __name__ == "__main__":
  uvicorn.run("main:app", reload=True)