class User:
    def __init__(self, name, surname, phone_number, e_mail, country, year=None):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.country = country
        self.first_time = year
        
    def info_user(self):
        print(f"{self.name.title()} {self.surname.title()} from {self.country.title()}, "
              f"phone number: {self.phone_number}, email address: {self.e_mail}.")
    def user_carer(self, time):
        if self.first_time:
            duration = time-self.first_time
            print('From "',duration,'" years in our team!')
        else:
            print("User's first action in our team have not added to list of information.")
        


valijon = User("Valijon", "poyonov", "+998915750000", "valijonpoyonovvvv@gmail.com", "uzbekistan")
valijon.info_user()
valijon.user_carer(2025)
jasurbek = User("jasurbek","jumag'ulov",+998975349999, "jasur@gamil.com", "Uzbekistan", 2021)
jasurbek.info_user()
jasurbek.user_carer(2025)
botir = User("botir", "xo'jayev", +998900010101, "xojayevaaa@gmail.com", "Armaniston", 2020)
sardor = User("sardorbek", "tursunov", 935541987, "sardor@gmail.com", "Tojikiston",2019)
