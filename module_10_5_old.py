from multiprocessing import Manager, Process


class WarehouseManager:
    def __init__(self):
        self.data = Manager().dict()

    def process_request(self, request):
        product_name, action, quantity = request

        if action == 'receipt':  # получение товара
            if product_name in self.data:
                self.data[product_name] += quantity
            else:
                self.data[product_name] = quantity
        elif action == 'shipment':  # отгрузка товара
            if product_name in self.data and self.data[product_name] >= quantity:
                self.data[product_name] -= quantity

    def run(self, inquiry):
        processes = []

        for request in inquiry:
            p = Process(target=self.process_request, args=(request,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()


if __name__ == '__main__':
    manager = WarehouseManager()

    requests = [
        ('product1', 'receipt', 100),
        ('product2', 'receipt', 150),
        ('product1', 'shipment', 30),
        ('product3', 'receipt', 200),
        ('product2', 'shipment', 50)
    ]

    manager.run(requests)

    print(manager.data)
