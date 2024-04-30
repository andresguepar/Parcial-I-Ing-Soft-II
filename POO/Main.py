
from poo.Payment import Payment
from poo.PaymentService import PaymentService
from poo.Product import Product
from poo.ShoppingCart import ShoppingCart
from poo.User import User
from poo.UserService import UserService


def main():
    shoppingCart = ShoppingCart()
    userService = UserService()
    paymentService = PaymentService()
    

    while True:
        user = User("Pacho","78132","pacho@email.com")
        product = Product("ProductoPredeterminado", 1)
        shoppingCart.add(product)
        userService.Add(user)
        print("\nOptions:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Edit Account")
        print("4. Checkout")
        print("5. Payment")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Name: ")
            price = input("Price: ")
            product2 = Product.Product(name,price)
            shoppingCart.add(product2)

        elif choice == '2':
            shoppingCart.remove(product2)

        elif choice == '3':
            id = 0
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            user2 = User.User(name,phone,email)
            userService.edit(id,user2)

        elif choice == '4':
            print(f"Your total price is: {shoppingCart.checkout(product)}")

        elif choice == '5':
            payment = Payment(user,product,shoppingCart.checkout(product))
            paymentService.pay(payment)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()