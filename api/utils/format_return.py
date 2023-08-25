def format_return(function):
    """
        Decorador para formatar retorno da chamada
    """
    def wrapper(*args, **kwargs):
        data = function(*args, **kwargs)

        if "worker_charge" in data[0]:
            worker_pay = 0
            for row in data:
                worker_pay += row['worker_charge']
                worker_pay += ((row['price'] * row['store_bonus_payment']) / 100)

            return_json = {
                "worker_name": data[0]['worker_name'],
                "order_count": len(data),
                "store_name": data[0]['store_name'],
                "worker_pay": worker_pay
            }
        else:
            return {"message": "Nenhum novo pedido a ser atendido"}
        return return_json
    return wrapper
