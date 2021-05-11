from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
app = FastAPI()


@app.api_route(
    path="/method", methods=["GET", "POST", "DELETE", "PUT", "OPTIONS"], status_code=200
)
def read_request(request: Request, response: Response):
    request_method = request.method
    return {"method": request_method}