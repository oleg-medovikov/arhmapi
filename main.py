import uvicorn
from reqs import app 


if __name__ == "__main__":
    uvicorn.run("main:app",
            host="0.0.0.0",port=8000,
            reload=True,workers =2, 
            ssl_keyfile='publ/oleg.key', 
            ssl_certfile='publ/oleg.crt',)
