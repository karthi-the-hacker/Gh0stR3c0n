set back-end/ -a

source back-end/config.env

set back-end/ +a

cd back-end/

uvicorn main:app --reload &
