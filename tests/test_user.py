from fastapi.testclient import TestClient
from app.api.routes import app
from app.api.services.user_service import get_user_service,UserService
from fastapi import Depends




client = TestClient(app)

def test_read_root():
    response = client.get("user/home")
    assert response.status_code == 200





@user_router.post('/login', description='My description', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def create_user(user_input: UserInput, service: UserService = Depends(get_user_service)):
    try:
        print(user_input.username)
        user_db = service.get_username(username=user_input.username)
        input_password = user_input.password
        hashed_password= user_db.password

        print(hashed_password)
        print(input_password)
        if not user_db or not user_db.password:
            raise HTTPException(401, detail='Incorrect username or password')
        isverif = service.validate_password(input_password=input_password,hashed_password=hashed_password)
        if isverif:
            return StandardOutput(message='Ok logado') 
        
        raise HTTPException(401, detail='Incorrect username or password')

    except Exception as error:
        raise HTTPException(400, detail=str(error))
