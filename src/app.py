from fastapi import FastAPI, Response

from src.routes.items import router as items_router


app = FastAPI()

# Incluir rutas de items
app.include_router(items_router)


@app.get('/')
def read_root():
    return 'Hello, world'


@app.get('/health')
def health_check():
    return {'status': 'ok'}


# Renderizar página HTML
@app.get('/home')
def render_home():
    with open('public/index.html', 'r') as f:
        return Response(content=f.read(), media_type='text/html')
    

PRODUCTS = [
    {'id': 1, 'name': 'Pepsi', 'price': 10.99},
    {'id': 2, 'name': 'Fanta', 'price': 19.99},
    {'id': 3, 'name': 'Sprite', 'price': 5.99},
]

# Renderizar página HTML con productos
@app.get('/products')
def render_products():
    with open('public/items.html', 'r') as f:
        html_content = f.read()
        product_list = ''
        for product in PRODUCTS:
            product_list += f'<li>{product["name"]} - {product["price"]}</li>'
        html_content_final = html_content.replace('{{ items }}', product_list)
        return Response(content=html_content_final, media_type='text/html')