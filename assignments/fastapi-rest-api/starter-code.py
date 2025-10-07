from fastapi import FastAPI, HTTPException

app = FastAPI()

# Estrutura de dados para armazenar usuários
users = []

@app.get("/users")
def list_users():
    return users

@app.post("/users")
def create_user(user: dict):
    user["id"] = len(users) + 1
    users.append(user)
    return user

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"detail": "Usuário removido"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
