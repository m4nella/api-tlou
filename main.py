from fastapi import FastAPI, HTTPException, status, Response, Path, Header, Depends
from model import Character
from typing import Optional, Any, List
from time import sleep

def fake_db():
    try:
        print("Abrindo banco de dados.")
        sleep(1)
    finally:
        print("Fechando banco de Dados.")
        sleep(1)
        
        
app = FastAPI(description='Nerd ahh API', title='The Last of Us API', version='0.0.1')

characters = {
    
    1: { 
        "name": "Ellie Williams",
        "status": "Alive", 
        "part": "The Last of Us Part I and Part II",
        "gender": "Female"
       },
    
    2: {
        "name": "Joel Miller",
        "status": "Deceased 💀",
        "part": "The Last of Us Part I and Part II",
        "gender": "Male"
       },
     
    3: {
        "name": "Riley Abel",
        "status": "Deceased 💀",
        "part": "The Last of Us Part I",
        "gender": "Female"
       },
        
    4: {
        "name": "Sarah Miller",
        "status": "Deceased 💀",
        "part": "The Last of Us Part I",
        "gender": "Female"
    
             
       },
        
    5: {
        "name": "Tommy Miller",
        "status": "Alive",
        "part": "The Last of Us Part I and Part II",
        "gender": "Male"
         
             
       },
    
    6: {
        "name": "Tess",
        "status": "Deceased 💀",
        "part": "The Last of Us Part I",
        "gender:": "Female"
        
        },
         
    7: {
        "name": "Marlene",
        "status": "Deceased 💀",
        "part": "The Last of Us Part I and Part II",
        "gender:": "Female"           
       },
        
    8: {
        "name": "Dina",
        "status": "Alive",
        "part": "The Last of Us Part II",
        "gender":"Female"      
       },
        
    9: {
        "name": "Jesse ",
        "status": "Deceased 💀",
        "part": "The Last of Us Part II",
        "gender":"Male"   
       },
        
    10: {
        "name": "Abby Anderson",
        "status": "Alive",
        "part": "The Last of Us Part II",
        "gender":"Female"
       },
        
    11: {
        "name": "Lev",
        "status": "Alive",
        "part": "The Last of Us Part II",
        "gender":"Male"
       },
        
    12: {
        "name": "Henry",
        "status": "Deceased 💀",
        "part": "The Last of Us Part I",
        "gender:": "Male"
       },
        
    13: {
        "name": "Sam",
        "status": "Deceased 💀",
        "part": "The Last of Us Part I",
        "gender:": "Male"
       },

    14: {
        "name": "Bill (Frank's boyfriend)",
        "status": "Deceased 💀",
        "part": "The Last of Us Part I",
        "gender:": "Male"
       },
        
    15: {
        "name": "Frank (Bill's boyfriend)",
        "status": "Deceased 💀",
        "part": "The Last of Us Part I",
        "gender:": "Male"
       },
        
    16: {
        "name": "Anna",
        "status": "Deceased 💀",
        "part": "The Last of Us (mentioned); The Last of Us: Left Behind (mentioned); The Last of Us: American Dreams (mentioned)",
        "gender:": "Male"
       },
        
    17: {
        "name": "Cat",
        "status": "Alive",
        "part": "The Last of Us Part II",
        "gender:": "Female" 
       },
        
    18: {
        "name": "Mel",
        "status": "Deceased x2 (cause she was pregnant) 💀",
        "part": "The Last of Us Part II",
        "gender:": "Female"
       },
        
    19: {
        "name": "Owen Moore",
        "age": "Deceased 💀",
        "part": "The Last of Us Part II",
        "gender:": "Male"
       },
        
    20: {
        "name": "Yara",
        "status": "Deceased 💀",
        "part": "The Last of Us Part II",
        "gender:": "Female"
       }
}

@app.get('/')
async def mensagem():
    return {"mensagem": "Deu Certo!"}

app.get('/characters')
async def get_characters():
    return characters

@app.get('/character/{character_id}')
async def get_characters(character_id: int = Path(..., title='get the character by ID', gt=0, lt=3, description='Select the character by ID , where the ID must be 1 or 2...')):
    try:
        character = characters[character_id]
        return character
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="character not found.")
    
@app.post('/character', status_code=status.HTTP_201_CREATED)
async def post_character(character: Optional [Character] = None):
    if character.id not in characters:
        next_id = len(characters) + 1
        characters[next_id] = character
        del character.id
        return character
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='this id already exist mb bro')
    
@app.put('character/{character_id}')
async def put_character(character_id: int, character: Character):
    if character_id in characters:
        characters[character_id] = character
        character.id = character_id
        return character
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='does not exist a character w this id')
    
@app.delete('/character/{character_id}', status_code=status.HTTP_204_NO_CONTENT)
async def del_character(character_id: int, character: Character):
    if character_id in characters:
        del characters[character_id]
        return{'message: f"Delete the character {character_id}"'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'does not existe a character w the id {character_id}')
    
# @app.get('/calculadora')
# async def calcular(n1, n2, n3):
#     soma = n1 + n2 + n3
#     return{"Resultado": soma}    

# @app.get('/headerEx')
# async def headerex(winson: str = Header(...)):
#     return{f'EllieWilliams': {elliewilliams}}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)