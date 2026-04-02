# Task 1 : Membuat Struktur Data
class Order:
    def __init__(self, order_id, customer_name, order_date, total_mount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_mount = total_mount

    def calculate_tax(self, tax_rate):
        return self.total_mount *  tax_rate

    def display_order(self):
        print(f"ID: {self.order_id} | Nama: {self.customer_name} | Total: {self.total_mount}")

# Task 2: Membuat Pengelola Banyak Data
class OrderProcessor:
    def __init__(self):
        self.orders = []
    
    def add_order(self, order):
        self.orders.append(order)
    
    def calculate_total_revenue(self):
        total = 0
        for order in self.orders:
            total += order.total_mount
        return total
    
    def calculate_total_tax(self, tax_rate):
        total_tax = 0
        for order in self.orders:
            total_tax+= order.calculate_tax(tax_rate)
        return total_tax
    
    def display_orders(self):
        for order in self.orders:
            order.display_order()

# Task 3: Menjalankan Program Utama
if __name__ == "__main__":
    pesanan1 = Order("001", "Naira", "2025-04-01", 100000.0)
    pesanan2 = Order("002", "Citra", "2025-04-02", 150000.0)
    pesanan3 = Order("003", "Nana", "2025-04-02", 50000.0)

prosesor = OrderProcessor()
prosesor.add_order(pesanan1)
prosesor.add_order(pesanan2)
prosesor.add_order(pesanan3)

print("--- Daftar Pesanan ---")
prosesor.display_orders()

tax_rate = 0.10

print("\n--- Ringkasan Total ---")
print(f"Total Pendapatan : Rp {prosesor.calculate_total_revenue()}")
print(f"Total Pajak (10%) : Rp {prosesor.calculate_total_tax(tax_rate)}")