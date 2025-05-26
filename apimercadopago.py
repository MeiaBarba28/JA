import mercadopago

def gerar_link_pagamento():
    sdk = mercadopago.SDK("TEST-3738074061566374-052609-88db4c463620da7ebd283858852df00c-2462057390")
    payment_data = {
        "items": [
            {"id": "1", "title": "Camisa", "quantity": 1, "currency_id": "BRL", "unit_price": 259.99}
        ],
        "back_urls": {
            "success": "https://casamentojessicaearthur.com.br/compracerta",
            "failure": "https://casamentojessicaearthur.com.br/compraerrada",
            "pending": "https://casamentojessicaearthur.com.br/compraerrada",
        },
        "auto_return": "all"
    }

    result = sdk.preference().create(payment_data)
    payment = result["response"]

    link_iniciar_pagamento = payment["init_point"]
    return link_iniciar_pagamento