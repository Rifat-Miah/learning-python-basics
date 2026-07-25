class ToffeeSubscription:                                                          # Super class
    def __init__(self, sub_id, plan, total_payment):
        self.id = sub_id
        self.plan = plan
        self.payment = total_payment

    def subscribe(self):
        print(f"Subscriber with ID = {self.id}, subscribed to the {self.plan} plan.")

    def unsubscribe(self):
        print(f"Subscriber with ID = {self.id}, Unsubscribed to the {self.plan} plan.")


class ProSubscription(ToffeeSubscription):                                        # sub class 
    def __init__(self, sub_id, plan, total_payment, screen):
        super().__init__(sub_id, plan, total_payment)
        self.max_screen = screen

    def set_max_screen(self, screen):
        self.max_screen = screen
        print(f"Maximum screen set to {self.max_screen} in the Pro Plan.")

toffee1 = ProSubscription("1212", "yearly", 1200, 1)
toffee1.subscribe()
toffee1.set_max_screen(8)

toffee1.unsubscribe()