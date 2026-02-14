from sanic import Sanic, Request, json, exceptions, response
from sanic_ext import Extend, openapi
import uuid
import io
import csv


app = Sanic("Cooking")
Extend(app)

recipes = [
    {"id":"f217cfe5-98e5-4164-afe6-80d9c54bab11",
     "title":"sushi",
     "category":"dinner",
     "estimated_time":12,
     "difficulty":"hard"}
]

class RecipeModel:
    title : str
    category : str
    estimated_time : int
    difficulty : str

@app.get("/recipes")
async def recipes_list(request: Request):
    return json(recipes)

@app.post("/recipes")
@openapi.body(RecipeModel)
async def recipes_create(request: Request):
    data = request.json

    if not data.get("title"):
        raise exceptions.BadRequest("title cannot be Null")

    recipes.append({
        "id":str(uuid.uuid4()),
        "title":data.get("title"),
        "category":data.get("category"),
        "estimated_time":data.get("estimated_time"),
        "difficulty":data.get("difficulty"),
    })

    return json({"details":"The recipe has been created"})

@app.get("/recipes/<recipe_id>")
async def recipes_get(request: Request, recipe_id):
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            return json(recipe)
        
    raise exceptions.NotFound("recipe does not exist")

@app.put("/recipes/<recipe_id>")
@openapi.body(RecipeModel)
async def recipes_edit(request: Request, recipe_id):
    data = request.json

    if not data.get("title"):
        raise exceptions.BadRequest("title cannot be Null")
    if not data.get("category"):
        raise exceptions.BadRequest("category cannot be Null")
    if not data.get("estimated_time"):
        raise exceptions.BadRequest("estimated_time cannot be Null")
    if not data.get("difficulty"):
        raise exceptions.BadRequest("difficulty cannot be Null")
    
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            recipe.update({
                "title":data.get("title"),
                "category":data.get("category"),
                "estimated_time":data.get("estimated_time"),
                "difficulty":data.get("difficulty"),
            })
            return json(recipe)

    raise exceptions.NotFound("recipe does not exist")

@app.delete("/recipes/<recipe_id>")
async def recipes_delete(request: Request, recipe_id):
    global recipes
    recipes = [recipe for recipe in recipes if recipe["id"] != recipe_id]
    return json({},status=204)
    

@app.get("/recipes/export")
async def recipes_export(request: Request):
    fmt = request.args.get("format", "json").lower()

    if fmt == "json":
        return json(recipes)

    elif fmt == "csv":
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=recipes[0].keys())
        writer.writeheader()
        writer.writerows(recipes)
        output.seek(0)
        return response.text(output.read(), content_type="text/csv")

    else:
        raise exceptions.BadRequest("Only JSON or CSV formats are supported")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, dev=True)