def userEntity(item) -> dict:
    return{
        "id":str(item(["_id"])),
        "name":item["name"],
        "email":item["email"],
        "password" : item["password "]
    }
    
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

# def serializeDict(a) -> dict:
#     return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

# def serializeList(entity) -> list:
#     return [serializeDict(a) for a in entity]
def serialize_dict(a) -> dict:
    serialized = {}
    for key, value in a.items():
        serialized[key] = str(value) if key == '_id' else value
    return serialized

def serialize_list(entity) -> list:
    return [serialize_dict(a) for a in entity]
