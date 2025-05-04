class VendingMachine:
    def __init__(self):
        self.drinks = {
            "1": {"name": "Air Mineral", "price": 5000, "stock": 10},
            "2": {"name": "Teh Botol", "price": 7000, "stock": 5},
            "3": {"name": "Kopi", "price": 8000, "stock": 8},
        }

    def show_menu(self):
        print("\n=== Mesin Minuman ===")
        for key, drink in self.drinks.items():
            print(f"{key}. {drink['name']} - Rp{drink['price']} (stok: {drink['stock']})")
        print("=====================")

    def buy_drink(self, choice, money):
        if choice not in self.drinks:
            return "Pilihan tidak valid.", money

        drink = self.drinks[choice]
        if drink["stock"] == 0:
            return f"{drink['name']} habis.", money

        if money < drink["price"]:
            return f"Uang tidak cukup. Harga {drink['name']} adalah Rp{drink['price']}.", money

        drink["stock"] -= 1
        money -= drink["price"]
        return f"Anda membeli {drink['name']}.", money

def main():
    vm = VendingMachine()
    saldo = 0

    while True:
        vm.show_menu()
        if saldo > 0:
            print(f"Saldo Anda: Rp{saldo}")

        choice = input("Pilih nomor minuman (atau 'q' untuk keluar): ")
        if choice.lower() == 'q':
            if saldo > 0:
                print(f"Uang kembalian Anda: Rp{saldo}")
            print("Terima kasih telah menggunakan mesin minuman.")
            break

        try:
            if saldo == 0:
                money = int(input("Masukkan jumlah uang (Rp): "))
                saldo += money

            result, saldo = vm.buy_drink(choice, saldo)
            print(result)

            if saldo > 0:
                while True:
                    lanjut = input(f"Saldo tersisa Rp{saldo}. Apakah Anda ingin (b)eli lagi atau (t)arik uang? ")
                    if lanjut.lower() == 'b':
                        break  # lanjut beli lagi
                    elif lanjut.lower() == 't':
                        print(f"Uang kembalian Anda: Rp{saldo}")
                        saldo = 0
                        break
                    else:
                        print("Pilihan tidak valid. Masukkan 'b' atau 't'.")
        except ValueError:
            print("Masukkan uang dalam angka.")

if __name__ == "__main__":
    main()
