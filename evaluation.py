while True:
    print("\t\t\t\t\t\tWelcome to the PYTHON JONE")
    print("\t\t\t\t\t\t NET LEGENT LAPTOP STORE")
    print("_-_-_-_-_-_-_-_--++--_-_-_-_-_-_-_-_--++--_-_-_-_-_-_-_-_--++--_-_-_-_-_-_-_-_--++--_-_-_-_-_-_-_-_--++--_-_-_-_-_-_-_-_-++--_-_-_-_-_-_")
    print("\n")
    print("Please Chouse Your Laptop...!")
    print("\t")
    print("HP \t\t press \t1")
    print("DELL \t\t press \t2")
    print("LENOVO \t\t press \t3")
    print("MACBOOK \t press \t4")
    print("ASUS \t\t press \t5")
    print("ACER \t\t press \t6")
    print("MSI \t\t press \t7")
    print("SAMSUNG \t press \t8")
    print("MICROSOFT \t press \t9")


    print("\n\n")

    try:
        inputs = int(input("Enter your selection..:"))
    except ValueError:
            print("Please Enter a Number")
    print("\n\n")




    #-------------------------------------FIRST__PROGRAM-------------------------------------
    try:
        if inputs == 1:
            print("Your Selection is HP and Chouse Your Model..!")
            print("________________________________________________________________________________________________________________________________________")

            print("\n\n")
            print("HP Pavilion Series \t\t press \t1")
            print("HP Envy Series  \t\t press \t2")
            print("HP Victus \t\t\t press \t3")
            print("HP Omen \t\t\t press \t4")
            print("HP ELightBook \t\t\t press \t5")
            print("HP ProBook \t\t\t press \t6")

            print("\n")
            try:
                models = int(input("Please! Enter Your Model :"))
            except:
                print("Please Enter a number")

            if models == 1:
                brand = "HP"
                model = "Pavilion"
                screeSize = 15.6
                cpu = "Ryzen 5"
                price = 94000 
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")


            elif models == 2:
                brand = "HP"
                model = "Envy"
                screeSize = 32.6
                cpu = "Intel i9"
                price = 150000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 3:
                brand = "HP"
                model = "Victus"
                screeSize = 32.6
                cpu = "Intel i7"
                price = 110000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 4:
                brand = "HP"
                model = "Omen"
                screeSize = 16.6
                cpu = "Intel i3"
                price = 40000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 5:
                brand = "HP"
                model = "ELightBook"
                screeSize = 16.6
                cpu = "Intel i5"
                price = 60000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 6:
                brand = "HP"
                model = "ProBook"
                screeSize = 16.6
                cpu = "Intel i9"
                price = 115000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            else:
                print("Please...! Enter a Valid Number...")


    #-------------------------------------SECOND__PROGRAM-------------------------------------
        elif inputs == 2:
            print("Your Selection is DELL and Chouse Your Model..!")
            print("________________________________________________________________________________________________________________________________________")

            print("\n\n")
            print("Dell Inspiron \t\t\t press \t1")
            print("Dell Xps  \t\t\t press \t2")
            print("Dell Vostro \t\t\t press \t3")
            print("Dell G15 \t\t\t press \t4")
            print("Dell Alienware \t\t\t press \t5")


            print("\n")
            try:
                models = int(input("Please! Enter Your Model :"))
            except:
                print("Please Enter a number")


            if models == 1:
                brand = "DELL"
                model = "Inspiron"
                screeSize = 16.6
                cpu = "Intel i3"
                price = 37000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 2:
                brand = "DELL"
                model = "Xps"
                screeSize = 32.6
                cpu = "Intel i5"
                price = 45000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 3:
                brand = "DELL"
                model = "Vostro"
                screeSize = 32.6
                cpu = "Intel i7"
                price = 67000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 4:
                brand = "DELL"
                model = "G15"
                screeSize = 32.6
                cpu = "Ryzen 5"
                price = 44000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 5:
                brand = "Dell"
                model = "Alienware"
                screeSize = 16.6
                cpu = "Intel i5"
                price = 46000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")
            else:
                print("Please...! Enter a Valid Number...")




    #-------------------------------------THIRD__PROGRAM-------------------------------------
        elif inputs == 3:
            print("Your Selection is LENOVO and Chouse Your Model..!")
            print("________________________________________________________________________________________________________________________________________")

            print("\n\n")
            print("Lenovo IdeaPad\t\t\t press \t1")
            print("Lenovo ThinkPad  \t\t press \t2")
            print("Lenovo Yoga \t\t\t press \t3")
            print("Lenovo Legion \t\t\t press \t4")


            print("\n")
            try:
                models = int(input("Please! Enter Your Model :"))
            except:
                print("Please Enter a number")

            if models == 1:
                brand = "Lenovo"
                model = "IdeaPad"
                screeSize = 32.6
                cpu = "Intel i3"
                price = 29000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 2:
                brand = "Lenovo"
                model = "ThinkPad"
                screeSize = 32.6
                cpu = "Intel i5"
                price = 44000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 3:
                brand = "Lenovo"
                model = "Yoga"
                screeSize = 16.6
                cpu = "Intel i7"
                price = 64000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 4:
                brand = "Lenovo"
                model = "Legion"
                screeSize = 32.6
                cpu = "Intel i3"
                price = 35000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            else:
                print("Please...! Enter a Valid Number...")



    #-------------------------------------FOURTH__PROGRAM-------------------------------------
        elif inputs == 4:
            print("Your Selection is MacBook and Chouse Your Model..!")
            print("________________________________________________________________________________________________________________________________________")

            print("\n\n")
            print("MacBook Air\t\t\t press \t1")
            print("MacBook Pro\t\t\t press \t2")


            print("\n")
            try:
                models = int(input("Please! Enter Your Model :"))
            except:
                print("Please Enter a number")

            if models == 1:
                brand = "MacBook"
                model = "Air"
                screeSize = 16.6
                cpu = "2020"
                price = 72000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 2:
                brand = "MacBook"
                model = "Pro"
                screeSize = 16.6
                cpu = "2020"
                price = 175000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            else:
                print("Please...! Enter a Valid Number...")


    #-------------------------------------FIFTH__PROGRAM-------------------------------------
        elif inputs == 5:
            print("Your Selection is ASUS and Chouse Your Model..!")
            print("________________________________________________________________________________________________________________________________________")

            print("\n\n")
            print("Asus VivoBook\t\t\t press \t1")
            print("Asus ZebBook  \t\t\t press \t2")
            print("Asus Rog \t\t\t press \t3")
            print("Asus Tuf \t\t\t press \t4")


            print("\n")
            try:
                models = int(input("Please! Enter Your Model :"))
            except:
                print("Please Enter a number")

            
            if models == 1:
                brand = "Asus"
                model = "VivoBook"
                screeSize = 32.6
                cpu = "Intel i5"
                price = 45000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 2:
                brand = "Asus"
                model = "ZebBook"
                screeSize = 32.6
                cpu = "Intel i3"
                price = 31000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 3:
                brand = "Asus"
                model = "Rog"
                screeSize = 32.6
                cpu = "Intel i7"
                price = 90000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 4:
                brand = "Asus"
                model = "Tuf"
                screeSize = 32.6
                cpu = "Intel i9"
                price = 135000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            else:
                print("Please...! Enter a Valid Number...")


    #-------------------------------------SIXTH__PROGRAM-------------------------------------
        elif inputs == 6:
            print("Your Selection is ACER and Chouse Your Model..!")
            print("________________________________________________________________________________________________________________________________________")

            print("\n\n")
            print("Acer Aspire\t\t\t press \t1")
            print("Acer Swift  \t\t\t press \t2")
            print("Acer Spin \t\t\t press \t3")
            print("Acer Nitro \t\t\t press \t4")


            print("\n")
            try:
                models = int(input("Please! Enter Your Model :"))
            except:
                print("Please Enter a number")

            if models == 1:
                brand = "Acer"
                model = "Aspire"
                screeSize = 32.6
                cpu = "Intel i3"
                price = 24000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 2:
                brand = "Acer"
                model = "Swift"
                screeSize = 32.6
                cpu = "Intel i5"
                price = 35000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 3:
                brand = "Acer"
                model = "Spin"
                screeSize = 16.6
                cpu = "Intel i5"
                price = 41000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 4:
                brand = "Acer"
                model = "Nitro"
                screeSize = 32.6
                cpu = "Intel i9"
                price = 120000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            else:
                print("Please...! Enter a Valid Number...")



    #-------------------------------------SEVENTH__PROGRAM-------------------------------------
        elif inputs == 7:
            print("Your Selection is MSI and Chouse Your Model..!")
            print("________________________________________________________________________________________________________________________________________")

            print("\n\n")
            print("Msi Modern\t\t\t press \t1")
            print("Msi Prestige\t\t\t press \t2")
            print("Msi Raider\t\t\t press \t3")
            print("Msi stealth\t\t\t press \t4")


            print("\n")
            try:
                models = int(input("Please! Enter Your Model :"))
            except:
                print("Please Enter a number")

            if models == 1:
                brand = "Msi"
                model = "Modern"
                screeSize = 16.6
                cpu = "Ryzen 5"
                price = 44000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 2:
                brand = "Msi"
                model = "Prestige"
                screeSize = 32.6
                cpu = "Intel i3"
                price = 35000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 3:
                brand = "Msi"
                model = "Raider"
                screeSize = 32.6
                cpu = "Intel i9"
                price = 140000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")
                
            elif models == 4:
                brand = "Msi"
                model = "stealth"
                screeSize = 32.6
                cpu = "Ryzen 5"
                price = 46000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            else:
                print("Please...! Enter a Valid Number...")


    #-------------------------------------EIGHTH__PROGRAM-------------------------------------
        elif inputs == 8:
            print("Your Selection is SAMSUNG and Chouse Your Model..!")
            print("________________________________________________________________________________________________________________________________________")

            print("\n\n")
            print("Samsung GalaxyBook GO\t\t\t press \t1")
            print("Samsung GalaxyBook Pro\t\t\t press \t2")
            print("Samsung GalaxyBook Odayssey\t\t press \t3")


            print("\n")
            try:
                models = int(input("Please! Enter Your Model :"))
            except:
                print("Please Enter a number")


            if models == 1:
                brand = "Samsung"
                model = "GalaxyBook GO"
                screeSize = 32.6
                cpu = "Intel i5"
                price = 48000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 2:
                brand = "Samsung"
                model = "GalaxyBook Pro"
                screeSize = 15.6
                cpu = "Intel i7"
                price = 75000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 3:
                brand = "Samsung"
                model = "GalaxyBook Odayssey"
                screeSize = 32.6
                cpu = "Intel i5"
                price = 45000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")


            else :
                print("Please...! Enter a Valid Number...")



    #-------------------------------------NINTH__PROGRAM-------------------------------------
        elif inputs == 9:
            print("Your Selection is MICROSOFT and Chouse Your Model..!")
            print("________________________________________________________________________________________________________________________________________")

            print("\n\n")
            print("Microsoft Surface GO\t\t\t press \t1")
            print("Microsoft Surface 4\t\t\t press \t2")
            print("Microsoft Surface Pro\t\t\t press \t3")
            print("Microsoft Book 3\t\t\t press \t4")


            print("\n")
            try:
                models = int(input("Please! Enter Your Model :"))
            except:
                print("Please Enter a number")

            
            if models == 1:
                brand = "Microsoft"
                model = "Surface GO"
                screeSize = 32.6
                cpu = "Intel i9"
                price = 180000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 2:
                brand = "Microsoft"
                model = "Surface 4"
                screeSize = 32.6
                cpu = "Intel i5"
                price = 54000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 3:
                brand = "Microsoft"
                model = "Surface Pro"
                screeSize = 32.6
                cpu = "Intel i7"
                price = 94000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            elif models == 4:
                brand = "Microsoft"
                model = "Book 3"
                screeSize = 32.6
                cpu = "Intel i7"
                price = 118000
                print(f"Brand \t\t{brand}")
                print(f"Model \t\t{model}")
                print(f"ScreenSize \t{screeSize}")
                print(f"cpu \t\t{cpu}")
                print(f"Price \t\t{price}")

                name = input("enter Your Name :")
                files = open(f"{name}.txt","w")
                files.write(f"Name \t\t{name}\n")
                files.write(f"GstNo. \t\t0710710\n")
                files.write(f"Brand \t\t{brand}\n")
                files.write(f"Model \t\t{model}\n")
                files.write(f"ScreenSize \t{screeSize}\n")
                files.write(f"cpu \t\t{cpu}\n")
                files.write("_______________________________________________\n")
                files.write(f"Price \t\t{price}\n")
                files.close()
                print("your Bill is printed...")

            else:
                print("Please...! Enter a Valid Number...")




    #-------------------------------------ELSE__PROGRAM-------------------------------------

        else:
            print("Oops! Your selection is worng..!")

    except NameError as sage:
        print("Restart program ?")




    #-------------------------------------EXIT__PROGRAM-------------------------------------

    
    print("exit of press 710")
    print("contniue for press '0'")
    try:
        exits = int(input("Enter number for exit :"))
        if exits == 710:
            break
    except:
        print("please Enter a valid Number..............")

print("Thankyou for Visting...")






