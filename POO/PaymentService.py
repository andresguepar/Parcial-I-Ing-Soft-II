
import Payment


class PaymentService:
    def pay(self,payment : Payment.Payment):
        print(f"Payment succesful, here is your receipt: {payment.user.name} compró {payment.product.name} con el valor de {payment.product.price}.")